/* ==============================================================================
   TRACE — AVIONICS FLIGHT PROFILE FORENSIC VISUALIZATION (CORE ENGINE)
   Visual Flight Trajectory (Runway ➔ Climb ➔ Cruise FL380 ➔ Descent ➔ Touchdown)
   3-Tier Semantic Zoom: Flight Trajectory ➔ Forensic Narration ➔ Raw Telemetry
   ============================================================================== */

(function () {
  'use strict';

  // Constants
  const MISSION_START_SEC = 0;        // 09:00:00 UTC
  const MISSION_END_SEC = 18004;      // 14:00:04 UTC (~5 hours)
  const SVG_VIEW_WIDTH = 2000;
  const SVG_VIEW_HEIGHT = 600;
  const X_MIN = 80;
  const X_MAX = 1920;
  const Y_RUNWAY = 550;               // Sea Level (0 ft)
  const Y_10K = 390;                  // 10,000 ft transition
  const Y_25K = 230;                  // 25,000 ft troposphere
  const Y_CRUISE = 80;                // 38,000 ft (FL380)

  // Application State
  const state = {
    incidents: [],
    filteredIncidents: [],
    selectedIncident: null,
    selectedEventIndex: 0,
    currentZoomLevel: 1, // 1: Flight Trajectory, 2: Narration, 3: Telemetry
    filterSeverity: 'all',
    searchQuery: '',
    currentFlightTime: 0, // In seconds from 09:00:00
    replayPlaying: false,
    replaySpeed: 1,       // 1x, 5x, 20x
    replayAnimFrame: null,
    lastFrameTime: null
  };

  // DOM Elements
  const dom = {
    // Zoom Stepper Buttons
    btnGotoL1: document.getElementById('btn-goto-level1'),
    btnGotoL2: document.getElementById('btn-goto-level2'),
    btnGotoL3: document.getElementById('btn-goto-level3'),
    level1: document.getElementById('level-1-flight-tape'),
    level2: document.getElementById('level-2-narration-deck'),
    level3: document.getElementById('level-3-telemetry-terminal'),

    // Search & Filters
    omniSearch: document.getElementById('omni-search'),
    btnClearSearch: document.getElementById('clear-search'),
    filterChips: document.querySelectorAll('.filter-chip'),

    // Level 1: Flight Profile & Trajectory
    hudClock: document.getElementById('hud-clock'),
    hudAlt: document.getElementById('hud-alt'),
    hudPhase: document.getElementById('hud-phase'),
    hudIncidentStat: document.getElementById('hud-incident-stat'),
    btnReplayFlight: document.getElementById('btn-replay-flight'),
    btnResetFlight: document.getElementById('btn-reset-flight'),
    replayPlayIcon: document.getElementById('replay-play-icon'),
    replayPlayText: document.getElementById('replay-play-text'),
    speedBtns: document.querySelectorAll('.speed-btn'),
    phaseJumpBtns: document.querySelectorAll('.phase-jump-btn'),
    flightSvg: document.getElementById('flight-trajectory-svg'),
    flightCanvasViewport: document.getElementById('flight-canvas-viewport'),
    btnZoomIn: document.getElementById('btn-zoom-in'),
    btnZoomOut: document.getElementById('btn-zoom-out'),
    btnZoomReset: document.getElementById('btn-zoom-reset'),
    zoomFactorBadge: document.getElementById('zoom-factor-badge'),
    trajGlow: document.getElementById('svg-trajectory-glow'),
    trajPath: document.getElementById('svg-trajectory-path'),
    trajTraveled: document.getElementById('svg-trajectory-traveled'),
    dotsGroup: document.getElementById('svg-incident-dots-group'),
    aircraftGroup: document.getElementById('svg-aircraft-group'),
    hoverHud: document.getElementById('incident-hover-hud'),
    hudTipIndex: document.getElementById('hud-tip-index'),
    hudTipCluster: document.getElementById('hud-tip-cluster'),
    hudTipSev: document.getElementById('hud-tip-sev'),
    hudTipPhase: document.getElementById('hud-tip-phase'),
    hudTipNodes: document.getElementById('hud-tip-nodes'),
    hudTipTrigger: document.getElementById('hud-tip-trigger'),
    scrubberBar: document.getElementById('flight-scrubber-bar'),
    scrubberFill: document.getElementById('flight-scrubber-fill'),
    scrubberHandle: document.getElementById('flight-scrubber-handle'),

    // Level 2: Narration Deck
    btnBackToL1: document.getElementById('btn-back-to-level1'),
    btnPrevIncident: document.getElementById('btn-prev-incident'),
    btnNextIncident: document.getElementById('btn-next-incident'),
    deckIndexBadge: document.getElementById('deck-index-badge'),
    deckClusterTitle: document.getElementById('deck-cluster-title'),
    deckTimeBadge: document.getElementById('deck-time-badge'),
    deckSeverityBadge: document.getElementById('deck-severity-badge'),
    deckSpecsMatrix: document.getElementById('deck-specs-matrix'),
    deckExecNarrative: document.getElementById('deck-exec-narrative'),
    deckTriggerTag: document.getElementById('deck-trigger-tag'),
    deckRcaDescription: document.getElementById('deck-rca-description'),
    deckImpactText: document.getElementById('deck-impact-text'),
    deckRecsText: document.getElementById('deck-recs-text'),
    deckCascadeCount: document.getElementById('deck-cascade-count'),
    deckCascadeFlowchart: document.getElementById('deck-cascade-flowchart'),
    btnReplayCascade: document.getElementById('btn-replay-cascade'),
    btnOpenRawModal: document.getElementById('btn-open-raw-modal'),
    btnZoomToTelemetry: document.getElementById('btn-zoom-to-telemetry'),
    btnJumpToRawFacts: document.getElementById('btn-jump-to-raw-facts'),

    // Section 6: Unified Dossier Raw Facts Elements
    dossierRawFactsSection: document.getElementById('dossier-raw-facts-section'),
    dossierPrevFrame: document.getElementById('dossier-prev-frame'),
    dossierNextFrame: document.getElementById('dossier-next-frame'),
    dossierFramePos: document.getElementById('dossier-frame-pos'),
    dossierNodeBadge: document.getElementById('dossier-node-badge'),
    dossierFamilyBadge: document.getElementById('dossier-family-badge'),
    dossierTimeBadge: document.getElementById('dossier-time-badge'),
    dossierSummaryHeadline: document.getElementById('dossier-summary-headline'),
    dossierCitationTag: document.getElementById('dossier-citation-tag'),
    dossierBtnCopyCitation: document.getElementById('dossier-btn-copy-citation'),
    dossierParamCount: document.getElementById('dossier-param-count'),
    dossierTelemetryTbody: document.getElementById('dossier-telemetry-tbody'),

    // Level 3: Telemetry Terminal
    btnBackToL2: document.getElementById('btn-back-to-level2'),
    termClusterRef: document.getElementById('term-cluster-ref'),
    termEventRef: document.getElementById('term-event-ref'),
    termPrevEvent: document.getElementById('term-prev-event'),
    termNextEvent: document.getElementById('term-next-event'),
    termEventPos: document.getElementById('term-event-pos'),
    termNodeBadge: document.getElementById('term-node-badge'),
    termFamilyBadge: document.getElementById('term-family-badge'),
    termTimeBadge: document.getElementById('term-time-badge'),
    termOccBadge: document.getElementById('term-occ-badge'),
    termSummaryHeadline: document.getElementById('term-summary-headline'),
    termCitationTag: document.getElementById('term-citation-tag'),
    btnCopyCitation: document.getElementById('btn-copy-citation'),
    termRawJson: document.getElementById('term-raw-json'),
    termParamCount: document.getElementById('term-param-count'),
    termTelemetryTbody: document.getElementById('term-telemetry-tbody'),

    // Full Report Modal
    reportModal: document.getElementById('report-modal'),
    modalHeading: document.getElementById('modal-heading'),
    modalMarkdownContainer: document.getElementById('modal-markdown-container'),
    btnModalClose: document.getElementById('btn-modal-close'),
    btnModalDismiss: document.getElementById('btn-modal-dismiss'),
    btnCopyFullMarkdown: document.getElementById('btn-copy-full-markdown')
  };

  // --------------------------------------------------------------------------
  // 1. FLIGHT MATHEMATICS & TRAJECTORY PROFILE CALCULATIONS
  // --------------------------------------------------------------------------

  // Convert clock string "09:12:45" to mission seconds from 09:00:00
  function timeStringToSeconds(clockStr) {
    if (!clockStr) return 0;
    const parts = clockStr.split(':').map(Number);
    const h = parts[0] || 9;
    const m = parts[1] || 0;
    const s = parts[2] || 0;
    const totalSec = h * 3600 + m * 60 + s;
    const baseSec = 9 * 3600; // 09:00:00
    return Math.max(0, Math.min(MISSION_END_SEC, totalSec - baseSec));
  }

  // Convert mission seconds back to UTC clock string
  function secondsToClockString(sec) {
    const total = 9 * 3600 + Math.round(sec);
    const h = Math.floor(total / 3600);
    const m = Math.floor((total % 3600) / 60);
    const s = Math.floor(total % 60);
    return `${String(h).padStart(2, '0')}:${String(m).padStart(2, '0')}:${String(s).padStart(2, '0')} UTC`;
  }

  // Calculate X in SVG (0 to 2000) for a given mission second t
  function getXForTime(t) {
    const fraction = t / MISSION_END_SEC;
    return X_MIN + fraction * (X_MAX - X_MIN);
  }

  // Calculate Altitude (ft) and Y coordinate in SVG (0 to 600) for a given mission second t
  function getAltitudeAndYForTime(t) {
    let alt = 0;
    let y = Y_RUNWAY;

    if (t < 720) {
      // 09:00:00 - 09:12:00 : Departure Runway 09L taxi & takeoff ground roll
      alt = 0;
      y = Y_RUNWAY;
    } else if (t < 4500) {
      // 09:12:00 - 10:15:00 : Ascent & Initial Climb to FL380 (Smooth cubic S-curve)
      const p = (t - 720) / (4500 - 720);
      const ease = p * p * (3 - 2 * p); // Smooth Hermite S-Curve
      alt = ease * 38000;
      y = Y_RUNWAY - ease * (Y_RUNWAY - Y_CRUISE);
    } else if (t < 13500) {
      // 10:15:00 - 12:45:00 : High Altitude Cruise FL380
      alt = 38000;
      // Gentle atmospheric stratospheric wave
      const wave = Math.sin(t / 250) * 3;
      y = Y_CRUISE + wave;
    } else if (t < 17280) {
      // 12:45:00 - 13:48:00 : Descent & Vectoring to Sea Level (Smooth S-curve)
      const p = (t - 13500) / (17280 - 13500);
      const ease = p * p * (3 - 2 * p);
      alt = (1 - ease) * 38000;
      y = Y_CRUISE + ease * (Y_RUNWAY - Y_CRUISE);
    } else {
      // 13:48:00 - 14:00:04 : Landing Touchdown & Runway 27R Rollout
      alt = 0;
      y = Y_RUNWAY;
    }

    return { alt, y };
  }

  // Determine Flight Phase name and descriptive badge
  function getFlightPhase(t, alt) {
    if (t < 720) {
      return { name: 'DEPARTURE ROLL', detail: 'RUNWAY 09L (0 FT)', class: 'takeoff' };
    } else if (t < 4500) {
      return { name: 'CLIMB PHASE', detail: `ASCENT • ${Math.round(alt).toLocaleString()} FT`, class: 'climb' };
    } else if (t < 13500) {
      return { name: 'CRUISE FL380', detail: '38,000 FT • STRATOSPHERE', class: 'cruise' };
    } else if (t < 17280) {
      return { name: 'DESCENT & VECTORING', detail: `APPROACH • ${Math.round(alt).toLocaleString()} FT`, class: 'descent' };
    } else {
      return { name: 'TOUCHDOWN & ROLLOUT', detail: 'RUNWAY 27R (0 FT)', class: 'rollout' };
    }
  }

  // Calculate tangent pitch angle (degrees) for the airplane orientation
  function getTrajectoryTangentAngle(t) {
    const delta = 15;
    const tPrev = Math.max(0, t - delta);
    const tNext = Math.min(MISSION_END_SEC, t + delta);

    const x1 = getXForTime(tPrev);
    const y1 = getAltitudeAndYForTime(tPrev).y;
    const x2 = getXForTime(tNext);
    const y2 = getAltitudeAndYForTime(tNext).y;

    const angleRad = Math.atan2(y2 - y1, x2 - x1);
    return (angleRad * 180) / Math.PI;
  }

  // --------------------------------------------------------------------------
  // 2. INITIALIZATION & RENDERING
  // --------------------------------------------------------------------------
  function init() {
    if (!window.TRACE_INCIDENTS || !Array.isArray(window.TRACE_INCIDENTS)) {
      console.error('Fatal: TRACE_INCIDENTS data array not found on window object.');
      return;
    }

    state.incidents = window.TRACE_INCIDENTS;
    state.filteredIncidents = [...state.incidents];
    state.selectedIncident = state.incidents[0]; // Default to incident #1

    // Pre-calculate flight coordinates and phase for all 124 incidents
    state.incidents.forEach(inc => {
      const sec = timeStringToSeconds(inc.start_clock);
      const coord = getAltitudeAndYForTime(sec);
      const phase = getFlightPhase(sec, coord.alt);
      inc._missionSec = sec;
      inc._x = getXForTime(sec);
      inc._y = coord.y;
      inc._alt = coord.alt;
      inc._phase = phase;
    });

    renderTrajectoryCurve();
    renderIncidentDots();
    updateFlightAircraftPosition(0);
    attachEventListeners();
    setZoomLevel(1);
  }

  // Generate smooth SVG Trajectory Curve path data
  function renderTrajectoryCurve() {
    const steps = 300;
    const points = [];

    for (let i = 0; i <= steps; i++) {
      const t = (i / steps) * MISSION_END_SEC;
      const x = getXForTime(t);
      const y = getAltitudeAndYForTime(t).y;
      points.push({ x, y });
    }

    // Build SVG path data with smooth cubic beziers
    let d = `M ${points[0].x.toFixed(1)},${points[0].y.toFixed(1)}`;
    for (let i = 1; i < points.length; i++) {
      d += ` L ${points[i].x.toFixed(1)},${points[i].y.toFixed(1)}`;
    }

    dom.trajPath.setAttribute('d', d);
    dom.trajGlow.setAttribute('d', d);
  }

  // Render the 124 Incident Dots pinned directly on the Trajectory Curve
  function renderIncidentDots() {
    dom.dotsGroup.innerHTML = '';

    state.incidents.forEach((inc) => {
      const g = document.createElementNS('http://www.w3.org/2000/svg', 'g');
      const sevClass = inc.severity.toLowerCase();
      g.setAttribute('class', `incident-dot-group ${sevClass}`);
      g.setAttribute('data-index', inc.index);
      g.setAttribute('data-cluster-id', inc.cluster_id);

      const x = inc._x;
      const y = inc._y;

      // Vertical stem / anchor line
      const stem = document.createElementNS('http://www.w3.org/2000/svg', 'line');
      stem.setAttribute('x1', x);
      stem.setAttribute('y1', y);
      stem.setAttribute('x2', x);
      stem.setAttribute('y2', y - 18);
      stem.setAttribute('stroke', 'rgba(255, 255, 255, 0.25)');
      stem.setAttribute('stroke-width', '1');
      stem.setAttribute('stroke-dasharray', '2,2');
      stem.setAttribute('vector-effect', 'non-scaling-stroke');

      // Outer pulsing beacon halo
      const halo = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
      halo.setAttribute('cx', x);
      halo.setAttribute('cy', y);
      halo.setAttribute('r', '10');
      halo.setAttribute('class', 'incident-beacon-halo');
      halo.setAttribute('fill', 'none');
      halo.setAttribute('stroke', inc.severity === 'CRITICAL' ? '#f43f5e' : (inc.severity === 'WARNING' ? '#f59e0b' : '#38bdf8'));
      halo.setAttribute('stroke-width', '2');
      halo.setAttribute('vector-effect', 'non-scaling-stroke');

      // Inner solid beacon dot
      const core = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
      core.setAttribute('cx', x);
      core.setAttribute('cy', y);
      core.setAttribute('r', '5.5');
      core.setAttribute('class', 'incident-beacon-core');
      core.setAttribute('vector-effect', 'non-scaling-stroke');

      // Micro index label tag (revealed on hover/selection)
      const label = document.createElementNS('http://www.w3.org/2000/svg', 'text');
      label.setAttribute('x', x);
      label.setAttribute('y', y - 22);
      label.setAttribute('class', 'incident-dot-label');
      label.textContent = `#${String(inc.index).padStart(3, '0')}`;

      g.appendChild(stem);
      g.appendChild(halo);
      g.appendChild(core);
      g.appendChild(label);

      dom.dotsGroup.appendChild(g);
    });

    updateIncidentFilters();
  }

  // --------------------------------------------------------------------------
  // 3. HOVER RADAR HUD & SELECTION TRANSITIONS (HIGH PRECISION / ZERO FLICKER)
  // --------------------------------------------------------------------------

  function showIncidentHoverHud(inc) {
    if (!inc) return;
    state.hoveredIncident = inc;
    dom.hudTipIndex.textContent = `#${String(inc.index).padStart(3, '0')}`;
    dom.hudTipCluster.textContent = inc.cluster_id;
    dom.hudTipSev.textContent = inc.severity;
    dom.hudTipSev.className = `hud-tooltip-sev ${inc.severity.toLowerCase()}`;
    dom.hudTipPhase.textContent = `${inc._phase.name} • ${inc.start_clock} UTC (${Math.round(inc._alt).toLocaleString()} FT)`;
    dom.hudTipNodes.textContent = inc.nodes.join(', ');

    // Extract first sentence of trigger
    let triggerText = inc.root_cause || inc.executive_summary || 'Operational state anomaly';
    if (triggerText.includes('.')) triggerText = triggerText.split('.')[0] + '.';
    dom.hudTipTrigger.textContent = triggerText.replace(/\[Source:[^\]]+\]/g, '').trim();

    // Position tooltip precisely using SVG transformation matrix (Zero Layout Thrashing)
    try {
      const pt = dom.flightSvg.createSVGPoint();
      pt.x = inc._x;
      pt.y = inc._y;
      const screenPt = pt.matrixTransform(dom.flightSvg.getScreenCTM());
      const viewRect = dom.flightCanvasViewport.getBoundingClientRect();
      const left = screenPt.x - viewRect.left;
      const top = screenPt.y - viewRect.top;

      // Keep tooltip horizontally clamped inside viewport bounds
      const clampedLeft = Math.max(165, Math.min(viewRect.width - 165, left));
      dom.hoverHud.style.left = `${clampedLeft}px`;
      dom.hoverHud.style.top = `${top}px`;

      // If near top of screen (cruise FL380), flip below dot, otherwise show above
      if (top < 180) {
        dom.hoverHud.style.transform = 'translate(-50%, 20px)';
      } else {
        dom.hoverHud.style.transform = 'translate(-50%, calc(-100% - 16px))';
      }

      dom.hoverHud.classList.add('visible');
    } catch (err) {
      dom.hoverHud.classList.add('visible');
    }
  }

  function hideIncidentHoverHud() {
    state.hoveredIncident = null;
    dom.hoverHud.classList.remove('visible');
    const dots = dom.dotsGroup.querySelectorAll('.incident-dot-group.hovered');
    dots.forEach(d => d.classList.remove('hovered'));
  }

  // Smoothly opens Level 2 Forensic Dossier for the selected incident
  function selectAndZoomToIncident(inc) {
    if (!inc) return;
    hideIncidentHoverHud();
    state.selectedIncident = inc;
    state.selectedEventIndex = 0;

    // Highlight selected dot beacon on flight path
    const dots = dom.dotsGroup.querySelectorAll('.incident-dot-group');
    dots.forEach(d => {
      d.classList.toggle('selected-active', Number(d.dataset.index) === inc.index);
    });

    updateFlightAircraftPosition(inc._missionSec);

    // Smoothly reveal Level 2 (Forensic Narration & Raw Facts Dossier)
    setZoomLevel(2);
  }

  // --------------------------------------------------------------------------
  // 4. AIRCRAFT MARKER & MISSION REPLAY ENGINE
  // --------------------------------------------------------------------------

  function updateFlightAircraftPosition(sec) {
    state.currentFlightTime = Math.max(0, Math.min(MISSION_END_SEC, sec));

    const x = getXForTime(state.currentFlightTime);
    const { alt, y } = getAltitudeAndYForTime(state.currentFlightTime);
    const angle = getTrajectoryTangentAngle(state.currentFlightTime);
    const phase = getFlightPhase(state.currentFlightTime, alt);

    // Move SVG aircraft group with dynamic pitch rotation
    dom.aircraftGroup.setAttribute('transform', `translate(${x.toFixed(1)}, ${y.toFixed(1)}) rotate(${angle.toFixed(1)})`);

    // Update Head-Up Display Telemetry Gauges
    dom.hudClock.textContent = secondsToClockString(state.currentFlightTime);
    dom.hudAlt.textContent = `${Math.round(alt).toLocaleString()} FT (${phase.detail})`;
    dom.hudPhase.textContent = phase.name;
    dom.hudPhase.className = `hud-gauge-val phase-pill ${phase.class}`;

    // Update bottom scrubber handle & progress fill
    const pct = (state.currentFlightTime / MISSION_END_SEC) * 100;
    dom.scrubberFill.style.width = `${pct}%`;
    dom.scrubberHandle.style.left = `${pct}%`;

    // Highlight nearest incident dot on trajectory
    highlightNearestIncidentDot(state.currentFlightTime);
  }

  function highlightNearestIncidentDot(sec) {
    const dots = dom.dotsGroup.querySelectorAll('.incident-dot-group');
    dots.forEach(d => d.classList.remove('active-aircraft-proximity'));

    // Find incident closest to current flight time within 60s
    const closest = state.incidents.find(inc => Math.abs(inc._missionSec - sec) < 60);
    if (closest) {
      const el = dom.dotsGroup.querySelector(`[data-index="${closest.index}"]`);
      if (el) el.classList.add('active-aircraft-proximity');
    }
  }

  // Play / Pause Mission Replay
  function toggleMissionReplay() {
    if (state.replayPlaying) {
      pauseMissionReplay();
    } else {
      startMissionReplay();
    }
  }

  function startMissionReplay() {
    state.replayPlaying = true;
    dom.btnReplayFlight.classList.add('active');
    dom.replayPlayIcon.textContent = '⏸';
    dom.replayPlayText.textContent = 'PAUSE MISSION';
    state.lastFrameTime = performance.now();
    runReplayLoop();
  }

  function pauseMissionReplay() {
    state.replayPlaying = false;
    dom.btnReplayFlight.classList.remove('active');
    dom.replayPlayIcon.textContent = '▶';
    dom.replayPlayText.textContent = 'PLAY MISSION';
    if (state.replayAnimFrame) {
      cancelAnimationFrame(state.replayAnimFrame);
      state.replayAnimFrame = null;
    }
  }

  function runReplayLoop() {
    if (!state.replayPlaying) return;

    const now = performance.now();
    const dt = (now - state.lastFrameTime) / 1000; // in seconds
    state.lastFrameTime = now;

    // Advance flight seconds: 1 second of real time = 60s * speed of flight time
    const advanceSec = dt * 120 * state.replaySpeed;
    let nextSec = state.currentFlightTime + advanceSec;

    if (nextSec >= MISSION_END_SEC) {
      nextSec = MISSION_END_SEC;
      updateFlightAircraftPosition(nextSec);
      pauseMissionReplay();
      return;
    }

    updateFlightAircraftPosition(nextSec);
    state.replayAnimFrame = requestAnimationFrame(runReplayLoop);
  }

  function resetFlightMission() {
    pauseMissionReplay();
    updateFlightAircraftPosition(0);
  }

  // --------------------------------------------------------------------------
  // 5. SEMANTIC ZOOM LEVEL SWITCHING
  // --------------------------------------------------------------------------
  function setZoomLevel(level) {
    state.currentZoomLevel = level;

    // Update Top Breadcrumb Stepper
    [dom.btnGotoL1, dom.btnGotoL2, dom.btnGotoL3].forEach((btn, idx) => {
      btn.classList.toggle('active', idx + 1 === level);
    });

    // Update Views Visibility
    dom.level1.classList.toggle('active', level === 1);
    dom.level2.classList.toggle('active', level === 2);
    dom.level3.classList.toggle('active', level === 3);

    if (level === 1) {
      // Return to flight profile view: ensure aircraft position is aligned
      if (state.selectedIncident) {
        updateFlightAircraftPosition(state.selectedIncident._missionSec);
      }
    } else if (level === 2) {
      populateNarrationDeck();
    } else if (level === 3) {
      populateTelemetryTerminal();
    }
  }

  // --------------------------------------------------------------------------
  // 6. LEVEL 2: FORENSIC NARRATION DECK
  // --------------------------------------------------------------------------
  function populateNarrationDeck() {
    const inc = state.selectedIncident;
    if (!inc) return;

    // Header Badges
    dom.deckIndexBadge.textContent = `INCIDENT #${String(inc.index).padStart(3, '0')}`;
    dom.deckClusterTitle.textContent = inc.cluster_id;
    dom.deckTimeBadge.textContent = `${inc.start_clock} — ${inc.end_clock} UTC (${inc._phase.name} • ${Math.round(inc._alt).toLocaleString()} FT)`;
    dom.deckSeverityBadge.textContent = inc.severity;
    dom.deckSeverityBadge.className = `incident-crit-badge ${inc.severity.toLowerCase()}`;

    // 1. Overview Specification Matrix
    dom.deckSpecsMatrix.innerHTML = `
      <div class="spec-cell"><span class="spec-k">DATE</span><span class="spec-v">2032-06-18</span></div>
      <div class="spec-cell"><span class="spec-k">FLIGHT PHASE</span><span class="spec-v" style="color:var(--cyan)">${inc._phase.name} (${Math.round(inc._alt).toLocaleString()} FT)</span></div>
      <div class="spec-cell"><span class="spec-k">DURATION</span><span class="spec-v">${inc.duration_sec}s</span></div>
      <div class="spec-cell"><span class="spec-k">AFFECTED NODES</span><span class="spec-v">${inc.nodes.join(', ')}</span></div>
      <div class="spec-cell"><span class="spec-k">DISCRETE EVENTS</span><span class="spec-v">${inc.event_count}</span></div>
      <div class="spec-cell"><span class="spec-k">SEVERITY RATING</span><span class="spec-v" style="color:var(--${inc.severity === 'CRITICAL' ? 'critical' : (inc.severity === 'WARNING' ? 'warning' : 'routine')})">${inc.severity}</span></div>
    `;

    // 2. Executive Forensic Narrative
    dom.deckExecNarrative.innerHTML = formatMarkdownWithCitations(inc.executive_summary || 'No narrative provided.');

    // 3. Root Cause Trigger & Mechanism
    dom.deckRcaDescription.innerHTML = formatMarkdownWithCitations(inc.root_cause || 'Root cause under investigation.');

    // 4. System Impact & Recommendations
    dom.deckImpactText.innerHTML = formatMarkdownWithCitations(inc.system_impact || 'Impact analysis pending.');
    dom.deckRecsText.innerHTML = formatMarkdownWithCitations(inc.corrective_actions || 'Corrective actions pending.');

    // 5. Failure Cascade Domino Sequence
    renderCascadeSequence(inc);

    // 6. Black Box Raw Facts & Sensor Telemetry (Unified into Dossier)
    renderDossierRawFacts(inc);
  }

  function renderCascadeSequence(inc) {
    dom.deckCascadeFlowchart.innerHTML = '';

    const lines = (inc.cascade_sequence || '').split('\n').filter(l => l.trim().length > 0);
    dom.deckCascadeCount.textContent = `${lines.length} Cascading Steps`;

    if (lines.length === 0) {
      dom.deckCascadeFlowchart.innerHTML = '<div class="empty-state">No cascade sequence records parsed.</div>';
      return;
    }

    lines.forEach((line, idx) => {
      // Step card
      const stepCard = document.createElement('div');
      stepCard.className = 'flow-step-card';
      stepCard.dataset.stepIndex = idx;

      // Extract timestamp or title if present: e.g. "1. **[09:00:31] Initiation:** ..."
      let stepNum = idx + 1;
      let stepTime = inc.start_clock;
      let text = line.replace(/^\d+\.\s*/, '').trim();

      const timeMatch = text.match(/\[(\d{2}:\d{2}:\d{2})\]/);
      if (timeMatch) {
        stepTime = timeMatch[1];
        text = text.replace(timeMatch[0], '').trim();
      }

      // Check node affiliation
      let nodeTag = 'AVIONICS BUS';
      for (const n of inc.nodes) {
        if (line.includes(n)) {
          nodeTag = n;
          break;
        }
      }

      stepCard.innerHTML = `
        <div class="step-card-header">
          <span class="step-badge">STEP ${stepNum}</span>
          <span class="step-time">⏱ ${stepTime}</span>
        </div>
        <div class="step-node-badge">${nodeTag}</div>
        <div class="step-body-text">${formatMarkdownWithCitations(text)}</div>
      `;

      dom.deckCascadeFlowchart.appendChild(stepCard);

      // Add connecting arrow if not last
      if (idx < lines.length - 1) {
        const arrow = document.createElement('div');
        arrow.className = 'flow-connector-arrow';
        arrow.innerHTML = '➔';
        dom.deckCascadeFlowchart.appendChild(arrow);
      }
    });
  }

  // Play Cascade Animation sequentially
  function playCascadeAnimation() {
    const cards = dom.deckCascadeFlowchart.querySelectorAll('.flow-step-card');
    if (!cards || cards.length === 0) return;

    cards.forEach(c => c.classList.remove('pulse-active'));

    let current = 0;
    const interval = setInterval(() => {
      if (current > 0) {
        cards[current - 1].classList.remove('pulse-active');
      }
      if (current < cards.length) {
        cards[current].classList.add('pulse-active');
        cards[current].scrollIntoView({ behavior: 'smooth', block: 'nearest', inline: 'center' });
        current++;
      } else {
        clearInterval(interval);
      }
    }, 600);
  }

  // --------------------------------------------------------------------------
  // 6B. UNIFIED DOSSIER: SECTION 6 RAW FACTS RENDERER
  // --------------------------------------------------------------------------
  function renderDossierRawFacts(inc) {
    if (!inc || !inc.events || inc.events.length === 0) {
      if (dom.dossierSummaryHeadline) dom.dossierSummaryHeadline.textContent = 'No discrete event records attached.';
      if (dom.dossierTelemetryTbody) dom.dossierTelemetryTbody.innerHTML = '<tr><td colspan="4" class="empty-cell">No telemetry events found.</td></tr>';
      return;
    }

    const totalEvents = inc.events.length;
    state.selectedEventIndex = Math.max(0, Math.min(totalEvents - 1, state.selectedEventIndex));
    const ev = inc.events[state.selectedEventIndex];

    if (dom.dossierFramePos) dom.dossierFramePos.textContent = `Frame ${state.selectedEventIndex + 1} of ${totalEvents}`;
    if (dom.dossierNodeBadge) dom.dossierNodeBadge.textContent = ev.node_id || 'UNKNOWN';
    if (dom.dossierFamilyBadge) dom.dossierFamilyBadge.textContent = ev.log_family || 'Telemetry Frame';
    if (dom.dossierTimeBadge) dom.dossierTimeBadge.textContent = ev.time_str || ev.timestamp || 'N/A';
    if (dom.dossierSummaryHeadline) dom.dossierSummaryHeadline.textContent = ev.event_summary || 'Discrete avionics telemetry frame';

    const citation = `[Source: ${ev.source_file} | Seq: ${ev.sequence_id} | UUID: ${ev.event_id}]`;
    if (dom.dossierCitationTag) {
      dom.dossierCitationTag.textContent = citation;
      dom.dossierCitationTag.dataset.rawCitation = citation;
    }

    // Decoded key-value parameters in Section 6 table
    renderDossierTelemetryParams(ev.raw_payload);
  }

  function renderDossierTelemetryParams(payload) {
    if (!dom.dossierTelemetryTbody) return;
    dom.dossierTelemetryTbody.innerHTML = '';

    if (!payload || typeof payload !== 'object') {
      dom.dossierTelemetryTbody.innerHTML = '<tr><td colspan="4" class="empty-cell">No decoded parameters.</td></tr>';
      if (dom.dossierParamCount) dom.dossierParamCount.textContent = '0 Parameters';
      return;
    }

    const flatParams = flattenObject(payload);
    const keys = Object.keys(flatParams);
    if (dom.dossierParamCount) dom.dossierParamCount.textContent = `${keys.length} Decoded Parameters`;

    keys.forEach((k) => {
      const v = flatParams[k];
      const tr = document.createElement('tr');

      let type = typeof v;
      let parity = 'VALID';
      let parityClass = 'parity-valid';

      if (v === '-' || v === null || v === undefined) {
        type = 'N/A';
        parity = 'INACTIVE';
        parityClass = 'parity-dim';
      } else if (String(v).toLowerCase().includes('fail') || String(v).toLowerCase().includes('unstable') || String(v).toLowerCase().includes('err')) {
        parity = 'FAULT';
        parityClass = 'parity-err';
      }

      tr.innerHTML = `
        <td class="param-key-cell" style="padding:6px 10px; font-family:var(--font-mono); color:var(--text-muted);">${escapeHtml(k)}</td>
        <td class="param-val-cell" style="padding:6px 10px; font-family:var(--font-mono); font-weight:700; color:#fff;">${escapeHtml(String(v))}</td>
        <td class="param-type-cell" style="padding:6px 10px; font-family:var(--font-mono); font-size:0.65rem; color:var(--text-dim);">${type.toUpperCase()}</td>
        <td class="param-parity-cell" style="padding:6px 10px;"><span class="parity-pill ${parityClass}">${parity}</span></td>
      `;

      dom.dossierTelemetryTbody.appendChild(tr);
    });
  }

  // --------------------------------------------------------------------------
  // 7. LEVEL 3: RAW TELEMETRY & BLACK BOX TERMINAL
  // --------------------------------------------------------------------------
  function populateTelemetryTerminal() {
    const inc = state.selectedIncident;
    if (!inc) return;

    dom.termClusterRef.textContent = `${inc.cluster_id} (#${String(inc.index).padStart(3, '0')})`;
    renderCurrentEvent();
  }

  function renderCurrentEvent() {
    const inc = state.selectedIncident;
    if (!inc || !inc.events || inc.events.length === 0) {
      dom.termSummaryHeadline.textContent = 'No discrete event records attached.';
      dom.termTelemetryTbody.innerHTML = '<tr><td colspan="4" class="empty-cell">No telemetry events found.</td></tr>';
      dom.termRawJson.textContent = '{}';
      return;
    }

    const totalEvents = inc.events.length;
    state.selectedEventIndex = Math.max(0, Math.min(totalEvents - 1, state.selectedEventIndex));
    const ev = inc.events[state.selectedEventIndex];

    dom.termEventPos.textContent = `Event ${state.selectedEventIndex + 1} of ${totalEvents}`;
    dom.termEventRef.textContent = `Seq ID #${ev.sequence_id || 'N/A'}`;
    dom.termNodeBadge.textContent = ev.node_id || 'UNKNOWN';
    dom.termFamilyBadge.textContent = ev.log_family || 'Telemetry Frame';
    dom.termTimeBadge.textContent = ev.time_str || ev.timestamp || 'N/A';
    dom.termOccBadge.textContent = `${ev.occurrences || 1} Occurrences`;
    dom.termSummaryHeadline.textContent = ev.event_summary || 'Discrete avionics telemetry frame';

    // Citation badge
    const citation = `[Source: ${ev.source_file} | Seq: ${ev.sequence_id} | UUID: ${ev.event_id}]`;
    dom.termCitationTag.textContent = citation;
    dom.termCitationTag.dataset.rawCitation = citation;

    // Syntax-highlighted raw JSON payload
    dom.termRawJson.textContent = JSON.stringify(ev.raw_payload || ev, null, 2);

    // Decoded Telemetry Key-Value Table
    renderTelemetryParameters(ev.raw_payload);
  }

  function renderTelemetryParameters(payload) {
    dom.termTelemetryTbody.innerHTML = '';
    if (!payload || typeof payload !== 'object') {
      dom.termTelemetryTbody.innerHTML = '<tr><td colspan="4" class="empty-cell">No decoded parameters.</td></tr>';
      dom.termParamCount.textContent = '0 Parameters';
      return;
    }

    const flatParams = flattenObject(payload);
    const keys = Object.keys(flatParams);
    dom.termParamCount.textContent = `${keys.length} Decoded Parameters`;

    keys.forEach((k) => {
      const v = flatParams[k];
      const tr = document.createElement('tr');

      let type = typeof v;
      let parity = 'VALID';
      let parityClass = 'parity-valid';

      if (v === '-' || v === null || v === undefined) {
        type = 'N/A';
        parity = 'INACTIVE';
        parityClass = 'parity-dim';
      } else if (String(v).toLowerCase().includes('fail') || String(v).toLowerCase().includes('unstable') || String(v).toLowerCase().includes('err')) {
        parity = 'FAULT';
        parityClass = 'parity-err';
      }

      tr.innerHTML = `
        <td class="param-key-cell">${escapeHtml(k)}</td>
        <td class="param-val-cell">${escapeHtml(String(v))}</td>
        <td class="param-type-cell">${type.toUpperCase()}</td>
        <td class="param-parity-cell"><span class="parity-pill ${parityClass}">${parity}</span></td>
      `;

      dom.termTelemetryTbody.appendChild(tr);
    });
  }

  // Flatten nested JSON for flat avionics table inspection
  function flattenObject(obj, prefix = '') {
    const res = {};
    for (const key in obj) {
      if (Object.prototype.hasOwnProperty.call(obj, key)) {
        const val = obj[key];
        const newKey = prefix ? `${prefix}.${key}` : key;
        if (typeof val === 'object' && val !== null && !Array.isArray(val)) {
          Object.assign(res, flattenObject(val, newKey));
        } else {
          res[newKey] = val;
        }
      }
    }
    return res;
  }

  // --------------------------------------------------------------------------
  // 8. OMNI-SEARCH & SEVERITY / PHASE FILTERS
  // --------------------------------------------------------------------------

  function updateIncidentFilters() {
    const dots = dom.dotsGroup.querySelectorAll('.incident-dot-group');
    const query = state.searchQuery.toLowerCase().trim();
    let matchingCount = 0;

    dots.forEach((dotEl) => {
      const idx = Number(dotEl.dataset.index);
      const inc = state.incidents.find(i => i.index === idx);
      if (!inc) return;

      // Severity check
      const matchesSev = (state.filterSeverity === 'all' || inc.severity === state.filterSeverity);

      // Search query check
      let matchesQuery = true;
      if (query.length > 0) {
        const str = `${inc.cluster_id} ${inc.executive_summary} ${inc.root_cause} ${inc.nodes.join(' ')} ${inc.start_clock}`.toLowerCase();
        matchesQuery = str.includes(query);
      }

      const isVisible = matchesSev && matchesQuery;
      dotEl.classList.toggle('dimmed', !isVisible);
      dotEl.classList.toggle('highlighted', query.length > 0 && matchesQuery);

      if (isVisible) matchingCount++;
    });

    dom.hudIncidentStat.textContent = `${matchingCount} of ${state.incidents.length} Incidents Active`;
  }

  // --------------------------------------------------------------------------
  // 8B. CANVAS INTERACTIVE ZOOM & PAN (SEPARATE CLOSE CLUSTERS)
  // --------------------------------------------------------------------------
  // --------------------------------------------------------------------------
  // 8B. CANVAS INTERACTIVE ZOOM & PAN (UNIFORM 2D ASPECT RATIO PRESERVATION)
  // --------------------------------------------------------------------------
  const camera = {
    zoom: 1.0,
    minZoom: 1.0,
    maxZoom: 8.0,
    baseW: 2000,
    baseH: 600,
    viewX: 0,
    viewY: 0,
    isDragging: false,
    dragStartX: 0,
    dragStartY: 0,
    dragStartViewX: 0,
    dragStartViewY: 0,
    hasDragged: false
  };

  function setCanvasZoom(newZoom, mouseRatioX = 0.5, mouseRatioY = 0.5) {
    const prevZoom = camera.zoom;
    const clampedZoom = Math.max(camera.minZoom, Math.min(camera.maxZoom, newZoom));
    if (Math.abs(clampedZoom - camera.zoom) < 0.001) return;

    const prevViewW = camera.baseW / prevZoom;
    const prevViewH = camera.baseH / prevZoom;
    const newViewW = camera.baseW / clampedZoom;
    const newViewH = camera.baseH / clampedZoom;

    // Anchor zoom around cursor position ratio (maintaining exact 2000:600 aspect ratio)
    const currentAnchorX = camera.viewX + prevViewW * mouseRatioX;
    const currentAnchorY = camera.viewY + prevViewH * mouseRatioY;

    let newViewX = currentAnchorX - newViewW * mouseRatioX;
    let newViewY = currentAnchorY - newViewH * mouseRatioY;

    newViewX = Math.max(0, Math.min(camera.baseW - newViewW, newViewX));
    newViewY = Math.max(0, Math.min(camera.baseH - newViewH, newViewY));

    camera.zoom = clampedZoom;
    camera.viewX = newViewX;
    camera.viewY = newViewY;

    updateCanvasViewBox();
  }

  function updateCanvasViewBox() {
    const viewW = camera.baseW / camera.zoom;
    const viewH = camera.baseH / camera.zoom;
    dom.flightSvg.setAttribute('viewBox', `${camera.viewX.toFixed(1)} ${camera.viewY.toFixed(1)} ${viewW.toFixed(1)} ${viewH.toFixed(1)}`);
    if (dom.zoomFactorBadge) {
      dom.zoomFactorBadge.textContent = `${camera.zoom.toFixed(1)}x`;
    }
    if (dom.flightCanvasViewport) {
      dom.flightCanvasViewport.style.cursor = camera.zoom > 1 ? (camera.isDragging ? 'grabbing' : 'grab') : 'default';
    }

    // Refresh hover tooltip position if visible
    if (state.hoveredIncident && dom.hoverHud && dom.hoverHud.classList.contains('visible')) {
      showIncidentHoverHud(state.hoveredIncident);
    }
  }

  function resetCanvasZoom() {
    camera.zoom = 1.0;
    camera.viewX = 0;
    camera.viewY = 0;
    updateCanvasViewBox();
  }

  // --------------------------------------------------------------------------
  // 9. EVENT LISTENERS & KEYBOARD SHORTCUTS
  // --------------------------------------------------------------------------
  function attachEventListeners() {
    // Zoom Breadcrumbs
    dom.btnGotoL1.addEventListener('click', () => setZoomLevel(1));
    dom.btnGotoL2.addEventListener('click', () => setZoomLevel(2));
    dom.btnGotoL3.addEventListener('click', () => setZoomLevel(3));

    // Canvas Zoom Controls (Buttons, Wheel, Pan)
    if (dom.btnZoomIn) {
      dom.btnZoomIn.addEventListener('click', (e) => {
        e.stopPropagation();
        setCanvasZoom(camera.zoom * 1.4, 0.5, 0.5);
      });
    }
    if (dom.btnZoomOut) {
      dom.btnZoomOut.addEventListener('click', (e) => {
        e.stopPropagation();
        setCanvasZoom(camera.zoom / 1.4, 0.5, 0.5);
      });
    }
    if (dom.btnZoomReset) {
      dom.btnZoomReset.addEventListener('click', (e) => {
        e.stopPropagation();
        resetCanvasZoom();
      });
    }

    // Canvas Mouse Wheel Zoom (Uniform 2D Zoom preserving perfect aspect ratio)
    dom.flightCanvasViewport.addEventListener('wheel', (e) => {
      e.preventDefault();
      const rect = dom.flightCanvasViewport.getBoundingClientRect();
      const mouseRatioX = Math.max(0, Math.min(1, (e.clientX - rect.left) / rect.width));
      const mouseRatioY = Math.max(0, Math.min(1, (e.clientY - rect.top) / rect.height));
      const factor = e.deltaY < 0 ? 1.25 : 0.8;
      setCanvasZoom(camera.zoom * factor, mouseRatioX, mouseRatioY);
    }, { passive: false });

    // Canvas Mousedown for Panning
    dom.flightCanvasViewport.addEventListener('mousedown', (e) => {
      if (e.target.closest('.canvas-zoom-toolbar') || e.target.closest('#incident-hover-hud')) return;

      camera.isDragging = true;
      camera.hasDragged = false;
      camera.dragStartX = e.clientX;
      camera.dragStartY = e.clientY;
      camera.dragStartViewX = camera.viewX;
      camera.dragStartViewY = camera.viewY;
      if (camera.zoom > 1.0) {
        dom.flightCanvasViewport.style.cursor = 'grabbing';
      }
    });

    // High-Precision Proximity Hover Engine (ZERO JITTER / ZERO FLICKER)
    dom.flightCanvasViewport.addEventListener('mousemove', (e) => {
      if (camera.isDragging) {
        const dx = e.clientX - camera.dragStartX;
        const dy = e.clientY - camera.dragStartY;
        if (Math.abs(dx) > 3 || Math.abs(dy) > 3) {
          camera.hasDragged = true;
        }
        if (camera.zoom > 1.0) {
          const rect = dom.flightCanvasViewport.getBoundingClientRect();
          const viewW = camera.baseW / camera.zoom;
          const viewH = camera.baseH / camera.zoom;
          const svgDx = (dx / rect.width) * viewW;
          const svgDy = (dy / rect.height) * viewH;
          camera.viewX = Math.max(0, Math.min(camera.baseW - viewW, camera.dragStartViewX - svgDx));
          camera.viewY = Math.max(0, Math.min(camera.baseH - viewH, camera.dragStartViewY - svgDy));
          updateCanvasViewBox();
          return;
        }
      }

      // Convert Screen Mouse Position to SVG Coordinates via Transformation Matrix
      try {
        const ctm = dom.flightSvg.getScreenCTM();
        if (!ctm) return;
        const pt = dom.flightSvg.createSVGPoint();
        pt.x = e.clientX;
        pt.y = e.clientY;
        const svgP = pt.matrixTransform(ctm.inverse());

        const rect = dom.flightCanvasViewport.getBoundingClientRect();
        // Screen snap radius ~24px converted to SVG coordinate space
        const snapRadiusSvg = 24 * (camera.baseW / (camera.zoom * rect.width));
        const snapRadiusSq = snapRadiusSvg * snapRadiusSvg;

        let closestInc = null;
        let minDistanceSq = Infinity;

        for (let i = 0; i < state.incidents.length; i++) {
          const inc = state.incidents[i];
          const dx = inc._x - svgP.x;
          const dy = inc._y - svgP.y;
          const distSq = dx * dx + dy * dy;
          if (distSq < minDistanceSq) {
            minDistanceSq = distSq;
            closestInc = inc;
          }
        }

        // Hysteresis threshold: only switch target if clearly closer (eliminates flicker)
        if (state.hoveredIncident && closestInc && state.hoveredIncident !== closestInc) {
          const curDx = state.hoveredIncident._x - svgP.x;
          const curDy = state.hoveredIncident._y - svgP.y;
          const curDistSq = curDx * curDx + curDy * curDy;
          if (minDistanceSq > curDistSq * 0.65) {
            closestInc = state.hoveredIncident;
            minDistanceSq = curDistSq;
          }
        }

        if (closestInc && minDistanceSq <= snapRadiusSq) {
          if (state.hoveredIncident !== closestInc) {
            const prevEl = dom.dotsGroup.querySelector('.incident-dot-group.hovered');
            if (prevEl) prevEl.classList.remove('hovered');

            const el = dom.dotsGroup.querySelector(`[data-index="${closestInc.index}"]`);
            if (el) el.classList.add('hovered');

            showIncidentHoverHud(closestInc);
          }
          dom.flightCanvasViewport.style.cursor = 'pointer';
        } else {
          if (state.hoveredIncident) {
            hideIncidentHoverHud();
          }
          dom.flightCanvasViewport.style.cursor = camera.zoom > 1.0 ? 'grab' : 'default';
        }
      } catch (err) {
        // Fallback safely
      }
    });

    dom.flightCanvasViewport.addEventListener('mouseleave', () => {
      hideIncidentHoverHud();
      if (camera.isDragging) {
        camera.isDragging = false;
        dom.flightCanvasViewport.style.cursor = camera.zoom > 1.0 ? 'grab' : 'default';
      }
    });

    dom.flightCanvasViewport.addEventListener('click', (e) => {
      if (e.target.closest('.canvas-zoom-toolbar')) return;
      if (camera.hasDragged) {
        camera.hasDragged = false;
        return; // Don't trigger click after a pan gesture
      }

      // If clicked near an incident dot, select and smoothly transition to it
      if (state.hoveredIncident) {
        selectAndZoomToIncident(state.hoveredIncident);
      }
    });

    dom.hoverHud.addEventListener('click', () => {
      if (state.hoveredIncident) {
        selectAndZoomToIncident(state.hoveredIncident);
      }
    });

    // Action Buttons in Level 2
    dom.btnPrevIncident.addEventListener('click', () => {
      if (!state.selectedIncident) return;
      const curIdx = state.selectedIncident.index;
      if (curIdx > 1) {
        const prev = state.incidents.find(i => i.index === curIdx - 1);
        if (prev) {
          state.selectedIncident = prev;
          state.selectedEventIndex = 0;
          populateNarrationDeck();
        }
      }
    });

    dom.btnNextIncident.addEventListener('click', () => {
      if (!state.selectedIncident) return;
      const curIdx = state.selectedIncident.index;
      if (curIdx < state.incidents.length) {
        const next = state.incidents.find(i => i.index === curIdx + 1);
        if (next) {
          state.selectedIncident = next;
          state.selectedEventIndex = 0;
          populateNarrationDeck();
        }
      }
    });

    dom.btnReplayCascade.addEventListener('click', playCascadeAnimation);
    dom.btnZoomToTelemetry.addEventListener('click', () => setZoomLevel(3));

    // Section 6: Unified Dossier Raw Facts in Level 2
    if (dom.btnJumpToRawFacts) {
      dom.btnJumpToRawFacts.addEventListener('click', () => {
        if (dom.dossierRawFactsSection) {
          dom.dossierRawFactsSection.scrollIntoView({ behavior: 'smooth' });
        }
      });
    }

    if (dom.dossierPrevFrame) {
      dom.dossierPrevFrame.addEventListener('click', () => {
        if (state.selectedEventIndex > 0) {
          state.selectedEventIndex--;
          renderDossierRawFacts(state.selectedIncident);
        }
      });
    }

    if (dom.dossierNextFrame) {
      dom.dossierNextFrame.addEventListener('click', () => {
        const total = state.selectedIncident?.events?.length || 0;
        if (state.selectedEventIndex < total - 1) {
          state.selectedEventIndex++;
          renderDossierRawFacts(state.selectedIncident);
        }
      });
    }

    if (dom.dossierBtnCopyCitation) {
      dom.dossierBtnCopyCitation.addEventListener('click', () => {
        const text = dom.dossierCitationTag?.dataset?.rawCitation || dom.dossierCitationTag?.textContent || '';
        navigator.clipboard.writeText(text).then(() => {
          dom.dossierBtnCopyCitation.textContent = '✓ COPIED';
          setTimeout(() => dom.dossierBtnCopyCitation.textContent = '📋 COPY VERIFIABLE CITATION', 1800);
        });
      });
    }

    // Full Report Modal
    dom.btnOpenRawModal.addEventListener('click', () => {
      if (!state.selectedIncident) return;
      dom.modalHeading.textContent = `Full Forensic Dossier: ${state.selectedIncident.cluster_id}`;
      dom.modalMarkdownContainer.innerHTML = formatMarkdownWithCitations(state.selectedIncident.full_markdown || 'No full report generated.');
      dom.reportModal.classList.add('open');
    });

    dom.btnModalClose.addEventListener('click', () => dom.reportModal.classList.remove('open'));
    dom.btnModalDismiss.addEventListener('click', () => dom.reportModal.classList.remove('open'));
    dom.btnCopyFullMarkdown.addEventListener('click', () => {
      if (state.selectedIncident && state.selectedIncident.full_markdown) {
        navigator.clipboard.writeText(state.selectedIncident.full_markdown).then(() => {
          dom.btnCopyFullMarkdown.textContent = '✓ COPIED!';
          setTimeout(() => dom.btnCopyFullMarkdown.textContent = 'COPY MARKDOWN', 2000);
        });
      }
    });

    // Event Pagination in Level 3
    dom.termPrevEvent.addEventListener('click', () => {
      if (state.selectedEventIndex > 0) {
        state.selectedEventIndex--;
        renderCurrentEvent();
      }
    });

    dom.termNextEvent.addEventListener('click', () => {
      const total = state.selectedIncident?.events?.length || 0;
      if (state.selectedEventIndex < total - 1) {
        state.selectedEventIndex++;
        renderCurrentEvent();
      }
    });

    // Citation Copy to Clipboard
    dom.btnCopyCitation.addEventListener('click', () => {
      const text = dom.termCitationTag.dataset.rawCitation || dom.termCitationTag.textContent;
      navigator.clipboard.writeText(text).then(() => {
        dom.btnCopyCitation.textContent = '✓ COPIED';
        setTimeout(() => dom.btnCopyCitation.textContent = 'COPY CITATION', 1800);
      });
    });

    // Omni Search
    dom.omniSearch.addEventListener('input', (e) => {
      state.searchQuery = e.target.value;
      updateIncidentFilters();
    });

    dom.btnClearSearch.addEventListener('click', () => {
      dom.omniSearch.value = '';
      state.searchQuery = '';
      updateIncidentFilters();
    });

    // Severity Filters
    dom.filterChips.forEach(chip => {
      chip.addEventListener('click', () => {
        dom.filterChips.forEach(c => c.classList.remove('active'));
        chip.classList.add('active');
        state.filterSeverity = chip.dataset.filter;
        updateIncidentFilters();
      });
    });

    // Global Keyboard Shortcuts
    window.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') {
        if (dom.reportModal.classList.contains('open')) {
          dom.reportModal.classList.remove('open');
        } else if (state.currentZoomLevel === 3) {
          setZoomLevel(2);
        } else if (state.currentZoomLevel === 2) {
          setZoomLevel(1);
        }
      } else if (e.key === ' ' && e.target.tagName !== 'INPUT') {
        // Spacebar toggles replay if in Level 1
        if (state.currentZoomLevel === 1) {
          e.preventDefault();
          toggleMissionReplay();
        }
      } else if (e.key === 'ArrowRight' && state.currentZoomLevel === 3) {
        dom.termNextEvent.click();
      } else if (e.key === 'ArrowLeft' && state.currentZoomLevel === 3) {
        dom.termPrevEvent.click();
      }
    });
  }

  // --------------------------------------------------------------------------
  // 10. FORMATTING UTILITIES (CITATIONS & MARKDOWN)
  // --------------------------------------------------------------------------

  // Formats text into HTML with clickable citation tags
  function formatMarkdownWithCitations(text) {
    if (!text) return '';

    // Sanitize basic HTML
    let html = escapeHtml(text);

    // Convert markdown bold **text** to <strong>
    html = html.replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>');

    // Convert markdown headers
    html = html.replace(/^### (.*$)/gim, '<h3 class="md-h3">$1</h3>');
    html = html.replace(/^## (.*$)/gim, '<h2 class="md-h2">$1</h2>');
    html = html.replace(/^# (.*$)/gim, '<h1 class="md-h1">$1</h1>');

    // Convert markdown bullets
    html = html.replace(/^\* (.*$)/gim, '<li class="md-li">$1</li>');
    html = html.replace(/^[0-9]+\. (.*$)/gim, '<li class="md-oli">$1</li>');

    // Wrap list items
    html = html.replace(/(<li class="md-li">[\s\S]*?<\/li>)/g, '<ul class="md-ul">$1</ul>');
    html = html.replace(/(<li class="md-oli">[\s\S]*?<\/li>)/g, '<ol class="md-ol">$1</ol>');

    // Convert citation tags: `[Source: ... | Seq: ... | UUID: ...]` into glowing copyable tags
    const citationRegex = /`?\[Source:\s*([^|\]]+)\s*\|\s*Seq:\s*([^|\]]+)\s*\|\s*UUID:\s*([^|\]]+)\]`?/gi;
    html = html.replace(citationRegex, (match, src, seq, uuid) => {
      const fullCitation = `[Source: ${src.trim()} | Seq: ${seq.trim()} | UUID: ${uuid.trim()}]`;
      return `<span class="forensic-citation-tag" data-citation="${escapeHtml(fullCitation)}" title="Click to copy verifiable forensic citation">🔍 ${escapeHtml(src.trim())} | Seq ${escapeHtml(seq.trim())}</span>`;
    });

    // Paragraph linebreaks
    html = html.replace(/\n\n/g, '<br><br>');

    return html;
  }

  function escapeHtml(str) {
    if (!str) return '';
    return String(str)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#39;');
  }

  // Document ready trigger
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

})();
