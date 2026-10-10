# AVIATION FORENSIC INVESTIGATION REPORT: cluster-ae64d7f5

## 1. Incident Overview

| Date | Duration | Affected Nodes | Total Events | Severity Rating |
| :--- | :--- | :--- | :--- | :--- |
| 2032-06-18 | 11:17:51 to 11:18:00 | NODE_A, NODE_C | 28 | **ROUTINE** |

## 2. Executive Summary
On 2032-06-18 during the operational window 11:17:51 to 11:18:00, an avionics incident comprising 28 correlated events was recorded across redundant flight management nodes NODE_A, NODE_C. The multi-node sequence completed with confirmed cross-channel synchronization and software dispatch.

## 3. Root Cause Analysis (Primary Trigger)
The initiating trigger for this incident occurred at 11:17:51 on **NODE_A** as a `Operator Interaction`.

**Initiating Event Details:** Operator interaction select vertical Revision revise pt | Dual mode: Dual | Master status: Master | Functional position: Captain | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 343.001953 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | Flight plan source - high: Active | Flight plan source - low: ActPrimary | Display system source: Operator interaction display system right | [Operator Interaction Event: Operator interaction select vertical Revision revise pt | Event status: Operator interaction entered | Event value: 131098]

The initial sequence began with a pilot CDU action on **NODE_A** (Operator interaction select vertical Revision revise pt | Dual mode: Dual | Master status: Master | Functional position: Captain | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 343.001953 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | Flight plan source - high: Active | Flight plan source - low: ActPrimary | Display system source: Operator interaction display system right | [Operator Interaction Event: Operator interaction select vertical Revision revise pt | Event status: Operator interaction entered | Event value: 131098]). This operator entry placed demands on the FMS software architecture, triggering subsequent software dispatching and cross-channel bus verification.

**Verifiable Initiating Record:**
[Source: NODE_A_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 485 | UUID: d2389820-5336-4818-9541-9bb857163db9]

## 4. Failure Cascade & Propagation Sequence
1. **[11:17:51] NODE_A (Operator Interaction)**: Operator interaction select vertical Revision revise pt | Dual mode: Dual | Master status: Master | Functional position: Captain | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 343.001953 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | Flight plan source - high: Active | Flight plan source - low: ActPrimary | Display system source: Operator interaction display system right | [Operator Interaction Event: Operator interaction select vertical Revision revise pt | Event status: Operator interaction entered | Event value: 131098]
   [Source: NODE_A_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 485 | UUID: d2389820-5336-4818-9541-9bb857163db9]

2. **[11:17:51] NODE_A (Operator Interaction)**: Operator Interaction Event | Dual mode: Dual | Master status: Master | Functional position: Captain | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 343.001953 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [Fix ident: Denut]
   [Source: NODE_A_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 486 | UUID: dc64e8ee-098d-410c-8efa-fead7f4622c2]

3. **[11:17:51] NODE_A (Software Event)**: Software Event: Operator interaction event identifier | Data Identifier: Operator interaction event identifier | Data Format: Format operator interaction event | Left FMS node: Master | Center FMS node: Standby | Right FMS node: Spare | Dual: Dual | [Event identifier: Operator interaction select vertical Revision revise pt | Source fms node: First officer]
   [Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 195 | UUID: 10ffd4d4-da4f-4f28-bcf6-b5e921574a5c]

4. **[11:17:52] NODE_C (Operator Interaction)**: Operator interaction select vertical Revision revise pt | Dual mode: Dual | Master status: Spare | Functional position: First officer | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 343.001923 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | Flight plan source - high: Active | Flight plan source - low: ActPrimary | Display system source: Operator interaction display system right | [Operator Interaction Event: Operator interaction select vertical Revision revise pt | Event status: Operator interaction entered | Event value: 131098]
   [Source: NODE_C_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 489 | UUID: 3c7ff0ac-068b-4cf3-9503-f3579d88cfc7]

5. **[11:17:52] NODE_C (Operator Interaction)**: Operator Interaction Event | Dual mode: Dual | Master status: Spare | Functional position: First officer | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 343.001923 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [Fix ident: Denut]
   [Source: NODE_C_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 490 | UUID: d534f478-50e9-4dfa-9dc1-f22838bd8599]

6. **[11:17:52] NODE_C (Software Event)**: Software Event: Operator interaction event identifier | Data Identifier: Operator interaction event identifier | Data Format: Format operator interaction event | Left FMS node: Master | Center FMS node: Standby | Right FMS node: Spare | Dual: Dual | [Event identifier: Operator interaction select vertical Revision revise pt | Source fms node: First officer]
   [Source: NODE_C_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 199 | UUID: c6007481-b3c7-4158-9b2b-cca490a3069e]

7. **[11:17:55] NODE_A (Operator Interaction)**: Operator interaction enter step | Dual mode: Dual | Master status: Master | Functional position: Captain | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 343.001678 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | Flight plan source - high: Active | Flight plan source - low: ActPrimary | Display system source: Operator interaction display system right | [Operator Interaction Event: Operator interaction enter step | Event status: Operator interaction entered | Event value: 17826462]
   [Source: NODE_A_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 488 | UUID: 46913eaa-aa65-4f5b-a4d8-96ded8c6cda6]

8. **[11:17:55] NODE_A (Operator Interaction)**: Operator Interaction Event | Dual mode: Dual | Master status: Master | Functional position: Captain | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 343.001678 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [Fix ident: Denut]
   [Source: NODE_A_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 489 | UUID: c3720151-876e-4781-b924-84ec731475a6]

9. **[11:17:55] NODE_A (Software Event)**: Software Event: Operator interaction event identifier | Data Identifier: Operator interaction event identifier | Data Format: Format operator interaction event | Left FMS node: Master | Center FMS node: Standby | Right FMS node: Spare | Dual: Dual | [Event identifier: Operator interaction enter step | Source fms node: First officer]
   [Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 196 | UUID: b8ba4dcb-d656-406d-af18-4d0cc9967046]

10. **[11:17:56] NODE_A (Operator Interaction)**: Operator Interaction Event | Dual mode: Dual | Master status: Master | Functional position: Captain | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 343.001678 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [FMS Operational Event: Optimized Step Selected | FMS node source: Captain | Event value: 17826504]
   [Source: NODE_A_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 491 | UUID: 5047f899-4cce-499d-a7c1-6cee84d3748d]

11. **[11:17:56] NODE_C (Operator Interaction)**: Operator interaction enter step | Dual mode: Dual | Master status: Spare | Functional position: First officer | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 343.001678 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | Flight plan source - high: Active | Flight plan source - low: ActPrimary | Display system source: Operator interaction display system right | [Operator Interaction Event: Operator interaction enter step | Event status: Operator interaction entered | Event value: 17826462]
   [Source: NODE_C_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 492 | UUID: c14c0f22-2ec8-4061-9624-81451811aeaf]

12. **[11:17:56] NODE_C (Operator Interaction)**: Operator Interaction Event | Dual mode: Dual | Master status: Spare | Functional position: First officer | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 343.001678 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [Fix ident: Denut]
   [Source: NODE_C_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 493 | UUID: c723d153-4d72-4825-a51d-7ec43fc20e41]

13. **[11:17:56] NODE_C (Software Event)**: Software Event: Operator interaction event identifier | Data Identifier: Operator interaction event identifier | Data Format: Format operator interaction event | Left FMS node: Master | Center FMS node: Standby | Right FMS node: Spare | Dual: Dual | [Event identifier: Operator interaction enter step | Source fms node: First officer]
   [Source: NODE_C_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 200 | UUID: 68a49338-665f-4442-ba7e-32f6842c3e1e]

14. **[11:17:57] NODE_A (Operator Interaction)**: Operator Interaction Event | Dual mode: Dual | Master status: Master | Functional position: Captain | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 343.001526 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [FMS Operational Event: Performance Data Changed | FMS node source: Standby | Event value: 131098]
   [Source: NODE_A_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 492 | UUID: 9c665e2f-8533-4744-a94d-a11fa6b3a799]

15. **[11:17:57] NODE_C (Operator Interaction)**: Operator Interaction Event | Dual mode: Dual | Master status: Spare | Functional position: First officer | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 343.001617 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [FMS Operational Event: Optimized Step Selected | FMS node source: Captain | Event value: 17826504]
   [Source: NODE_C_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 495 | UUID: f1bba685-a8f5-4475-a402-f50778863c68]

16. **[11:17:58] NODE_A (Operator Interaction)**: Operator Interaction Event | Dual mode: Dual | Master status: Master | Functional position: Captain | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 343.001526 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [FMS Operational Event: Performance Data Changed | FMS node source: Captain | Event value: 65555]
   [Source: NODE_A_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 493 | UUID: bf6f32bf-9cc8-424c-8dfd-0d1994cc8301]

17. **[11:17:58] NODE_A (Operator Interaction)**: Operator interaction insert temporary | Dual mode: Dual | Master status: Master | Functional position: Captain | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 343.001526 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | Flight plan source - high: Temporary Efb | Flight plan source - low: TmpyPrimary | Display system source: Operator interaction display system right | [Operator Interaction Event: Operator interaction insert temporary | Event status: Operator interaction entered | Event value: 131091]
   [Source: NODE_A_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 494 | UUID: 0f32d920-5c89-4db7-a0d9-374d90d47701]

18. **[11:17:58] NODE_A (Operator Interaction)**: Operator Interaction Event
   [Source: NODE_A_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 495 | UUID: d4ecbe2f-e34b-4e93-ab73-f850869d43bd]

19. **[11:17:58] NODE_A (Software Event)**: Software Event: Operator interaction event identifier | Data Identifier: Operator interaction event identifier | Data Format: Format operator interaction event | Left FMS node: Master | Center FMS node: Standby | Right FMS node: Spare | Dual: Dual | [Event identifier: Operator interaction insert temporary | Source fms node: First officer]
   [Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 197 | UUID: 3ffa58a4-9f53-49b6-bb30-16b794cec0ac]

20. **[11:17:58] NODE_C (Operator Interaction)**: Operator Interaction Event | Dual mode: Dual | Master status: Spare | Functional position: First officer | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 343.001526 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [FMS Operational Event: Performance Data Changed | FMS node source: Standby | Event value: 131098]
   [Source: NODE_C_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 496 | UUID: 13b09f1f-6d9f-4ef4-876c-5acfb8a61e62]

21. **[11:17:59] NODE_A (Operator Interaction)**: Operator Interaction Event | Dual mode: Dual | Master status: Master | Functional position: Captain | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 343.001404 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [FMS Operational Event: Optimized Step Selected | FMS node source: Captain | Event value: 26477079]
   [Source: NODE_A_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 496 | UUID: 0161fed8-5292-4618-942b-2ace60b13ba7]

22. **[11:17:59] NODE_A (Software Event)**: Software Event: Operator interaction event identifier | Data Identifier: Operator interaction event identifier | Data Format: Format operator interaction event | Left FMS node: Master | Center FMS node: Standby | Right FMS node: Spare | Dual: Dual | [Event identifier: Operator interaction insert temporary | Source fms node: First officer]
   [Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 198 | UUID: 7eb97613-43e9-44c9-a26a-9c29f7854dd9]

23. **[11:17:59] NODE_C (Operator Interaction)**: Operator Interaction Event | Dual mode: Dual | Master status: Spare | Functional position: First officer | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 343.001526 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [FMS Operational Event: Performance Data Changed | FMS node source: Captain | Event value: 65555]
   [Source: NODE_C_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 497 | UUID: de61baf4-02d0-418e-bbb4-58870aee3e46]

24. **[11:17:59] NODE_C (Operator Interaction)**: Operator interaction insert temporary | Dual mode: Dual | Master status: Spare | Functional position: First officer | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 343.001526 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | Flight plan source - high: Temporary Efb | Flight plan source - low: TmpyPrimary | Display system source: Operator interaction display system right | [Operator Interaction Event: Operator interaction insert temporary | Event status: Operator interaction entered | Event value: 131091]
   [Source: NODE_C_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 498 | UUID: 71554281-7b16-4185-8889-8aa02cababd7]

25. **[11:17:59] NODE_C (Operator Interaction)**: Operator Interaction Event
   [Source: NODE_C_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 499 | UUID: cb34c115-8938-43db-b607-40c6b3fd1fd1]

26. **[11:17:59] NODE_C (Software Event)**: Software Event: Operator interaction event identifier | Data Identifier: Operator interaction event identifier | Data Format: Format operator interaction event | Left FMS node: Master | Center FMS node: Standby | Right FMS node: Spare | Dual: Dual | [Event identifier: Operator interaction insert temporary | Source fms node: First officer]
   [Source: NODE_C_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 201 | UUID: 511e121a-7b83-4fc2-84b1-d12b5968831c]

27. **[11:18:00] NODE_C (Operator Interaction)**: Operator Interaction Event | Dual mode: Dual | Master status: Spare | Functional position: First officer | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 343.001404 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [FMS Operational Event: Optimized Step Selected | FMS node source: Captain | Event value: 26477079]
   [Source: NODE_C_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 500 | UUID: c066d400-1e46-4c60-87d5-46300fa1395e]

28. **[11:18:00] NODE_C (Software Event)**: Software Event: Operator interaction event identifier | Data Identifier: Operator interaction event identifier | Data Format: Format operator interaction event | Left FMS node: Master | Center FMS node: Standby | Right FMS node: Spare | Dual: Dual | [Event identifier: Operator interaction insert temporary | Source fms node: First officer]
   [Source: NODE_C_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 202 | UUID: 0e98d703-1c41-4946-bd73-b04762025872]

## 5. System Impact Assessment
* **Assessed Severity Rating:** `ROUTINE (Operational Dispatch & Synchronization)`
* **Nodes Involved in Sequence:** NODE_A, NODE_C
* **Total Correlated Audit Records:** 28
* **Redundancy State Degradation:** No (Dual-mode channel redundancy maintained)
* **Subsystem Cold Reboots Observed:** No
* **Operational Mode Context:** The multi-node sequence completed with confirmed cross-channel synchronization and software dispatch.

## 6. Recommended Corrective & Maintenance Actions
1. **Routine Avionics Log Telemetry Verification:** Confirm normal flight plan dispatch and operational status transition parameters.
2. **Periodic Maintenance Cycle:** Continue regular scheduled avionics maintenance intervals.

## 7. Forensic Evidence Citations
- [Source: NODE_A_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 485 | UUID: d2389820-5336-4818-9541-9bb857163db9]
- [Source: NODE_A_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 486 | UUID: dc64e8ee-098d-410c-8efa-fead7f4622c2]
- [Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 195 | UUID: 10ffd4d4-da4f-4f28-bcf6-b5e921574a5c]
- [Source: NODE_C_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 489 | UUID: 3c7ff0ac-068b-4cf3-9503-f3579d88cfc7]
- [Source: NODE_C_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 490 | UUID: d534f478-50e9-4dfa-9dc1-f22838bd8599]
- [Source: NODE_C_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 199 | UUID: c6007481-b3c7-4158-9b2b-cca490a3069e]
- [Source: NODE_A_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 488 | UUID: 46913eaa-aa65-4f5b-a4d8-96ded8c6cda6]
- [Source: NODE_A_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 489 | UUID: c3720151-876e-4781-b924-84ec731475a6]
- [Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 196 | UUID: b8ba4dcb-d656-406d-af18-4d0cc9967046]
- [Source: NODE_A_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 491 | UUID: 5047f899-4cce-499d-a7c1-6cee84d3748d]
- [Source: NODE_C_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 492 | UUID: c14c0f22-2ec8-4061-9624-81451811aeaf]
- [Source: NODE_C_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 493 | UUID: c723d153-4d72-4825-a51d-7ec43fc20e41]
- [Source: NODE_C_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 200 | UUID: 68a49338-665f-4442-ba7e-32f6842c3e1e]
- [Source: NODE_A_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 492 | UUID: 9c665e2f-8533-4744-a94d-a11fa6b3a799]
- [Source: NODE_C_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 495 | UUID: f1bba685-a8f5-4475-a402-f50778863c68]
- [Source: NODE_A_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 493 | UUID: bf6f32bf-9cc8-424c-8dfd-0d1994cc8301]
- [Source: NODE_A_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 494 | UUID: 0f32d920-5c89-4db7-a0d9-374d90d47701]
- [Source: NODE_A_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 495 | UUID: d4ecbe2f-e34b-4e93-ab73-f850869d43bd]
- [Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 197 | UUID: 3ffa58a4-9f53-49b6-bb30-16b794cec0ac]
- [Source: NODE_C_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 496 | UUID: 13b09f1f-6d9f-4ef4-876c-5acfb8a61e62]
- [Source: NODE_A_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 496 | UUID: 0161fed8-5292-4618-942b-2ace60b13ba7]
- [Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 198 | UUID: 7eb97613-43e9-44c9-a26a-9c29f7854dd9]
- [Source: NODE_C_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 497 | UUID: de61baf4-02d0-418e-bbb4-58870aee3e46]
- [Source: NODE_C_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 498 | UUID: 71554281-7b16-4185-8889-8aa02cababd7]
- [Source: NODE_C_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 499 | UUID: cb34c115-8938-43db-b607-40c6b3fd1fd1]
- [Source: NODE_C_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 201 | UUID: 511e121a-7b83-4fc2-84b1-d12b5968831c]
- [Source: NODE_C_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 500 | UUID: c066d400-1e46-4c60-87d5-46300fa1395e]
- [Source: NODE_C_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 202 | UUID: 0e98d703-1c41-4946-bd73-b04762025872]
