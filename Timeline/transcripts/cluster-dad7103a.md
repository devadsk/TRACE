# Incident Cluster: cluster-dad7103a
**Date:** 2032-06-18
**Duration:** 12:20:15 to 12:22:38
**Nodes Involved:** NODE_A, NODE_B
**Total Events:** 122 (Filtered from 155 raw logs)

## Timeline Transcript

**[12:20:15]**
* **NODE_B** [Fault History] (x2 occurrences collapsed): Background Service Identity Failure (Code: 6025)
  * *Details:* Serial Number: 458 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6025 | Fault Code: 6025 | Sub Code: Thunderbolt fault | Fault Name: Background Service Identity Failure | Date and Time: 2032-06-18 12:20:15 PM | Module Temperature: 37 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Initializing | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 35 | Application Data: get current process id failure 653;
  * *Citation:* `[Source: NODE_B_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 458 | UUID: ea7db662-1406-4ca0-84ae-88b560cd51c7]`

**[12:20:16]**
* **NODE_B** [Fault History] (x2 occurrences collapsed): Background Service Identity Failure (Code: 6025)
  * *Details:* Serial Number: 460 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6025 | Fault Code: 6025 | Sub Code: Thunderbolt fault | Fault Name: Background Service Identity Failure | Date and Time: 2032-06-18 12:20:16 PM | Module Temperature: 36 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Initializing | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 35 | Application Data: get current process id failure 653;
  * *Citation:* `[Source: NODE_B_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 460 | UUID: ca00947e-6d52-4132-834a-57cb5b939ff5]`
* **NODE_B** [Fault History]: Oss loading failure (Code: 6052)
  * *Details:* Serial Number: 462 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6052 | Fault Code: 6052 | Sub Code: Thunderbolt fault | Fault Name: Oss loading failure | Date and Time: 2032-06-18 12:20:16 PM | Module Temperature: 37 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Initializing | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 100 | Application Data: Failed to load library in Deos 653 - Libpssl dtf manager so.so 11 11;
  * *Citation:* `[Source: NODE_B_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 462 | UUID: c51772e1-e198-49cd-aa87-18b7e1cac332]`
* **NODE_B** [Fault History] (x2 occurrences collapsed): Background Service Identity Failure (Code: 6025)
  * *Details:* Serial Number: 463 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6025 | Fault Code: 6025 | Sub Code: Thunderbolt fault | Fault Name: Background Service Identity Failure | Date and Time: 2032-06-18 12:20:16 PM | Module Temperature: 37 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Initializing | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 35 | Application Data: get current process id failure 653;
  * *Citation:* `[Source: NODE_B_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 463 | UUID: 1983fa63-64b0-421a-9bc1-c70987838968]`

**[12:20:17]**
* **NODE_B** [Operator Interaction]: Operator Interaction Event
  * *Details:* Dual mode: Dual | Master status: Spare | Functional position: First officer | Calibrated airspeed data: 30.000000 | Message: No displayable fields
  * *Citation:* `[Source: NODE_B_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 7 | UUID: 8f44837c-b95a-4e24-89d1-6a278cbc3d01]`

**[12:20:18]**
* **NODE_A** [Operator Interaction]: Operator Interaction Event
  * *Details:* Dual mode: Dual | Master status: Master | Functional position: Captain | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 343.001465 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [FMS Operational Event: redisplay | FMS node source: Standby | Event value: 65536]
  * *Citation:* `[Source: NODE_A_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 12 | UUID: d67a1094-f7d7-48be-9e1b-cf20a1411713]`
* **NODE_A** [Software Event]: Software Event: Dual mode identifier
  * *Details:* Data Identifier: Dual mode identifier | Data Format: Format fixed str | Left FMS node: Master | Dual: Dual | [Event identifier: 68 | Operational dual mode: Operational dual mode Changed]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 12 | UUID: 3ed27d16-7c74-4300-9e5f-7b106b41014a]`
* **NODE_A** [State Transition]: State Transition: Master status -> Master
  * *Details:* [Master status: Master | Dual mode: Dual | Opposite fms ok: Not ok | Other dual fms node position: FMS node center | Standby fms node position: FMS node invalid | Functional position: Captain]
  * *Citation:* `[Source: NODE_A_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 20 | UUID: 69ca1a64-edf8-41f5-9c2d-edda8c19eff8]`
* **NODE_B** [Fault History]: Oss generic fault (Code: 6080)
  * *Details:* Serial Number: 465 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6080 | Fault Code: 6080 | Sub Code: Thunderbolt fault | Fault Name: Oss generic fault | Date and Time: 2032-06-18 12:20:18 PM | Module Temperature: 37 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Initializing | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 48 | Application Data: Get parent task rate : Process is not found 653;
  * *Citation:* `[Source: NODE_B_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 465 | UUID: 60d0dd3f-959c-4dfd-acdf-5ba6a56864ea]`
* **NODE_B** [Fault History] (x8 occurrences collapsed): Oss bind failure (Code: 6035)
  * *Details:* Serial Number: 466 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6035 | Fault Code: 6035 | Sub Code: Thunderbolt fault | Fault Name: Oss bind failure | Date and Time: 2032-06-18 12:20:18 PM | Module Temperature: 36 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Ready | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 100 | Application Data: Client Cb not found in deos 653 - -933180756;
  * *Citation:* `[Source: NODE_B_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 466 | UUID: 5090748c-eb4b-45c1-8d5f-efbf6870c460]`
* **NODE_B** [Fault History] (x2 occurrences collapsed): Oss task client failure (Code: 6024)
  * *Details:* Serial Number: 474 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6024 | Fault Code: 6024 | Sub Code: Thunderbolt fault | Fault Name: Oss task client failure | Date and Time: 2032-06-18 12:20:18 PM | Module Temperature: 36 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Ready | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 22 | Application Data: Task Client not found;
  * *Citation:* `[Source: NODE_B_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 474 | UUID: efe4a333-6fbf-4e7c-b5e3-3a2c1e7c8dd8]`
* **NODE_B** [Fault History] (x3 occurrences collapsed): Oss generic fault (Code: 6080)
  * *Details:* Serial Number: 476 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6080 | Fault Code: 6080 | Sub Code: Thunderbolt fault | Fault Name: Oss generic fault | Date and Time: 2032-06-18 12:20:18 PM | Module Temperature: 36 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 45 | Application Data: Background Task:Set priority Deos Api failure in 653;
  * *Citation:* `[Source: NODE_B_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 476 | UUID: 4adcfb06-51ca-4731-95fa-fdca590a162b]`
* **NODE_B** [Fault History]: Oss task client failure (Code: 6024)
  * *Details:* Serial Number: 479 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6024 | Fault Code: 6024 | Sub Code: Thunderbolt fault | Fault Name: Oss task client failure | Date and Time: 2032-06-18 12:20:18 PM | Module Temperature: 37 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 22 | Application Data: Task Client not found;
  * *Citation:* `[Source: NODE_B_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 479 | UUID: 04460365-29db-43a4-bf1c-aab64371c72d]`
* **NODE_B** [Fault History] (x3 occurrences collapsed): Oss generic fault (Code: 6080)
  * *Details:* Serial Number: 480 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6080 | Fault Code: 6080 | Sub Code: Thunderbolt fault | Fault Name: Oss generic fault | Date and Time: 2032-06-18 12:20:18 PM | Module Temperature: 37 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 45 | Application Data: Background Task:Set priority Deos Api failure in 653;
  * *Citation:* `[Source: NODE_B_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 480 | UUID: 3a720b17-7134-45c1-a968-b636d576622b]`
* **NODE_B** [Fault History] (x3 occurrences collapsed): Oss task client failure (Code: 6024)
  * *Details:* Serial Number: 483 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6024 | Fault Code: 6024 | Sub Code: Thunderbolt fault | Fault Name: Oss task client failure | Date and Time: 2032-06-18 12:20:18 PM | Module Temperature: 37 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 22 | Application Data: Task Client not found;
  * *Citation:* `[Source: NODE_B_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 483 | UUID: cbd3300a-6217-4119-9fe1-7e87b13306a6]`
* **NODE_B** [Software Event]: Software Event: Operational startup mode identifier
  * *Details:* Data Identifier: Operational startup mode identifier | Data Format: Format fixed str | Left FMS node: Spare | Dual: Dual | [Event identifier: 68 | Operational startup mode: Operational startup cold]
  * *Citation:* `[Source: NODE_B_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 17 | UUID: 2cc69106-50de-4664-848a-2a5a24ae45a7]`
* **NODE_B** [Software Event]: Software Event: Operational powerup identifier
  * *Details:* Data Identifier: Operational powerup identifier | Data Format: Format fixed str | Left FMS node: Spare | Dual: Dual | [Event identifier: 68 | Operational powerup: Operational powerup normal]
  * *Citation:* `[Source: NODE_B_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 18 | UUID: 816049f1-e08e-4476-beed-3f68c36caa7f]`
* **NODE_B** [State Transition]: State Transition: Master status -> Spare
  * *Details:* [Master status: Spare | Dual mode: Dual | Opposite fms ok: Unknown | Other dual fms node position: FMS node left | Standby fms node position: FMS node invalid | Functional position: First officer]
  * *Citation:* `[Source: NODE_B_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 9 | UUID: 71b747af-0202-4490-beda-4b96e8293ee9]`

**[12:20:19]**
* **NODE_A** [Operator Interaction]: Operator Interaction Event
  * *Details:* Dual mode: Dual | Master status: Master | Functional position: Captain | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 343.001251 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [FMS Operational Event: redisplay | FMS node source: Captain | Event value: 65536]
  * *Citation:* `[Source: NODE_A_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 13 | UUID: c9f8bbdc-c2e2-460f-a661-5f3263aa7337]`
* **NODE_A** [State Transition]: State Transition: Master status -> Master
  * *Details:* [Master status: Master | Dual mode: Dual | Opposite fms ok: Unstable | Other dual fms node position: FMS node center | Standby fms node position: FMS node invalid | Functional position: Captain]
  * *Citation:* `[Source: NODE_A_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 21 | UUID: d3ca1697-5107-4962-8731-db6231a6885f]`
* **NODE_B** [Operator Interaction] (x2 occurrences collapsed): Operator Interaction Event
  * *Details:* Dual mode: Dual | Master status: Spare | Functional position: First officer | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 365.757385 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [FMS Operational Event: redisplay | FMS node source: Standby]
  * *Citation:* `[Source: NODE_B_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 8 | UUID: bfe8ee44-f489-4a40-bdae-e942bfddfc98]`
* **NODE_B** [State Transition]: State Transition: Master status -> Spare
  * *Details:* [Master status: Spare | Dual mode: Dual | Opposite fms ok: Unstable | Other dual fms node position: FMS node left | Standby fms node position: FMS node invalid | Functional position: First officer]
  * *Citation:* `[Source: NODE_B_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 10 | UUID: 1b82b47b-caab-4636-a884-df7e948db47d]`

**[12:20:20]**
* **NODE_A** [State Transition]: State Transition: Master status -> Master
  * *Details:* [Master status: Master | Dual mode: Dual | Opposite fms ok: Ok | Other dual fms node position: FMS node center | Standby fms node position: FMS node invalid | Functional position: Captain]
  * *Citation:* `[Source: NODE_A_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 22 | UUID: df8884a4-4185-468b-942b-5b5c49253760]`
* **NODE_B** [Fault History]: Oss task client failure (Code: 6024)
  * *Details:* Serial Number: 486 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6024 | Fault Code: 6024 | Sub Code: Thunderbolt fault | Fault Name: Oss task client failure | Date and Time: 2032-06-18 12:20:20 PM | Module Temperature: 35 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 22 | Application Data: Task Client not found;
  * *Citation:* `[Source: NODE_B_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 486 | UUID: e334b27b-3074-40eb-88d5-a44e4d1de221]`
* **NODE_B** [State Transition]: State Transition: Master status -> Spare
  * *Details:* [Master status: Spare | Dual mode: Dual | Opposite fms ok: Ok | Other dual fms node position: FMS node left | Standby fms node position: FMS node invalid | Functional position: First officer]
  * *Citation:* `[Source: NODE_B_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 11 | UUID: 6dde8133-4e8e-44e4-b7c8-2663ea19447a]`

**[12:20:22]**
* **NODE_B** [Fault History]: Scheduled FMS Activity Missed Timing Requirement (Code: 6000)
  * *Details:* Serial Number: 487 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6000 | Fault Code: 6000 | Sub Code: Thunderbolt fault | Fault Name: Scheduled FMS Activity Missed Timing Requirement | Date and Time: 2032-06-18 12:20:22 PM | Module Temperature: 36 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 50 | Application Data: Deadline miss` Background service - 2162714;
  * *Citation:* `[Source: NODE_B_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 487 | UUID: a3027b57-2a7f-4e3d-9d1d-5d4df64cd373]`

**[12:20:23]**
* **NODE_A** [Operator Interaction] (x2 occurrences collapsed): Operator Interaction Event
  * *Details:* Dual mode: Dual | Master status: Master | Functional position: Captain | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 342.999786 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [FMS Operational Event: clear altitude | FMS node source: Standby | Event value: 131072]
  * *Citation:* `[Source: NODE_A_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 14 | UUID: 29d4b5bd-fb30-4403-8e4e-0c19160a5d3c]`
* **NODE_A** [Software Event]: Software Event: Master spare identifier
  * *Details:* Data Identifier: Master spare identifier | Data Format: Format fixed str | Left FMS node: Master | Center FMS node: Spare | Dual: Dual | [Event identifier: 68 | FMS node position: Operational master spare Changed]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 13 | UUID: 7123825b-5f35-4f5c-93e4-19035915cd05]`
* **NODE_B** [Operator Interaction] (x2 occurrences collapsed): Operator Interaction Event
  * *Details:* Dual mode: Dual | Master status: Spare | Functional position: First officer | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 366.104828 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [FMS Operational Event: clear altitude | FMS node source: Standby | Event value: 131072]
  * *Citation:* `[Source: NODE_B_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 10 | UUID: fda8b83f-8b55-4e3d-bed3-90cc7c393626]`

**[12:20:24]**
* **NODE_A** [Operator Interaction]: Operator Interaction Event
  * *Details:* Dual mode: Dual | Master status: Master | Functional position: Captain | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 342.999573 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [FMS Operational Event: no phase change | FMS node source: Standby | Event value: 65540]
  * *Citation:* `[Source: NODE_A_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 16 | UUID: b4e2ee6f-328a-4e2c-bf02-47b26a262708]`

**[12:20:25]**
* **NODE_B** [Operator Interaction]: Operator Interaction Event
  * *Details:* Dual mode: Dual | Master status: Spare | Functional position: First officer | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 366.746246 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [FMS Operational Event: no phase change | FMS node source: Standby | Event value: 65540]
  * *Citation:* `[Source: NODE_B_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 12 | UUID: 90d0e22d-6aab-4536-a433-ec6c6ba71cae]`
* **NODE_B** [Software Event]: Software Event: Master spare identifier
  * *Details:* Data Identifier: Master spare identifier | Data Format: Format fixed str | Left FMS node: Master | Center FMS node: Spare | Dual: Dual | [Event identifier: 68 | FMS node position: Operational master spare Changed]
  * *Citation:* `[Source: NODE_B_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 19 | UUID: cd86b4c5-9597-4dda-83f8-34e9bd8ecdad]`

**[12:20:27]**
* **NODE_B** [Fault History]: Oss semaphore failure (Code: 6029)
  * *Details:* Serial Number: 488 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6029 | Fault Code: 6029 | Sub Code: Thunderbolt fault | Fault Name: Oss semaphore failure | Date and Time: 2032-06-18 12:20:27 PM | Module Temperature: 36 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 100 | Application Data: wait semaphore failed in deos 653 - 6 ;
  * *Citation:* `[Source: NODE_B_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 488 | UUID: a826566b-ac33-4d32-b0c1-ad0ccc114e08]`

**[12:20:28]**
* **NODE_B** [Fault History]: Oss semaphore failure (Code: 6029)
  * *Details:* Serial Number: 489 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6029 | Fault Code: 6029 | Sub Code: Thunderbolt fault | Fault Name: Oss semaphore failure | Date and Time: 2032-06-18 12:20:28 PM | Module Temperature: 36 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 100 | Application Data: wait semaphore failed in deos 653 - 6 ;
  * *Citation:* `[Source: NODE_B_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 489 | UUID: 60535778-609b-4cad-ba6c-f5f6061aae65]`

**[12:20:30]**
* **NODE_B** [Fault History]: Oss semaphore failure (Code: 6029)
  * *Details:* Serial Number: 490 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6029 | Fault Code: 6029 | Sub Code: Thunderbolt fault | Fault Name: Oss semaphore failure | Date and Time: 2032-06-18 12:20:30 PM | Module Temperature: 36 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 100 | Application Data: wait semaphore failed in deos 653 - 6 ;
  * *Citation:* `[Source: NODE_B_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 490 | UUID: 0bf0aa5b-9c75-4e50-be01-9b63fd870263]`
* **NODE_B** [Fault History]: Scheduled FMS Activity Missed Timing Requirement (Code: 6000)
  * *Details:* Serial Number: 491 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6000 | Fault Code: 6000 | Sub Code: Thunderbolt fault | Fault Name: Scheduled FMS Activity Missed Timing Requirement | Date and Time: 2032-06-18 12:20:30 PM | Module Temperature: 36 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 50 | Application Data: Deadline miss` Background service - 2162713;
  * *Citation:* `[Source: NODE_B_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 491 | UUID: d4eafeac-7334-4035-8425-d17573afc10e]`

**[12:20:31]**
* **NODE_B** [Fault History]: Oss semaphore failure (Code: 6029)
  * *Details:* Serial Number: 492 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6029 | Fault Code: 6029 | Sub Code: Thunderbolt fault | Fault Name: Oss semaphore failure | Date and Time: 2032-06-18 12:20:31 PM | Module Temperature: 36 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 100 | Application Data: wait semaphore failed in deos 653 - 6 ;
  * *Citation:* `[Source: NODE_B_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 492 | UUID: 123b9207-6100-4cfd-b3c0-8b18e9dcd520]`

**[12:20:33]**
* **NODE_B** [Fault History] (x2 occurrences collapsed): Oss semaphore failure (Code: 6029)
  * *Details:* Serial Number: 493 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6029 | Fault Code: 6029 | Sub Code: Thunderbolt fault | Fault Name: Oss semaphore failure | Date and Time: 2032-06-18 12:20:33 PM | Module Temperature: 37 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 100 | Application Data: wait semaphore failed in deos 653 - 6 ;
  * *Citation:* `[Source: NODE_B_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 493 | UUID: 2dff46e0-4cf1-4894-9a1d-42e5ebb8e5cb]`

**[12:20:35]**
* **NODE_B** [Fault History]: Oss semaphore failure (Code: 6029)
  * *Details:* Serial Number: 495 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6029 | Fault Code: 6029 | Sub Code: Thunderbolt fault | Fault Name: Oss semaphore failure | Date and Time: 2032-06-18 12:20:35 PM | Module Temperature: 37 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 100 | Application Data: wait semaphore failed in deos 653 - 6 ;
  * *Citation:* `[Source: NODE_B_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 495 | UUID: 1badf5ec-a00c-42f8-adc7-2cccebfe4e8e]`

**[12:20:36]**
* **NODE_B** [Fault History]: Oss semaphore failure (Code: 6029)
  * *Details:* Serial Number: 496 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6029 | Fault Code: 6029 | Sub Code: Thunderbolt fault | Fault Name: Oss semaphore failure | Date and Time: 2032-06-18 12:20:36 PM | Module Temperature: 36 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 100 | Application Data: wait semaphore failed in deos 653 - 6 ;
  * *Citation:* `[Source: NODE_B_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 496 | UUID: de13735d-e0bc-4a1e-abd9-73715b08082d]`

**[12:20:38]**
* **NODE_B** [Fault History]: Oss semaphore failure (Code: 6029)
  * *Details:* Serial Number: 497 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6029 | Fault Code: 6029 | Sub Code: Thunderbolt fault | Fault Name: Oss semaphore failure | Date and Time: 2032-06-18 12:20:38 PM | Module Temperature: 36 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 100 | Application Data: wait semaphore failed in deos 653 - 6 ;
  * *Citation:* `[Source: NODE_B_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 497 | UUID: 5036b023-87f8-4c89-b592-dec8547952bf]`
* **NODE_B** [Fault History]: Navigation Data Coordination Activity Failure (Code: 11)
  * *Details:* Serial Number: 498 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 12925 | Fault Code: 11 | Sub Code: 109 | Fault Name: Navigation Data Coordination Activity Failure | Date and Time: 2032-06-18 12:20:38 PM | Module Temperature: 36 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 8 | Application Data: ?~J;
  * *Citation:* `[Source: NODE_B_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 498 | UUID: d66b824d-6749-49a1-9e37-8497f1831126]`
* **NODE_B** [Software Event]: Software Event: Opc configuration data identifier
  * *Details:* Data Identifier: Opc configuration data identifier | Data Format: Format opc configuration data | Left FMS node: Master | Center FMS node: Spare | Dual: Dual | [Identifier: Configuration data | Performance custo 3: False | Performance custo 2: False | Performance custo 1: False | Operational data link datalink: True | Air traffic service enable: True | Kilogram enable: True | Metric enable: True | Display trajectory: 1 | Grid mora enable: True | I4d rta enable: False | Radio navigation 2 installed: True | Aim disable: True | No radio navigation on board: False | Passenger count enable: True | Fls enable: True | To securization enable: True | No ap fd mda mdh disconnect: True | To derate enable: True | Climb derate enable: False | Fnl des enable: True | Cda enable: 1 | Cpdb opc enable: False | Vor2 dme2 on board: True | Rnp function enable: True | Leg sequencing monitoring enable: True | Resync check enable: True | To securization 2 enable: True | Sbas enable: True | Sls enable: True | Jfgw display on mfd enable: True | Acr 2 on board: False | Vertical display enable: True | FMS trjctry on vd enable: True | Mora on vd enable: True | Msa on vd enable: True | Etoc enable: True | Freeze scale on vd enable: False | Fls axis on vd enable: True | Aess twsf trjctry enable: True | Auto derate climb enable: True | Polar navigation enabled: True | Back beam approach en: True | FMS platform type 1: True | FMS platform type 2: True | FMS platform type 3: False | FMS platform type 4: False | FMS engine manuf 1: False | FMS engine manuf 2: True | FMS engine manuf 3: False | FMS engine type 1: False | FMS engine type 2: True | FMS engine type 3: False | FMS engine type 4: False | FMS engine type 5: False | Takeoff rnp: 1.000000 | Gps approach rnp: 0.300000 | Precision approach rnp: 0.500000 | Nonprecision approach rnp: 0.500000 | Terminal rnp: 1.000000 | Enroute rnp: 2.000000 | Oceanic rnp: 2.000000 | Takeoff tla: 110.991997 | Takeoff hal: 1.000000 | Approach hal: 0.300000 | Terminal hal: 1.000000 | Enroute hal: 2.000000 | Oceanic hal: 2.000000 | Tail number 32: .F-Wzht | Tail number 16: Zht | Tail number 8: T | Configuration data version: [Redacted Payload] | Opc integrity validation: 61]
  * *Citation:* `[Source: NODE_B_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 20 | UUID: 337a36ff-43a0-4378-94bc-6d6782980d6f]`

**[12:20:39]**
* **NODE_B** [Software Event]: Software Event: Sys status identifier
  * *Details:* Data Identifier: Sys status identifier | Data Format: Format sys status | Left FMS node: Master | Center FMS node: Spare | Dual: Dual | [Identifier: Sys | Platform family: A350 | Air frame ident: A350 | FMS node physical position: Center | Engine ident: Trent | Engine manufact: 2 | Opsys pn: Hnp5dxcl01xea01 | Ndb pn: Abv2601l01 | Ami database pn: Hnp40 | Database Reference: [Removed]: Hnp56xcd06xha08 | Cpdb pn: Not loaded]
  * *Citation:* `[Source: NODE_B_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 21 | UUID: 8c6eb083-a26c-42f4-ac4f-5b32ed05ecf5]`

**[12:20:41]**
* **NODE_B** [Fault History]: Oss semaphore failure (Code: 6029)
  * *Details:* Serial Number: 499 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6029 | Fault Code: 6029 | Sub Code: Thunderbolt fault | Fault Name: Oss semaphore failure | Date and Time: 2032-06-18 12:20:41 PM | Module Temperature: 36 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 100 | Application Data: wait semaphore failed in deos 653 - 6 ;
  * *Citation:* `[Source: NODE_B_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 499 | UUID: 18622a10-05b0-4475-be54-e1d1a3a9816e]`

**[12:20:44]**
* **NODE_B** [Fault History]: Oss semaphore failure (Code: 6029)
  * *Details:* Serial Number: 500 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6029 | Fault Code: 6029 | Sub Code: Thunderbolt fault | Fault Name: Oss semaphore failure | Date and Time: 2032-06-18 12:20:44 PM | Module Temperature: 36 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 100 | Application Data: wait semaphore failed in deos 653 - 6 ;
  * *Citation:* `[Source: NODE_B_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 500 | UUID: 571a176d-53e1-4a97-92ee-56d32b153657]`

**[12:20:47]**
* **NODE_B** [Fault History]: Oss semaphore failure (Code: 6029)
  * *Details:* Serial Number: 501 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6029 | Fault Code: 6029 | Sub Code: Thunderbolt fault | Fault Name: Oss semaphore failure | Date and Time: 2032-06-18 12:20:47 PM | Module Temperature: 36 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 100 | Application Data: wait semaphore failed in deos 653 - 6 ;
  * *Citation:* `[Source: NODE_B_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 501 | UUID: c4a2843d-2a48-4625-804a-39f946c931ba]`

**[12:20:52]**
* **NODE_B** [Fault History]: Oss semaphore failure (Code: 6029)
  * *Details:* Serial Number: 502 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6029 | Fault Code: 6029 | Sub Code: Thunderbolt fault | Fault Name: Oss semaphore failure | Date and Time: 2032-06-18 12:20:52 PM | Module Temperature: 36 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 100 | Application Data: wait semaphore failed in deos 653 - 6 ;
  * *Citation:* `[Source: NODE_B_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 502 | UUID: 665a37d7-f6c0-4eab-9ad6-14bfe4e899a5]`

**[12:20:53]**
* **NODE_B** [Fault History]: Scheduled FMS Activity Missed Timing Requirement (Code: 6000)
  * *Details:* Serial Number: 503 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6000 | Fault Code: 6000 | Sub Code: Thunderbolt fault | Fault Name: Scheduled FMS Activity Missed Timing Requirement | Date and Time: 2032-06-18 12:20:53 PM | Module Temperature: 36 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 50 | Application Data: Deadline miss` Background service - 2162712;
  * *Citation:* `[Source: NODE_B_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 503 | UUID: 3172b466-bfd7-4114-a81b-f896f0b0f2ac]`

**[12:20:54]**
* **NODE_B** [Fault History]: Oss semaphore failure (Code: 6029)
  * *Details:* Serial Number: 504 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6029 | Fault Code: 6029 | Sub Code: Thunderbolt fault | Fault Name: Oss semaphore failure | Date and Time: 2032-06-18 12:20:54 PM | Module Temperature: 38 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 100 | Application Data: wait semaphore failed in deos 653 - 6 ;
  * *Citation:* `[Source: NODE_B_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 504 | UUID: 8a4575e4-c562-4818-9e37-d6605e0f66b7]`

**[12:20:55]**
* **NODE_B** [Fault History]: Oss semaphore failure (Code: 6029)
  * *Details:* Serial Number: 505 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6029 | Fault Code: 6029 | Sub Code: Thunderbolt fault | Fault Name: Oss semaphore failure | Date and Time: 2032-06-18 12:20:55 PM | Module Temperature: 36 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 100 | Application Data: wait semaphore failed in deos 653 - 6 ;
  * *Citation:* `[Source: NODE_B_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 505 | UUID: d792ba76-4fba-4397-887f-1318ffeb2598]`

**[12:20:57]**
* **NODE_B** [Fault History]: Oss semaphore failure (Code: 6029)
  * *Details:* Serial Number: 506 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6029 | Fault Code: 6029 | Sub Code: Thunderbolt fault | Fault Name: Oss semaphore failure | Date and Time: 2032-06-18 12:20:57 PM | Module Temperature: 37 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 100 | Application Data: wait semaphore failed in deos 653 - 6 ;
  * *Citation:* `[Source: NODE_B_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 506 | UUID: 60eaabe2-dd41-47a5-8893-e58bfec76395]`

**[12:20:58]**
* **NODE_B** [Fault History]: Oss semaphore failure (Code: 6029)
  * *Details:* Serial Number: 507 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6029 | Fault Code: 6029 | Sub Code: Thunderbolt fault | Fault Name: Oss semaphore failure | Date and Time: 2032-06-18 12:20:58 PM | Module Temperature: 36 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 100 | Application Data: wait semaphore failed in deos 653 - 6 ;
  * *Citation:* `[Source: NODE_B_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 507 | UUID: 690a708b-d3f0-475d-bfdc-cac3d82e5563]`

**[12:20:59]**
* **NODE_B** [Fault History]: Oss semaphore failure (Code: 6029)
  * *Details:* Serial Number: 508 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6029 | Fault Code: 6029 | Sub Code: Thunderbolt fault | Fault Name: Oss semaphore failure | Date and Time: 2032-06-18 12:20:59 PM | Module Temperature: 36 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 100 | Application Data: wait semaphore failed in deos 653 - 6 ;
  * *Citation:* `[Source: NODE_B_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 508 | UUID: 09952fc1-08ad-4115-97c5-f5ba24c3294e]`

**[12:21:00]**
* **NODE_B** [Fault History]: Oss semaphore failure (Code: 6029)
  * *Details:* Serial Number: 509 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6029 | Fault Code: 6029 | Sub Code: Thunderbolt fault | Fault Name: Oss semaphore failure | Date and Time: 2032-06-18 12:21:00 PM | Module Temperature: 36 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 100 | Application Data: wait semaphore failed in deos 653 - 6 ;
  * *Citation:* `[Source: NODE_B_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 509 | UUID: 974247d8-df58-473c-baf8-280a06448ea7]`

**[12:21:02]**
* **NODE_B** [Fault History]: Oss semaphore failure (Code: 6029)
  * *Details:* Serial Number: 510 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6029 | Fault Code: 6029 | Sub Code: Thunderbolt fault | Fault Name: Oss semaphore failure | Date and Time: 2032-06-18 12:21:02 PM | Module Temperature: 36 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 100 | Application Data: wait semaphore failed in deos 653 - 6 ;
  * *Citation:* `[Source: NODE_B_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 510 | UUID: 0cc64f88-6383-4764-a3a7-92f63d1c27fa]`

**[12:21:06]**
* **NODE_A** [State Transition]: State Transition: Master status -> Master
  * *Details:* [Master status: Master | Dual mode: Dual | Opposite fms ok: Unstable | Other dual fms node position: FMS node center | Standby fms node position: FMS node invalid | Functional position: Captain]
  * *Citation:* `[Source: NODE_A_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 23 | UUID: cd906ec8-cb6e-498a-a63f-8768a6d8893e]`

**[12:21:07]**
* **NODE_A** [State Transition]: State Transition: Master status -> Master
  * *Details:* [Master status: Master | Dual mode: Dual | Opposite fms ok: Not ok | Other dual fms node position: FMS node center | Standby fms node position: FMS node invalid | Functional position: Captain]
  * *Citation:* `[Source: NODE_A_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 24 | UUID: 155241f7-e2b2-4784-a81e-c8f773e93dfa]`
* **NODE_B** [State Transition]: State Transition: Master status -> Spare
  * *Details:* [Master status: Spare | Dual mode: Dual | Opposite fms ok: Unstable | Other dual fms node position: FMS node left | Standby fms node position: FMS node invalid | Functional position: First officer]
  * *Citation:* `[Source: NODE_B_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 12 | UUID: a8be704b-399b-4285-bb4e-187ac00f80dc]`

**[12:21:08]**
* **NODE_A** [State Transition]: State Transition: Master status -> Master
  * *Details:* [Master status: Master | Dual mode: Dual | Opposite fms ok: Unstable | Other dual fms node position: FMS node center | Standby fms node position: FMS node invalid | Functional position: Captain]
  * *Citation:* `[Source: NODE_A_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 25 | UUID: 644fb0e0-d2fc-4143-8900-5e1ffbc3a082]`
* **NODE_B** [State Transition]: State Transition: Master status -> Spare
  * *Details:* [Master status: Spare | Dual mode: Dual | Opposite fms ok: Not ok | Other dual fms node position: FMS node left | Standby fms node position: FMS node invalid | Functional position: First officer]
  * *Citation:* `[Source: NODE_B_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 13 | UUID: 71040b5a-62f1-47b1-a25a-57facb9855fb]`

**[12:21:09]**
* **NODE_A** [State Transition]: State Transition: Master status -> Master
  * *Details:* [Master status: Master | Dual mode: Dual | Opposite fms ok: Ok | Other dual fms node position: FMS node center | Standby fms node position: FMS node invalid | Functional position: Captain]
  * *Citation:* `[Source: NODE_A_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 26 | UUID: 7cefd16b-87b6-4b52-a5ea-ffe3212e388c]`
* **NODE_B** [State Transition]: State Transition: Master status -> Spare
  * *Details:* [Master status: Spare | Dual mode: Dual | Opposite fms ok: Unstable | Other dual fms node position: FMS node left | Standby fms node position: FMS node invalid | Functional position: First officer]
  * *Citation:* `[Source: NODE_B_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 14 | UUID: 71ef15a1-7162-4b04-ad15-6156829f7e16]`

**[12:21:10]**
* **NODE_A** [Operator Interaction]: Operator interaction process Computed flight plan Request
  * *Details:* Dual mode: Dual | Master status: Master | Functional position: Captain | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 343.001099 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | Flight plan source - high: Active | Flight plan source - low: ActPrimary | Display system source: Operator interaction display system right | [Operator Interaction Event: Operator interaction process Computed flight plan Request | Event status: Operator interaction entered | Event value: 65547]
  * *Citation:* `[Source: NODE_A_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 17 | UUID: fe470760-78c7-4035-b01c-33ee66a21cb6]`
* **NODE_A** [Software Event]: Software Event: Operator interaction event identifier
  * *Details:* Data Identifier: Operator interaction event identifier | Data Format: Format operator interaction event | Left FMS node: Master | Center FMS node: Spare | Dual: Dual | [Event identifier: Operator interaction process Computed flight plan Request | Source fms node: First officer]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 14 | UUID: 4851246a-20ee-49eb-8a8a-944a7a927af5]`
* **NODE_A** [State Transition]: State Transition: Master status -> Master
  * *Details:* [Master status: Master | Dual mode: Dual | Opposite fms ok: Unstable | Other dual fms node position: FMS node center | Standby fms node position: FMS node invalid | Functional position: Captain]
  * *Citation:* `[Source: NODE_A_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 27 | UUID: 0195c47f-cfb9-4ce0-8298-6428165c36f0]`

**[12:21:11]**
* **NODE_A** [State Transition]: State Transition: Master status -> Master
  * *Details:* [Master status: Master | Dual mode: Dual | Opposite fms ok: Not ok | Other dual fms node position: FMS node center | Standby fms node position: FMS node invalid | Functional position: Captain]
  * *Citation:* `[Source: NODE_A_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 28 | UUID: e11ae53c-f8c2-42c6-9279-86fd3d65eb1e]`
* **NODE_B** [Operator Interaction]: Operator interaction process Computed flight plan Request
  * *Details:* Dual mode: Dual | Master status: Spare | Functional position: First officer | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 370.999298 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | Flight plan source - high: Active | Flight plan source - low: ActPrimary | Display system source: Operator interaction display system right | [Operator Interaction Event: Operator interaction process Computed flight plan Request | Event status: Operator interaction entered | Event value: 65547]
  * *Citation:* `[Source: NODE_B_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 13 | UUID: 93272c67-fb83-416d-b903-6bed28a13d1b]`
* **NODE_B** [Software Event]: Software Event: Operator interaction event identifier
  * *Details:* Data Identifier: Operator interaction event identifier | Data Format: Format operator interaction event | Left FMS node: Master | Center FMS node: Spare | Dual: Dual | [Event identifier: Operator interaction process Computed flight plan Request | Source fms node: First officer]
  * *Citation:* `[Source: NODE_B_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 22 | UUID: 04a3ef94-422e-45be-b43e-757be8623893]`

**[12:21:12]**
* **NODE_A** [Operator Interaction]: Operator interaction send operational data link flight plan request
  * *Details:* Dual mode: Dual | Master status: Master | Functional position: Captain | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 343.001251 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | Flight plan source - high: Active | Flight plan source - low: ActPrimary | Display system source: Operator interaction display system right | [Operator Interaction Event: Operator interaction send operational data link flight plan request | Event status: Operator interaction entered | Event value: 17826538]
  * *Citation:* `[Source: NODE_A_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 18 | UUID: 367da02d-2706-4579-8f08-b91c36799856]`
* **NODE_A** [Operator Interaction]: Operator Interaction Event
  * *Citation:* `[Source: NODE_A_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 19 | UUID: b658bf54-dc3a-493f-8fcf-a3c2d9f931eb]`
* **NODE_A** [Software Event]: Software Event: Operator interaction event identifier
  * *Details:* Data Identifier: Operator interaction event identifier | Data Format: Format operator interaction event | Left FMS node: Master | Center FMS node: Spare | Dual: Dual | [Event identifier: Operator interaction send operational data link flight plan request | Source fms node: First officer]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 15 | UUID: 8c4c799d-639e-4faf-a804-244cb94ec112]`
* **NODE_A** [State Transition]: State Transition: Master status -> Master
  * *Details:* [Master status: Master | Dual mode: Dual | Opposite fms ok: Unstable | Other dual fms node position: FMS node center | Standby fms node position: FMS node invalid | Functional position: Captain]
  * *Citation:* `[Source: NODE_A_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 29 | UUID: f706686c-640d-4922-ac81-e24e898a675e]`
* **NODE_B** [Operator Interaction]: Operator interaction send operational data link flight plan request
  * *Details:* Dual mode: Dual | Master status: Spare | Functional position: First officer | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 370.999420 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | Flight plan source - high: Active | Flight plan source - low: ActPrimary | Display system source: Operator interaction display system right | [Operator Interaction Event: Operator interaction send operational data link flight plan request | Event status: Operator interaction entered | Event value: 17826538]
  * *Citation:* `[Source: NODE_B_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 14 | UUID: bb5b8c4a-393c-42d2-bcc8-e22286872303]`
* **NODE_B** [Operator Interaction]: Operator Interaction Event
  * *Citation:* `[Source: NODE_B_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 15 | UUID: 50c4d596-ee48-47e4-a9fe-05df3f600d4d]`
* **NODE_B** [Software Event]: Software Event: Operator interaction event identifier
  * *Details:* Data Identifier: Operator interaction event identifier | Data Format: Format operator interaction event | Left FMS node: Master | Center FMS node: Spare | Dual: Dual | [Event identifier: Operator interaction send operational data link flight plan request | Source fms node: First officer]
  * *Citation:* `[Source: NODE_B_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 23 | UUID: 1c09eb12-1b0f-457a-af22-4e30c3ec4f11]`
* **NODE_B** [State Transition]: State Transition: Master status -> Spare
  * *Details:* [Master status: Spare | Dual mode: Dual | Opposite fms ok: Ok | Other dual fms node position: FMS node left | Standby fms node position: FMS node invalid | Functional position: First officer]
  * *Citation:* `[Source: NODE_B_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 15 | UUID: 49ea0af6-ed10-45ee-9785-4c702bb4b609]`

**[12:21:13]**
* **NODE_A** [State Transition]: State Transition: Master status -> Master
  * *Details:* [Master status: Master | Dual mode: Dual | Opposite fms ok: Ok | Other dual fms node position: FMS node center | Standby fms node position: FMS node invalid | Functional position: Captain]
  * *Citation:* `[Source: NODE_A_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 30 | UUID: fb750dd0-9cb6-4c3e-92b8-a525dd8a8259]`
* **NODE_B** [Fault History] (x3 occurrences collapsed): Scheduled FMS Activity Missed Timing Requirement (Code: 6000)
  * *Details:* Serial Number: 511 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6000 | Fault Code: 6000 | Sub Code: Thunderbolt fault | Fault Name: Scheduled FMS Activity Missed Timing Requirement | Date and Time: 2032-06-18 12:21:13 PM | Module Temperature: 36 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 50 | Application Data: Deadline miss` Background service - 2162706;
  * *Citation:* `[Source: NODE_B_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 511 | UUID: dd02b014-8858-4500-ace1-91483bacc2ee]`
* **NODE_B** [Operator Interaction]: Operator Interaction Event
  * *Details:* Dual mode: Dual | Master status: Spare | Functional position: First officer | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 370.999786 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [FMS Operational Event: uplink | FMS node source: Standby | Event value: 17826393]
  * *Citation:* `[Source: NODE_B_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 16 | UUID: 80218e3b-95ee-4906-a9db-2f2151826fa0]`
* **NODE_B** [Operator Interaction]: Operator interaction insert operational data link flight plan uplink
  * *Details:* Dual mode: Dual | Master status: Spare | Functional position: First officer | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 370.999786 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | Flight plan source - high: Active | Flight plan source - low: ActPrimary | Display system source: Operator interaction display system left | [Operator Interaction Event: Operator interaction insert operational data link flight plan uplink | Event status: Operator interaction entered | Event value: 65549]
  * *Citation:* `[Source: NODE_B_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 17 | UUID: 776a89b1-d3f0-4967-8431-25013e33484e]`
* **NODE_B** [Operator Interaction] (x4 occurrences collapsed): Operator Interaction Event
  * *Citation:* `[Source: NODE_B_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 18 | UUID: 55fcf0bc-aeb7-4e46-9632-44f64ccdbecb]`
* **NODE_B** [Software Event]: Software Event: S pad message identifier l
  * *Details:* Data Identifier: S pad message identifier l | Data Format: Format one unsign 32 | Left FMS node: Master | Center FMS node: Spare | Dual: Dual | [L message identifier: Air traffic control inserted in sec3]
  * *Citation:* `[Source: NODE_B_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 24 | UUID: 4371a18f-e6bb-42f1-ac57-c99743ff442f]`
* **NODE_B** [Software Event]: Software Event: S pad message identifier r
  * *Details:* Data Identifier: S pad message identifier r | Data Format: Format one unsign 32 | Left FMS node: Master | Center FMS node: Spare | Dual: Dual | [R message identifier: Air traffic control inserted in sec3]
  * *Citation:* `[Source: NODE_B_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 25 | UUID: 088644aa-eb2a-42e5-a185-ad3b2216657b]`
* **NODE_B** [Software Event]: Software Event: Operator interaction event identifier
  * *Details:* Data Identifier: Operator interaction event identifier | Data Format: Format operator interaction event | Left FMS node: Master | Center FMS node: Spare | Dual: Dual | [Event identifier: Operator interaction insert operational data link flight plan uplink | Source fms node: Captain]
  * *Citation:* `[Source: NODE_B_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 26 | UUID: 41bcf324-67b2-476e-9e91-b34514d1ac01]`
* **NODE_B** [Software Event]: Software Event: S pad message identifier l
  * *Details:* Data Identifier: S pad message identifier l | Data Format: Format one unsign 32 | Left FMS node: Master | Center FMS node: Spare | Dual: Dual | [L message identifier: Cpny insert in prog]
  * *Citation:* `[Source: NODE_B_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 27 | UUID: 9d388652-55f4-45d9-8171-9b45bda1a11d]`
* **NODE_B** [Software Event]: Software Event: S pad message identifier r
  * *Details:* Data Identifier: S pad message identifier r | Data Format: Format one unsign 32 | Left FMS node: Master | Center FMS node: Spare | Dual: Dual | [R message identifier: Cpny insert in prog]
  * *Citation:* `[Source: NODE_B_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 28 | UUID: aa877a74-1975-4547-9903-fc0d25a4e28e]`
* **NODE_B** [Software Event]: Software Event: Lnav identifier
  * *Details:* Data Identifier: Lnav identifier | Data Format: Format fixed str | Left FMS node: Master | Center FMS node: Spare | Dual: Dual | [Event identifier: 68 | L navigation status: L navigation path]
  * *Citation:* `[Source: NODE_B_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 29 | UUID: b469c437-60e9-4496-91f7-d258200c5666]`
* **NODE_B** [State Transition] (x6 occurrences collapsed): State Transition: Master status -> Spare
  * *Details:* [Master status: Spare | Dual mode: Dual | Opposite fms ok: Unstable | Other dual fms node position: FMS node left | Standby fms node position: FMS node invalid | Functional position: First officer]
  * *Citation:* `[Source: NODE_B_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 16 | UUID: bcb6fb40-4764-4c1e-b271-9b21c251f27e]`

**[12:21:15]**
* **NODE_A** [State Transition]: State Transition: Master status -> Master
  * *Details:* [Master status: Master | Dual mode: Dual | Opposite fms ok: Unstable | Other dual fms node position: FMS node center | Standby fms node position: FMS node invalid | Functional position: Captain]
  * *Citation:* `[Source: NODE_A_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 31 | UUID: fa3b816a-5ed2-4b68-b79e-715145b8f073]`

**[12:21:16]**
* **NODE_A** [State Transition] (x2 occurrences collapsed): State Transition: Master status -> Master
  * *Details:* [Master status: Master | Dual mode: Dual | Opposite fms ok: Not ok | Other dual fms node position: FMS node center | Standby fms node position: FMS node invalid | Functional position: Captain]
  * *Citation:* `[Source: NODE_A_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 32 | UUID: 95182e09-245a-4704-90e0-30a54d629f43]`

**[12:21:17]**
* **NODE_A** [State Transition]: State Transition: Master status -> Master
  * *Details:* [Master status: Master | Dual mode: Dual | Opposite fms ok: Ok | Other dual fms node position: FMS node center | Standby fms node position: FMS node invalid | Functional position: Captain]
  * *Citation:* `[Source: NODE_A_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 34 | UUID: 7aaf8e35-3a33-418d-98f0-905bcb9dbd00]`

**[12:21:18]**
* **NODE_A** [State Transition]: State Transition: Master status -> Master
  * *Details:* [Master status: Master | Dual mode: Dual | Opposite fms ok: Unstable | Other dual fms node position: FMS node center | Standby fms node position: FMS node invalid | Functional position: Captain]
  * *Citation:* `[Source: NODE_A_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 35 | UUID: 35351394-e438-4bd4-ae05-f9c595f990d4]`

**[12:21:20]**
* **NODE_A** [State Transition]: State Transition: Master status -> Master
  * *Details:* [Master status: Master | Dual mode: Dual | Opposite fms ok: Ok | Other dual fms node position: FMS node center | Standby fms node position: FMS node invalid | Functional position: Captain]
  * *Citation:* `[Source: NODE_A_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 36 | UUID: 1fe16b8b-2af0-4802-97b9-2d4d28e4d679]`

**[12:21:37]**
* **NODE_A** [Operator Interaction]: Operator Interaction Event
  * *Details:* Dual mode: Dual | Master status: Master | Functional position: Captain | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 343.000763 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [FMS Operational Event: uplink | FMS node source: Standby | Event value: 17826393]
  * *Citation:* `[Source: NODE_A_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 20 | UUID: 3c8cd8ae-c54b-4a58-b3df-a3669f376d70]`

**[12:21:38]**
* **NODE_A** [Software Event]: Software Event: S pad message identifier l
  * *Details:* Data Identifier: S pad message identifier l | Data Format: Format one unsign 32 | Left FMS node: Master | Center FMS node: Spare | Dual: Dual | [L message identifier: Air traffic control inserted in sec3]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 16 | UUID: 0233b5e2-2deb-4a46-b571-41d10c715607]`
* **NODE_A** [Software Event]: Software Event: S pad message identifier r
  * *Details:* Data Identifier: S pad message identifier r | Data Format: Format one unsign 32 | Left FMS node: Master | Center FMS node: Spare | Dual: Dual | [R message identifier: Air traffic control inserted in sec3]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 17 | UUID: 480b85bc-1365-4b45-961b-7b3c271667c9]`

**[12:21:43]**
* **NODE_A** [Fault History]: Scheduled FMS Activity Missed Timing Requirement (Code: 6000)
  * *Details:* Serial Number: 579 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6000 | Fault Code: 6000 | Sub Code: Thunderbolt fault | Fault Name: Scheduled FMS Activity Missed Timing Requirement | Date and Time: 2032-06-18 12:21:43 PM | Module Temperature: 40 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 50 | Application Data: Deadline miss` Background service - 65557;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 579 | UUID: a7e5cc18-dbc5-47da-a022-0884575b6bd1]`
* **NODE_A** [Operator Interaction]: Operator interaction insert operational data link flight plan uplink
  * *Details:* Dual mode: Dual | Master status: Master | Functional position: Captain | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 342.999847 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | Flight plan source - high: Active | Flight plan source - low: ActPrimary | Display system source: Operator interaction display system left | [Operator Interaction Event: Operator interaction insert operational data link flight plan uplink | Event status: Operator interaction entered | Event value: 65549]
  * *Citation:* `[Source: NODE_A_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 21 | UUID: 43f240c8-457f-43bf-a928-7a0edc612c4f]`
* **NODE_A** [Operator Interaction]: Operator Interaction Event
  * *Citation:* `[Source: NODE_A_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 22 | UUID: e535939e-9005-4477-9b82-bfe5a02ee4e6]`
* **NODE_A** [Software Event]: Software Event: Operator interaction event identifier
  * *Details:* Data Identifier: Operator interaction event identifier | Data Format: Format operator interaction event | Left FMS node: Master | Center FMS node: Spare | Dual: Dual | [Event identifier: Operator interaction insert operational data link flight plan uplink | Source fms node: Captain]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 18 | UUID: 63d2fc66-efeb-433d-987a-5e78d75f4c3c]`
* **NODE_A** [Software Event]: Software Event: S pad message identifier l
  * *Details:* Data Identifier: S pad message identifier l | Data Format: Format one unsign 32 | Left FMS node: Master | Center FMS node: Spare | Dual: Dual | [L message identifier: Cpny insert in prog]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 19 | UUID: 22d9b032-e846-44d1-9ad8-527cd148c82d]`
* **NODE_A** [Software Event]: Software Event: S pad message identifier r
  * *Details:* Data Identifier: S pad message identifier r | Data Format: Format one unsign 32 | Left FMS node: Master | Center FMS node: Spare | Dual: Dual | [R message identifier: Cpny insert in prog]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 20 | UUID: 5cade536-e15b-4718-88eb-a51e9deb800d]`

**[12:21:45]**
* **NODE_A** [Operator Interaction]: Operator Interaction Event
  * *Details:* Dual mode: Dual | Master status: Master | Functional position: Captain | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 342.999664 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [FMS Operational Event: Vertical Guidance Sequence Changed | FMS node source: Standby | Event value: 1049172]
  * *Citation:* `[Source: NODE_A_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 23 | UUID: b98568db-b5b1-406a-9245-ca31879d1b19]`
* **NODE_A** [Software Event]: Software Event: Lnav identifier
  * *Details:* Data Identifier: Lnav identifier | Data Format: Format fixed str | Left FMS node: Master | Center FMS node: Spare | Dual: Dual | [Event identifier: 68 | L navigation status: L navigation path]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 21 | UUID: b4c6d0cf-23fe-4d2a-93a1-872a389b08f0]`

**[12:21:46]**
* **NODE_A** [Operator Interaction] (x2 occurrences collapsed): Operator Interaction Event
  * *Details:* Dual mode: Dual | Master status: Master | Functional position: Captain | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 342.999634 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [FMS Operational Event: Guidance Recalculation Completed | FMS node source: Standby | Event value: 65543]
  * *Citation:* `[Source: NODE_A_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 24 | UUID: 4dc4f288-cf99-4c0c-a4e1-91d09ecb682d]`

**[12:22:31]**
* **NODE_A** [Operator Interaction]: Operator interaction enter zfw
  * *Details:* Dual mode: Dual | Master status: Master | Functional position: Captain | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 342.998322 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | Flight plan source - high: Active | Flight plan source - low: ActPrimary | Display system source: Operator interaction display system right | [Operator Interaction Event: Operator interaction enter zfw | Event status: Operator interaction entered | Event value: 131110]
  * *Citation:* `[Source: NODE_A_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 26 | UUID: a147b1e0-dc5d-405b-98f5-0cf03ad69ed0]`
* **NODE_A** [Software Event]: Software Event: Operator interaction event identifier
  * *Details:* Data Identifier: Operator interaction event identifier | Data Format: Format operator interaction event | Left FMS node: Master | Center FMS node: Spare | Dual: Dual | [Event identifier: Operator interaction enter zfw | Source fms node: First officer]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 22 | UUID: 03d65640-9b7a-40a9-a2d2-cfba38699d48]`

**[12:22:32]**
* **NODE_A** [Software Event]: Software Event: S pad message identifier l
  * *Details:* Data Identifier: S pad message identifier l | Data Format: Format one unsign 32 | Left FMS node: Master | Center FMS node: Spare | Dual: Dual | [L message identifier: Lrc mode in use]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 23 | UUID: 3821b2ad-a036-4376-a5ff-fc9ddfdf1bcc]`
* **NODE_A** [Software Event]: Software Event: S pad message identifier r
  * *Details:* Data Identifier: S pad message identifier r | Data Format: Format one unsign 32 | Left FMS node: Master | Center FMS node: Spare | Dual: Dual | [R message identifier: Lrc mode in use]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 24 | UUID: 158668fd-e7e7-4ba4-bf6e-64d13caa8256]`
* **NODE_B** [Operator Interaction]: Operator interaction enter zfw
  * *Details:* Dual mode: Dual | Master status: Spare | Functional position: First officer | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 370.999786 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | Flight plan source - high: Active | Flight plan source - low: ActPrimary | Display system source: Operator interaction display system right | [Operator Interaction Event: Operator interaction enter zfw | Event status: Operator interaction entered | Event value: 131110]
  * *Citation:* `[Source: NODE_B_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 22 | UUID: 536e4bb5-4175-4419-9862-2bc1e7e7932c]`
* **NODE_B** [Software Event]: Software Event: Operator interaction event identifier
  * *Details:* Data Identifier: Operator interaction event identifier | Data Format: Format operator interaction event | Left FMS node: Master | Center FMS node: Spare | Dual: Dual | [Event identifier: Operator interaction enter zfw | Source fms node: First officer]
  * *Citation:* `[Source: NODE_B_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 30 | UUID: 48b6a6cc-2a40-48b5-9a11-e343a30957b5]`
* **NODE_B** [Software Event]: Software Event: S pad message identifier l
  * *Details:* Data Identifier: S pad message identifier l | Data Format: Format one unsign 32 | Left FMS node: Master | Center FMS node: Spare | Dual: Dual | [L message identifier: Lrc mode in use]
  * *Citation:* `[Source: NODE_B_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 31 | UUID: cfd1ef82-0c23-4e8e-acce-0b2df629c06c]`
* **NODE_B** [Software Event]: Software Event: S pad message identifier r
  * *Details:* Data Identifier: S pad message identifier r | Data Format: Format one unsign 32 | Left FMS node: Master | Center FMS node: Spare | Dual: Dual | [R message identifier: Lrc mode in use]
  * *Citation:* `[Source: NODE_B_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 32 | UUID: 4c10d57d-b5ec-4dc3-bb2b-eb969cbf5e39]`

**[12:22:34]**
* **NODE_A** [Operator Interaction]: Operator interaction enter zfwcg
  * *Details:* Dual mode: Dual | Master status: Master | Functional position: Captain | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 342.997253 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | Flight plan source - high: Active | Flight plan source - low: ActPrimary | Display system source: Operator interaction display system right | [Operator Interaction Event: Operator interaction enter zfwcg | Event status: Operator interaction entered | Event value: 17826335]
  * *Citation:* `[Source: NODE_A_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 27 | UUID: a82897bd-fd42-4c9d-a9be-4e713053dc3c]`
* **NODE_A** [Software Event]: Software Event: Operator interaction event identifier
  * *Details:* Data Identifier: Operator interaction event identifier | Data Format: Format operator interaction event | Left FMS node: Master | Center FMS node: Spare | Dual: Dual | [Event identifier: Operator interaction enter zfwcg | Source fms node: First officer]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 25 | UUID: beeb9fc3-d8c2-4efa-8e98-a76c148b2eef]`

**[12:22:35]**
* **NODE_B** [Operator Interaction]: Operator interaction enter zfwcg
  * *Details:* Dual mode: Dual | Master status: Spare | Functional position: First officer | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 370.999786 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | Flight plan source - high: Active | Flight plan source - low: ActPrimary | Display system source: Operator interaction display system right | [Operator Interaction Event: Operator interaction enter zfwcg | Event status: Operator interaction entered | Event value: 17826335]
  * *Citation:* `[Source: NODE_B_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 23 | UUID: 084048a7-a280-49d5-84bf-34bab36db822]`
* **NODE_B** [Software Event]: Software Event: Operator interaction event identifier
  * *Details:* Data Identifier: Operator interaction event identifier | Data Format: Format operator interaction event | Left FMS node: Master | Center FMS node: Spare | Dual: Dual | [Event identifier: Operator interaction enter zfwcg | Source fms node: First officer]
  * *Citation:* `[Source: NODE_B_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 33 | UUID: f3b1ef03-913b-4f4d-b143-47fa2b1a5085]`

**[12:22:37]**
* **NODE_B** [Operator Interaction]: Operator interaction enter block
  * *Details:* Dual mode: Dual | Master status: Spare | Functional position: First officer | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 370.999786 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | Flight plan source - high: Active | Flight plan source - low: ActPrimary | Display system source: Operator interaction display system right | [Operator Interaction Event: Operator interaction enter block | Event status: Operator interaction entered | Event value: 17826336]
  * *Citation:* `[Source: NODE_B_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 24 | UUID: d4dd99c3-7627-479a-98a9-607558296467]`
* **NODE_B** [Software Event]: Software Event: Operator interaction event identifier
  * *Details:* Data Identifier: Operator interaction event identifier | Data Format: Format operator interaction event | Left FMS node: Master | Center FMS node: Spare | Dual: Dual | [Event identifier: Operator interaction enter block | Source fms node: First officer]
  * *Citation:* `[Source: NODE_B_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 34 | UUID: 7fb0888a-b8cd-4e59-9520-21274689d0da]`

**[12:22:38]**
* **NODE_A** [Operator Interaction]: Operator interaction enter block
  * *Details:* Dual mode: Dual | Master status: Master | Functional position: Captain | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 342.995941 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | Flight plan source - high: Active | Flight plan source - low: ActPrimary | Display system source: Operator interaction display system right | [Operator Interaction Event: Operator interaction enter block | Event status: Operator interaction entered | Event value: 17826336]
  * *Citation:* `[Source: NODE_A_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 28 | UUID: 156acdf3-f381-4bc8-8f62-d4e2e227911d]`
* **NODE_A** [Software Event]: Software Event: Operator interaction event identifier
  * *Details:* Data Identifier: Operator interaction event identifier | Data Format: Format operator interaction event | Left FMS node: Master | Center FMS node: Spare | Dual: Dual | [Event identifier: Operator interaction enter block | Source fms node: First officer]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 26 | UUID: bc441ca3-db33-40d3-8cc6-669e4eff024b]`
