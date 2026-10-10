# Incident Cluster: cluster-161c0fe5
**Date:** 2032-06-18
**Duration:** 11:46:26 to 11:54:38
**Nodes Involved:** NODE_A, NODE_B, NODE_C
**Total Events:** 353 (Filtered from 524 raw logs)

## Timeline Transcript

**[11:46:26]**
* **NODE_C** [State Transition]: State Transition: Master status -> Master
  * *Details:* [Master status: Master | Dual mode: Single | Opposite fms ok: Not ok | Other dual fms node position: FMS node left | Standby fms node position: FMS node invalid | Functional position: First officer]
  * *Citation:* `[Source: NODE_C_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 54 | UUID: 2bcd0df2-3193-492f-afe4-7eab5d03e05e]`

**[11:46:31]**
* **NODE_C** [Software Event]: Software Event: Master spare identifier
  * *Details:* Data Identifier: Master spare identifier | Data Format: Format fixed str | Right FMS node: Master | Dual: Single | [Event identifier: 68 | FMS node position: Operational master spare Changed]
  * *Citation:* `[Source: NODE_C_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 248 | UUID: 1f21af90-8fb4-44c4-a199-2eb3b8dc9c6e]`

**[11:46:34]**
* **NODE_A** [Fault History] (x2 occurrences collapsed): Background Service Identity Failure (Code: 6025)
  * *Details:* Serial Number: 224 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6025 | Fault Code: 6025 | Sub Code: Thunderbolt fault | Fault Name: Background Service Identity Failure | Date and Time: 2032-06-18 11:46:34 AM | Module Temperature: 40 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Initializing | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 35 | Application Data: get current process id failure 653;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 224 | UUID: 87c1c623-3f18-489c-b9a5-f8af9c4c22e7]`
* **NODE_A** [Fault History] (x20 occurrences collapsed): FMS Data Repository Access Failure (Code: 6074)
  * *Details:* Serial Number: 226 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6074 | Fault Code: 6074 | Sub Code: Thunderbolt fault | Fault Name: FMS Data Repository Access Failure | Date and Time: 2032-06-18 11:46:34 AM | Module Temperature: 41 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Initializing | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: True | Application Data Size: 196 | Application Data: can not Get line Public FMS Artifact file due to Fs end of file e error code;;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 226 | UUID: ab488492-8d99-4e9d-857d-d8469e01baf4]`

**[11:46:35]**
* **NODE_A** [Fault History] (x2 occurrences collapsed): Background Service Identity Failure (Code: 6025)
  * *Details:* Serial Number: 246 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6025 | Fault Code: 6025 | Sub Code: Thunderbolt fault | Fault Name: Background Service Identity Failure | Date and Time: 2032-06-18 11:46:35 AM | Module Temperature: 39 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Initializing | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 35 | Application Data: get current process id failure 653;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 246 | UUID: c747a95d-3780-4bfb-8d62-ebc8cc44b98f]`
* **NODE_A** [Fault History]: Oss loading failure (Code: 6052)
  * *Details:* Serial Number: 248 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6052 | Fault Code: 6052 | Sub Code: Thunderbolt fault | Fault Name: Oss loading failure | Date and Time: 2032-06-18 11:46:35 AM | Module Temperature: 39 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Initializing | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 100 | Application Data: Failed to load library in Deos 653 - Libpssl dtf manager so.so 11 11;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 248 | UUID: 4a4f988b-5bb6-4101-9897-75ac69da41ec]`
* **NODE_A** [Fault History] (x2 occurrences collapsed): Background Service Identity Failure (Code: 6025)
  * *Details:* Serial Number: 249 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6025 | Fault Code: 6025 | Sub Code: Thunderbolt fault | Fault Name: Background Service Identity Failure | Date and Time: 2032-06-18 11:46:35 AM | Module Temperature: 40 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Initializing | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 35 | Application Data: get current process id failure 653;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 249 | UUID: fb6c9d1e-47c1-4485-9c6d-59cd9f60fdb6]`

**[11:46:36]**
* **NODE_A** [Fault History]: Cpdb opc not not enabled (Code: 6)
  * *Details:* Serial Number: 251 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 11643 | Fault Code: 6 | Sub Code: 107 | Fault Name: Cpdb opc not not enabled | Date and Time: 2032-06-18 11:46:36 AM | Module Temperature: 39 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Initializing | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 8 | Application Data: ?~J;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 251 | UUID: f0b49c85-4e47-45af-b77f-12a145ca19b7]`
* **NODE_A** [Fault History]: Background Service Identity Failure (Code: 6025)
  * *Details:* Serial Number: 252 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6025 | Fault Code: 6025 | Sub Code: Thunderbolt fault | Fault Name: Background Service Identity Failure | Date and Time: 2032-06-18 11:46:36 AM | Module Temperature: 40 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Initializing | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 35 | Application Data: get current process id failure 653;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 252 | UUID: b818713e-eae6-4b0c-bb8a-bd03e0af6f89]`
* **NODE_A** [Fault History]: Oss generic fault (Code: 6080)
  * *Details:* Serial Number: 253 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6080 | Fault Code: 6080 | Sub Code: Thunderbolt fault | Fault Name: Oss generic fault | Date and Time: 2032-06-18 11:46:36 AM | Module Temperature: 40 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Initializing | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 48 | Application Data: Get parent task rate : Process is not found 653;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 253 | UUID: 81585063-8d27-4147-8346-bdf560b89798]`
* **NODE_A** [Fault History] (x7 occurrences collapsed): Background Service Identity Failure (Code: 6025)
  * *Details:* Serial Number: 254 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6025 | Fault Code: 6025 | Sub Code: Thunderbolt fault | Fault Name: Background Service Identity Failure | Date and Time: 2032-06-18 11:46:36 AM | Module Temperature: 40 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Ready | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 35 | Application Data: get current process id failure 653;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 254 | UUID: 42de419c-a5d6-4a8d-84bd-9856b3ec9a07]`
* **NODE_A** [Fault History] (x8 occurrences collapsed): Oss bind failure (Code: 6035)
  * *Details:* Serial Number: 261 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6035 | Fault Code: 6035 | Sub Code: Thunderbolt fault | Fault Name: Oss bind failure | Date and Time: 2032-06-18 11:46:36 AM | Module Temperature: 40 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Ready | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 100 | Application Data: Client Cb not found in deos 653 - -933180756;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 261 | UUID: b63811a3-bd26-46bf-9ac0-81fb7c5d3987]`
* **NODE_A** [Operator Interaction]: Operator Interaction Event
  * *Details:* Dual mode: Single | Master status: Master | Functional position: Captain | Calibrated airspeed data: 30.000000 | Message: No displayable fields
  * *Citation:* `[Source: NODE_A_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 1 | UUID: 30108748-9f64-48c6-935b-40e27450c825]`
* **NODE_C** [State Transition]: State Transition: Master status -> Master
  * *Details:* [Master status: Master | Dual mode: Single | Opposite fms ok: Not ok | Other dual fms node position: FMS node left | Standby fms node position: FMS node left | Functional position: First officer]
  * *Citation:* `[Source: NODE_C_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 55 | UUID: 8dd35c9b-a51b-4819-8375-a5de21a3e90a]`

**[11:46:37]**
* **NODE_A** [Fault History]: Oss task client failure (Code: 6024)
  * *Details:* Serial Number: 269 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6024 | Fault Code: 6024 | Sub Code: Thunderbolt fault | Fault Name: Oss task client failure | Date and Time: 2032-06-18 11:46:37 AM | Module Temperature: 39 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Ready | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 22 | Application Data: Task Client not found;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 269 | UUID: ade5f7c1-cf1b-494a-9261-e19e779626f5]`
* **NODE_A** [Fault History]: Ndb out of date (Code: 5)
  * *Details:* Serial Number: 270 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 11311 | Fault Code: 5 | Sub Code: 31 | Fault Name: Ndb out of date | Date and Time: 2032-06-18 11:46:37 AM | Module Temperature: 39 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 8 | Application Data: ?~J;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 270 | UUID: 13f10160-ff65-4438-b70b-d0ee5e1fd4bf]`
* **NODE_A** [Fault History]: Oss task client failure (Code: 6024)
  * *Details:* Serial Number: 271 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6024 | Fault Code: 6024 | Sub Code: Thunderbolt fault | Fault Name: Oss task client failure | Date and Time: 2032-06-18 11:46:37 AM | Module Temperature: 39 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 22 | Application Data: Task Client not found;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 271 | UUID: e5ef11c6-352a-444f-8f48-78c134c0c0eb]`
* **NODE_A** [Fault History]: Error during start process (Code: 9)
  * *Details:* Serial Number: 272 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 12315 | Fault Code: 9 | Sub Code: 11 | Fault Name: Error during start process | Date and Time: 2032-06-18 11:46:37 AM | Module Temperature: 39 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 8 | Application Data: ?~J;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 272 | UUID: 016588b5-b3fc-44ac-9d41-9523d940a552]`
* **NODE_A** [Fault History] (x2 occurrences collapsed): Oss generic fault (Code: 6080)
  * *Details:* Serial Number: 273 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6080 | Fault Code: 6080 | Sub Code: Thunderbolt fault | Fault Name: Oss generic fault | Date and Time: 2032-06-18 11:46:37 AM | Module Temperature: 39 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 45 | Application Data: Background Task:Set priority Deos Api failure in 653;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 273 | UUID: a628667b-b453-4d34-9492-aed48aff9f65]`
* **NODE_A** [Software Event]: Software Event: Operational startup mode identifier
  * *Details:* Data Identifier: Operational startup mode identifier | Data Format: Format fixed str | Left FMS node: Spare | Dual: Single | [Event identifier: 68 | Operational startup mode: Operational startup cold]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 1 | UUID: f8a23a2d-f591-4524-ae0a-013b1dd65cac]`
* **NODE_A** [Software Event]: Software Event: Dual mode identifier
  * *Details:* Data Identifier: Dual mode identifier | Data Format: Format fixed str | Left FMS node: Spare | Dual: Single | [Event identifier: 68 | Operational dual mode: Operational dual mode Changed]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 2 | UUID: d4157e77-86ef-46f5-bad7-a4dca0bfea83]`
* **NODE_A** [Software Event]: Software Event: Operational powerup identifier
  * *Details:* Data Identifier: Operational powerup identifier | Data Format: Format fixed str | Left FMS node: Spare | Dual: Single | [Event identifier: 68 | Operational powerup: Operational powerup normal]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 3 | UUID: 5a7eeaef-ae8d-496c-901d-e3831fa2907f]`
* **NODE_A** [State Transition]: State Transition: Master status -> Master
  * *Details:* [Master status: Master | Dual mode: Single | Opposite fms ok: Unknown | Other dual fms node position: FMS node invalid | Standby fms node position: FMS node invalid | Functional position: Standby]
  * *Citation:* `[Source: NODE_A_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 1 | UUID: 6297cd4f-33d6-4b23-b312-2961159b27b5]`
* **NODE_A** [State Transition]: State Transition: Master status -> Standby
  * *Details:* [Master status: Standby | Dual mode: Single | Opposite fms ok: Unknown | Other dual fms node position: FMS node invalid | Standby fms node position: FMS node invalid | Functional position: Standby]
  * *Citation:* `[Source: NODE_A_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 2 | UUID: e4918c8a-9374-4f04-b2d6-c7cb26797b93]`
* **NODE_C** [State Transition]: State Transition: Master status -> Spare
  * *Details:* [Master status: Spare | Dual mode: Single | Opposite fms ok: Not ok | Other dual fms node position: FMS node left | Standby fms node position: FMS node left | Functional position: First officer]
  * *Citation:* `[Source: NODE_C_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 56 | UUID: 861c182f-c1c9-4ee0-92d1-fb849b4da80b]`

**[11:46:38]**
* **NODE_A** [Fault History]: Error during start process (Code: 9)
  * *Details:* Serial Number: 275 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 12315 | Fault Code: 9 | Sub Code: 11 | Fault Name: Error during start process | Date and Time: 2032-06-18 11:46:38 AM | Module Temperature: 39 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 8 | Application Data: ?~J;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 275 | UUID: ea78acef-d2c2-4d10-8fab-63d4473b014c]`
* **NODE_A** [Fault History]: Scheduled FMS Activity Missed Timing Requirement (Code: 6000)
  * *Details:* Serial Number: 276 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6000 | Fault Code: 6000 | Sub Code: Thunderbolt fault | Fault Name: Scheduled FMS Activity Missed Timing Requirement | Date and Time: 2032-06-18 11:46:38 AM | Module Temperature: 39 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 50 | Application Data: Deadline miss` Background service - 65563;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 276 | UUID: b47a2540-d167-4801-a2a8-227f47f68b11]`
* **NODE_A** [Fault History]: Oss task client failure (Code: 6024)
  * *Details:* Serial Number: 277 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6024 | Fault Code: 6024 | Sub Code: Thunderbolt fault | Fault Name: Oss task client failure | Date and Time: 2032-06-18 11:46:38 AM | Module Temperature: 39 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 22 | Application Data: Task Client not found;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 277 | UUID: 3c19b0b1-ea26-4625-a85b-a9e4a78cfee4]`
* **NODE_A** [Fault History]: Scheduled FMS Activity Missed Timing Requirement (Code: 6000)
  * *Details:* Serial Number: 278 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6000 | Fault Code: 6000 | Sub Code: Thunderbolt fault | Fault Name: Scheduled FMS Activity Missed Timing Requirement | Date and Time: 2032-06-18 11:46:38 AM | Module Temperature: 40 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 50 | Application Data: Deadline miss` Background service - 65552;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 278 | UUID: 69a825bc-6662-471b-91b7-8e7ca7805a50]`
* **NODE_A** [Operator Interaction] (x5 occurrences collapsed): Operator Interaction Event
  * *Details:* Dual mode: Single | Master status: Master | Functional position: Captain | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 342.999451 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [FMS Operational Event: clear altitude | FMS node source: Standby]
  * *Citation:* `[Source: NODE_A_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 2 | UUID: 9355b25f-5d53-4af5-9fa5-8e5771af2dab]`
* **NODE_A** [Software Event]: Software Event: S pad message identifier l
  * *Details:* Data Identifier: S pad message identifier l | Data Format: Format one unsign 32 | Left FMS node: Spare | Dual: Single | [L message identifier: Please wait]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 4 | UUID: 135479a8-bc18-4406-9940-b899c6a8f928]`
* **NODE_A** [Software Event]: Software Event: S pad message identifier r
  * *Details:* Data Identifier: S pad message identifier r | Data Format: Format one unsign 32 | Left FMS node: Spare | Dual: Single | [R message identifier: Please wait]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 5 | UUID: 37c3d5ad-f64c-46cd-b086-3ece642ee929]`
* **NODE_A** [State Transition] (x5 occurrences collapsed): State Transition: Master status -> Master
  * *Details:* [Master status: Master | Dual mode: Single | Opposite fms ok: Unknown | Other dual fms node position: FMS node invalid | Standby fms node position: FMS node invalid | Functional position: Captain]
  * *Citation:* `[Source: NODE_A_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 3 | UUID: 397cece8-51fc-4c8d-8659-0e40697d46d1]`
* **NODE_C** [Fault History]: Scheduled FMS Activity Missed Timing Requirement (Code: 6000)
  * *Details:* Serial Number: 236 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6000 | Fault Code: 6000 | Sub Code: Thunderbolt fault | Fault Name: Scheduled FMS Activity Missed Timing Requirement | Date and Time: 2032-06-18 11:46:38 AM | Module Temperature: 39 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Count: 5 | Last Context Reset Reason: Fr context shutdown e | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 50 | Application Data: Deadline miss` Background service - 3211280;
  * *Citation:* `[Source: NODE_C_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 236 | UUID: dc521a1c-e79f-4dd0-9520-4e07679d791e]`
* **NODE_C** [Software Event]: Software Event: S pad message identifier l
  * *Details:* Data Identifier: S pad message identifier l | Data Format: Format one unsign 32 | Right FMS node: Master | Dual: Single | [L message identifier: Please wait]
  * *Citation:* `[Source: NODE_C_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 249 | UUID: 90baf0a8-0e5e-44b2-b769-59d87f56cd04]`
* **NODE_C** [Software Event]: Software Event: S pad message identifier r
  * *Details:* Data Identifier: S pad message identifier r | Data Format: Format one unsign 32 | Right FMS node: Master | Dual: Single | [R message identifier: Please wait]
  * *Citation:* `[Source: NODE_C_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 250 | UUID: 558adac4-bac4-4678-9362-b6d30fe0bf91]`
* **NODE_C** [State Transition] (x2 occurrences collapsed): State Transition: Master status -> Spare
  * *Details:* [Master status: Spare | Dual mode: Single | Opposite fms ok: Unstable | Other dual fms node position: FMS node left | Standby fms node position: FMS node left | Functional position: First officer]
  * *Citation:* `[Source: NODE_C_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 57 | UUID: f83c97ef-2f7b-4dda-a587-6b1fcc35222a]`

**[11:46:39]**
* **NODE_A** [Fault History]: Oss semaphore failure (Code: 6029)
  * *Details:* Serial Number: 279 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6029 | Fault Code: 6029 | Sub Code: Thunderbolt fault | Fault Name: Oss semaphore failure | Date and Time: 2032-06-18 11:46:39 AM | Module Temperature: 39 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 100 | Application Data: wait semaphore failed in deos 653 - 6 ;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 279 | UUID: a7bbe180-aac4-4b81-980b-38ab75a89497]`
* **NODE_C** [State Transition]: State Transition: Master status -> Spare
  * *Details:* [Master status: Spare | Dual mode: Single | Opposite fms ok: Ok | Other dual fms node position: FMS node left | Standby fms node position: FMS node invalid | Functional position: First officer]
  * *Citation:* `[Source: NODE_C_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 59 | UUID: dfe4e7ba-401c-4a47-850c-1e429a200ed7]`

**[11:46:40]**
* **NODE_A** [Fault History]: Oss semaphore failure (Code: 6029)
  * *Details:* Serial Number: 280 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6029 | Fault Code: 6029 | Sub Code: Thunderbolt fault | Fault Name: Oss semaphore failure | Date and Time: 2032-06-18 11:46:40 AM | Module Temperature: 40 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 100 | Application Data: wait semaphore failed in deos 653 - 6 ;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 280 | UUID: c52a5259-d599-4e9f-b3b6-a9d7694ccbfb]`

**[11:46:41]**
* **NODE_A** [Fault History]: Scheduled FMS Activity Missed Timing Requirement (Code: 6000)
  * *Details:* Serial Number: 281 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6000 | Fault Code: 6000 | Sub Code: Thunderbolt fault | Fault Name: Scheduled FMS Activity Missed Timing Requirement | Date and Time: 2032-06-18 11:46:41 AM | Module Temperature: 40 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 50 | Application Data: Deadline miss` Background service - 65562;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 281 | UUID: 981c427c-0760-40f4-9beb-0f1bce8db27d]`
* **NODE_A** [Fault History]: Oss semaphore failure (Code: 6029)
  * *Details:* Serial Number: 282 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6029 | Fault Code: 6029 | Sub Code: Thunderbolt fault | Fault Name: Oss semaphore failure | Date and Time: 2032-06-18 11:46:41 AM | Module Temperature: 39 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 100 | Application Data: wait semaphore failed in deos 653 - 6 ;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 282 | UUID: 96fa5297-a304-45ce-95fd-6debb54f9a47]`

**[11:46:42]**
* **NODE_A** [Fault History]: Oss semaphore failure (Code: 6029)
  * *Details:* Serial Number: 283 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6029 | Fault Code: 6029 | Sub Code: Thunderbolt fault | Fault Name: Oss semaphore failure | Date and Time: 2032-06-18 11:46:42 AM | Module Temperature: 40 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 100 | Application Data: wait semaphore failed in deos 653 - 6 ;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 283 | UUID: 4e977515-44e7-407b-9f27-2a6038630c9d]`
* **NODE_A** [Fault History]: Scheduled FMS Activity Missed Timing Requirement (Code: 6000)
  * *Details:* Serial Number: 284 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6000 | Fault Code: 6000 | Sub Code: Thunderbolt fault | Fault Name: Scheduled FMS Activity Missed Timing Requirement | Date and Time: 2032-06-18 11:46:42 AM | Module Temperature: 40 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 50 | Application Data: Deadline miss` Background service - 65561;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 284 | UUID: 95bc7885-bf69-4d5d-904d-a759ec1efb62]`
* **NODE_A** [Software Event]: Software Event: Master spare identifier
  * *Details:* Data Identifier: Master spare identifier | Data Format: Format fixed str | Left FMS node: Master | Dual: Single | [Event identifier: 68 | FMS node position: Operational master spare Changed]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 6 | UUID: d6bad624-129e-4c49-9ba7-58f9f8234316]`

**[11:46:43]**
* **NODE_A** [Fault History]: Oss semaphore failure (Code: 6029)
  * *Details:* Serial Number: 285 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6029 | Fault Code: 6029 | Sub Code: Thunderbolt fault | Fault Name: Oss semaphore failure | Date and Time: 2032-06-18 11:46:43 AM | Module Temperature: 40 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 100 | Application Data: wait semaphore failed in deos 653 - 6 ;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 285 | UUID: d06d527f-f87a-44b5-9587-c837d68996da]`

**[11:46:44]**
* **NODE_A** [Fault History]: Oss semaphore failure (Code: 6029)
  * *Details:* Serial Number: 286 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6029 | Fault Code: 6029 | Sub Code: Thunderbolt fault | Fault Name: Oss semaphore failure | Date and Time: 2032-06-18 11:46:44 AM | Module Temperature: 39 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 100 | Application Data: wait semaphore failed in deos 653 - 6 ;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 286 | UUID: 0ba5c6ff-3923-42d4-b701-6a5ad9db9778]`
* **NODE_C** [Software Event]: Software Event: Master spare identifier
  * *Details:* Data Identifier: Master spare identifier | Data Format: Format fixed str | Left FMS node: Master | Right FMS node: Spare | Dual: Single | [Event identifier: 68 | FMS node position: Operational master spare Changed]
  * *Citation:* `[Source: NODE_C_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 251 | UUID: e1dbc2f4-2dcd-4ac9-b787-375d9dac5d74]`

**[11:46:45]**
* **NODE_A** [Fault History]: Oss semaphore failure (Code: 6029)
  * *Details:* Serial Number: 287 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6029 | Fault Code: 6029 | Sub Code: Thunderbolt fault | Fault Name: Oss semaphore failure | Date and Time: 2032-06-18 11:46:45 AM | Module Temperature: 39 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 100 | Application Data: wait semaphore failed in deos 653 - 6 ;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 287 | UUID: c069e0f3-7a7f-4515-a607-38c334777f45]`

**[11:46:46]**
* **NODE_A** [Fault History]: Oss semaphore failure (Code: 6029)
  * *Details:* Serial Number: 288 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6029 | Fault Code: 6029 | Sub Code: Thunderbolt fault | Fault Name: Oss semaphore failure | Date and Time: 2032-06-18 11:46:46 AM | Module Temperature: 40 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 100 | Application Data: wait semaphore failed in deos 653 - 6 ;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 288 | UUID: 274a0372-02f6-42b9-83e6-4695f94c0c4e]`

**[11:46:47]**
* **NODE_A** [Operator Interaction]: Operator Interaction Event
  * *Details:* Dual mode: Dual | Master status: Master | Functional position: Captain | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 342.998138 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [Fault/Event: Cold Start Due To A Re-Synch On The Receiver]
  * *Citation:* `[Source: NODE_A_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 7 | UUID: 91449f23-de1f-46dc-bf43-b912a437a2d6]`

**[11:46:48]**
* **NODE_C** [State Transition]: State Transition: Master status -> Spare
  * *Details:* [Master status: Spare | Dual mode: Single | Opposite fms ok: Unstable | Other dual fms node position: FMS node left | Standby fms node position: FMS node invalid | Functional position: First officer]
  * *Citation:* `[Source: NODE_C_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 60 | UUID: f725c411-e287-4cf8-9d4b-405093baedcf]`

**[11:46:49]**
* **NODE_C** [State Transition]: State Transition: Master status -> Spare
  * *Details:* [Master status: Spare | Dual mode: Single | Opposite fms ok: Not ok | Other dual fms node position: FMS node left | Standby fms node position: FMS node invalid | Functional position: First officer]
  * *Citation:* `[Source: NODE_C_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 61 | UUID: 6df1ceb3-e716-4842-a5df-b0adcf9bff18]`

**[11:46:57]**
* **NODE_C** [State Transition]: State Transition: Master status -> Master
  * *Details:* [Master status: Master | Dual mode: Single | Opposite fms ok: Not ok | Other dual fms node position: FMS node left | Standby fms node position: FMS node invalid | Functional position: First officer]
  * *Citation:* `[Source: NODE_C_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 62 | UUID: 2a9f792b-3ed0-41f3-9395-13ce5d29c6bd]`

**[11:47:03]**
* **NODE_C** [Software Event]: Software Event: Master spare identifier
  * *Details:* Data Identifier: Master spare identifier | Data Format: Format fixed str | Right FMS node: Master | Dual: Single | [Event identifier: 68 | FMS node position: Operational master spare Changed]
  * *Citation:* `[Source: NODE_C_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 252 | UUID: e509ea6c-f629-49d7-b6a4-7a61e53d490b]`

**[11:47:35]**
* **NODE_B** [Fault History] (x2 occurrences collapsed): Background Service Identity Failure (Code: 6025)
  * *Details:* Serial Number: 153 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6025 | Fault Code: 6025 | Sub Code: Thunderbolt fault | Fault Name: Background Service Identity Failure | Date and Time: 2032-06-18 11:47:35 AM | Module Temperature: 37 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Initializing | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 35 | Application Data: get current process id failure 653;
  * *Citation:* `[Source: NODE_B_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 153 | UUID: ccf6c99e-97f7-4de4-99ea-f89e6ad2b760]`
* **NODE_B** [Fault History] (x3 occurrences collapsed): FMS Data Repository Access Failure (Code: 6074)
  * *Details:* Serial Number: 155 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6074 | Fault Code: 6074 | Sub Code: Thunderbolt fault | Fault Name: FMS Data Repository Access Failure | Date and Time: 2032-06-18 11:47:35 AM | Module Temperature: 37 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Initializing | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: True | Application Data Size: 196 | Application Data: can not Get line Public FMS Artifact file due to Fs end of file e error code;;
  * *Citation:* `[Source: NODE_B_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 155 | UUID: 18148411-1f77-4b14-8c65-49360a41cee9]`

**[11:47:36]**
* **NODE_B** [Fault History] (x17 occurrences collapsed): FMS Data Repository Access Failure (Code: 6074)
  * *Details:* Serial Number: 158 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6074 | Fault Code: 6074 | Sub Code: Thunderbolt fault | Fault Name: FMS Data Repository Access Failure | Date and Time: 2032-06-18 11:47:36 AM | Module Temperature: 37 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Initializing | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: True | Application Data Size: 196 | Application Data: can not Get line Public FMS Artifact file due to Fs end of file e error code;;
  * *Citation:* `[Source: NODE_B_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 158 | UUID: 25732584-cfba-4ce6-b8a9-930672cdb376]`
* **NODE_B** [Fault History] (x2 occurrences collapsed): Background Service Identity Failure (Code: 6025)
  * *Details:* Serial Number: 175 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6025 | Fault Code: 6025 | Sub Code: Thunderbolt fault | Fault Name: Background Service Identity Failure | Date and Time: 2032-06-18 11:47:36 AM | Module Temperature: 38 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Initializing | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 35 | Application Data: get current process id failure 653;
  * *Citation:* `[Source: NODE_B_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 175 | UUID: 8dfde998-7068-47f6-882f-012fbe1a041b]`
* **NODE_B** [Fault History]: Oss loading failure (Code: 6052)
  * *Details:* Serial Number: 177 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6052 | Fault Code: 6052 | Sub Code: Thunderbolt fault | Fault Name: Oss loading failure | Date and Time: 2032-06-18 11:47:36 AM | Module Temperature: 35 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Initializing | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 100 | Application Data: Failed to load library in Deos 653 - Libpssl dtf manager so.so 11 11;
  * *Citation:* `[Source: NODE_B_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 177 | UUID: 6de03665-113e-45bc-a637-a84559b1eb47]`
* **NODE_B** [Fault History] (x2 occurrences collapsed): Background Service Identity Failure (Code: 6025)
  * *Details:* Serial Number: 178 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6025 | Fault Code: 6025 | Sub Code: Thunderbolt fault | Fault Name: Background Service Identity Failure | Date and Time: 2032-06-18 11:47:36 AM | Module Temperature: 35 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Initializing | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 35 | Application Data: get current process id failure 653;
  * *Citation:* `[Source: NODE_B_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 178 | UUID: 63cf54d0-70f0-4790-bc9b-ce88ca7767ab]`

**[11:47:37]**
* **NODE_B** [Operator Interaction]: Operator Interaction Event
  * *Details:* Dual mode: Single | Master status: Standby | Functional position: Captain | Calibrated airspeed data: 30.000000 | Message: No displayable fields
  * *Citation:* `[Source: NODE_B_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 2 | UUID: 4b3c8337-7446-4ea8-8cc3-3c02ecbb01bb]`

**[11:47:38]**
* **NODE_B** [Fault History]: Background Service Identity Failure (Code: 6025)
  * *Details:* Serial Number: 180 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6025 | Fault Code: 6025 | Sub Code: Thunderbolt fault | Fault Name: Background Service Identity Failure | Date and Time: 2032-06-18 11:47:38 AM | Module Temperature: 36 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Initializing | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 35 | Application Data: get current process id failure 653;
  * *Citation:* `[Source: NODE_B_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 180 | UUID: 2dc604cc-dab6-4725-a84b-54cbaa399ba4]`
* **NODE_B** [Fault History]: Oss generic fault (Code: 6080)
  * *Details:* Serial Number: 181 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6080 | Fault Code: 6080 | Sub Code: Thunderbolt fault | Fault Name: Oss generic fault | Date and Time: 2032-06-18 11:47:38 AM | Module Temperature: 36 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Initializing | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 48 | Application Data: Get parent task rate : Process is not found 653;
  * *Citation:* `[Source: NODE_B_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 181 | UUID: 3dbfbce9-3995-4ab6-9358-dff97c067c40]`
* **NODE_B** [Fault History] (x7 occurrences collapsed): Background Service Identity Failure (Code: 6025)
  * *Details:* Serial Number: 182 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6025 | Fault Code: 6025 | Sub Code: Thunderbolt fault | Fault Name: Background Service Identity Failure | Date and Time: 2032-06-18 11:47:38 AM | Module Temperature: 36 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Ready | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 35 | Application Data: get current process id failure 653;
  * *Citation:* `[Source: NODE_B_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 182 | UUID: 85ffff3c-9179-45da-807f-b20fae2cc194]`
* **NODE_B** [Fault History] (x8 occurrences collapsed): Oss bind failure (Code: 6035)
  * *Details:* Serial Number: 189 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6035 | Fault Code: 6035 | Sub Code: Thunderbolt fault | Fault Name: Oss bind failure | Date and Time: 2032-06-18 11:47:38 AM | Module Temperature: 36 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Ready | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 100 | Application Data: Client Cb not found in deos 653 - -933180756;
  * *Citation:* `[Source: NODE_B_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 189 | UUID: fcefa458-8fbb-45ae-b5eb-aee5174a89c4]`
* **NODE_B** [Fault History] (x2 occurrences collapsed): Oss task client failure (Code: 6024)
  * *Details:* Serial Number: 197 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6024 | Fault Code: 6024 | Sub Code: Thunderbolt fault | Fault Name: Oss task client failure | Date and Time: 2032-06-18 11:47:38 AM | Module Temperature: 36 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Ready | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 22 | Application Data: Task Client not found;
  * *Citation:* `[Source: NODE_B_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 197 | UUID: f2f28090-140d-41c1-97e1-9b77deed5000]`
* **NODE_B** [Fault History] (x3 occurrences collapsed): Oss generic fault (Code: 6080)
  * *Details:* Serial Number: 199 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6080 | Fault Code: 6080 | Sub Code: Thunderbolt fault | Fault Name: Oss generic fault | Date and Time: 2032-06-18 11:47:38 AM | Module Temperature: 36 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 45 | Application Data: Background Task:Set priority Deos Api failure in 653;
  * *Citation:* `[Source: NODE_B_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 199 | UUID: 279fe754-d29a-4a8b-b1f1-efbf0b79678f]`
* **NODE_B** [Operator Interaction] (x3 occurrences collapsed): Operator Interaction Event
  * *Details:* Dual mode: Single | Master status: Master | Functional position: Captain | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 343.001678 | Magnetic track: 66.049805 | [FMS Operational Event: clear altitude | FMS node source: Standby]
  * *Citation:* `[Source: NODE_B_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 3 | UUID: c3319d7b-aa47-45d3-ba53-278635ec4662]`
* **NODE_B** [Software Event]: Software Event: Operational startup mode identifier
  * *Details:* Data Identifier: Operational startup mode identifier | Data Format: Format fixed str | Left FMS node: Spare | Dual: Single | [Event identifier: 68 | Operational startup mode: Operational startup cold]
  * *Citation:* `[Source: NODE_B_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 26 | UUID: a8a1d5b2-5fe9-497d-9d33-3a91bcb6cee9]`
* **NODE_B** [Software Event]: Software Event: Dual mode identifier
  * *Details:* Data Identifier: Dual mode identifier | Data Format: Format fixed str | Left FMS node: Spare | Dual: Single | [Event identifier: 68 | Operational dual mode: Operational dual mode Changed]
  * *Citation:* `[Source: NODE_B_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 27 | UUID: df7a0a07-0a75-4773-9b24-d61a4c74e97e]`
* **NODE_B** [Software Event]: Software Event: Operational powerup identifier
  * *Details:* Data Identifier: Operational powerup identifier | Data Format: Format fixed str | Left FMS node: Spare | Dual: Single | [Event identifier: 68 | Operational powerup: Operational powerup normal]
  * *Citation:* `[Source: NODE_B_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 28 | UUID: 080444af-3c4e-4d95-8ed9-5871bb4b93dc]`
* **NODE_B** [State Transition]: State Transition: Master status -> Standby
  * *Details:* [Master status: Standby | Dual mode: Single | Opposite fms ok: Unknown | Other dual fms node position: FMS node invalid | Standby fms node position: FMS node invalid | Functional position: Captain]
  * *Citation:* `[Source: NODE_B_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 4 | UUID: 8261863b-bf8a-4cb5-a309-0605bae676e4]`
* **NODE_B** [State Transition] (x2 occurrences collapsed): State Transition: Master status -> Master
  * *Details:* [Master status: Master | Dual mode: Single | Opposite fms ok: Unknown | Other dual fms node position: FMS node invalid | Standby fms node position: FMS node invalid | Functional position: Captain]
  * *Citation:* `[Source: NODE_B_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 5 | UUID: 9162254c-e43e-4038-8808-697d70001ddd]`

**[11:47:39]**
* **NODE_B** [Fault History] (x2 occurrences collapsed): Scheduled FMS Activity Missed Timing Requirement (Code: 6000)
  * *Details:* Serial Number: 202 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6000 | Fault Code: 6000 | Sub Code: Thunderbolt fault | Fault Name: Scheduled FMS Activity Missed Timing Requirement | Date and Time: 2032-06-18 11:47:39 AM | Module Temperature: 37 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 50 | Application Data: Deadline miss` Background service - 1114128;
  * *Citation:* `[Source: NODE_B_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 202 | UUID: f89c858a-11b8-46e3-ba63-7eacbd2f6f7d]`
* **NODE_B** [Software Event]: Software Event: S pad message identifier l
  * *Details:* Data Identifier: S pad message identifier l | Data Format: Format one unsign 32 | Left FMS node: Spare | Dual: Single | [L message identifier: Please wait]
  * *Citation:* `[Source: NODE_B_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 29 | UUID: c636346e-5241-4718-96d9-25b42b8a6eb8]`
* **NODE_B** [Software Event]: Software Event: S pad message identifier r
  * *Details:* Data Identifier: S pad message identifier r | Data Format: Format one unsign 32 | Left FMS node: Spare | Dual: Single | [R message identifier: Please wait]
  * *Citation:* `[Source: NODE_B_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 30 | UUID: 38833c1f-4261-429e-a5ab-d18b9c64a90b]`
* **NODE_B** [State Transition]: State Transition: Master status -> Master
  * *Details:* [Master status: Master | Dual mode: Single | Opposite fms ok: Unstable | Other dual fms node position: FMS node right | Standby fms node position: FMS node invalid | Functional position: Captain]
  * *Citation:* `[Source: NODE_B_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 7 | UUID: 0ebf3569-43c3-43d1-95dc-531cf27faabb]`
* **NODE_C** [Operator Interaction]: Operator Interaction Event
  * *Details:* Dual mode: Single | Master status: Spare | Functional position: First officer | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 343.001923 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [FMS Operational Event: redisplay | FMS node source: Captain | Event value: 131091]
  * *Citation:* `[Source: NODE_C_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 674 | UUID: e447d63d-0f0a-409f-b1b2-bdd3c7f22cab]`
* **NODE_C** [State Transition] (x2 occurrences collapsed): State Transition: Master status -> Spare
  * *Details:* [Master status: Spare | Dual mode: Single | Opposite fms ok: Not ok | Other dual fms node position: FMS node center | Standby fms node position: FMS node invalid | Functional position: First officer]
  * *Citation:* `[Source: NODE_C_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 63 | UUID: 711b5c6c-3550-45c9-9c46-04e197e39022]`

**[11:47:40]**
* **NODE_B** [Fault History]: Oss task client failure (Code: 6024)
  * *Details:* Serial Number: 204 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6024 | Fault Code: 6024 | Sub Code: Thunderbolt fault | Fault Name: Oss task client failure | Date and Time: 2032-06-18 11:47:40 AM | Module Temperature: 36 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 22 | Application Data: Task Client not found;
  * *Citation:* `[Source: NODE_B_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 204 | UUID: 017238b5-2608-4bdc-be78-d55b42feb1d1]`
* **NODE_B** [Fault History]: Oss semaphore failure (Code: 6029)
  * *Details:* Serial Number: 205 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6029 | Fault Code: 6029 | Sub Code: Thunderbolt fault | Fault Name: Oss semaphore failure | Date and Time: 2032-06-18 11:47:40 AM | Module Temperature: 37 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 100 | Application Data: wait semaphore failed in deos 653 - 6 ;
  * *Citation:* `[Source: NODE_B_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 205 | UUID: 6ad02f27-8073-4397-9edb-80ca9da461a1]`
* **NODE_B** [State Transition]: State Transition: Master status -> Master
  * *Details:* [Master status: Master | Dual mode: Single | Opposite fms ok: Ok | Other dual fms node position: FMS node right | Standby fms node position: FMS node invalid | Functional position: Captain]
  * *Citation:* `[Source: NODE_B_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 8 | UUID: 507c38bd-7fd3-4d0b-8f59-cb4ed5958154]`
* **NODE_C** [State Transition]: State Transition: Master status -> Spare
  * *Details:* [Master status: Spare | Dual mode: Single | Opposite fms ok: Ok | Other dual fms node position: FMS node center | Standby fms node position: FMS node invalid | Functional position: First officer]
  * *Citation:* `[Source: NODE_C_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 65 | UUID: b5dad2b4-19d6-4bce-b3da-c5293a0bf2dd]`

**[11:47:41]**
* **NODE_B** [Fault History]: Oss semaphore failure (Code: 6029)
  * *Details:* Serial Number: 206 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6029 | Fault Code: 6029 | Sub Code: Thunderbolt fault | Fault Name: Oss semaphore failure | Date and Time: 2032-06-18 11:47:41 AM | Module Temperature: 37 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 100 | Application Data: wait semaphore failed in deos 653 - 6 ;
  * *Citation:* `[Source: NODE_B_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 206 | UUID: c4827b40-c1cd-4f84-ba5a-6c82c72c9618]`

**[11:47:42]**
* **NODE_B** [Fault History]: Oss semaphore failure (Code: 6029)
  * *Details:* Serial Number: 207 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6029 | Fault Code: 6029 | Sub Code: Thunderbolt fault | Fault Name: Oss semaphore failure | Date and Time: 2032-06-18 11:47:42 AM | Module Temperature: 37 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 100 | Application Data: wait semaphore failed in deos 653 - 6 ;
  * *Citation:* `[Source: NODE_B_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 207 | UUID: 1c5bd751-d034-45ab-80a4-517a76d2cfed]`

**[11:47:43]**
* **NODE_B** [Fault History]: Oss semaphore failure (Code: 6029)
  * *Details:* Serial Number: 208 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6029 | Fault Code: 6029 | Sub Code: Thunderbolt fault | Fault Name: Oss semaphore failure | Date and Time: 2032-06-18 11:47:43 AM | Module Temperature: 37 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 100 | Application Data: wait semaphore failed in deos 653 - 6 ;
  * *Citation:* `[Source: NODE_B_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 208 | UUID: d0f91cb9-862a-4b51-b4ab-9be2a8ad70b1]`

**[11:47:44]**
* **NODE_B** [Fault History]: Oss semaphore failure (Code: 6029)
  * *Details:* Serial Number: 209 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6029 | Fault Code: 6029 | Sub Code: Thunderbolt fault | Fault Name: Oss semaphore failure | Date and Time: 2032-06-18 11:47:44 AM | Module Temperature: 38 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 100 | Application Data: wait semaphore failed in deos 653 - 6 ;
  * *Citation:* `[Source: NODE_B_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 209 | UUID: cae5e603-2b08-4a2c-bc03-72e58e01c106]`
* **NODE_B** [Software Event]: Software Event: Master spare identifier
  * *Details:* Data Identifier: Master spare identifier | Data Format: Format fixed str | Center FMS node: Master | Dual: Single | [Event identifier: 68 | FMS node position: Operational master spare Changed]
  * *Citation:* `[Source: NODE_B_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 31 | UUID: b5f48571-ea94-4fad-8669-a35bab2977ae]`
* **NODE_C** [Software Event]: Software Event: Master spare identifier
  * *Details:* Data Identifier: Master spare identifier | Data Format: Format fixed str | Center FMS node: Master | Right FMS node: Spare | Dual: Single | [Event identifier: 68 | FMS node position: Operational master spare Changed]
  * *Citation:* `[Source: NODE_C_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 253 | UUID: 7f4b15b0-c985-415d-9d4f-e7f11f8ddcc0]`

**[11:47:45]**
* **NODE_B** [Fault History]: Oss semaphore failure (Code: 6029)
  * *Details:* Serial Number: 210 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6029 | Fault Code: 6029 | Sub Code: Thunderbolt fault | Fault Name: Oss semaphore failure | Date and Time: 2032-06-18 11:47:45 AM | Module Temperature: 36 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 100 | Application Data: wait semaphore failed in deos 653 - 6 ;
  * *Citation:* `[Source: NODE_B_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 210 | UUID: 4458cae0-bab8-409f-a8a4-d06ca6e54d95]`

**[11:47:46]**
* **NODE_B** [Fault History]: Oss semaphore failure (Code: 6029)
  * *Details:* Serial Number: 211 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6029 | Fault Code: 6029 | Sub Code: Thunderbolt fault | Fault Name: Oss semaphore failure | Date and Time: 2032-06-18 11:47:46 AM | Module Temperature: 37 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 100 | Application Data: wait semaphore failed in deos 653 - 6 ;
  * *Citation:* `[Source: NODE_B_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 211 | UUID: c95465cf-3f55-49c7-83cb-3de333441e65]`

**[11:47:47]**
* **NODE_B** [Fault History]: Oss semaphore failure (Code: 6029)
  * *Details:* Serial Number: 212 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6029 | Fault Code: 6029 | Sub Code: Thunderbolt fault | Fault Name: Oss semaphore failure | Date and Time: 2032-06-18 11:47:47 AM | Module Temperature: 36 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 100 | Application Data: wait semaphore failed in deos 653 - 6 ;
  * *Citation:* `[Source: NODE_B_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 212 | UUID: f335317c-2b5d-46d7-84d7-9a53d9e5a693]`

**[11:47:48]**
* **NODE_B** [Fault History]: Oss semaphore failure (Code: 6029)
  * *Details:* Serial Number: 213 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6029 | Fault Code: 6029 | Sub Code: Thunderbolt fault | Fault Name: Oss semaphore failure | Date and Time: 2032-06-18 11:47:48 AM | Module Temperature: 36 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 100 | Application Data: wait semaphore failed in deos 653 - 6 ;
  * *Citation:* `[Source: NODE_B_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 213 | UUID: 005a2351-7482-45f5-9763-208a37c07073]`
* **NODE_B** [Operator Interaction]: Operator Interaction Event
  * *Details:* Dual mode: Dual | Master status: Master | Functional position: Captain | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 343.007172 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [Fault/Event: Cold Start Due To A Re-Synch On The Receiver]
  * *Citation:* `[Source: NODE_B_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 6 | UUID: d8ed536a-f1e7-47c1-af97-a99aa8f99a44]`

**[11:47:49]**
* **NODE_C** [State Transition]: State Transition: Master status -> Spare
  * *Details:* [Master status: Spare | Dual mode: Single | Opposite fms ok: Unstable | Other dual fms node position: FMS node center | Standby fms node position: FMS node invalid | Functional position: First officer]
  * *Citation:* `[Source: NODE_C_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 66 | UUID: dd293059-04f8-44e9-bda2-aba8cc85472b]`

**[11:47:50]**
* **NODE_C** [State Transition]: State Transition: Master status -> Spare
  * *Details:* [Master status: Spare | Dual mode: Single | Opposite fms ok: Not ok | Other dual fms node position: FMS node center | Standby fms node position: FMS node invalid | Functional position: First officer]
  * *Citation:* `[Source: NODE_C_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 67 | UUID: a2335e82-e232-4816-b923-56d38b1fdf5a]`

**[11:47:57]**
* **NODE_A** [Fault History] (x2 occurrences collapsed): Background Service Identity Failure (Code: 6025)
  * *Details:* Serial Number: 289 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6025 | Fault Code: 6025 | Sub Code: Thunderbolt fault | Fault Name: Background Service Identity Failure | Date and Time: 2032-06-18 11:47:57 AM | Module Temperature: 41 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Initializing | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 35 | Application Data: get current process id failure 653;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 289 | UUID: 2c3df763-90a3-4e2e-8f3a-af6283c91d38]`

**[11:47:58]**
* **NODE_A** [Fault History] (x2 occurrences collapsed): Background Service Identity Failure (Code: 6025)
  * *Details:* Serial Number: 291 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6025 | Fault Code: 6025 | Sub Code: Thunderbolt fault | Fault Name: Background Service Identity Failure | Date and Time: 2032-06-18 11:47:58 AM | Module Temperature: 40 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Initializing | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 35 | Application Data: get current process id failure 653;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 291 | UUID: 76067a54-2f83-4abb-99e6-f544db41db09]`
* **NODE_A** [Fault History]: Oss loading failure (Code: 6052)
  * *Details:* Serial Number: 293 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6052 | Fault Code: 6052 | Sub Code: Thunderbolt fault | Fault Name: Oss loading failure | Date and Time: 2032-06-18 11:47:58 AM | Module Temperature: 40 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Initializing | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 100 | Application Data: Failed to load library in Deos 653 - Libpssl dtf manager so.so 11 11;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 293 | UUID: 1f3d130a-a416-45f1-981c-71f9f832c8db]`
* **NODE_A** [Fault History] (x2 occurrences collapsed): Background Service Identity Failure (Code: 6025)
  * *Details:* Serial Number: 294 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6025 | Fault Code: 6025 | Sub Code: Thunderbolt fault | Fault Name: Background Service Identity Failure | Date and Time: 2032-06-18 11:47:58 AM | Module Temperature: 39 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Initializing | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 35 | Application Data: get current process id failure 653;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 294 | UUID: c54e0427-7a62-47a8-bdbd-17a3ce155620]`

**[11:47:59]**
* **NODE_A** [Fault History] (x8 occurrences collapsed): Oss bind failure (Code: 6035)
  * *Details:* Serial Number: 296 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6035 | Fault Code: 6035 | Sub Code: Thunderbolt fault | Fault Name: Oss bind failure | Date and Time: 2032-06-18 11:47:59 AM | Module Temperature: 41 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Ready | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 100 | Application Data: Client Cb not found in deos 653 - -933180756;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 296 | UUID: eada54fb-09fd-4d21-88c8-30126232c3e4]`
* **NODE_A** [Operator Interaction]: Operator Interaction Event
  * *Details:* Dual mode: Dual | Master status: Master | Functional position: Captain | Calibrated airspeed data: 30.000000 | Message: No displayable fields
  * *Citation:* `[Source: NODE_A_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 8 | UUID: c3e2cf79-b06b-4d7b-97f4-e75a0493dded]`
* **NODE_C** [State Transition]: State Transition: Master status -> Master
  * *Details:* [Master status: Master | Dual mode: Single | Opposite fms ok: Not ok | Other dual fms node position: FMS node center | Standby fms node position: FMS node invalid | Functional position: First officer]
  * *Citation:* `[Source: NODE_C_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 68 | UUID: 4c36327b-b53c-4c2f-829f-aba07f245445]`

**[11:48:00]**
* **NODE_A** [Fault History] (x6 occurrences collapsed): Oss task client failure (Code: 6024)
  * *Details:* Serial Number: 304 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6024 | Fault Code: 6024 | Sub Code: Thunderbolt fault | Fault Name: Oss task client failure | Date and Time: 2032-06-18 11:48:00 AM | Module Temperature: 40 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Ready | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 22 | Application Data: Task Client not found;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 304 | UUID: fb743211-f38e-4381-9154-1ce891262086]`
* **NODE_A** [Operator Interaction]: Operator Interaction Event
  * *Details:* Dual mode: Dual | Master status: Master | Functional position: Captain | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 343.006744 | Magnetic track: 66.049805 | [FMS Operational Event: redisplay | FMS node source: Standby]
  * *Citation:* `[Source: NODE_A_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 9 | UUID: 3d304557-7f3d-4721-a6eb-f4e1acd2f1f8]`
* **NODE_A** [Software Event]: Software Event: Operational startup mode identifier
  * *Details:* Data Identifier: Operational startup mode identifier | Data Format: Format fixed str | Left FMS node: Spare | Dual: Dual | [Event identifier: 68 | Operational startup mode: Operational startup cold]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 7 | UUID: 74941053-15df-4879-94dc-58af9388a7b2]`
* **NODE_A** [Software Event]: Software Event: Operational powerup identifier
  * *Details:* Data Identifier: Operational powerup identifier | Data Format: Format fixed str | Left FMS node: Spare | Dual: Dual | [Event identifier: 68 | Operational powerup: Operational powerup normal]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 8 | UUID: 8f37b277-32b7-4f33-8ac3-fa324de0cdd4]`
* **NODE_A** [State Transition]: State Transition: Master status -> Master
  * *Details:* [Master status: Master | Dual mode: Dual | Opposite fms ok: Unknown | Other dual fms node position: FMS node right | Standby fms node position: FMS node invalid | Functional position: Captain]
  * *Citation:* `[Source: NODE_A_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 8 | UUID: 4b251b73-3b25-4f3e-b498-b376e525705d]`

**[11:48:01]**
* **NODE_A** [Fault History]: Oss semaphore failure (Code: 6029)
  * *Details:* Serial Number: 310 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6029 | Fault Code: 6029 | Sub Code: Thunderbolt fault | Fault Name: Oss semaphore failure | Date and Time: 2032-06-18 11:48:01 AM | Module Temperature: 39 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 100 | Application Data: wait semaphore failed in deos 653 - 6 ;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 310 | UUID: cf83173b-41ee-42cd-8d8c-c7ff624cafdf]`
* **NODE_A** [State Transition]: State Transition: Master status -> Master
  * *Details:* [Master status: Master | Dual mode: Dual | Opposite fms ok: Unstable | Other dual fms node position: FMS node right | Standby fms node position: FMS node invalid | Functional position: Captain]
  * *Citation:* `[Source: NODE_A_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 9 | UUID: 5ccabc19-bc6e-479f-8cf4-2e045470e1ec]`
* **NODE_C** [Operator Interaction]: Operator Interaction Event
  * *Details:* Dual mode: Single | Master status: Spare | Functional position: First officer | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 343.006409 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [FMS Operational Event: redisplay | FMS node source: Captain | Event value: 131072]
  * *Citation:* `[Source: NODE_C_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 675 | UUID: 717ef41c-945c-4f6b-8dc3-7db70ab79170]`
* **NODE_C** [Software Event]: Software Event: S pad message identifier l
  * *Details:* Data Identifier: S pad message identifier l | Data Format: Format one unsign 32 | Center FMS node: Master | Right FMS node: Spare | Dual: Single | [L message identifier: Check data base cycle]
  * *Citation:* `[Source: NODE_C_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 254 | UUID: 87d81b8d-21d4-42a0-8c92-e64f8bcab271]`
* **NODE_C** [Software Event]: Software Event: S pad message identifier r
  * *Details:* Data Identifier: S pad message identifier r | Data Format: Format one unsign 32 | Center FMS node: Master | Right FMS node: Spare | Dual: Single | [R message identifier: Check data base cycle]
  * *Citation:* `[Source: NODE_C_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 255 | UUID: d83da3cf-992d-478a-9c8a-634e61ff63bf]`
* **NODE_C** [State Transition] (x2 occurrences collapsed): State Transition: Master status -> Spare
  * *Details:* [Master status: Spare | Dual mode: Single | Opposite fms ok: Not ok | Other dual fms node position: FMS node left | Standby fms node position: FMS node invalid | Functional position: First officer]
  * *Citation:* `[Source: NODE_C_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 69 | UUID: 0ba73ad6-ea1f-4617-bcc6-e62329241644]`

**[11:48:02]**
* **NODE_A** [Fault History]: Oss task client failure (Code: 6024)
  * *Details:* Serial Number: 311 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6024 | Fault Code: 6024 | Sub Code: Thunderbolt fault | Fault Name: Oss task client failure | Date and Time: 2032-06-18 11:48:02 AM | Module Temperature: 40 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 22 | Application Data: Task Client not found;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 311 | UUID: 882f3687-0c15-4f38-aa5f-817fd1ea4072]`
* **NODE_A** [Fault History]: Oss semaphore failure (Code: 6029)
  * *Details:* Serial Number: 312 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6029 | Fault Code: 6029 | Sub Code: Thunderbolt fault | Fault Name: Oss semaphore failure | Date and Time: 2032-06-18 11:48:02 AM | Module Temperature: 40 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 100 | Application Data: wait semaphore failed in deos 653 - 6 ;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 312 | UUID: c00850f9-2b9c-4213-897a-6c2e562d1611]`
* **NODE_A** [Fault History] (x3 occurrences collapsed): Scheduled FMS Activity Missed Timing Requirement (Code: 6000)
  * *Details:* Serial Number: 313 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6000 | Fault Code: 6000 | Sub Code: Thunderbolt fault | Fault Name: Scheduled FMS Activity Missed Timing Requirement | Date and Time: 2032-06-18 11:48:02 AM | Module Temperature: 40 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 50 | Application Data: Deadline miss` Background service - 1114128;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 313 | UUID: bae23c18-fc7b-43fc-afae-7dffde710456]`
* **NODE_A** [Software Event]: Software Event: S pad message identifier l
  * *Details:* Data Identifier: S pad message identifier l | Data Format: Format one unsign 32 | Left FMS node: Spare | Dual: Dual | [L message identifier: Please wait]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 9 | UUID: 8f002b70-6e74-4b25-890e-fbd1311bf804]`
* **NODE_A** [Software Event]: Software Event: S pad message identifier r
  * *Details:* Data Identifier: S pad message identifier r | Data Format: Format one unsign 32 | Left FMS node: Spare | Dual: Dual | [R message identifier: Please wait]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 10 | UUID: 532687f3-4b61-480f-8613-926cce4d4145]`
* **NODE_A** [State Transition]: State Transition: Master status -> Master
  * *Details:* [Master status: Master | Dual mode: Dual | Opposite fms ok: Ok | Other dual fms node position: FMS node right | Standby fms node position: FMS node invalid | Functional position: Captain]
  * *Citation:* `[Source: NODE_A_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 10 | UUID: bd9cfbb9-65d7-4c95-b79c-f53a0c04356c]`
* **NODE_C** [Software Event]: Software Event: S pad message identifier l
  * *Details:* Data Identifier: S pad message identifier l | Data Format: Format one unsign 32 | Center FMS node: Master | Right FMS node: Spare | Dual: Single | [L message identifier: Please wait]
  * *Citation:* `[Source: NODE_C_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 256 | UUID: ce2d6fa8-ca0d-4cd1-a248-dbce75f34fec]`
* **NODE_C** [Software Event]: Software Event: S pad message identifier r
  * *Details:* Data Identifier: S pad message identifier r | Data Format: Format one unsign 32 | Center FMS node: Master | Right FMS node: Spare | Dual: Single | [R message identifier: Please wait]
  * *Citation:* `[Source: NODE_C_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 257 | UUID: a860a3d4-59d5-4a47-9f94-dff39dc2e449]`
* **NODE_C** [State Transition]: State Transition: Master status -> Spare
  * *Details:* [Master status: Spare | Dual mode: Single | Opposite fms ok: Ok | Other dual fms node position: FMS node left | Standby fms node position: FMS node invalid | Functional position: First officer]
  * *Citation:* `[Source: NODE_C_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 71 | UUID: acc059e7-1b2b-4bf3-a22d-618099056da9]`

**[11:48:03]**
* **NODE_A** [Fault History]: Scheduled FMS Activity Missed Timing Requirement (Code: 6000)
  * *Details:* Serial Number: 316 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6000 | Fault Code: 6000 | Sub Code: Thunderbolt fault | Fault Name: Scheduled FMS Activity Missed Timing Requirement | Date and Time: 2032-06-18 11:48:03 AM | Module Temperature: 39 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 50 | Application Data: Deadline miss` Background service - 1114138;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 316 | UUID: 1ccb6bc1-6a15-4244-a632-2768aa553631]`

**[11:48:05]**
* **NODE_A** [Software Event]: Software Event: Master spare identifier
  * *Details:* Data Identifier: Master spare identifier | Data Format: Format fixed str | Left FMS node: Master | Right FMS node: Spare | Dual: Dual | [Event identifier: 68 | FMS node position: Operational master spare Changed]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 11 | UUID: ef0c7bfc-6aa7-40b0-8832-461b1f3840b6]`

**[11:48:06]**
* **NODE_C** [Software Event]: Software Event: Master spare identifier
  * *Details:* Data Identifier: Master spare identifier | Data Format: Format fixed str | Left FMS node: Master | Right FMS node: Spare | Dual: Single | [Event identifier: 68 | FMS node position: Operational master spare Changed]
  * *Citation:* `[Source: NODE_C_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 258 | UUID: 1fcb3cbf-37eb-4987-bf02-65714d0df4bd]`

**[11:48:09]**
* **NODE_C** [Fault History]: Na (Code: 0)
  * *Details:* Serial Number: 237 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Sub Code: Thunderbolt fault | Fault Name: Na | Date and Time: 2032-06-18 11:48:09 AM | Current Recovery Type: No Recovery Action | Module State: Ms unequipped e | Context State: Cs not equipped e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: Power Loss | Fault Exception: False | Extended Record: False | Application Data: ;
  * *Citation:* `[Source: NODE_C_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 237 | UUID: 4c6b2323-7ecf-44f2-b89c-7fae5e038b63]`
* **NODE_C** [Operator Interaction]: Operator Interaction Event
  * *Details:* Dual mode: Dual | Master status: Spare | Functional position: First officer | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 343.005432 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [Fault/Event: Cold Start Due To A Re-Synch On The Receiver]
  * *Citation:* `[Source: NODE_C_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 676 | UUID: ca3e28be-fc2a-4f80-b018-d754553f26df]`

**[11:48:10]**
* **NODE_A** [Fault History]: Application error (Code: 6001)
  * *Details:* Serial Number: 317 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6001 | Fault Code: 6001 | Sub Code: Thunderbolt fault | Fault Name: Application error | Date and Time: 2032-06-18 11:48:10 AM | Module Temperature: 40 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: Fr context shutdown e | Module State: Operational | Context State: Cs fault recovery e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: True | Extended Record: True | Application Data Size: 372 | Application Data: @x};P?;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 317 | UUID: bc79ae56-ef56-4716-bc0e-99a20be4a016]`

**[11:48:11]**
* **NODE_A** [Fault History] (x2 occurrences collapsed): Application error (Code: 6001)
  * *Details:* Serial Number: 318 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6001 | Fault Code: 6001 | Sub Code: Thunderbolt fault | Fault Name: Application error | Date and Time: 2032-06-18 11:48:11 AM | Module Temperature: 40 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: Fr context shutdown e | Module State: Operational | Context State: Cs fault recovery e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: True | Extended Record: True | Application Data Size: 192 | Application Data: @x};
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 318 | UUID: 8aefc687-a041-40b7-b7aa-9eb9bdad4375]`

**[11:48:58]**
* **NODE_B** [Fault History] (x2 occurrences collapsed): Background Service Identity Failure (Code: 6025)
  * *Details:* Serial Number: 214 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6025 | Fault Code: 6025 | Sub Code: Thunderbolt fault | Fault Name: Background Service Identity Failure | Date and Time: 2032-06-18 11:48:58 AM | Module Temperature: 37 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Initializing | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 35 | Application Data: get current process id failure 653;
  * *Citation:* `[Source: NODE_B_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 214 | UUID: e21fcc4f-069d-454e-b723-ef267474136c]`

**[11:48:59]**
* **NODE_B** [Fault History] (x2 occurrences collapsed): Background Service Identity Failure (Code: 6025)
  * *Details:* Serial Number: 216 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6025 | Fault Code: 6025 | Sub Code: Thunderbolt fault | Fault Name: Background Service Identity Failure | Date and Time: 2032-06-18 11:48:59 AM | Module Temperature: 37 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Initializing | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 35 | Application Data: get current process id failure 653;
  * *Citation:* `[Source: NODE_B_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 216 | UUID: b3ffeb86-2f30-46c3-aa4b-56daef20cd95]`
* **NODE_B** [Fault History]: Oss loading failure (Code: 6052)
  * *Details:* Serial Number: 218 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6052 | Fault Code: 6052 | Sub Code: Thunderbolt fault | Fault Name: Oss loading failure | Date and Time: 2032-06-18 11:48:59 AM | Module Temperature: 37 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Initializing | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 100 | Application Data: Failed to load library in Deos 653 - Libpssl dtf manager so.so 11 11;
  * *Citation:* `[Source: NODE_B_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 218 | UUID: bc91036c-2c41-4557-aa9b-2b51e361813c]`
* **NODE_B** [Fault History] (x2 occurrences collapsed): Background Service Identity Failure (Code: 6025)
  * *Details:* Serial Number: 219 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6025 | Fault Code: 6025 | Sub Code: Thunderbolt fault | Fault Name: Background Service Identity Failure | Date and Time: 2032-06-18 11:48:59 AM | Module Temperature: 36 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Initializing | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 35 | Application Data: get current process id failure 653;
  * *Citation:* `[Source: NODE_B_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 219 | UUID: 4b4a1dea-2d76-4749-8120-7f379911d167]`

**[11:49:00]**
* **NODE_B** [Operator Interaction]: Operator Interaction Event
  * *Details:* Dual mode: Dual | Master status: Master | Functional position: Captain | Calibrated airspeed data: 30.000000 | Message: No displayable fields
  * *Citation:* `[Source: NODE_B_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 7 | UUID: 7e257910-66fd-41df-9149-723d33798b70]`

**[11:49:01]**
* **NODE_B** [Fault History] (x8 occurrences collapsed): Oss bind failure (Code: 6035)
  * *Details:* Serial Number: 221 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6035 | Fault Code: 6035 | Sub Code: Thunderbolt fault | Fault Name: Oss bind failure | Date and Time: 2032-06-18 11:49:01 AM | Module Temperature: 36 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Ready | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 100 | Application Data: Client Cb not found in deos 653 - -933180756;
  * *Citation:* `[Source: NODE_B_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 221 | UUID: 7d3e8246-d2cd-49a9-95be-43d8b41dac11]`
* **NODE_B** [Fault History] (x4 occurrences collapsed): Oss task client failure (Code: 6024)
  * *Details:* Serial Number: 229 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6024 | Fault Code: 6024 | Sub Code: Thunderbolt fault | Fault Name: Oss task client failure | Date and Time: 2032-06-18 11:49:01 AM | Module Temperature: 38 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Ready | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 22 | Application Data: Task Client not found;
  * *Citation:* `[Source: NODE_B_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 229 | UUID: e110fc54-16c5-42d5-a140-a221d39ca953]`
* **NODE_B** [Operator Interaction]: Operator Interaction Event
  * *Details:* Dual mode: Dual | Master status: Master | Functional position: Captain | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 342.997345 | Magnetic track: 66.049805 | [FMS Operational Event: redisplay | FMS node source: Standby]
  * *Citation:* `[Source: NODE_B_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 8 | UUID: e425c1b6-2c43-4af9-a6f8-6fb8101a84b2]`
* **NODE_B** [Software Event]: Software Event: Operational startup mode identifier
  * *Details:* Data Identifier: Operational startup mode identifier | Data Format: Format fixed str | Left FMS node: Spare | Dual: Dual | [Event identifier: 68 | Operational startup mode: Operational startup cold]
  * *Citation:* `[Source: NODE_B_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 32 | UUID: 3b63f8ff-3890-461c-9198-2301c4f22d08]`
* **NODE_B** [Software Event]: Software Event: Operational powerup identifier
  * *Details:* Data Identifier: Operational powerup identifier | Data Format: Format fixed str | Left FMS node: Spare | Dual: Dual | [Event identifier: 68 | Operational powerup: Operational powerup normal]
  * *Citation:* `[Source: NODE_B_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 33 | UUID: 50d70e7d-280b-407f-a8ce-ff620956583b]`
* **NODE_B** [State Transition]: State Transition: Master status -> Master
  * *Details:* [Master status: Master | Dual mode: Dual | Opposite fms ok: Unknown | Other dual fms node position: FMS node right | Standby fms node position: FMS node invalid | Functional position: Captain]
  * *Citation:* `[Source: NODE_B_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 9 | UUID: a5b00d24-e742-42d6-9719-83decb73af08]`

**[11:49:02]**
* **NODE_B** [Fault History] (x2 occurrences collapsed): Oss task client failure (Code: 6024)
  * *Details:* Serial Number: 233 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6024 | Fault Code: 6024 | Sub Code: Thunderbolt fault | Fault Name: Oss task client failure | Date and Time: 2032-06-18 11:49:02 AM | Module Temperature: 37 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 22 | Application Data: Task Client not found;
  * *Citation:* `[Source: NODE_B_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 233 | UUID: b329d52a-0f1e-4020-a5fe-2e3c646cc9d6]`
* **NODE_B** [Fault History]: Oss semaphore failure (Code: 6029)
  * *Details:* Serial Number: 235 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6029 | Fault Code: 6029 | Sub Code: Thunderbolt fault | Fault Name: Oss semaphore failure | Date and Time: 2032-06-18 11:49:02 AM | Module Temperature: 36 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 100 | Application Data: wait semaphore failed in deos 653 - 6 ;
  * *Citation:* `[Source: NODE_B_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 235 | UUID: 43fd3641-4095-45f8-9143-c02847d02dd2]`
* **NODE_B** [State Transition]: State Transition: Master status -> Master
  * *Details:* [Master status: Master | Dual mode: Dual | Opposite fms ok: Not ok | Other dual fms node position: FMS node right | Standby fms node position: FMS node invalid | Functional position: Captain]
  * *Citation:* `[Source: NODE_B_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 10 | UUID: f831dd20-cc77-4664-80b2-f59abb4247cd]`

**[11:49:03]**
* **NODE_B** [Fault History]: Oss task client failure (Code: 6024)
  * *Details:* Serial Number: 236 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6024 | Fault Code: 6024 | Sub Code: Thunderbolt fault | Fault Name: Oss task client failure | Date and Time: 2032-06-18 11:49:03 AM | Module Temperature: 36 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 22 | Application Data: Task Client not found;
  * *Citation:* `[Source: NODE_B_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 236 | UUID: 38462005-1242-4588-b896-e530fae72856]`

**[11:49:05]**
* **NODE_B** [Fault History]: Scheduled FMS Activity Missed Timing Requirement (Code: 6000)
  * *Details:* Serial Number: 237 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6000 | Fault Code: 6000 | Sub Code: Thunderbolt fault | Fault Name: Scheduled FMS Activity Missed Timing Requirement | Date and Time: 2032-06-18 11:49:05 AM | Module Temperature: 36 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 50 | Application Data: Deadline miss` Background service - 2162714;
  * *Citation:* `[Source: NODE_B_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 237 | UUID: b72ff7b1-32d8-4294-8937-0486b42c3eba]`

**[11:49:06]**
* **NODE_B** [Software Event]: Software Event: Data link comm master identifier
  * *Details:* Data Identifier: Data link comm master identifier | Data Format: Format fixed str | Left FMS node: Spare | Dual: Dual | [Event identifier: 68 | Data link comm master status log: Data link comm slave to master]
  * *Citation:* `[Source: NODE_B_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 34 | UUID: bfff1c94-f432-48cf-827d-2a1a546aeb55]`

**[11:49:07]**
* **NODE_B** [Software Event]: Software Event: Master spare identifier
  * *Details:* Data Identifier: Master spare identifier | Data Format: Format fixed str | Center FMS node: Master | Right FMS node: Spare | Dual: Dual | [Event identifier: 68 | FMS node position: Operational master spare Changed]
  * *Citation:* `[Source: NODE_B_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 35 | UUID: f96b8754-5382-4a59-a8e0-d0d9238d37c5]`

**[11:49:09]**
* **NODE_B** [Software Event]: Software Event: Dual mode identifier
  * *Details:* Data Identifier: Dual mode identifier | Data Format: Format fixed str | Center FMS node: Master | Right FMS node: Spare | Dual: Single | [Event identifier: 68 | Operational dual mode: Operational dual mode Changed]
  * *Citation:* `[Source: NODE_B_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 36 | UUID: 40ad7df3-c808-4465-879d-4053b8bce265]`
* **NODE_B** [State Transition]: State Transition: Master status -> Master
  * *Details:* [Master status: Master | Dual mode: Single | Opposite fms ok: Not ok | Other dual fms node position: FMS node right | Standby fms node position: FMS node invalid | Functional position: Captain]
  * *Citation:* `[Source: NODE_B_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 11 | UUID: 8319b5f7-89e1-42d5-b9e5-976aa8b95f40]`

**[11:49:10]**
* **NODE_B** [Fault History] (x2 occurrences collapsed): Scheduled FMS Activity Missed Timing Requirement (Code: 6000)
  * *Details:* Serial Number: 238 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6000 | Fault Code: 6000 | Sub Code: Thunderbolt fault | Fault Name: Scheduled FMS Activity Missed Timing Requirement | Date and Time: 2032-06-18 11:49:10 AM | Module Temperature: 37 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 50 | Application Data: Deadline miss` Background service - 2162715;
  * *Citation:* `[Source: NODE_B_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 238 | UUID: 13dacfa2-7ceb-41b7-bebd-b8fc971fb959]`
* **NODE_B** [Operator Interaction] (x4 occurrences collapsed): Operator Interaction Event
  * *Details:* Dual mode: Single | Master status: Master | Functional position: Captain | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 342.995850 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [FMS Operational Event: clear altitude | FMS node source: Standby | Event value: 65536]
  * *Citation:* `[Source: NODE_B_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 9 | UUID: e48495c6-40f4-4b62-b253-8209c87975da]`

**[11:49:11]**
* **NODE_B** [Operator Interaction] (x2 occurrences collapsed): Operator Interaction Event
  * *Details:* Dual mode: Single | Master status: Master | Functional position: Captain | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 342.995667 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [FMS Operational Event: clear altitude | FMS node source: Standby | Event value: 65540]
  * *Citation:* `[Source: NODE_B_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 13 | UUID: 065256d4-fca3-4065-aa3d-ef048fda6a40]`

**[11:49:12]**
* **NODE_B** [Fault History]: Scheduled FMS Activity Missed Timing Requirement (Code: 6000)
  * *Details:* Serial Number: 240 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6000 | Fault Code: 6000 | Sub Code: Thunderbolt fault | Fault Name: Scheduled FMS Activity Missed Timing Requirement | Date and Time: 2032-06-18 11:49:12 AM | Module Temperature: 36 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 50 | Application Data: Deadline miss` Background service - 2162713;
  * *Citation:* `[Source: NODE_B_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 240 | UUID: 1b7e004e-bdd8-4aa8-907a-48d41fdda815]`
* **NODE_B** [Operator Interaction]: Operator Interaction Event
  * *Details:* Dual mode: Single | Master status: Master | Functional position: Captain | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 342.995667 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [FMS Operational Event: no phase change | FMS node source: Standby | Event value: 65540]
  * *Citation:* `[Source: NODE_B_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 15 | UUID: 0977919b-e155-4202-8292-99292360ebfb]`

**[11:49:14]**
* **NODE_B** [Fault History]: Scheduled FMS Activity Missed Timing Requirement (Code: 6000)
  * *Details:* Serial Number: 241 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6000 | Fault Code: 6000 | Sub Code: Thunderbolt fault | Fault Name: Scheduled FMS Activity Missed Timing Requirement | Date and Time: 2032-06-18 11:49:14 AM | Module Temperature: 36 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 50 | Application Data: Deadline miss` Background service - 2162712;
  * *Citation:* `[Source: NODE_B_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 241 | UUID: 6875de8d-533f-4c04-baf6-c7beae2862ed]`
* **NODE_B** [Fault History]: Oss semaphore failure (Code: 6029)
  * *Details:* Serial Number: 242 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6029 | Fault Code: 6029 | Sub Code: Thunderbolt fault | Fault Name: Oss semaphore failure | Date and Time: 2032-06-18 11:49:14 AM | Module Temperature: 37 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 100 | Application Data: wait semaphore failed in deos 653 - 6 ;
  * *Citation:* `[Source: NODE_B_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 242 | UUID: 60371485-0881-4f55-b218-1c8f35951edb]`

**[11:49:15]**
* **NODE_B** [Software Event]: Software Event: Master spare identifier
  * *Details:* Data Identifier: Master spare identifier | Data Format: Format fixed str | Center FMS node: Master | Dual: Single | [Event identifier: 68 | FMS node position: Operational master spare Changed]
  * *Citation:* `[Source: NODE_B_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 37 | UUID: 01a4449b-8cc9-4575-bb59-64eaaa97e287]`

**[11:49:16]**
* **NODE_B** [Fault History]: Oss semaphore failure (Code: 6029)
  * *Details:* Serial Number: 243 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6029 | Fault Code: 6029 | Sub Code: Thunderbolt fault | Fault Name: Oss semaphore failure | Date and Time: 2032-06-18 11:49:16 AM | Module Temperature: 36 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 100 | Application Data: wait semaphore failed in deos 653 - 6 ;
  * *Citation:* `[Source: NODE_B_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 243 | UUID: 43bb1efd-11a7-4fdd-8507-d7d9679784bf]`
* **NODE_B** [Software Event]: Software Event: S pad message identifier l
  * *Details:* Data Identifier: S pad message identifier l | Data Format: Format one unsign 32 | Center FMS node: Master | Dual: Single | [L message identifier: Navigation primary lost]
  * *Citation:* `[Source: NODE_B_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 38 | UUID: 21b6a43b-35a6-4824-afa1-ec8fab3a79f5]`
* **NODE_B** [Software Event]: Software Event: S pad message identifier r
  * *Details:* Data Identifier: S pad message identifier r | Data Format: Format one unsign 32 | Center FMS node: Master | Dual: Single | [R message identifier: Navigation primary lost]
  * *Citation:* `[Source: NODE_B_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 39 | UUID: 16442dc7-7bc9-4b40-94e4-e99cb87c374b]`

**[11:49:17]**
* **NODE_B** [Fault History]: Oss semaphore failure (Code: 6029)
  * *Details:* Serial Number: 244 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6029 | Fault Code: 6029 | Sub Code: Thunderbolt fault | Fault Name: Oss semaphore failure | Date and Time: 2032-06-18 11:49:17 AM | Module Temperature: 37 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 100 | Application Data: wait semaphore failed in deos 653 - 6 ;
  * *Citation:* `[Source: NODE_B_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 244 | UUID: d4da7213-54cc-426b-a3ab-b16c32b6d867]`

**[11:49:18]**
* **NODE_B** [Operator Interaction]: Operator Interaction Event
  * *Details:* Dual mode: Single | Master status: Master | Functional position: Captain | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 342.995605 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [FMS Operational Event: Performance Data Changed | FMS node source: Standby | Event value: 65547]
  * *Citation:* `[Source: NODE_B_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 16 | UUID: bbdc80cf-2d79-4a02-a70e-6d3af369a988]`

**[11:49:19]**
* **NODE_B** [Fault History]: Oss semaphore failure (Code: 6029)
  * *Details:* Serial Number: 245 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6029 | Fault Code: 6029 | Sub Code: Thunderbolt fault | Fault Name: Oss semaphore failure | Date and Time: 2032-06-18 11:49:19 AM | Module Temperature: 36 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 100 | Application Data: wait semaphore failed in deos 653 - 6 ;
  * *Citation:* `[Source: NODE_B_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 245 | UUID: 65c45938-1d64-4725-8582-fa3754a412ae]`

**[11:49:20]**
* **NODE_A** [Fault History]: Oss loading failure (Code: 6052)
  * *Details:* Serial Number: 320 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6052 | Fault Code: 6052 | Sub Code: Thunderbolt fault | Fault Name: Oss loading failure | Date and Time: 2032-06-18 11:49:20 AM | Module Temperature: 40 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Initializing | Last Context Reset Reason: Fr context shutdown e | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 100 | Application Data: Failed to load library in Deos 653 - Libpssl dtf manager so.so 11 11;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 320 | UUID: 789d80e8-2338-424c-87a1-147c5edb31cb]`
* **NODE_B** [Fault History]: Oss semaphore failure (Code: 6029)
  * *Details:* Serial Number: 246 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6029 | Fault Code: 6029 | Sub Code: Thunderbolt fault | Fault Name: Oss semaphore failure | Date and Time: 2032-06-18 11:49:20 AM | Module Temperature: 36 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 100 | Application Data: wait semaphore failed in deos 653 - 6 ;
  * *Citation:* `[Source: NODE_B_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 246 | UUID: 00e70944-3ae8-45ca-9e3e-a03e84ac642b]`
* **NODE_C** [Fault History]: Oss loading failure (Code: 6052)
  * *Details:* Serial Number: 238 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6052 | Fault Code: 6052 | Sub Code: Thunderbolt fault | Fault Name: Oss loading failure | Date and Time: 2032-06-18 11:49:20 AM | Module Temperature: 39 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Initializing | Last Context Reset Count: 5 | Last Context Reset Reason: Fr context shutdown e | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 100 | Application Data: Failed to load library in Deos 653 - Libpssl dtf manager so.so 11 11;
  * *Citation:* `[Source: NODE_C_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 238 | UUID: 8dfebb8c-eea9-43cb-85c8-360206440fb5]`

**[11:49:21]**
* **NODE_A** [Fault History]: Cpdb opc not not enabled (Code: 6)
  * *Details:* Serial Number: 321 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 11643 | Fault Code: 6 | Sub Code: 107 | Fault Name: Cpdb opc not not enabled | Date and Time: 2032-06-18 11:49:21 AM | Module Temperature: 40 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Initializing | Last Context Reset Reason: Fr context shutdown e | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 8 | Application Data: ?~J;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 321 | UUID: 64d07c4c-7199-4efa-8a26-a66b40525892]`
* **NODE_A** [Operator Interaction]: Operator Interaction Event
  * *Details:* Dual mode: Single | Master status: Master | Functional position: Captain | Calibrated airspeed data: 30.000000 | Message: No displayable fields
  * *Citation:* `[Source: NODE_A_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 10 | UUID: 62344a59-5293-4b8a-b9c6-0cd91201b35f]`
* **NODE_B** [Software Event]: Software Event: S pad message identifier l
  * *Details:* Data Identifier: S pad message identifier l | Data Format: Format one unsign 32 | Center FMS node: Master | Dual: Single | [L message identifier: Navigation primary]
  * *Citation:* `[Source: NODE_B_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 40 | UUID: 27912ab1-779e-47be-b2c2-7422a8abb6c5]`
* **NODE_B** [Software Event]: Software Event: S pad message identifier r
  * *Details:* Data Identifier: S pad message identifier r | Data Format: Format one unsign 32 | Center FMS node: Master | Dual: Single | [R message identifier: Navigation primary]
  * *Citation:* `[Source: NODE_B_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 41 | UUID: 29d90522-328d-46a3-a728-0d265a556191]`
* **NODE_B** [Software Event]: Software Event: Opc configuration data identifier
  * *Details:* Data Identifier: Opc configuration data identifier | Data Format: Format opc configuration data | Center FMS node: Master | Dual: Single | [Identifier: Configuration data | Performance custo 3: False | Performance custo 2: False | Performance custo 1: False | Operational data link datalink: True | Air traffic service enable: True | Kilogram enable: True | Metric enable: True | Display trajectory: 1 | Grid mora enable: True | I4d rta enable: False | Radio navigation 2 installed: True | Aim disable: True | No radio navigation on board: False | Passenger count enable: True | Fls enable: True | To securization enable: True | No ap fd mda mdh disconnect: True | To derate enable: True | Climb derate enable: False | Fnl des enable: True | Cda enable: 1 | Cpdb opc enable: False | Vor2 dme2 on board: True | Rnp function enable: True | Leg sequencing monitoring enable: True | Resync check enable: True | To securization 2 enable: True | Sbas enable: True | Sls enable: True | Jfgw display on mfd enable: True | Acr 2 on board: False | Vertical display enable: True | FMS trjctry on vd enable: True | Mora on vd enable: True | Msa on vd enable: True | Etoc enable: True | Freeze scale on vd enable: False | Fls axis on vd enable: True | Aess twsf trjctry enable: True | Auto derate climb enable: True | Polar navigation enabled: True | Back beam approach en: True | FMS platform type 1: True | FMS platform type 2: True | FMS platform type 3: False | FMS platform type 4: False | FMS engine manuf 1: False | FMS engine manuf 2: True | FMS engine manuf 3: False | FMS engine type 1: False | FMS engine type 2: True | FMS engine type 3: False | FMS engine type 4: False | FMS engine type 5: False | Takeoff rnp: 1.000000 | Gps approach rnp: 0.300000 | Precision approach rnp: 0.500000 | Nonprecision approach rnp: 0.500000 | Terminal rnp: 1.000000 | Enroute rnp: 2.000000 | Oceanic rnp: 2.000000 | Takeoff tla: 110.991997 | Takeoff hal: 1.000000 | Approach hal: 0.300000 | Terminal hal: 1.000000 | Enroute hal: 2.000000 | Oceanic hal: 2.000000 | Tail number 32: .F-Wzht | Tail number 16: Zht | Tail number 8: T | Configuration data version: [Redacted Payload] | Opc integrity validation: 61]
  * *Citation:* `[Source: NODE_B_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 42 | UUID: 0ab966ba-95c9-41b6-bf8e-c0aefca4da42]`
* **NODE_C** [Operator Interaction]: Operator Interaction Event
  * *Details:* Dual mode: Dual | Master status: Spare | Functional position: First officer | Calibrated airspeed data: 30.000000 | Message: No displayable fields
  * *Citation:* `[Source: NODE_C_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 677 | UUID: 25cb7032-0ab4-4e0b-abe1-4292e93563a9]`

**[11:49:22]**
* **NODE_A** [Fault History] (x4 occurrences collapsed): Oss bind failure (Code: 6035)
  * *Details:* Serial Number: 322 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6035 | Fault Code: 6035 | Sub Code: Thunderbolt fault | Fault Name: Oss bind failure | Date and Time: 2032-06-18 11:49:22 AM | Module Temperature: 40 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Ready | Last Context Reset Reason: Fr context shutdown e | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 100 | Application Data: Client Cb not found in deos 653 - -933180756;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 322 | UUID: 30dead47-c000-4e7a-9ee0-f60ebc8b55d4]`
* **NODE_A** [Fault History]: Oss task client failure (Code: 6024)
  * *Details:* Serial Number: 326 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6024 | Fault Code: 6024 | Sub Code: Thunderbolt fault | Fault Name: Oss task client failure | Date and Time: 2032-06-18 11:49:22 AM | Module Temperature: 39 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Ready | Last Context Reset Reason: Fr context shutdown e | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 22 | Application Data: Task Client not found;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 326 | UUID: 2cae2644-4a27-4b40-949f-20207b87f7df]`
* **NODE_A** [Fault History]: Ndb out of date (Code: 5)
  * *Details:* Serial Number: 327 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 11311 | Fault Code: 5 | Sub Code: 31 | Fault Name: Ndb out of date | Date and Time: 2032-06-18 11:49:22 AM | Module Temperature: 39 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: Fr context shutdown e | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 8 | Application Data: ?~J;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 327 | UUID: f5945550-4e5b-4e6f-9719-e99ab80716c5]`
* **NODE_A** [Fault History]: Oss task client failure (Code: 6024)
  * *Details:* Serial Number: 328 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6024 | Fault Code: 6024 | Sub Code: Thunderbolt fault | Fault Name: Oss task client failure | Date and Time: 2032-06-18 11:49:22 AM | Module Temperature: 39 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: Fr context shutdown e | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 22 | Application Data: Task Client not found;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 328 | UUID: 8cbe993f-7e90-46b5-8359-72f4f022d837]`
* **NODE_A** [Fault History]: Error during start process (Code: 9)
  * *Details:* Serial Number: 329 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 12315 | Fault Code: 9 | Sub Code: 11 | Fault Name: Error during start process | Date and Time: 2032-06-18 11:49:22 AM | Module Temperature: 39 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: Fr context shutdown e | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 8 | Application Data: ?~J;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 329 | UUID: 51b9b8e7-c7a4-440a-97e2-e5097a0f2538]`
* **NODE_A** [Fault History] (x2 occurrences collapsed): Oss task client failure (Code: 6024)
  * *Details:* Serial Number: 330 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6024 | Fault Code: 6024 | Sub Code: Thunderbolt fault | Fault Name: Oss task client failure | Date and Time: 2032-06-18 11:49:22 AM | Module Temperature: 40 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: Fr context shutdown e | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 22 | Application Data: Task Client not found;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 330 | UUID: 33831599-4afa-4af1-8d74-c7c1d21fb7ea]`
* **NODE_A** [Software Event]: Software Event: Operational startup mode identifier
  * *Details:* Data Identifier: Operational startup mode identifier | Data Format: Format fixed str | Left FMS node: Spare | Dual: Single | [Event identifier: 68 | Operational startup mode: Operational startup cold]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 12 | UUID: e5cce961-8c1d-4d56-8328-d516d6cfe9d1]`
* **NODE_A** [Software Event]: Software Event: Dual mode identifier
  * *Details:* Data Identifier: Dual mode identifier | Data Format: Format fixed str | Left FMS node: Spare | Dual: Single | [Event identifier: 68 | Operational dual mode: Operational dual mode Changed]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 13 | UUID: 8ff0b324-db37-4c63-877d-083096cd9b10]`
* **NODE_A** [Software Event]: Software Event: Operational powerup identifier
  * *Details:* Data Identifier: Operational powerup identifier | Data Format: Format fixed str | Left FMS node: Spare | Dual: Single | [Event identifier: 68 | Operational powerup: Operational powerup normal]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 14 | UUID: 343dcfaf-2aa9-491f-b58f-6f83b23ce3ba]`
* **NODE_A** [State Transition]: State Transition: Master status -> Master
  * *Details:* [Master status: Master | Dual mode: Single | Opposite fms ok: Unknown | Other dual fms node position: FMS node invalid | Standby fms node position: FMS node invalid | Functional position: Standby]
  * *Citation:* `[Source: NODE_A_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 11 | UUID: 5ac06619-99b5-4393-80f7-26c56ff402d6]`
* **NODE_B** [Fault History]: Navigation Data Coordination Activity Failure (Code: 11)
  * *Details:* Serial Number: 247 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 12925 | Fault Code: 11 | Sub Code: 109 | Fault Name: Navigation Data Coordination Activity Failure | Date and Time: 2032-06-18 11:49:22 AM | Module Temperature: 36 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 8 | Application Data: ?~J;
  * *Citation:* `[Source: NODE_B_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 247 | UUID: dc1b7879-8f17-4d80-9e4b-e1e355282729]`
* **NODE_B** [Software Event]: Software Event: Sys status identifier
  * *Details:* Data Identifier: Sys status identifier | Data Format: Format sys status | Center FMS node: Master | Dual: Single | [Identifier: Sys | Platform family: A350 | Air frame ident: A350 | FMS node physical position: Center | Engine ident: Trent | Engine manufact: 2 | Opsys pn: Hnp5dxcl01xea01 | Ndb pn: Abv2601l01 | Ami database pn: Hnp40 | Database Reference: [Removed]: Hnp56xcd06xha08 | Cpdb pn: Not loaded]
  * *Citation:* `[Source: NODE_B_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 43 | UUID: 30fe2a0d-af0a-4619-89f4-be099d7645e6]`
* **NODE_C** [Software Event]: Software Event: Operational startup mode identifier
  * *Details:* Data Identifier: Operational startup mode identifier | Data Format: Format fixed str | Left FMS node: Spare | Dual: Dual | [Event identifier: 68 | Operational startup mode: Operational startup cold]
  * *Citation:* `[Source: NODE_C_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 259 | UUID: ed5c5eae-94bc-4f11-8ad9-3feb6b5d123d]`
* **NODE_C** [Software Event]: Software Event: Operational powerup identifier
  * *Details:* Data Identifier: Operational powerup identifier | Data Format: Format fixed str | Left FMS node: Spare | Dual: Dual | [Event identifier: 68 | Operational powerup: Operational powerup normal]
  * *Citation:* `[Source: NODE_C_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 260 | UUID: 8d4f786b-1a8e-47cb-829d-2963ae43c1c5]`
* **NODE_C** [State Transition]: State Transition: Master status -> Spare
  * *Details:* [Master status: Spare | Dual mode: Dual | Opposite fms ok: Unknown | Other dual fms node position: FMS node left | Standby fms node position: FMS node invalid | Functional position: First officer]
  * *Citation:* `[Source: NODE_C_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 72 | UUID: 3e5ed883-3b3b-4152-91ad-0d804b3080d6]`

**[11:49:23]**
* **NODE_B** [State Transition]: State Transition: Master status -> Master
  * *Details:* [Master status: Master | Dual mode: Single | Opposite fms ok: Unstable | Other dual fms node position: FMS node right | Standby fms node position: FMS node invalid | Functional position: Captain]
  * *Citation:* `[Source: NODE_B_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 12 | UUID: 4ca4e98f-7d39-46bc-a32f-0d68995aa1c5]`
* **NODE_B** [State Transition]: State Transition: Master status -> Standby
  * *Details:* [Master status: Standby | Dual mode: Single | Opposite fms ok: Unstable | Other dual fms node position: FMS node right | Standby fms node position: FMS node left | Functional position: Standby]
  * *Citation:* `[Source: NODE_B_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 13 | UUID: bd52b420-5c1e-43a2-87a4-a6f20ae21f38]`
* **NODE_C** [Software Event]: Software Event: Dual mode identifier
  * *Details:* Data Identifier: Dual mode identifier | Data Format: Format fixed str | Left FMS node: Spare | Dual: Single | [Event identifier: 68 | Operational dual mode: Operational dual mode Changed]
  * *Citation:* `[Source: NODE_C_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 261 | UUID: 05ceab4e-43ba-4a7e-ae62-e3bc580aa7a3]`
* **NODE_C** [State Transition] (x3 occurrences collapsed): State Transition: Master status -> Spare
  * *Details:* [Master status: Spare | Dual mode: Single | Opposite fms ok: Unknown | Other dual fms node position: FMS node center | Standby fms node position: FMS node invalid | Functional position: First officer]
  * *Citation:* `[Source: NODE_C_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 73 | UUID: 61c19fcf-fe5c-4811-b1f2-3db8f7854693]`

**[11:49:24]**
* **NODE_A** [Fault History] (x2 occurrences collapsed): Oss task client failure (Code: 6024)
  * *Details:* Serial Number: 332 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6024 | Fault Code: 6024 | Sub Code: Thunderbolt fault | Fault Name: Oss task client failure | Date and Time: 2032-06-18 11:49:24 AM | Module Temperature: 39 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: Fr context shutdown e | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 22 | Application Data: Task Client not found;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 332 | UUID: 3285e2f4-4c4e-41f2-a9de-ece3b6312da7]`
* **NODE_A** [State Transition]: State Transition: Master status -> Standby
  * *Details:* [Master status: Standby | Dual mode: Single | Opposite fms ok: Unknown | Other dual fms node position: FMS node invalid | Standby fms node position: FMS node invalid | Functional position: Standby]
  * *Citation:* `[Source: NODE_A_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 12 | UUID: bdfcd854-b193-4c03-b714-dfdf7aae0521]`
* **NODE_C** [Fault History] (x2 occurrences collapsed): Scheduled FMS Activity Missed Timing Requirement (Code: 6000)
  * *Details:* Serial Number: 239 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6000 | Fault Code: 6000 | Sub Code: Thunderbolt fault | Fault Name: Scheduled FMS Activity Missed Timing Requirement | Date and Time: 2032-06-18 11:49:24 AM | Module Temperature: 38 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Count: 5 | Last Context Reset Reason: Fr context shutdown e | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 50 | Application Data: Deadline miss` Background service - 4259858;
  * *Citation:* `[Source: NODE_C_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 239 | UUID: d7cf9cbb-529b-47ff-852c-e9b72ac26038]`
* **NODE_C** [State Transition] (x2 occurrences collapsed): State Transition: Master status -> Spare
  * *Details:* [Master status: Spare | Dual mode: Single | Opposite fms ok: Ok | Other dual fms node position: FMS node center | Standby fms node position: FMS node left | Functional position: First officer]
  * *Citation:* `[Source: NODE_C_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 76 | UUID: 6f10cca7-2bcc-470f-ba15-11018a7fc082]`

**[11:49:25]**
* **NODE_A** [Fault History]: Error during start process (Code: 9)
  * *Details:* Serial Number: 334 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 12315 | Fault Code: 9 | Sub Code: 11 | Fault Name: Error during start process | Date and Time: 2032-06-18 11:49:25 AM | Module Temperature: 40 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: Fr context shutdown e | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 8 | Application Data: ?~J;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 334 | UUID: 36f40ffa-31a3-416e-bfb9-8207eab72058]`
* **NODE_A** [Fault History]: Scheduled FMS Activity Missed Timing Requirement (Code: 6000)
  * *Details:* Serial Number: 335 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6000 | Fault Code: 6000 | Sub Code: Thunderbolt fault | Fault Name: Scheduled FMS Activity Missed Timing Requirement | Date and Time: 2032-06-18 11:49:25 AM | Module Temperature: 40 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: Fr context shutdown e | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 50 | Application Data: Deadline miss` Background service - 2162715;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 335 | UUID: 4818ed4a-b72d-46f6-906d-9cbdcc3aadb1]`
* **NODE_A** [Operator Interaction] (x4 occurrences collapsed): Operator Interaction Event
  * *Details:* Dual mode: Single | Master status: Master | Functional position: Captain | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 342.996246 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [FMS Operational Event: clear altitude | FMS node source: Standby]
  * *Citation:* `[Source: NODE_A_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 11 | UUID: c92d5efc-b6d9-4b90-bb4b-29803231e5de]`
* **NODE_A** [State Transition]: State Transition: Master status -> Standby
  * *Details:* [Master status: Standby | Dual mode: Single | Opposite fms ok: Not ok | Other dual fms node position: FMS node invalid | Standby fms node position: FMS node invalid | Functional position: Standby]
  * *Citation:* `[Source: NODE_A_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 13 | UUID: 51fbf2e9-aa6a-40d9-adb9-eb1c91a5dae5]`
* **NODE_A** [State Transition]: State Transition: Master status -> Master
  * *Details:* [Master status: Master | Dual mode: Single | Opposite fms ok: Not ok | Other dual fms node position: FMS node invalid | Standby fms node position: FMS node invalid | Functional position: Captain]
  * *Citation:* `[Source: NODE_A_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 14 | UUID: b448d50f-d169-4000-ab05-5a56c884a98d]`
* **NODE_C** [State Transition] (x3 occurrences collapsed): State Transition: Master status -> Spare
  * *Details:* [Master status: Spare | Dual mode: Single | Opposite fms ok: Unstable | Other dual fms node position: FMS node center | Standby fms node position: FMS node center | Functional position: First officer]
  * *Citation:* `[Source: NODE_C_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 78 | UUID: a4151e2e-3f54-477b-b383-22c3c9e16e37]`

**[11:49:26]**
* **NODE_A** [Operator Interaction]: Operator Interaction Event
  * *Details:* Dual mode: Single | Master status: Master | Functional position: Captain | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 342.996246 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [FMS Operational Event: Optimized Step Selected | FMS node source: Standby | Event value: 65547]
  * *Citation:* `[Source: NODE_A_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 15 | UUID: 8c4d509a-f1fd-4631-bfa5-68793687acae]`
* **NODE_A** [State Transition] (x2 occurrences collapsed): State Transition: Master status -> Master
  * *Details:* [Master status: Master | Dual mode: Single | Opposite fms ok: Not ok | Other dual fms node position: FMS node right | Standby fms node position: FMS node invalid | Functional position: Captain]
  * *Citation:* `[Source: NODE_A_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 15 | UUID: f9bdda6f-4bc6-4537-8ed3-e8d8543dd03b]`

**[11:49:27]**
* **NODE_A** [Fault History]: Scheduled FMS Activity Missed Timing Requirement (Code: 6000)
  * *Details:* Serial Number: 336 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6000 | Fault Code: 6000 | Sub Code: Thunderbolt fault | Fault Name: Scheduled FMS Activity Missed Timing Requirement | Date and Time: 2032-06-18 11:49:27 AM | Module Temperature: 40 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: Fr context shutdown e | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 50 | Application Data: Deadline miss` Background service - 2162706;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 336 | UUID: 4f412d4d-0156-4164-9df0-19f72088add2]`
* **NODE_A** [State Transition]: State Transition: Master status -> Master
  * *Details:* [Master status: Master | Dual mode: Single | Opposite fms ok: Ok | Other dual fms node position: FMS node right | Standby fms node position: FMS node invalid | Functional position: Captain]
  * *Citation:* `[Source: NODE_A_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 17 | UUID: de43f0b0-4339-42ac-906f-d51822638a14]`
* **NODE_C** [State Transition]: State Transition: Master status -> Spare
  * *Details:* [Master status: Spare | Dual mode: Single | Opposite fms ok: Ok | Other dual fms node position: FMS node left | Standby fms node position: FMS node invalid | Functional position: First officer]
  * *Citation:* `[Source: NODE_C_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 81 | UUID: 331f8ea9-1345-4d4d-812e-6c322b6f41ac]`

**[11:49:28]**
* **NODE_A** [Fault History]: Scheduled FMS Activity Missed Timing Requirement (Code: 6000)
  * *Details:* Serial Number: 337 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6000 | Fault Code: 6000 | Sub Code: Thunderbolt fault | Fault Name: Scheduled FMS Activity Missed Timing Requirement | Date and Time: 2032-06-18 11:49:28 AM | Module Temperature: 40 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: Fr context shutdown e | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 50 | Application Data: Deadline miss` Background service - 2162704;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 337 | UUID: d3bbce4f-5da2-42b1-aef7-96f8151c55d7]`
* **NODE_A** [Fault History]: Oss semaphore failure (Code: 6029)
  * *Details:* Serial Number: 338 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6029 | Fault Code: 6029 | Sub Code: Thunderbolt fault | Fault Name: Oss semaphore failure | Date and Time: 2032-06-18 11:49:28 AM | Module Temperature: 40 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: Fr context shutdown e | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 100 | Application Data: wait semaphore failed in deos 653 - 6 ;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 338 | UUID: 54a5f475-c4b5-4b88-8868-19ec147e5906]`
* **NODE_A** [Software Event]: Software Event: S pad message identifier l
  * *Details:* Data Identifier: S pad message identifier l | Data Format: Format one unsign 32 | Left FMS node: Spare | Dual: Single | [L message identifier: Please wait]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 15 | UUID: 4126e200-76f2-4acd-b51e-73740b476258]`
* **NODE_A** [Software Event]: Software Event: S pad message identifier r
  * *Details:* Data Identifier: S pad message identifier r | Data Format: Format one unsign 32 | Left FMS node: Spare | Dual: Single | [R message identifier: Please wait]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 16 | UUID: 3766d4c9-8c7f-45e0-b883-a3e864a4932f]`
* **NODE_C** [Software Event]: Software Event: S pad message identifier l
  * *Details:* Data Identifier: S pad message identifier l | Data Format: Format one unsign 32 | Left FMS node: Spare | Dual: Single | [L message identifier: Please wait]
  * *Citation:* `[Source: NODE_C_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 262 | UUID: c9472d1a-1ba7-41bb-b81c-29d7654fcfed]`
* **NODE_C** [Software Event]: Software Event: S pad message identifier r
  * *Details:* Data Identifier: S pad message identifier r | Data Format: Format one unsign 32 | Left FMS node: Spare | Dual: Single | [R message identifier: Please wait]
  * *Citation:* `[Source: NODE_C_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 263 | UUID: ef3108ca-bcf7-4883-92ef-9aa09b5801f5]`

**[11:49:29]**
* **NODE_A** [Fault History]: Scheduled FMS Activity Missed Timing Requirement (Code: 6000)
  * *Details:* Serial Number: 339 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6000 | Fault Code: 6000 | Sub Code: Thunderbolt fault | Fault Name: Scheduled FMS Activity Missed Timing Requirement | Date and Time: 2032-06-18 11:49:29 AM | Module Temperature: 40 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: Fr context shutdown e | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 50 | Application Data: Deadline miss` Background service - 2162714;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 339 | UUID: 316032f9-660a-4baf-9848-5175a785fc00]`
* **NODE_A** [Fault History]: Oss semaphore failure (Code: 6029)
  * *Details:* Serial Number: 340 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6029 | Fault Code: 6029 | Sub Code: Thunderbolt fault | Fault Name: Oss semaphore failure | Date and Time: 2032-06-18 11:49:29 AM | Module Temperature: 39 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: Fr context shutdown e | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 100 | Application Data: wait semaphore failed in deos 653 - 6 ;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 340 | UUID: 0ca56933-6a35-46e2-a433-fb2ee944d0c1]`

**[11:49:30]**
* **NODE_A** [Fault History]: Oss semaphore failure (Code: 6029)
  * *Details:* Serial Number: 341 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6029 | Fault Code: 6029 | Sub Code: Thunderbolt fault | Fault Name: Oss semaphore failure | Date and Time: 2032-06-18 11:49:30 AM | Module Temperature: 39 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: Fr context shutdown e | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 100 | Application Data: wait semaphore failed in deos 653 - 6 ;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 341 | UUID: a01848e8-800d-41c8-80ff-4a71550fea9f]`
* **NODE_A** [Fault History]: Scheduled FMS Activity Missed Timing Requirement (Code: 6000)
  * *Details:* Serial Number: 342 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6000 | Fault Code: 6000 | Sub Code: Thunderbolt fault | Fault Name: Scheduled FMS Activity Missed Timing Requirement | Date and Time: 2032-06-18 11:49:30 AM | Module Temperature: 40 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: Fr context shutdown e | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 50 | Application Data: Deadline miss` Background service - 2162713;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 342 | UUID: 7f21f791-1031-412e-9026-4898c2dceecc]`
* **NODE_C** [Fault History]: Navigation Data Coordination Activity Failure (Code: 11)
  * *Details:* Serial Number: 241 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 12925 | Fault Code: 11 | Sub Code: 109 | Fault Name: Navigation Data Coordination Activity Failure | Date and Time: 2032-06-18 11:49:30 AM | Module Temperature: 38 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Count: 5 | Last Context Reset Reason: Fr context shutdown e | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 8 | Application Data: ?~J;
  * *Citation:* `[Source: NODE_C_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 241 | UUID: afdce123-6f06-4c20-ba6f-d7f6f6f8a0fb]`

**[11:49:31]**
* **NODE_A** [Fault History]: Oss semaphore failure (Code: 6029)
  * *Details:* Serial Number: 343 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6029 | Fault Code: 6029 | Sub Code: Thunderbolt fault | Fault Name: Oss semaphore failure | Date and Time: 2032-06-18 11:49:31 AM | Module Temperature: 40 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: Fr context shutdown e | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 100 | Application Data: wait semaphore failed in deos 653 - 6 ;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 343 | UUID: 0c84db61-ed8a-441c-8db9-4a2fe945eff8]`
* **NODE_A** [Software Event]: Software Event: Master spare identifier
  * *Details:* Data Identifier: Master spare identifier | Data Format: Format fixed str | Left FMS node: Master | Dual: Single | [Event identifier: 68 | FMS node position: Operational master spare Changed]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 17 | UUID: 57cb547c-3c24-40d8-8a6d-1803d4c2f6bd]`
* **NODE_A** [Software Event]: Software Event: Flight display cp identifier
  * *Details:* Data Identifier: Flight display cp identifier | Data Format: Format flight display cp | Left FMS node: Master | Dual: Single | [Scale: 160.000000 | Mode: Plan]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 18 | UUID: 86376dbb-3037-41ff-b3a5-3ee5c7051824]`
* **NODE_C** [Software Event]: Software Event: Master spare identifier
  * *Details:* Data Identifier: Master spare identifier | Data Format: Format fixed str | Left FMS node: Master | Right FMS node: Spare | Dual: Single | [Event identifier: 68 | FMS node position: Operational master spare Changed]
  * *Citation:* `[Source: NODE_C_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 264 | UUID: d361d804-faa7-4dc6-abf3-47eff94c8d8b]`

**[11:49:32]**
* **NODE_A** [Fault History] (x2 occurrences collapsed): Oss semaphore failure (Code: 6029)
  * *Details:* Serial Number: 344 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6029 | Fault Code: 6029 | Sub Code: Thunderbolt fault | Fault Name: Oss semaphore failure | Date and Time: 2032-06-18 11:49:32 AM | Module Temperature: 40 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: Fr context shutdown e | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 100 | Application Data: wait semaphore failed in deos 653 - 6 ;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 344 | UUID: 25d694b2-f33b-4275-92a6-c1df66c0c113]`

**[11:49:33]**
* **NODE_A** [Fault History]: Oss semaphore failure (Code: 6029)
  * *Details:* Serial Number: 346 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6029 | Fault Code: 6029 | Sub Code: Thunderbolt fault | Fault Name: Oss semaphore failure | Date and Time: 2032-06-18 11:49:33 AM | Module Temperature: 40 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: Fr context shutdown e | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 100 | Application Data: wait semaphore failed in deos 653 - 6 ;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 346 | UUID: 9aa21536-adff-4f3a-bd06-54add936eed0]`

**[11:49:34]**
* **NODE_A** [Fault History]: Oss semaphore failure (Code: 6029)
  * *Details:* Serial Number: 347 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6029 | Fault Code: 6029 | Sub Code: Thunderbolt fault | Fault Name: Oss semaphore failure | Date and Time: 2032-06-18 11:49:34 AM | Module Temperature: 40 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: Fr context shutdown e | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 100 | Application Data: wait semaphore failed in deos 653 - 6 ;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 347 | UUID: 6014acce-62cd-426a-ade7-e7ddc55fa7aa]`

**[11:49:35]**
* **NODE_A** [Fault History]: Oss semaphore failure (Code: 6029)
  * *Details:* Serial Number: 348 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6029 | Fault Code: 6029 | Sub Code: Thunderbolt fault | Fault Name: Oss semaphore failure | Date and Time: 2032-06-18 11:49:35 AM | Module Temperature: 39 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: Fr context shutdown e | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 100 | Application Data: wait semaphore failed in deos 653 - 6 ;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 348 | UUID: e52e9778-15e6-44ea-8514-4c591b4c88c1]`

**[11:49:36]**
* **NODE_A** [Fault History] (x2 occurrences collapsed): Na (Code: 0)
  * *Details:* Serial Number: 349 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Sub Code: Thunderbolt fault | Fault Name: Na | Date and Time: 2032-06-18 11:49:36 AM | Current Recovery Type: No Recovery Action | Module State: Ms unequipped e | Context State: Cs not equipped e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: Power Loss | Fault Exception: False | Extended Record: False | Application Data: ;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 349 | UUID: b3977f57-a857-42f9-ae58-6f7b26e84921]`
* **NODE_A** [Operator Interaction]: Operator Interaction Event
  * *Details:* Dual mode: Dual | Master status: Master | Functional position: Captain | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 342.995117 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [Fault/Event: Cold Start Due To A Re-Synch On The Receiver]
  * *Citation:* `[Source: NODE_A_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 16 | UUID: 4c548223-a317-4d0f-97fd-9c680a90d90d]`

**[11:49:37]**
* **NODE_C** [State Transition]: State Transition: Master status -> Spare
  * *Details:* [Master status: Spare | Dual mode: Single | Opposite fms ok: Unstable | Other dual fms node position: FMS node left | Standby fms node position: FMS node invalid | Functional position: First officer]
  * *Citation:* `[Source: NODE_C_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 82 | UUID: dc3c0b55-28a2-4846-8cf0-20d914c6b1d8]`

**[11:49:38]**
* **NODE_C** [State Transition]: State Transition: Master status -> Spare
  * *Details:* [Master status: Spare | Dual mode: Single | Opposite fms ok: Not ok | Other dual fms node position: FMS node left | Standby fms node position: FMS node invalid | Functional position: First officer]
  * *Citation:* `[Source: NODE_C_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 83 | UUID: 62dee505-28bd-49c8-9614-5c7711a31cf6]`

**[11:49:42]**
* **NODE_C** [Software Event]: Software Event: Opc configuration data identifier
  * *Details:* Data Identifier: Opc configuration data identifier | Data Format: Format opc configuration data | Left FMS node: Master | Right FMS node: Spare | Dual: Single | [Identifier: Configuration data | Performance custo 3: False | Performance custo 2: False | Performance custo 1: False | Operational data link datalink: True | Air traffic service enable: True | Kilogram enable: True | Metric enable: True | Display trajectory: 1 | Grid mora enable: True | I4d rta enable: False | Radio navigation 2 installed: True | Aim disable: True | No radio navigation on board: False | Passenger count enable: True | Fls enable: True | To securization enable: True | No ap fd mda mdh disconnect: True | To derate enable: True | Climb derate enable: False | Fnl des enable: True | Cda enable: 1 | Cpdb opc enable: False | Vor2 dme2 on board: True | Rnp function enable: True | Leg sequencing monitoring enable: True | Resync check enable: True | To securization 2 enable: True | Sbas enable: True | Sls enable: True | Jfgw display on mfd enable: True | Acr 2 on board: False | Vertical display enable: True | FMS trjctry on vd enable: True | Mora on vd enable: True | Msa on vd enable: True | Etoc enable: True | Freeze scale on vd enable: False | Fls axis on vd enable: True | Aess twsf trjctry enable: True | Auto derate climb enable: True | Polar navigation enabled: True | Back beam approach en: True | FMS platform type 1: True | FMS platform type 2: True | FMS platform type 3: False | FMS platform type 4: False | FMS engine manuf 1: False | FMS engine manuf 2: True | FMS engine manuf 3: False | FMS engine type 1: False | FMS engine type 2: True | FMS engine type 3: False | FMS engine type 4: False | FMS engine type 5: False | Takeoff rnp: 1.000000 | Gps approach rnp: 0.300000 | Precision approach rnp: 0.500000 | Nonprecision approach rnp: 0.500000 | Terminal rnp: 1.000000 | Enroute rnp: 2.000000 | Oceanic rnp: 2.000000 | Takeoff tla: 110.991997 | Takeoff hal: 1.000000 | Approach hal: 0.300000 | Terminal hal: 1.000000 | Enroute hal: 2.000000 | Oceanic hal: 2.000000 | Tail number 32: .F-Wzht | Tail number 16: Zht | Tail number 8: T | Configuration data version: [Redacted Payload] | Opc integrity validation: 61]
  * *Citation:* `[Source: NODE_C_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 265 | UUID: 2c6f62d1-41fe-4fba-84f3-694df87bd0fb]`

**[11:49:43]**
* **NODE_C** [Software Event]: Software Event: Sys status identifier
  * *Details:* Data Identifier: Sys status identifier | Data Format: Format sys status | Left FMS node: Master | Right FMS node: Spare | Dual: Single | [Identifier: Sys | Platform family: A350 | Air frame ident: A350 | FMS node physical position: Right | Engine ident: Trent | Engine manufact: 2 | Opsys pn: Hnp5dxcl01xea01 | Ndb pn: Abv2601l01 | Ami database pn: Hnp40 | Database Reference: [Removed]: Hnp56xcd06xha08 | Cpdb pn: Not loaded]
  * *Citation:* `[Source: NODE_C_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 266 | UUID: ce4b12ff-4e93-4a3a-8ad6-1f66d05d79c3]`

**[11:49:47]**
* **NODE_C** [State Transition]: State Transition: Master status -> Master
  * *Details:* [Master status: Master | Dual mode: Single | Opposite fms ok: Not ok | Other dual fms node position: FMS node left | Standby fms node position: FMS node invalid | Functional position: First officer]
  * *Citation:* `[Source: NODE_C_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 84 | UUID: bf8ca8b8-1ca7-4680-8253-73f2b48dc5b0]`

**[11:49:52]**
* **NODE_C** [Software Event]: Software Event: Master spare identifier
  * *Details:* Data Identifier: Master spare identifier | Data Format: Format fixed str | Right FMS node: Master | Dual: Single | [Event identifier: 68 | FMS node position: Operational master spare Changed]
  * *Citation:* `[Source: NODE_C_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 267 | UUID: e8f5d55c-fb8b-4007-9f30-ef66d0298f56]`

**[11:50:35]**
* **NODE_B** [Fault History]: Oss loading failure (Code: 6052)
  * *Details:* Serial Number: 248 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6052 | Fault Code: 6052 | Sub Code: Thunderbolt fault | Fault Name: Oss loading failure | Date and Time: 2032-06-18 11:50:35 AM | Module Temperature: 37 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Initializing | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 100 | Application Data: Failed to load library in Deos 653 - Libpssl dtf manager so.so 11 11;
  * *Citation:* `[Source: NODE_B_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 248 | UUID: d34ed172-6000-467f-89cb-646d3f96ae46]`

**[11:50:36]**
* **NODE_B** [Operator Interaction]: Operator Interaction Event
  * *Details:* Dual mode: Single | Master status: Standby | Functional position: Standby | Calibrated airspeed data: 30.000000 | Message: No displayable fields
  * *Citation:* `[Source: NODE_B_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 17 | UUID: 8ccff865-86df-4189-8117-925ef38379a8]`

**[11:50:37]**
* **NODE_B** [Fault History] (x4 occurrences collapsed): Oss bind failure (Code: 6035)
  * *Details:* Serial Number: 249 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6035 | Fault Code: 6035 | Sub Code: Thunderbolt fault | Fault Name: Oss bind failure | Date and Time: 2032-06-18 11:50:37 AM | Module Temperature: 36 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Ready | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 100 | Application Data: Client Cb not found in deos 653 - -933180756;
  * *Citation:* `[Source: NODE_B_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 249 | UUID: e487c46e-0a72-4094-9642-6d715d9b1082]`
* **NODE_B** [Fault History] (x2 occurrences collapsed): Oss task client failure (Code: 6024)
  * *Details:* Serial Number: 253 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6024 | Fault Code: 6024 | Sub Code: Thunderbolt fault | Fault Name: Oss task client failure | Date and Time: 2032-06-18 11:50:37 AM | Module Temperature: 37 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Ready | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 22 | Application Data: Task Client not found;
  * *Citation:* `[Source: NODE_B_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 253 | UUID: b5cf8284-e549-446d-9a70-fa06a635a032]`
* **NODE_B** [Fault History]: Error during start process (Code: 9)
  * *Details:* Serial Number: 255 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 12315 | Fault Code: 9 | Sub Code: 11 | Fault Name: Error during start process | Date and Time: 2032-06-18 11:50:37 AM | Module Temperature: 37 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 8 | Application Data: ?~J;
  * *Citation:* `[Source: NODE_B_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 255 | UUID: c9d5d074-864c-4fa9-a6e4-e71eb6e422b7]`
* **NODE_B** [Fault History] (x2 occurrences collapsed): Oss task client failure (Code: 6024)
  * *Details:* Serial Number: 256 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6024 | Fault Code: 6024 | Sub Code: Thunderbolt fault | Fault Name: Oss task client failure | Date and Time: 2032-06-18 11:50:37 AM | Module Temperature: 36 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 22 | Application Data: Task Client not found;
  * *Citation:* `[Source: NODE_B_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 256 | UUID: 93bf227e-0999-4f1b-8285-d7bf8de1c14d]`
* **NODE_B** [Software Event]: Software Event: Operational startup mode identifier
  * *Details:* Data Identifier: Operational startup mode identifier | Data Format: Format fixed str | Left FMS node: Spare | Dual: Single | [Event identifier: 68 | Operational startup mode: Operational startup cold]
  * *Citation:* `[Source: NODE_B_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 44 | UUID: 1bb7059f-f5a7-4f1c-be4b-2c4fc1ebb550]`
* **NODE_B** [Software Event]: Software Event: Dual mode identifier
  * *Details:* Data Identifier: Dual mode identifier | Data Format: Format fixed str | Left FMS node: Spare | Dual: Single | [Event identifier: 68 | Operational dual mode: Operational dual mode Changed]
  * *Citation:* `[Source: NODE_B_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 45 | UUID: 4cd372c1-6485-42fc-a543-fb61225ac78e]`
* **NODE_B** [Software Event]: Software Event: Operational powerup identifier
  * *Details:* Data Identifier: Operational powerup identifier | Data Format: Format fixed str | Left FMS node: Spare | Dual: Single | [Event identifier: 68 | Operational powerup: Operational powerup normal]
  * *Citation:* `[Source: NODE_B_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 46 | UUID: b527fe71-1d03-4099-8448-8d7b70b0522a]`
* **NODE_B** [State Transition]: State Transition: Master status -> Standby
  * *Details:* [Master status: Standby | Dual mode: Single | Opposite fms ok: Unknown | Other dual fms node position: FMS node right | Standby fms node position: FMS node invalid | Functional position: Standby]
  * *Citation:* `[Source: NODE_B_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 14 | UUID: 5d31111e-0e8e-4e31-afb6-0470e9c2690d]`

**[11:50:38]**
* **NODE_B** [Fault History] (x2 occurrences collapsed): Oss task client failure (Code: 6024)
  * *Details:* Serial Number: 258 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6024 | Fault Code: 6024 | Sub Code: Thunderbolt fault | Fault Name: Oss task client failure | Date and Time: 2032-06-18 11:50:38 AM | Module Temperature: 36 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 22 | Application Data: Task Client not found;
  * *Citation:* `[Source: NODE_B_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 258 | UUID: 23f3d252-c8f6-4f44-b9aa-04e2d11c09cb]`
* **NODE_C** [State Transition]: State Transition: Master status -> Master
  * *Details:* [Master status: Master | Dual mode: Single | Opposite fms ok: Not ok | Other dual fms node position: FMS node left | Standby fms node position: FMS node center | Functional position: First officer]
  * *Citation:* `[Source: NODE_C_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 85 | UUID: 4cb53c5c-a037-4ff1-a3a8-d12a054d2715]`

**[11:50:39]**
* **NODE_B** [State Transition]: State Transition: Master status -> Standby
  * *Details:* [Master status: Standby | Dual mode: Single | Opposite fms ok: Not ok | Other dual fms node position: FMS node right | Standby fms node position: FMS node invalid | Functional position: Standby]
  * *Citation:* `[Source: NODE_B_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 15 | UUID: 6a3da38a-6c7f-4b01-a815-06e8e74c36c4]`

**[11:50:40]**
* **NODE_B** [Operator Interaction]: Operator Interaction Event
  * *Details:* Dual mode: Single | Master status: Standby | Functional position: Standby | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 342.998596 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [Fault/Event: Dual State Trans Timeout]
  * *Citation:* `[Source: NODE_B_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 18 | UUID: af9d7d41-aa33-451a-8394-e59b886baff0]`

**[11:50:44]**
* **NODE_B** [Operator Interaction]: Operator Interaction Event
  * *Details:* Dual mode: Single | Master status: Standby | Functional position: Standby | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 342.998016 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [Fault/Event: Dual State Trans Timeout]
  * *Citation:* `[Source: NODE_B_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 19 | UUID: 25965a9d-d8a9-4845-8310-18b7a26e8aea]`
* **NODE_B** [Software Event]: Software Event: Master spare identifier
  * *Details:* Data Identifier: Master spare identifier | Data Format: Format fixed str | Center FMS node: Standby | Right FMS node: Master | Dual: Single | [Event identifier: 68 | FMS node position: Operational master spare Changed]
  * *Citation:* `[Source: NODE_B_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 47 | UUID: c267d044-22f7-41f6-b09b-2932c96321ca]`
* **NODE_C** [Software Event]: Software Event: Master spare identifier
  * *Details:* Data Identifier: Master spare identifier | Data Format: Format fixed str | Center FMS node: Standby | Right FMS node: Master | Dual: Single | [Event identifier: 68 | FMS node position: Operational master spare Changed]
  * *Citation:* `[Source: NODE_C_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 268 | UUID: f55bedfb-6ecd-4ccd-aeee-f380ea104846]`

**[11:50:47]**
* **NODE_A** [Fault History]: Oss loading failure (Code: 6052)
  * *Details:* Serial Number: 351 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6052 | Fault Code: 6052 | Sub Code: Thunderbolt fault | Fault Name: Oss loading failure | Date and Time: 2032-06-18 11:50:47 AM | Module Temperature: 40 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Initializing | Last Context Reset Reason: Fr context shutdown e | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 100 | Application Data: Failed to load library in Deos 653 - Libpssl dtf manager so.so 11 11;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 351 | UUID: 5c3481f1-c5b8-4e75-8151-645a45ab29ad]`

**[11:50:48]**
* **NODE_A** [Operator Interaction]: Operator Interaction Event
  * *Details:* Dual mode: Dual | Master status: Master | Functional position: Captain | Calibrated airspeed data: 30.000000 | Message: No displayable fields
  * *Citation:* `[Source: NODE_A_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 17 | UUID: 24be1739-044d-41b4-a265-bdb7d15236fd]`
* **NODE_B** [Operator Interaction]: Operator Interaction Event
  * *Details:* Dual mode: Single | Master status: Standby | Functional position: Standby | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 342.996704 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [Fault/Event: Dual State Trans Timeout]
  * *Citation:* `[Source: NODE_B_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 20 | UUID: 26f887da-496b-46a7-a86b-4faeaf503084]`

**[11:50:49]**
* **NODE_A** [Operator Interaction]: Operator Interaction Event
  * *Details:* Dual mode: Dual | Master status: Master | Functional position: Captain | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 342.996643 | Magnetic track: 66.049805 | [FMS Operational Event: redisplay | FMS node source: Standby]
  * *Citation:* `[Source: NODE_A_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 18 | UUID: 5e39dc87-c857-4cd5-8599-61e6e360a65e]`
* **NODE_A** [Software Event]: Software Event: Operational startup mode identifier
  * *Details:* Data Identifier: Operational startup mode identifier | Data Format: Format fixed str | Left FMS node: Spare | Dual: Dual | [Event identifier: 68 | Operational startup mode: Operational startup cold]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 19 | UUID: 67e9f200-3452-4ea4-921f-069218cbbdf4]`
* **NODE_A** [Software Event]: Software Event: Operational powerup identifier
  * *Details:* Data Identifier: Operational powerup identifier | Data Format: Format fixed str | Left FMS node: Spare | Dual: Dual | [Event identifier: 68 | Operational powerup: Operational powerup normal]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 20 | UUID: 98eaf78c-39b6-4ac2-93d2-c342c0a63cbe]`
* **NODE_A** [State Transition] (x2 occurrences collapsed): State Transition: Master status -> Master
  * *Details:* [Master status: Master | Dual mode: Dual | Opposite fms ok: Unknown | Other dual fms node position: FMS node right | Standby fms node position: FMS node invalid | Functional position: Captain]
  * *Citation:* `[Source: NODE_A_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 18 | UUID: 82b6ef5e-58c3-4786-8970-a4ff003b873a]`
* **NODE_C** [Operator Interaction]: Operator Interaction Event
  * *Details:* Dual mode: Dual | Master status: Master | Functional position: First officer | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 342.996460 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [FMS Operational Event: redisplay | FMS node source: Standby]
  * *Citation:* `[Source: NODE_C_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 678 | UUID: dc0d7dbc-86a9-4695-b5d5-2c2c1fd309ef]`
* **NODE_C** [Software Event]: Software Event: Dual mode identifier
  * *Details:* Data Identifier: Dual mode identifier | Data Format: Format fixed str | Center FMS node: Standby | Right FMS node: Master | Dual: Dual | [Event identifier: 68 | Operational dual mode: Operational dual mode Changed]
  * *Citation:* `[Source: NODE_C_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 269 | UUID: 32f9d140-23ef-43b0-8e99-76ddf280c327]`
* **NODE_C** [State Transition]: State Transition: Master status -> Master
  * *Details:* [Master status: Master | Dual mode: Dual | Opposite fms ok: Not ok | Other dual fms node position: FMS node left | Standby fms node position: FMS node center | Functional position: First officer]
  * *Citation:* `[Source: NODE_C_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 86 | UUID: ebd86121-360b-4884-87f3-6fbd2c7a94ec]`

**[11:50:50]**
* **NODE_A** [State Transition]: State Transition: Master status -> Master
  * *Details:* [Master status: Master | Dual mode: Dual | Opposite fms ok: Unstable | Other dual fms node position: FMS node right | Standby fms node position: FMS node center | Functional position: Captain]
  * *Citation:* `[Source: NODE_A_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 20 | UUID: ef1fd9ef-a5c0-4f2f-a66e-f37ebf5d23f8]`
* **NODE_C** [State Transition] (x2 occurrences collapsed): State Transition: Master status -> Spare
  * *Details:* [Master status: Spare | Dual mode: Dual | Opposite fms ok: Not ok | Other dual fms node position: FMS node left | Standby fms node position: FMS node center | Functional position: First officer]
  * *Citation:* `[Source: NODE_C_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 87 | UUID: e3532243-0d1c-48bf-a443-18d279ed3420]`

**[11:50:51]**
* **NODE_A** [Operator Interaction]: Operator Interaction Event
  * *Details:* Dual mode: Dual | Master status: Master | Functional position: Captain | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 342.996185 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [FMS Operational Event: redisplay | FMS node source: Captain | Event value: 65536]
  * *Citation:* `[Source: NODE_A_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 19 | UUID: fee588ba-e2bc-4e8a-a8e6-09c3b1721b9c]`
* **NODE_A** [State Transition]: State Transition: Master status -> Master
  * *Details:* [Master status: Master | Dual mode: Dual | Opposite fms ok: Ok | Other dual fms node position: FMS node right | Standby fms node position: FMS node center | Functional position: Captain]
  * *Citation:* `[Source: NODE_A_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 21 | UUID: c1152aab-5a16-43d4-9f85-78177abcc77a]`
* **NODE_C** [State Transition]: State Transition: Master status -> Spare
  * *Details:* [Master status: Spare | Dual mode: Dual | Opposite fms ok: Ok | Other dual fms node position: FMS node left | Standby fms node position: FMS node center | Functional position: First officer]
  * *Citation:* `[Source: NODE_C_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 89 | UUID: ce17f1c4-187b-4d08-9f08-24f32882d8c9]`

**[11:50:52]**
* **NODE_A** [Fault History] (x2 occurrences collapsed): Scheduled FMS Activity Missed Timing Requirement (Code: 6000)
  * *Details:* Serial Number: 352 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6000 | Fault Code: 6000 | Sub Code: Thunderbolt fault | Fault Name: Scheduled FMS Activity Missed Timing Requirement | Date and Time: 2032-06-18 11:50:52 AM | Module Temperature: 40 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: Fr context shutdown e | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 50 | Application Data: Deadline miss` Background service - 3211290;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 352 | UUID: cff35db0-77ed-44ec-ae1e-ca129b2ba9b9]`
* **NODE_C** [Operator Interaction]: Operator Interaction Event
  * *Details:* Dual mode: Dual | Master status: Spare | Functional position: First officer | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 342.995972 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [FMS Operational Event: redisplay | FMS node source: Captain | Event value: 65536]
  * *Citation:* `[Source: NODE_C_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 679 | UUID: 6679028b-12a0-4818-8a19-e4db9527ebca]`

**[11:50:53]**
* **NODE_A** [Software Event]: Software Event: Data link comm master identifier
  * *Details:* Data Identifier: Data link comm master identifier | Data Format: Format fixed str | Left FMS node: Spare | Dual: Dual | [Event identifier: 68 | Data link comm master status log: Data link comm slave to master]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 21 | UUID: 8d3a46b7-04c2-46b3-9b6d-521cd188c2c0]`

**[11:50:54]**
* **NODE_A** [Aircraft State]: Aircraft State Update
  * *Details:* [Button push in progress: 1 | Ndb selected cycle: 1 | Ils mode: 17 | Previous leg terminator: 4 | Active leg terminator: 2 | Current lateral leg Sequence: -1417712574 | Next lateral leg Sequence: -1935671229 | Gross weight: 160045.109375 | Cost index: 201326657 | Track: 12946.814453 | FMS button push39: 2816 | Software fault address: 6 | Last in: 1 | First in: 16 | Ioci button push: 6]
  * *Citation:* `[Source: NODE_A_Aircraft_State_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 1 | UUID: 74c18543-878e-4296-8aa2-841b0888c93d]`
* **NODE_A** [Fault History]: Rnp standby standby restarted (Code: 6)
  * *Details:* Serial Number: 354 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 11635 | Fault Code: 6 | Sub Code: 99 | Fault Name: Rnp standby standby restarted | Date and Time: 2032-06-18 11:50:54 AM | Module Temperature: 39 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: Fr context shutdown e | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 8 | Application Data: ?~J;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 354 | UUID: 1e570369-0aa4-413a-811b-ee6fbe35d02b]`
* **NODE_A** [Operator Interaction]: Operator Interaction Event
  * *Details:* Dual mode: Dual | Master status: Master | Functional position: Captain | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 342.995483 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [FMS Operational Event: rnp bld fp | FMS node source: Standby | Event value: 131072]
  * *Citation:* `[Source: NODE_A_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 20 | UUID: 333b7d78-9a20-41da-93f6-e8cf16864a9f]`
* **NODE_C** [Aircraft State]: Aircraft State Update
  * *Details:* [Button push in progress: 1 | Ndb selected cycle: 1 | Ils mode: 17 | Previous leg terminator: 4 | Active leg terminator: 2 | Current lateral leg Sequence: -1417714878 | Next lateral leg Sequence: -1935671229 | Gross weight: 160045.109375 | Cost index: 201326657 | Track: 12946.814453 | FMS button push39: 5376 | Simsoft data: 1610612736 | Software fault address: 537264290 | Last in: 2 | First in: 16 | Right bite trc history: 6 | Ioci button push: 570425344]
  * *Citation:* `[Source: NODE_C_Aircraft_State_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 3 | UUID: b32a560a-bdd8-42b2-b829-866a19ac474b]`
* **NODE_C** [Fault History]: Rnp dual dual reestablished (Code: 6)
  * *Details:* Serial Number: 242 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 11636 | Fault Code: 6 | Sub Code: 100 | Fault Name: Rnp dual dual reestablished | Date and Time: 2032-06-18 11:50:54 AM | Module Temperature: 38 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Count: 5 | Last Context Reset Reason: Fr context shutdown e | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 8 | Application Data: ?~J;
  * *Citation:* `[Source: NODE_C_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 242 | UUID: 18e7e1e2-e529-4c5c-9c1a-2d13fbaa4f67]`
* **NODE_C** [Operator Interaction]: Operator Interaction Event
  * *Details:* Dual mode: Dual | Master status: Spare | Functional position: First officer | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 342.995209 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [FMS Operational Event: rnp bld fp | FMS node source: Standby | Event value: 131072]
  * *Citation:* `[Source: NODE_C_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 680 | UUID: 68995355-e1bc-4fcd-b87b-ac2b2eb00368]`
* **NODE_C** [Software Event]: Software Event: Data link comm master identifier
  * *Details:* Data Identifier: Data link comm master identifier | Data Format: Format fixed str | Center FMS node: Standby | Right FMS node: Master | Dual: Dual | [Event identifier: 68 | Data link comm master status log: Data link comm master to slave]
  * *Citation:* `[Source: NODE_C_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 270 | UUID: d7d31c88-df30-47d3-a509-c4201bd6b07d]`

**[11:50:55]**
* **NODE_A** [Software Event]: Software Event: Master spare identifier
  * *Details:* Data Identifier: Master spare identifier | Data Format: Format fixed str | Left FMS node: Master | Center FMS node: Standby | Right FMS node: Spare | Dual: Dual | [Event identifier: 68 | FMS node position: Operational master spare Changed]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 22 | UUID: 2def8eca-63e2-4445-a1fa-a7960e4d7429]`
* **NODE_B** [Software Event]: Software Event: Master spare identifier
  * *Details:* Data Identifier: Master spare identifier | Data Format: Format fixed str | Left FMS node: Master | Center FMS node: Standby | Right FMS node: Spare | Dual: Single | [Event identifier: 68 | FMS node position: Operational master spare Changed]
  * *Citation:* `[Source: NODE_B_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 48 | UUID: 262ed9da-fe7b-4fce-8de6-3a5a5c4a4777]`

**[11:50:56]**
* **NODE_A** [Fault History]: Scheduled FMS Activity Missed Timing Requirement (Code: 6000)
  * *Details:* Serial Number: 355 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6000 | Fault Code: 6000 | Sub Code: Thunderbolt fault | Fault Name: Scheduled FMS Activity Missed Timing Requirement | Date and Time: 2032-06-18 11:50:56 AM | Module Temperature: 40 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: Fr context shutdown e | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 50 | Application Data: Deadline miss` Background service - 3211288;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 355 | UUID: 7dcaa852-873c-4707-8ea5-45f710ef1810]`
* **NODE_A** [Operator Interaction] (x2 occurrences collapsed): Operator Interaction Event
  * *Details:* Dual mode: Dual | Master status: Master | Functional position: Captain | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 342.995148 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [FMS Operational Event: clear altitude | FMS node source: Standby | Event value: 65596]
  * *Citation:* `[Source: NODE_A_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 21 | UUID: b7789ebe-5591-4b88-af81-d56a92b21a1e]`
* **NODE_C** [Software Event]: Software Event: Master spare identifier
  * *Details:* Data Identifier: Master spare identifier | Data Format: Format fixed str | Left FMS node: Master | Center FMS node: Standby | Right FMS node: Spare | Dual: Dual | [Event identifier: 68 | FMS node position: Operational master spare Changed]
  * *Citation:* `[Source: NODE_C_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 271 | UUID: 0239caff-8aaa-4df4-a303-506b22502c60]`

**[11:50:57]**
* **NODE_A** [Operator Interaction] (x2 occurrences collapsed): Operator Interaction Event
  * *Details:* Dual mode: Dual | Master status: Master | Functional position: Captain | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 342.995117 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [FMS Operational Event: clear altitude | FMS node source: Captain | Event value: 65540]
  * *Citation:* `[Source: NODE_A_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 23 | UUID: 96764008-09f4-4351-9afb-e75b652d3240]`
* **NODE_B** [Software Event]: Software Event: Opc configuration data identifier
  * *Details:* Data Identifier: Opc configuration data identifier | Data Format: Format opc configuration data | Left FMS node: Master | Center FMS node: Standby | Right FMS node: Spare | Dual: Single | [Identifier: Configuration data | Performance custo 3: False | Performance custo 2: False | Performance custo 1: False | Operational data link datalink: True | Air traffic service enable: True | Kilogram enable: True | Metric enable: True | Display trajectory: 1 | Grid mora enable: True | I4d rta enable: False | Radio navigation 2 installed: True | Aim disable: True | No radio navigation on board: False | Passenger count enable: True | Fls enable: True | To securization enable: True | No ap fd mda mdh disconnect: True | To derate enable: True | Climb derate enable: False | Fnl des enable: True | Cda enable: 1 | Cpdb opc enable: False | Vor2 dme2 on board: True | Rnp function enable: True | Leg sequencing monitoring enable: True | Resync check enable: True | To securization 2 enable: True | Sbas enable: True | Sls enable: True | Jfgw display on mfd enable: True | Acr 2 on board: False | Vertical display enable: True | FMS trjctry on vd enable: True | Mora on vd enable: True | Msa on vd enable: True | Etoc enable: True | Freeze scale on vd enable: False | Fls axis on vd enable: True | Aess twsf trjctry enable: True | Auto derate climb enable: True | Polar navigation enabled: True | Back beam approach en: True | FMS platform type 1: True | FMS platform type 2: True | FMS platform type 3: False | FMS platform type 4: False | FMS engine manuf 1: False | FMS engine manuf 2: True | FMS engine manuf 3: False | FMS engine type 1: False | FMS engine type 2: True | FMS engine type 3: False | FMS engine type 4: False | FMS engine type 5: False | Takeoff rnp: 1.000000 | Gps approach rnp: 0.300000 | Precision approach rnp: 0.500000 | Nonprecision approach rnp: 0.500000 | Terminal rnp: 1.000000 | Enroute rnp: 2.000000 | Oceanic rnp: 2.000000 | Takeoff tla: 110.991997 | Takeoff hal: 1.000000 | Approach hal: 0.300000 | Terminal hal: 1.000000 | Enroute hal: 2.000000 | Oceanic hal: 2.000000 | Tail number 32: .F-Wzht | Tail number 16: Zht | Tail number 8: T | Configuration data version: [Redacted Payload] | Opc integrity validation: 61]
  * *Citation:* `[Source: NODE_B_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 49 | UUID: 12d19aa3-98ff-4725-852c-5dc30f2d3083]`
* **NODE_C** [Operator Interaction] (x4 occurrences collapsed): Operator Interaction Event
  * *Details:* Dual mode: Dual | Master status: Spare | Functional position: First officer | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 342.994965 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [FMS Operational Event: clear altitude | FMS node source: Standby | Event value: 65596]
  * *Citation:* `[Source: NODE_C_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 681 | UUID: 4233cbee-0a7e-491d-bc89-eaa94e92aa42]`

**[11:50:58]**
* **NODE_A** [Operator Interaction]: Operator Interaction Event
  * *Details:* Dual mode: Dual | Master status: Master | Functional position: Captain | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 342.995270 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [FMS Operational Event: no phase change | FMS node source: Standby | Event value: 131076]
  * *Citation:* `[Source: NODE_A_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 25 | UUID: 8f71cc05-49d1-4ab0-a4e7-2c904c021be1]`
* **NODE_B** [Fault History]: Navigation Data Coordination Activity Failure (Code: 11)
  * *Details:* Serial Number: 260 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 12925 | Fault Code: 11 | Sub Code: 109 | Fault Name: Navigation Data Coordination Activity Failure | Date and Time: 2032-06-18 11:50:58 AM | Module Temperature: 37 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 8 | Application Data: ?~J;
  * *Citation:* `[Source: NODE_B_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 260 | UUID: 375ff084-05bc-40c6-9d57-b7c2f7eeff09]`
* **NODE_B** [Software Event]: Software Event: Sys status identifier
  * *Details:* Data Identifier: Sys status identifier | Data Format: Format sys status | Left FMS node: Master | Center FMS node: Standby | Right FMS node: Spare | Dual: Single | [Identifier: Sys | Platform family: A350 | Air frame ident: A350 | FMS node physical position: Center | Engine ident: Trent | Engine manufact: 2 | Opsys pn: Hnp5dxcl01xea01 | Ndb pn: Abv2601l01 | Ami database pn: Hnp40 | Database Reference: [Removed]: Hnp56xcd06xha08 | Cpdb pn: Not loaded]
  * *Citation:* `[Source: NODE_B_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 50 | UUID: 38a9b186-8fc7-4831-bc98-10b63b0a5245]`

**[11:50:59]**
* **NODE_A** [Aircraft State]: Aircraft State Update
  * *Details:* [Ndb selected cycle: 1 | Ils mode: 17 | Previous leg terminator: 4 | Active leg terminator: 2 | Current lateral leg Sequence: -1417714110 | Next lateral leg Sequence: -1935671229 | Gross weight: 160045.109375 | Cost index: 201326657 | Track: 12946.814453 | FMS button push39: 83896320 | FMS button push40: 4294907393 | Software fault address: 6 | Last in: 1 | First in: 16 | Ioci button push: 6]
  * *Citation:* `[Source: NODE_A_Aircraft_State_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 2 | UUID: b0227de6-bf30-405b-ae75-f2ebffc00c93]`
* **NODE_A** [Fault History]: Rnp legs transmitter io (Code: 6)
  * *Details:* Serial Number: 356 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 11629 | Fault Code: 6 | Sub Code: 93 | Fault Name: Rnp legs transmitter io | Date and Time: 2032-06-18 11:50:59 AM | Module Temperature: 40 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: Fr context shutdown e | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 8 | Application Data: ?~J;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 356 | UUID: 4b96f5c8-2f13-4207-87fe-8e26ae760e5e]`
* **NODE_A** [Operator Interaction] (x2 occurrences collapsed): Operator Interaction Event
  * *Details:* Dual mode: Dual | Master status: Master | Functional position: Captain | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 342.995300 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [FMS Operational Event: clear altitude | FMS node source: Standby | Event value: 65547]
  * *Citation:* `[Source: NODE_A_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 26 | UUID: 182ab4b4-1682-4e6b-a7a8-9c9ae1c964f5]`
* **NODE_B** [Aircraft State]: Aircraft State Update
  * *Details:* [Ndb selected cycle: 1 | Ils mode: 1 | Previous leg terminator: 4 | Active leg terminator: 2 | Current lateral leg Sequence: -1417715646 | Next lateral leg Sequence: -1935671229 | Gross weight: 160045.109375 | Cost index: 201326657 | Track: 12946.814453 | FMS button push39: 26624]
  * *Citation:* `[Source: NODE_B_Aircraft_State_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 90 | UUID: 5c5d9c3f-8c21-4ae8-a0de-c2c0eb591270]`
* **NODE_B** [Fault History]: Rnp integrity validation receiver timeout (Code: 6)
  * *Details:* Serial Number: 261 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 11633 | Fault Code: 6 | Sub Code: 97 | Fault Name: Rnp integrity validation receiver timeout | Date and Time: 2032-06-18 11:50:59 AM | Module Temperature: 37 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 8 | Application Data: ?~J;
  * *Citation:* `[Source: NODE_B_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 261 | UUID: 06573289-8545-46d3-ac6e-55e90e907667]`
* **NODE_C** [Operator Interaction] (x3 occurrences collapsed): Operator Interaction Event
  * *Details:* Dual mode: Dual | Master status: Spare | Functional position: First officer | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 342.995117 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [FMS Operational Event: no phase change | FMS node source: Standby | Event value: 131076]
  * *Citation:* `[Source: NODE_C_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 685 | UUID: 9fc8e5f1-9391-411a-bdfc-3c39d2c4d1da]`

**[11:51:00]**
* **NODE_A** [Fault History]: Scheduled FMS Activity Missed Timing Requirement (Code: 6000)
  * *Details:* Serial Number: 357 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6000 | Fault Code: 6000 | Sub Code: Thunderbolt fault | Fault Name: Scheduled FMS Activity Missed Timing Requirement | Date and Time: 2032-06-18 11:51:00 AM | Module Temperature: 40 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: Fr context shutdown e | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 50 | Application Data: Deadline miss` Background service - 3211289;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 357 | UUID: e6c68b89-4870-4f65-9f7e-be7c9010a37c]`
* **NODE_A** [Operator Interaction]: Operator Interaction Event
  * *Details:* Dual mode: Dual | Master status: Master | Functional position: Captain | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 342.995453 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [FMS Operational Event: no phase change | FMS node source: Standby | Event value: 65540]
  * *Citation:* `[Source: NODE_A_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 28 | UUID: 95c03beb-82a4-4bcd-94dd-f83a09742d67]`
* **NODE_C** [Operator Interaction]: Operator Interaction Event
  * *Details:* Dual mode: Dual | Master status: Spare | Functional position: First officer | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 342.995270 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [FMS Operational Event: no phase change | FMS node source: Standby | Event value: 65540]
  * *Citation:* `[Source: NODE_C_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 688 | UUID: 73b200a1-acef-4fbc-817d-30ba655efa3d]`

**[11:51:01]**
* **NODE_A** [Fault History]: Oss semaphore failure (Code: 6029)
  * *Details:* Serial Number: 358 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6029 | Fault Code: 6029 | Sub Code: Thunderbolt fault | Fault Name: Oss semaphore failure | Date and Time: 2032-06-18 11:51:01 AM | Module Temperature: 40 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: Fr context shutdown e | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 100 | Application Data: wait semaphore failed in deos 653 - 6 ;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 358 | UUID: 55fa3f67-6d86-42f6-97b0-4a55ed4a30c4]`

**[11:51:04]**
* **NODE_C** [Operator Interaction]: Operator Interaction Event
  * *Details:* Dual mode: Dual | Master status: Spare | Functional position: First officer | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 342.995270 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [FMS Operational Event: Performance Data Changed | FMS node source: Standby | Event value: 65547]
  * *Citation:* `[Source: NODE_C_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 689 | UUID: 59ae42c1-0e7e-4629-b076-16540ac9ce91]`

**[11:51:05]**
* **NODE_C** [Operator Interaction]: Operator Interaction Event
  * *Details:* Dual mode: Dual | Master status: Spare | Functional position: First officer | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 342.995605 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [FMS Operational Event: Performance Data Changed | FMS node source: Captain | Event value: 65555]
  * *Citation:* `[Source: NODE_C_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 690 | UUID: f1108fa2-5517-4036-98b3-7e3b054eda95]`

**[11:51:08]**
* **NODE_A** [Software Event]: Software Event: Operator interaction event identifier
  * *Details:* Data Identifier: Operator interaction event identifier | Data Format: Format operator interaction event | Left FMS node: Master | Center FMS node: Standby | Right FMS node: Spare | Dual: Dual | [Event identifier: Operator interaction flight plan orient destination event | Source fms node: Captain]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 23 | UUID: 5cbd920b-025b-4677-87b4-c7536705863a]`
* **NODE_C** [Operator Interaction]: Operator interaction flight plan orient destination event
  * *Details:* Dual mode: Dual | Master status: Spare | Functional position: First officer | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 342.996246 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | Flight plan source - high: Active | Flight plan source - low: ActPrimary | Display system source: Operator interaction display system left | [Operator Interaction Event: Operator interaction flight plan orient destination event | Event status: Operator interaction entered | Event value: 131091]
  * *Citation:* `[Source: NODE_C_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 691 | UUID: ade0d899-9484-4b05-9e05-033f4a5a6cc1]`
* **NODE_C** [Operator Interaction]: Operator Interaction Event
  * *Citation:* `[Source: NODE_C_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 692 | UUID: acdb5af0-1212-4166-be9d-e29c9f9e4c7f]`
* **NODE_C** [Software Event]: Software Event: Operator interaction event identifier
  * *Details:* Data Identifier: Operator interaction event identifier | Data Format: Format operator interaction event | Left FMS node: Master | Center FMS node: Standby | Right FMS node: Spare | Dual: Dual | [Event identifier: Operator interaction flight plan orient destination event | Source fms node: Captain]
  * *Citation:* `[Source: NODE_C_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 272 | UUID: 062400d4-64c8-4b7c-9814-aef9c19ddef3]`

**[11:51:10]**
* **NODE_A** [Software Event]: Software Event: Opc configuration data identifier
  * *Details:* Data Identifier: Opc configuration data identifier | Data Format: Format opc configuration data | Left FMS node: Master | Center FMS node: Standby | Right FMS node: Spare | Dual: Dual | [Identifier: Configuration data | Performance custo 3: False | Performance custo 2: False | Performance custo 1: False | Operational data link datalink: True | Air traffic service enable: True | Kilogram enable: True | Metric enable: True | Display trajectory: 1 | Grid mora enable: True | I4d rta enable: False | Radio navigation 2 installed: True | Aim disable: True | No radio navigation on board: False | Passenger count enable: True | Fls enable: True | To securization enable: True | No ap fd mda mdh disconnect: True | To derate enable: True | Climb derate enable: False | Fnl des enable: True | Cda enable: 1 | Cpdb opc enable: False | Vor2 dme2 on board: True | Rnp function enable: True | Leg sequencing monitoring enable: True | Resync check enable: True | To securization 2 enable: True | Sbas enable: True | Sls enable: True | Jfgw display on mfd enable: True | Acr 2 on board: False | Vertical display enable: True | FMS trjctry on vd enable: True | Mora on vd enable: True | Msa on vd enable: True | Etoc enable: True | Freeze scale on vd enable: False | Fls axis on vd enable: True | Aess twsf trjctry enable: True | Auto derate climb enable: True | Polar navigation enabled: True | Back beam approach en: True | FMS platform type 1: True | FMS platform type 2: True | FMS platform type 3: False | FMS platform type 4: False | FMS engine manuf 1: False | FMS engine manuf 2: True | FMS engine manuf 3: False | FMS engine type 1: False | FMS engine type 2: True | FMS engine type 3: False | FMS engine type 4: False | FMS engine type 5: False | Takeoff rnp: 1.000000 | Gps approach rnp: 0.300000 | Precision approach rnp: 0.500000 | Nonprecision approach rnp: 0.500000 | Terminal rnp: 1.000000 | Enroute rnp: 2.000000 | Oceanic rnp: 2.000000 | Takeoff tla: 110.991997 | Takeoff hal: 1.000000 | Approach hal: 0.300000 | Terminal hal: 1.000000 | Enroute hal: 2.000000 | Oceanic hal: 2.000000 | Tail number 32: .F-Wzht | Tail number 16: Zht | Tail number 8: T | Configuration data version: [Redacted Payload] | Opc integrity validation: 61]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 24 | UUID: 4a7860e4-a248-4add-b9b5-bd56c4d8fca5]`

**[11:51:11]**
* **NODE_A** [Fault History]: Navigation Data Coordination Activity Failure (Code: 11)
  * *Details:* Serial Number: 359 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 12925 | Fault Code: 11 | Sub Code: 109 | Fault Name: Navigation Data Coordination Activity Failure | Date and Time: 2032-06-18 11:51:11 AM | Module Temperature: 40 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: Fr context shutdown e | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 8 | Application Data: ?~J;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 359 | UUID: 7a10d906-eca8-4132-bae7-7a2ca8033a0d]`
* **NODE_A** [Software Event]: Software Event: Sys status identifier
  * *Details:* Data Identifier: Sys status identifier | Data Format: Format sys status | Left FMS node: Master | Center FMS node: Standby | Right FMS node: Spare | Dual: Dual | [Identifier: Sys | Platform family: A350 | Air frame ident: A350 | FMS node physical position: Left | Engine ident: Trent | Engine manufact: 2 | Opsys pn: Hnp5dxcl01xea01 | Ndb pn: Abv2601l01 | Ami database pn: Hnp40 | Database Reference: [Removed]: Hnp56xcd06xha08 | Cpdb pn: Not loaded]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 25 | UUID: e53e12a8-595d-4193-8d13-58ae1f340fad]`

**[11:51:14]**
* **NODE_C** [Operator Interaction]: Operator Interaction Event
  * *Details:* Dual mode: Dual | Master status: Spare | Functional position: First officer | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 342.995911 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [FMS Operational Event: Optimized Step Selected | FMS node source: Captain | Event value: 1049171]
  * *Citation:* `[Source: NODE_C_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 693 | UUID: 0fe886fa-f07c-43a8-8f63-b1d54afc74a6]`

**[11:51:17]**
* **NODE_A** [Software Event]: Software Event: Operator interaction event identifier
  * *Details:* Data Identifier: Operator interaction event identifier | Data Format: Format operator interaction event | Left FMS node: Master | Center FMS node: Standby | Right FMS node: Spare | Dual: Dual | [Event identifier: Operator interaction enter flt nbr | Source fms node: First officer]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 26 | UUID: 2835e0fb-4829-4e76-a9cf-11f01e2dd6df]`
* **NODE_C** [Operator Interaction]: Operator interaction enter flt nbr
  * *Details:* Dual mode: Dual | Master status: Spare | Functional position: First officer | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 342.996002 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | Flight plan source - high: Active | Flight plan source - low: ActPrimary | Display system source: Operator interaction display system right | [Operator Interaction Event: Operator interaction enter flt nbr | Event status: Operator interaction entered | Event value: 131098]
  * *Citation:* `[Source: NODE_C_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 694 | UUID: 6bf6ef3f-336e-44f4-bca5-cb16a3081d1b]`
* **NODE_C** [Software Event]: Software Event: Operator interaction event identifier
  * *Details:* Data Identifier: Operator interaction event identifier | Data Format: Format operator interaction event | Left FMS node: Master | Center FMS node: Standby | Right FMS node: Spare | Dual: Dual | [Event identifier: Operator interaction enter flt nbr | Source fms node: First officer]
  * *Citation:* `[Source: NODE_C_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 273 | UUID: 23410f3d-b1a7-4232-a3c9-1ede429e1ddc]`

**[11:51:56]**
* **NODE_C** [Operator Interaction] (x2 occurrences collapsed): Operator Interaction Event
  * *Details:* Dual mode: Dual | Master status: Spare | Functional position: First officer | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 343.000854 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [Fault/Event: Performance Defined Event | Event value: 1]
  * *Citation:* `[Source: NODE_C_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 695 | UUID: 43e97b66-f78b-4e31-a03d-21a016969898]`

**[11:52:00]**
* **NODE_C** [State Transition]: State Transition: Master status -> Spare
  * *Details:* [Master status: Spare | Dual mode: Dual | Opposite fms ok: Unstable | Other dual fms node position: FMS node left | Standby fms node position: FMS node center | Functional position: First officer]
  * *Citation:* `[Source: NODE_C_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 90 | UUID: d250928a-4587-4c67-88ec-0154f0fc451d]`

**[11:52:04]**
* **NODE_C** [State Transition]: State Transition: Master status -> Spare
  * *Details:* [Master status: Spare | Dual mode: Dual | Opposite fms ok: Not ok | Other dual fms node position: FMS node left | Standby fms node position: FMS node center | Functional position: First officer]
  * *Citation:* `[Source: NODE_C_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 91 | UUID: 4f1b85a8-246a-4776-a8f9-4048022da6ed]`

**[11:52:05]**
* **NODE_C** [State Transition]: State Transition: Master status -> Spare
  * *Details:* [Master status: Spare | Dual mode: Dual | Opposite fms ok: Unstable | Other dual fms node position: FMS node left | Standby fms node position: FMS node center | Functional position: First officer]
  * *Citation:* `[Source: NODE_C_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 92 | UUID: e94a588a-6628-4c3c-917e-e913046e2f42]`

**[11:52:09]**
* **NODE_C** [State Transition]: State Transition: Master status -> Spare
  * *Details:* [Master status: Spare | Dual mode: Dual | Opposite fms ok: Ok | Other dual fms node position: FMS node left | Standby fms node position: FMS node center | Functional position: First officer]
  * *Citation:* `[Source: NODE_C_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 93 | UUID: 4fcd6e10-b49f-4229-b5bc-89c120aa3017]`

**[11:52:10]**
* **NODE_C** [State Transition]: State Transition: Master status -> Spare
  * *Details:* [Master status: Spare | Dual mode: Dual | Opposite fms ok: Unstable | Other dual fms node position: FMS node left | Standby fms node position: FMS node center | Functional position: First officer]
  * *Citation:* `[Source: NODE_C_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 94 | UUID: 2f5a283f-002c-4b94-be9b-1e6b2e97e343]`

**[11:52:12]**
* **NODE_C** [State Transition]: State Transition: Master status -> Spare
  * *Details:* [Master status: Spare | Dual mode: Dual | Opposite fms ok: Ok | Other dual fms node position: FMS node left | Standby fms node position: FMS node center | Functional position: First officer]
  * *Citation:* `[Source: NODE_C_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 95 | UUID: 14818097-7d03-4f8f-9118-6828d90e9cca]`

**[11:52:13]**
* **NODE_A** [Fault History]: Scheduled FMS Activity Missed Timing Requirement (Code: 6000)
  * *Details:* Serial Number: 360 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6000 | Fault Code: 6000 | Sub Code: Thunderbolt fault | Fault Name: Scheduled FMS Activity Missed Timing Requirement | Date and Time: 2032-06-18 11:52:13 AM | Module Temperature: 40 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: Fr context shutdown e | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 50 | Application Data: Deadline miss` Background service - 3211282;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 360 | UUID: e9f7e9f2-46b2-4287-90da-ee21cb748727]`
* **NODE_A** [Software Event]: Software Event: Operator interaction event identifier
  * *Details:* Data Identifier: Operator interaction event identifier | Data Format: Format operator interaction event | Left FMS node: Master | Center FMS node: Standby | Right FMS node: Spare | Dual: Dual | [Event identifier: Operator interaction string new waypoint ato | Source fms node: Captain]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 27 | UUID: 995653ae-7c41-4e45-a0e6-12af37aa4438]`
* **NODE_A** [Software Event]: Software Event: S pad message identifier l
  * *Details:* Data Identifier: S pad message identifier l | Data Format: Format one unsign 32 | Left FMS node: Master | Center FMS node: Standby | Right FMS node: Spare | Dual: Dual | [L message identifier: Entry out of range]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 28 | UUID: 91ef3bd0-1c5a-4109-a793-e7ac99180111]`
* **NODE_A** [Software Event] (x3 occurrences collapsed): Software Event: Operator interaction event identifier
  * *Details:* Data Identifier: Operator interaction event identifier | Data Format: Format operator interaction event | Left FMS node: Master | Center FMS node: Standby | Right FMS node: Spare | Dual: Dual | [Event identifier: Operator interaction string new waypoint ato | Source fms node: Captain]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 29 | UUID: f57edee8-9d1e-4097-b557-11ebd14628e7]`

**[11:52:22]**
* **NODE_C** [Operator Interaction]: Operator interaction string new waypoint ato
  * *Details:* Dual mode: Dual | Master status: Spare | Functional position: First officer | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 343.001251 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | Flight plan source - high: Active | Flight plan source - low: ActPrimary | Display system source: Operator interaction display system left | [Operator Interaction Event: Operator interaction string new waypoint ato | Event status: Operator interaction entered | Event value: 17826345]
  * *Citation:* `[Source: NODE_C_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 697 | UUID: c229a74e-d941-452d-b8a3-bf8395a3bf68]`
* **NODE_C** [Operator Interaction] (x2 occurrences collapsed): Operator Interaction Event
  * *Details:* Dual mode: Dual | Master status: Spare | Functional position: First officer | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 343.001251 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [Fix ident: Pd03]
  * *Citation:* `[Source: NODE_C_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 698 | UUID: 3d5490d6-8267-49b5-adcc-820958ffc153]`
* **NODE_C** [Software Event]: Software Event: Operator interaction event identifier
  * *Details:* Data Identifier: Operator interaction event identifier | Data Format: Format operator interaction event | Left FMS node: Master | Center FMS node: Standby | Right FMS node: Spare | Dual: Dual | [Event identifier: Operator interaction string new waypoint ato | Source fms node: Captain]
  * *Citation:* `[Source: NODE_C_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 274 | UUID: 868b4091-1fda-4472-9e92-343a2c4c5226]`

**[11:52:24]**
* **NODE_C** [Operator Interaction]: Operator interaction string new waypoint ato
  * *Details:* Dual mode: Dual | Master status: Spare | Functional position: First officer | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 343.001373 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | Flight plan source - high: Active | Flight plan source - low: ActPrimary | Display system source: Operator interaction display system left | [Operator Interaction Event: Operator interaction string new waypoint ato | Event status: Operator interaction entered | Event value: 1049267]
  * *Citation:* `[Source: NODE_C_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 700 | UUID: 0d6895d1-06d3-48b6-8482-d230af6cb7ee]`
* **NODE_C** [Operator Interaction] (x2 occurrences collapsed): Operator Interaction Event
  * *Details:* Dual mode: Dual | Master status: Spare | Functional position: First officer | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 343.001373 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [Fix ident: Pd03]
  * *Citation:* `[Source: NODE_C_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 701 | UUID: f58a7032-8b36-4b9e-879f-f51526d310d6]`
* **NODE_C** [Software Event]: Software Event: Operator interaction event identifier
  * *Details:* Data Identifier: Operator interaction event identifier | Data Format: Format operator interaction event | Left FMS node: Master | Center FMS node: Standby | Right FMS node: Spare | Dual: Dual | [Event identifier: Operator interaction string new waypoint ato | Source fms node: Captain]
  * *Citation:* `[Source: NODE_C_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 275 | UUID: 28c8a463-69ba-4f97-9f3c-04f4349de501]`

**[11:52:29]**
* **NODE_C** [Operator Interaction]: Operator interaction string new waypoint ato
  * *Details:* Dual mode: Dual | Master status: Spare | Functional position: First officer | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 343.002228 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | Flight plan source - high: Active | Flight plan source - low: ActPrimary | Display system source: Operator interaction display system left | [Operator Interaction Event: Operator interaction string new waypoint ato | Event status: Operator interaction entered | Event value: 1049267]
  * *Citation:* `[Source: NODE_C_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 703 | UUID: 75a2527d-8dd4-4d6c-8975-fcc8c59bf1a6]`
* **NODE_C** [Operator Interaction] (x2 occurrences collapsed): Operator Interaction Event
  * *Details:* Dual mode: Dual | Master status: Spare | Functional position: First officer | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 343.002228 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [Fix ident: Pd03]
  * *Citation:* `[Source: NODE_C_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 704 | UUID: dc8d6b1f-1b30-403c-b07a-92ba778b8d10]`
* **NODE_C** [Software Event]: Software Event: Operator interaction event identifier
  * *Details:* Data Identifier: Operator interaction event identifier | Data Format: Format operator interaction event | Left FMS node: Master | Center FMS node: Standby | Right FMS node: Spare | Dual: Dual | [Event identifier: Operator interaction string new waypoint ato | Source fms node: Captain]
  * *Citation:* `[Source: NODE_C_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 276 | UUID: 741abfb4-d697-4fff-81fc-74803e7e346c]`

**[11:52:30]**
* **NODE_C** [Operator Interaction]: Operator Interaction Event
  * *Details:* Dual mode: Dual | Master status: Spare | Functional position: First officer | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 343.002350 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [FMS Operational Event: Optimized Step Selected | FMS node source: Captain | Event value: 1049267]
  * *Citation:* `[Source: NODE_C_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 706 | UUID: d75b9f2a-39ff-4195-b20c-570549ffbcd4]`

**[11:52:31]**
* **NODE_C** [Operator Interaction]: Operator Interaction Event
  * *Details:* Dual mode: Dual | Master status: Spare | Functional position: First officer | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 343.002563 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [FMS Operational Event: Performance Data Changed | FMS node source: Captain | Event value: 131098]
  * *Citation:* `[Source: NODE_C_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 707 | UUID: 27ab4287-7625-42e0-ad3c-6c58bd7290e6]`

**[11:52:32]**
* **NODE_C** [Operator Interaction]: Operator Interaction Event
  * *Details:* Dual mode: Dual | Master status: Spare | Functional position: First officer | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 343.002625 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [FMS Operational Event: Performance Data Changed | FMS node source: Standby | Event value: 131091]
  * *Citation:* `[Source: NODE_C_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 708 | UUID: e99a6dbc-4c18-463a-a2a8-bc4bf7fcd98d]`

**[11:52:36]**
* **NODE_C** [Operator Interaction]: Operator interaction insert temporary
  * *Details:* Dual mode: Dual | Master status: Spare | Functional position: First officer | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 343.002777 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | Flight plan source - high: Temporary Efb | Flight plan source - low: TmpyPrimary | Display system source: Operator interaction display system left | [Operator Interaction Event: Operator interaction insert temporary | Event status: Operator interaction entered | Event value: 65555]
  * *Citation:* `[Source: NODE_C_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 709 | UUID: 7094c191-1879-437e-88c4-848d09beb54b]`
* **NODE_C** [Operator Interaction]: Operator Interaction Event
  * *Citation:* `[Source: NODE_C_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 710 | UUID: ad8e364b-9bdc-4e9f-b350-8bf4d27629dd]`
* **NODE_C** [Software Event]: Software Event: Operator interaction event identifier
  * *Details:* Data Identifier: Operator interaction event identifier | Data Format: Format operator interaction event | Left FMS node: Master | Center FMS node: Standby | Right FMS node: Spare | Dual: Dual | [Event identifier: Operator interaction insert temporary | Source fms node: Captain]
  * *Citation:* `[Source: NODE_C_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 277 | UUID: bdd65b0c-52f8-4498-bc20-64c1c47b39b4]`

**[11:53:20]**
* **NODE_C** [Operator Interaction] (x2 occurrences collapsed): Operator Interaction Event
  * *Details:* Dual mode: Dual | Master status: Spare | Functional position: First officer | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 342.999176 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [Fault/Event: Performance Defined Event | Event value: 1]
  * *Citation:* `[Source: NODE_C_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 711 | UUID: 99a32160-ad82-443e-99eb-5f0e2716654c]`

**[11:53:45]**
* **NODE_A** [Software Event]: Software Event: Operator interaction event identifier
  * *Details:* Data Identifier: Operator interaction event identifier | Data Format: Format operator interaction event | Left FMS node: Master | Center FMS node: Standby | Right FMS node: Spare | Dual: Dual | [Event identifier: Operator interaction select vertical Revision revise pt | Source fms node: Captain]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 32 | UUID: 6b7099ce-9d1f-4025-9316-3629356432bf]`

**[11:53:47]**
* **NODE_C** [Operator Interaction]: Operator interaction select vertical Revision revise pt
  * *Details:* Dual mode: Dual | Master status: Spare | Functional position: First officer | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 342.996857 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | Flight plan source - high: Active | Flight plan source - low: ActPrimary | Display system source: Operator interaction display system left | [Operator Interaction Event: Operator interaction select vertical Revision revise pt | Event status: Operator interaction entered | Event value: 9699863]
  * *Citation:* `[Source: NODE_C_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 713 | UUID: 6d920301-a8a9-4df7-8730-0baa450af384]`
* **NODE_C** [Operator Interaction] (x2 occurrences collapsed): Operator Interaction Event
  * *Details:* Dual mode: Dual | Master status: Spare | Functional position: First officer | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 342.996857 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [Fix ident: Pd03]
  * *Citation:* `[Source: NODE_C_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 714 | UUID: 41d7d7f3-902e-4950-a39b-b382f738aea1]`
* **NODE_C** [Software Event]: Software Event: Operator interaction event identifier
  * *Details:* Data Identifier: Operator interaction event identifier | Data Format: Format operator interaction event | Left FMS node: Master | Center FMS node: Standby | Right FMS node: Spare | Dual: Dual | [Event identifier: Operator interaction select vertical Revision revise pt | Source fms node: Captain]
  * *Citation:* `[Source: NODE_C_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 278 | UUID: ab765daa-1d71-4103-b57a-eb3477e4d8f6]`

**[11:53:48]**
* **NODE_C** [Operator Interaction]: Operator interaction enter altitude constraint
  * *Details:* Dual mode: Dual | Master status: Spare | Functional position: First officer | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 342.997070 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | Flight plan source - high: Active | Flight plan source - low: ActPrimary | Display system source: Operator interaction display system left | [Operator Interaction Event: Operator interaction enter altitude constraint | Event status: Operator interaction entered | Event value: 1049246]
  * *Citation:* `[Source: NODE_C_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 716 | UUID: 8d1d8dd4-64dd-4818-b1e4-99144144668b]`
* **NODE_C** [Operator Interaction] (x2 occurrences collapsed): Operator Interaction Event
  * *Details:* Dual mode: Dual | Master status: Spare | Functional position: First officer | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 342.997070 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [Fix ident: Pd03]
  * *Citation:* `[Source: NODE_C_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 717 | UUID: 7076db8a-0949-437f-89d0-d74e468cca33]`
* **NODE_C** [Software Event]: Software Event: Operator interaction event identifier
  * *Details:* Data Identifier: Operator interaction event identifier | Data Format: Format operator interaction event | Left FMS node: Master | Center FMS node: Standby | Right FMS node: Spare | Dual: Dual | [Event identifier: Operator interaction enter altitude constraint | Source fms node: Captain]
  * *Citation:* `[Source: NODE_C_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 279 | UUID: 2f15a66e-045c-46f1-9c02-2e93c5242320]`

**[11:53:52]**
* **NODE_C** [Operator Interaction]: Operator interaction enter altitude constraint
  * *Details:* Dual mode: Dual | Master status: Spare | Functional position: First officer | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 342.997498 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | Flight plan source - high: Active | Flight plan source - low: ActPrimary | Display system source: Operator interaction display system left | [Operator Interaction Event: Operator interaction enter altitude constraint | Event status: Operator interaction entered | Event value: 1049247]
  * *Citation:* `[Source: NODE_C_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 719 | UUID: 5dfd8df3-4b26-4836-b793-f9fd00aa3b52]`
* **NODE_C** [Operator Interaction] (x2 occurrences collapsed): Operator Interaction Event
  * *Details:* Dual mode: Dual | Master status: Spare | Functional position: First officer | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 342.997498 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [Fix ident: Pd03]
  * *Citation:* `[Source: NODE_C_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 720 | UUID: 9409e07c-e890-454c-8448-9583ac44519e]`
* **NODE_C** [Software Event]: Software Event: Operator interaction event identifier
  * *Details:* Data Identifier: Operator interaction event identifier | Data Format: Format operator interaction event | Left FMS node: Master | Center FMS node: Standby | Right FMS node: Spare | Dual: Dual | [Event identifier: Operator interaction enter altitude constraint | Source fms node: Captain]
  * *Citation:* `[Source: NODE_C_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 280 | UUID: de411a2d-2786-4e8c-b191-253789b04e50]`

**[11:53:54]**
* **NODE_C** [Operator Interaction]: Operator interaction insert temporary
  * *Details:* Dual mode: Dual | Master status: Spare | Functional position: First officer | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 342.997955 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | Flight plan source - high: Temporary Efb | Flight plan source - low: TmpyPrimary | Display system source: Operator interaction display system left | [Operator Interaction Event: Operator interaction insert temporary | Event status: Operator interaction entered | Event value: 1049247]
  * *Citation:* `[Source: NODE_C_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 722 | UUID: 33ce6168-a2d0-4cc2-8cb2-ca3e6d693d90]`
* **NODE_C** [Operator Interaction]: Operator Interaction Event
  * *Citation:* `[Source: NODE_C_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 723 | UUID: 716f0b04-1179-4449-b665-fe7f69624302]`
* **NODE_C** [Software Event]: Software Event: Operator interaction event identifier
  * *Details:* Data Identifier: Operator interaction event identifier | Data Format: Format operator interaction event | Left FMS node: Master | Center FMS node: Standby | Right FMS node: Spare | Dual: Dual | [Event identifier: Operator interaction insert temporary | Source fms node: Captain]
  * *Citation:* `[Source: NODE_C_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 281 | UUID: f8b4b181-9194-4013-bd26-9dcf16edbe90]`

**[11:53:57]**
* **NODE_C** [Operator Interaction] (x2 occurrences collapsed): Operator Interaction Event
  * *Details:* Dual mode: Dual | Master status: Spare | Functional position: First officer | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 342.998596 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [FMS Operational Event: Performance Data Changed | FMS node source: Standby | Event value: 9699863]
  * *Citation:* `[Source: NODE_C_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 724 | UUID: d6b219bc-6176-4b33-9adf-f1bc5e194b47]`

**[11:54:38]**
* **NODE_C** [Operator Interaction] (x2 occurrences collapsed): Operator Interaction Event
  * *Details:* Dual mode: Dual | Master status: Spare | Functional position: First officer | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 343.000427 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [Fault/Event: Performance Defined Event | Event value: 2]
  * *Citation:* `[Source: NODE_C_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 726 | UUID: e5469fc4-5a83-41df-9cb1-3400cef6f0a3]`
