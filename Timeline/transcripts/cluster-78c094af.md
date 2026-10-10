# Incident Cluster: cluster-78c094af
**Date:** 2032-06-18
**Duration:** 12:12:45 to 12:13:52
**Nodes Involved:** NODE_A, NODE_C
**Total Events:** 16 (Filtered from 26 raw logs)

## Timeline Transcript

**[12:12:45]**
* **NODE_A** [Operator Interaction]: Operator interaction enter flt nbr
  * *Details:* Dual mode: Single | Master status: Master | Functional position: Captain | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 342.997314 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | Flight plan source - high: Active | Flight plan source - low: ActPrimary | Display system source: Operator interaction display system left | [Operator Interaction Event: Operator interaction enter flt nbr | Event status: Operator interaction entered | Event value: 65547]
  * *Citation:* `[Source: NODE_A_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 7 | UUID: d3963bd5-a8bf-444d-a9d7-a0692046423c]`
* **NODE_A** [Software Event]: Software Event: Operator interaction event identifier
  * *Details:* Data Identifier: Operator interaction event identifier | Data Format: Format operator interaction event | Left FMS node: Master | Dual: Single | [Event identifier: Operator interaction enter flt nbr | Source fms node: Captain]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 7 | UUID: 48047931-0807-4c87-9f78-c7dd0c1443e8]`

**[12:13:44]**
* **NODE_C** [Fault History] (x2 occurrences collapsed): Background Service Identity Failure (Code: 6025)
  * *Details:* Serial Number: 250 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6025 | Fault Code: 6025 | Sub Code: Thunderbolt fault | Fault Name: Background Service Identity Failure | Date and Time: 2032-06-18 12:13:44 PM | Module Temperature: 37 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Initializing | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 35 | Application Data: get current process id failure 653;
  * *Citation:* `[Source: NODE_C_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 250 | UUID: e7768338-8b9d-403a-b5a3-07229c934784]`
* **NODE_C** [Fault History] (x9 occurrences collapsed): FMS Data Repository Access Failure (Code: 6074)
  * *Details:* Serial Number: 252 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6074 | Fault Code: 6074 | Sub Code: Thunderbolt fault | Fault Name: FMS Data Repository Access Failure | Date and Time: 2032-06-18 12:13:44 PM | Module Temperature: 38 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Initializing | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: True | Application Data Size: 196 | Application Data: can not Get line Public FMS Artifact file due to Fs end of file e error code;;
  * *Citation:* `[Source: NODE_C_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 252 | UUID: 9ac380a7-dfbe-4574-ae6e-b32488647bf8]`

**[12:13:46]**
* **NODE_C** [Software Event]: Software Event: Operational startup mode identifier
  * *Details:* Data Identifier: Operational startup mode identifier | Data Format: Format fixed str | Left FMS node: Spare | Dual: Single | [Event identifier: 68 | Operational startup mode: Operational startup cold]
  * *Citation:* `[Source: NODE_C_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 1 | UUID: c26cc195-5df4-468e-9f4f-12e85eb7fef0]`
* **NODE_C** [Software Event]: Software Event: Dual mode identifier
  * *Details:* Data Identifier: Dual mode identifier | Data Format: Format fixed str | Left FMS node: Spare | Dual: Single | [Event identifier: 68 | Operational dual mode: Operational dual mode Changed]
  * *Citation:* `[Source: NODE_C_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 2 | UUID: ba87c6ed-5083-4697-8b20-d27d5125b03f]`
* **NODE_C** [Software Event]: Software Event: Operational powerup identifier
  * *Details:* Data Identifier: Operational powerup identifier | Data Format: Format fixed str | Left FMS node: Spare | Dual: Single | [Event identifier: 68 | Operational powerup: Operational powerup normal]
  * *Citation:* `[Source: NODE_C_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 3 | UUID: 623d4d4d-8b48-48cf-8936-b483013cb98e]`

**[12:13:48]**
* **NODE_A** [State Transition]: State Transition: Master status -> Master
  * *Details:* [Master status: Master | Dual mode: Single | Opposite fms ok: Not ok | Other dual fms node position: FMS node invalid | Standby fms node position: FMS node right | Functional position: Captain]
  * *Citation:* `[Source: NODE_A_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 5 | UUID: 5fe29c2a-ba5c-442f-9fd2-4fb240d2ddf1]`

**[12:13:49]**
* **NODE_A** [Fault History]: Scheduled FMS Activity Missed Timing Requirement (Code: 6000)
  * *Details:* Serial Number: 577 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6000 | Fault Code: 6000 | Sub Code: Thunderbolt fault | Fault Name: Scheduled FMS Activity Missed Timing Requirement | Date and Time: 2032-06-18 12:13:49 PM | Module Temperature: 39 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 50 | Application Data: Deadline miss` Background service - 65563;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 577 | UUID: f890be7b-a009-4808-817e-f5be005110bc]`
* **NODE_A** [State Transition] (x2 occurrences collapsed): State Transition: Master status -> Master
  * *Details:* [Master status: Master | Dual mode: Single | Opposite fms ok: Not ok | Other dual fms node position: FMS node right | Standby fms node position: FMS node right | Functional position: Captain]
  * *Citation:* `[Source: NODE_A_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 6 | UUID: 3d5c880a-2cdf-4148-ac47-1030459d9298]`

**[12:13:50]**
* **NODE_A** [Fault History]: Scheduled FMS Activity Missed Timing Requirement (Code: 6000)
  * *Details:* Serial Number: 578 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6000 | Fault Code: 6000 | Sub Code: Thunderbolt fault | Fault Name: Scheduled FMS Activity Missed Timing Requirement | Date and Time: 2032-06-18 12:13:50 PM | Module Temperature: 39 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 50 | Application Data: Deadline miss` Background service - 65552;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 578 | UUID: 801ac1bf-22a0-4940-ab5e-1577a6776634]`
* **NODE_A** [Software Event]: Software Event: S pad message identifier l
  * *Details:* Data Identifier: S pad message identifier l | Data Format: Format one unsign 32 | Left FMS node: Master | Dual: Single | [L message identifier: Please wait]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 8 | UUID: f2adc17d-718c-4a01-857f-1d13cf7c9320]`
* **NODE_A** [Software Event]: Software Event: S pad message identifier r
  * *Details:* Data Identifier: S pad message identifier r | Data Format: Format one unsign 32 | Left FMS node: Master | Dual: Single | [R message identifier: Please wait]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 9 | UUID: 76096cae-1f01-43e2-9954-1351a5298047]`
* **NODE_A** [State Transition]: State Transition: Master status -> Master
  * *Details:* [Master status: Master | Dual mode: Single | Opposite fms ok: Ok | Other dual fms node position: FMS node right | Standby fms node position: FMS node invalid | Functional position: Captain]
  * *Citation:* `[Source: NODE_A_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 8 | UUID: 2a99049a-466a-446e-b6b9-389e1e3d47da]`

**[12:13:51]**
* **NODE_A** [State Transition]: State Transition: Master status -> Master
  * *Details:* [Master status: Master | Dual mode: Single | Opposite fms ok: Unstable | Other dual fms node position: FMS node right | Standby fms node position: FMS node invalid | Functional position: Captain]
  * *Citation:* `[Source: NODE_A_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 9 | UUID: 2c1a7203-dd98-444c-8827-ee49fc5e2085]`

**[12:13:52]**
* **NODE_A** [State Transition]: State Transition: Master status -> Master
  * *Details:* [Master status: Master | Dual mode: Single | Opposite fms ok: Not ok | Other dual fms node position: FMS node right | Standby fms node position: FMS node invalid | Functional position: Captain]
  * *Citation:* `[Source: NODE_A_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 10 | UUID: 7ba2a34b-e5e4-4381-81f5-38a69262443d]`
