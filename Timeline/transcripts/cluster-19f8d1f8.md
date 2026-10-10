# Incident Cluster: cluster-19f8d1f8
**Date:** 2032-06-18
**Duration:** 11:57:42 to 12:03:14
**Nodes Involved:** NODE_A, NODE_B, NODE_C
**Total Events:** 248 (Filtered from 351 raw logs)

## Timeline Transcript

**[11:57:42]**
* **NODE_C** [Operator Interaction] (x2 occurrences collapsed): Operator Interaction Event
  * *Details:* Dual mode: Single | Master status: Master | Functional position: First officer | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 342.998108 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [Fault/Event: Performance Defined Event | Event value: 2]
  * *Citation:* `[Source: NODE_C_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 743 | UUID: 62658e94-3362-497f-bb6e-7e55c2e235a7]`

**[11:57:44]**
* **NODE_C** [State Transition] (x2 occurrences collapsed): State Transition: Master status -> Spare
  * *Details:* [Master status: Spare | Dual mode: Single | Opposite fms ok: Not ok | Other dual fms node position: FMS node left | Standby fms node position: FMS node center | Functional position: First officer]
  * *Citation:* `[Source: NODE_C_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 100 | UUID: c98f326f-932b-4d45-b4f3-b26699affdc6]`

**[11:57:45]**
* **NODE_C** [State Transition] (x2 occurrences collapsed): State Transition: Master status -> Master
  * *Details:* [Master status: Master | Dual mode: Single | Opposite fms ok: Unstable | Other dual fms node position: FMS node left | Standby fms node position: FMS node center | Functional position: First officer]
  * *Citation:* `[Source: NODE_C_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 102 | UUID: fbd303a0-ccd5-429c-9c7b-4ce5ea67bbc7]`

**[11:57:46]**
* **NODE_C** [State Transition]: State Transition: Master status -> Master
  * *Details:* [Master status: Master | Dual mode: Single | Opposite fms ok: Not ok | Other dual fms node position: FMS node left | Standby fms node position: FMS node invalid | Functional position: First officer]
  * *Citation:* `[Source: NODE_C_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 104 | UUID: fc067f7a-3573-41c4-b690-7338f008cdec]`

**[11:57:51]**
* **NODE_C** [Software Event]: Software Event: Master spare identifier
  * *Details:* Data Identifier: Master spare identifier | Data Format: Format fixed str | Right FMS node: Master | Dual: Single | [Event identifier: 68 | FMS node position: Operational master spare Changed]
  * *Citation:* `[Source: NODE_C_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 288 | UUID: e80a2a28-66e0-4342-94ec-e6cc8ff2e544]`

**[11:58:11]**
* **NODE_A** [Fault History] (x2 occurrences collapsed): Background Service Identity Failure (Code: 6025)
  * *Details:* Serial Number: 363 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6025 | Fault Code: 6025 | Sub Code: Thunderbolt fault | Fault Name: Background Service Identity Failure | Date and Time: 2032-06-18 11:58:11 AM | Module Temperature: 40 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Initializing | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 35 | Application Data: get current process id failure 653;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 363 | UUID: cb54ea5f-f464-431b-ae55-73101433c084]`
* **NODE_A** [Fault History] (x20 occurrences collapsed): FMS Data Repository Access Failure (Code: 6074)
  * *Details:* Serial Number: 365 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6074 | Fault Code: 6074 | Sub Code: Thunderbolt fault | Fault Name: FMS Data Repository Access Failure | Date and Time: 2032-06-18 11:58:11 AM | Module Temperature: 40 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Initializing | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: True | Application Data Size: 196 | Application Data: can not Get line Public FMS Artifact file due to Fs end of file e error code;;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 365 | UUID: 71d6366a-2bbf-4f96-ae04-d2aa8e2de9b2]`

**[11:58:12]**
* **NODE_A** [Fault History] (x2 occurrences collapsed): Background Service Identity Failure (Code: 6025)
  * *Details:* Serial Number: 385 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6025 | Fault Code: 6025 | Sub Code: Thunderbolt fault | Fault Name: Background Service Identity Failure | Date and Time: 2032-06-18 11:58:12 AM | Module Temperature: 41 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Initializing | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 35 | Application Data: get current process id failure 653;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 385 | UUID: a461da73-e7f3-4f1b-b85f-139a32b4282c]`
* **NODE_A** [Fault History]: Oss loading failure (Code: 6052)
  * *Details:* Serial Number: 387 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6052 | Fault Code: 6052 | Sub Code: Thunderbolt fault | Fault Name: Oss loading failure | Date and Time: 2032-06-18 11:58:12 AM | Module Temperature: 41 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Initializing | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 100 | Application Data: Failed to load library in Deos 653 - Libpssl dtf manager so.so 11 11;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 387 | UUID: b93f462b-c4e0-48a0-b725-49ee06fa66c5]`
* **NODE_A** [Fault History] (x2 occurrences collapsed): Background Service Identity Failure (Code: 6025)
  * *Details:* Serial Number: 388 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6025 | Fault Code: 6025 | Sub Code: Thunderbolt fault | Fault Name: Background Service Identity Failure | Date and Time: 2032-06-18 11:58:12 AM | Module Temperature: 40 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Initializing | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 35 | Application Data: get current process id failure 653;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 388 | UUID: e2f8f289-947a-437b-83ea-0aacd3e3f752]`
* **NODE_A** [Fault History]: Cpdb opc not not enabled (Code: 6)
  * *Details:* Serial Number: 390 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 11643 | Fault Code: 6 | Sub Code: 107 | Fault Name: Cpdb opc not not enabled | Date and Time: 2032-06-18 11:58:12 AM | Module Temperature: 40 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Initializing | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 8 | Application Data: ?~J;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 390 | UUID: e3fc8ede-090a-42e2-af12-8757ede065da]`
* **NODE_A** [Operator Interaction]: Operator Interaction Event
  * *Details:* Dual mode: Single | Master status: Master | Functional position: Captain | Calibrated airspeed data: 30.000000 | Message: No displayable fields
  * *Citation:* `[Source: NODE_A_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 1 | UUID: 316d8d73-e434-4324-9e31-f9813a6d1afa]`

**[11:58:13]**
* **NODE_A** [Fault History]: Background Service Identity Failure (Code: 6025)
  * *Details:* Serial Number: 391 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6025 | Fault Code: 6025 | Sub Code: Thunderbolt fault | Fault Name: Background Service Identity Failure | Date and Time: 2032-06-18 11:58:13 AM | Module Temperature: 39 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Initializing | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 35 | Application Data: get current process id failure 653;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 391 | UUID: 34bee436-69b1-4cc6-b67d-a958dfab9158]`
* **NODE_A** [Fault History]: Oss generic fault (Code: 6080)
  * *Details:* Serial Number: 392 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6080 | Fault Code: 6080 | Sub Code: Thunderbolt fault | Fault Name: Oss generic fault | Date and Time: 2032-06-18 11:58:13 AM | Module Temperature: 39 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Initializing | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 48 | Application Data: Get parent task rate : Process is not found 653;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 392 | UUID: 55d31f50-d679-4d73-a1fa-48b89920b326]`
* **NODE_A** [Fault History] (x7 occurrences collapsed): Background Service Identity Failure (Code: 6025)
  * *Details:* Serial Number: 393 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6025 | Fault Code: 6025 | Sub Code: Thunderbolt fault | Fault Name: Background Service Identity Failure | Date and Time: 2032-06-18 11:58:13 AM | Module Temperature: 40 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Ready | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 35 | Application Data: get current process id failure 653;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 393 | UUID: 606749c2-6088-41ff-8858-b13f978fc3ce]`
* **NODE_A** [Fault History] (x8 occurrences collapsed): Oss bind failure (Code: 6035)
  * *Details:* Serial Number: 400 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6035 | Fault Code: 6035 | Sub Code: Thunderbolt fault | Fault Name: Oss bind failure | Date and Time: 2032-06-18 11:58:13 AM | Module Temperature: 39 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Ready | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 100 | Application Data: Client Cb not found in deos 653 - -933180756;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 400 | UUID: 249b40c2-b546-40ad-aa4b-ef654ad29eaa]`
* **NODE_A** [Fault History]: Oss task client failure (Code: 6024)
  * *Details:* Serial Number: 408 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6024 | Fault Code: 6024 | Sub Code: Thunderbolt fault | Fault Name: Oss task client failure | Date and Time: 2032-06-18 11:58:13 AM | Module Temperature: 41 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Ready | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 22 | Application Data: Task Client not found;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 408 | UUID: 84206321-c126-432c-b092-af4f939afce0]`
* **NODE_A** [Fault History]: Ndb out of date (Code: 5)
  * *Details:* Serial Number: 409 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 11311 | Fault Code: 5 | Sub Code: 31 | Fault Name: Ndb out of date | Date and Time: 2032-06-18 11:58:13 AM | Module Temperature: 41 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 8 | Application Data: ?~J;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 409 | UUID: fa12381e-bb09-4625-8a60-be66a0ff52b2]`
* **NODE_A** [Fault History]: Oss task client failure (Code: 6024)
  * *Details:* Serial Number: 410 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6024 | Fault Code: 6024 | Sub Code: Thunderbolt fault | Fault Name: Oss task client failure | Date and Time: 2032-06-18 11:58:13 AM | Module Temperature: 41 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 22 | Application Data: Task Client not found;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 410 | UUID: f60d60cf-c85a-4ed4-872b-f8606368c500]`
* **NODE_A** [Fault History]: Error during start process (Code: 9)
  * *Details:* Serial Number: 411 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 12315 | Fault Code: 9 | Sub Code: 11 | Fault Name: Error during start process | Date and Time: 2032-06-18 11:58:13 AM | Module Temperature: 41 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 8 | Application Data: ?~J;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 411 | UUID: ec9b8e07-01ca-40d2-9de9-e430b610939b]`
* **NODE_A** [Fault History]: Oss generic fault (Code: 6080)
  * *Details:* Serial Number: 412 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6080 | Fault Code: 6080 | Sub Code: Thunderbolt fault | Fault Name: Oss generic fault | Date and Time: 2032-06-18 11:58:13 AM | Module Temperature: 40 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 45 | Application Data: Background Task:Set priority Deos Api failure in 653;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 412 | UUID: 5c1191ab-9ed0-4d88-8087-260c57ef8367]`
* **NODE_A** [Software Event]: Software Event: Operational startup mode identifier
  * *Details:* Data Identifier: Operational startup mode identifier | Data Format: Format fixed str | Left FMS node: Spare | Dual: Single | [Event identifier: 68 | Operational startup mode: Operational startup cold]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 1 | UUID: fb3aab1e-850e-45dc-b1e2-3fa9128382c5]`
* **NODE_A** [Software Event]: Software Event: Dual mode identifier
  * *Details:* Data Identifier: Dual mode identifier | Data Format: Format fixed str | Left FMS node: Spare | Dual: Single | [Event identifier: 68 | Operational dual mode: Operational dual mode Changed]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 2 | UUID: 5598de11-254e-49fe-b89f-89287694df89]`
* **NODE_A** [Software Event]: Software Event: Operational powerup identifier
  * *Details:* Data Identifier: Operational powerup identifier | Data Format: Format fixed str | Left FMS node: Spare | Dual: Single | [Event identifier: 68 | Operational powerup: Operational powerup normal]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 3 | UUID: e69dc023-2195-4240-804c-753f9c43f0b0]`
* **NODE_A** [State Transition]: State Transition: Master status -> Master
  * *Details:* [Master status: Master | Dual mode: Single | Opposite fms ok: Unknown | Other dual fms node position: FMS node invalid | Standby fms node position: FMS node invalid | Functional position: Standby]
  * *Citation:* `[Source: NODE_A_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 1 | UUID: e9abdd04-8fe6-425e-82ad-24c93d6cf2cd]`
* **NODE_A** [State Transition]: State Transition: Master status -> Standby
  * *Details:* [Master status: Standby | Dual mode: Single | Opposite fms ok: Unknown | Other dual fms node position: FMS node invalid | Standby fms node position: FMS node invalid | Functional position: Standby]
  * *Citation:* `[Source: NODE_A_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 2 | UUID: ce025526-5786-4327-9742-8dc7f7f6a3f8]`
* **NODE_C** [State Transition]: State Transition: Master status -> Master
  * *Details:* [Master status: Master | Dual mode: Single | Opposite fms ok: Not ok | Other dual fms node position: FMS node left | Standby fms node position: FMS node left | Functional position: First officer]
  * *Citation:* `[Source: NODE_C_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 105 | UUID: 86cc6d0b-6d3c-4bb0-83de-9eb8433f4a6c]`

**[11:58:14]**
* **NODE_A** [Fault History]: Oss task client failure (Code: 6024)
  * *Details:* Serial Number: 413 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6024 | Fault Code: 6024 | Sub Code: Thunderbolt fault | Fault Name: Oss task client failure | Date and Time: 2032-06-18 11:58:14 AM | Module Temperature: 41 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 22 | Application Data: Task Client not found;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 413 | UUID: 27d276a7-fe17-4b5c-9f0f-a7d83ac8b58b]`
* **NODE_A** [Fault History]: Error during start process (Code: 9)
  * *Details:* Serial Number: 414 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 12315 | Fault Code: 9 | Sub Code: 11 | Fault Name: Error during start process | Date and Time: 2032-06-18 11:58:14 AM | Module Temperature: 40 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 8 | Application Data: ?~J;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 414 | UUID: 1c265bf5-06bd-4eb5-ab85-f934336300a6]`
* **NODE_A** [Operator Interaction] (x3 occurrences collapsed): Operator Interaction Event
  * *Details:* Dual mode: Single | Master status: Master | Functional position: Captain | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 342.999176 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [FMS Operational Event: clear altitude | FMS node source: Standby]
  * *Citation:* `[Source: NODE_A_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 2 | UUID: 755e3731-8422-4180-ad1e-2c6d29ba4a13]`
* **NODE_A** [State Transition] (x4 occurrences collapsed): State Transition: Master status -> Master
  * *Details:* [Master status: Master | Dual mode: Single | Opposite fms ok: Unknown | Other dual fms node position: FMS node invalid | Standby fms node position: FMS node invalid | Functional position: Captain]
  * *Citation:* `[Source: NODE_A_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 3 | UUID: ab2992aa-4630-420e-bccf-312fb2ee698d]`
* **NODE_C** [State Transition] (x2 occurrences collapsed): State Transition: Master status -> Spare
  * *Details:* [Master status: Spare | Dual mode: Single | Opposite fms ok: Not ok | Other dual fms node position: FMS node left | Standby fms node position: FMS node left | Functional position: First officer]
  * *Citation:* `[Source: NODE_C_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 106 | UUID: 0ca056d5-3526-4e5d-abc6-9f39dca98401]`

**[11:58:15]**
* **NODE_A** [Fault History] (x2 occurrences collapsed): Scheduled FMS Activity Missed Timing Requirement (Code: 6000)
  * *Details:* Serial Number: 415 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6000 | Fault Code: 6000 | Sub Code: Thunderbolt fault | Fault Name: Scheduled FMS Activity Missed Timing Requirement | Date and Time: 2032-06-18 11:58:15 AM | Module Temperature: 40 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 50 | Application Data: Deadline miss` Background service - 65563;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 415 | UUID: 04f3d8ca-32fc-49c8-a22b-40ddd6aaad27]`
* **NODE_A** [Operator Interaction] (x2 occurrences collapsed): Operator Interaction Event
  * *Details:* Dual mode: Single | Master status: Master | Functional position: Captain | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 342.998993 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [FMS Operational Event: Vertical Guidance Sequence Changed | FMS node source: Standby | Event value: 65562]
  * *Citation:* `[Source: NODE_A_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 5 | UUID: 632c1230-ef00-4c69-8274-66778a7fb3ca]`
* **NODE_A** [Software Event]: Software Event: S pad message identifier l
  * *Details:* Data Identifier: S pad message identifier l | Data Format: Format one unsign 32 | Left FMS node: Spare | Dual: Single | [L message identifier: Please wait]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 4 | UUID: b8cd734c-bb16-4f4c-bdc7-ff1906dc9c86]`
* **NODE_A** [Software Event]: Software Event: S pad message identifier r
  * *Details:* Data Identifier: S pad message identifier r | Data Format: Format one unsign 32 | Left FMS node: Spare | Dual: Single | [R message identifier: Please wait]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 5 | UUID: 23189e35-1808-45ce-a5be-e9440e072850]`
* **NODE_A** [State Transition]: State Transition: Master status -> Master
  * *Details:* [Master status: Master | Dual mode: Single | Opposite fms ok: Ok | Other dual fms node position: FMS node right | Standby fms node position: FMS node invalid | Functional position: Captain]
  * *Citation:* `[Source: NODE_A_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 7 | UUID: e274706b-913a-4441-87c6-28a9ab519588]`
* **NODE_C** [State Transition] (x2 occurrences collapsed): State Transition: Master status -> Spare
  * *Details:* [Master status: Spare | Dual mode: Single | Opposite fms ok: Unstable | Other dual fms node position: FMS node left | Standby fms node position: FMS node invalid | Functional position: First officer]
  * *Citation:* `[Source: NODE_C_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 108 | UUID: 8d2bd404-741a-43c6-a80f-225481158ff3]`

**[11:58:16]**
* **NODE_A** [Fault History]: Oss semaphore failure (Code: 6029)
  * *Details:* Serial Number: 417 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6029 | Fault Code: 6029 | Sub Code: Thunderbolt fault | Fault Name: Oss semaphore failure | Date and Time: 2032-06-18 11:58:16 AM | Module Temperature: 39 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 100 | Application Data: wait semaphore failed in deos 653 - 6 ;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 417 | UUID: a53c7e6b-b9e6-4c17-b47a-101c5042c69f]`

**[11:58:17]**
* **NODE_A** [Fault History]: Oss semaphore failure (Code: 6029)
  * *Details:* Serial Number: 418 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6029 | Fault Code: 6029 | Sub Code: Thunderbolt fault | Fault Name: Oss semaphore failure | Date and Time: 2032-06-18 11:58:17 AM | Module Temperature: 40 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 100 | Application Data: wait semaphore failed in deos 653 - 6 ;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 418 | UUID: 0783419b-4d03-4729-b4ce-3885fc4a5dfa]`

**[11:58:18]**
* **NODE_A** [Fault History]: Scheduled FMS Activity Missed Timing Requirement (Code: 6000)
  * *Details:* Serial Number: 419 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6000 | Fault Code: 6000 | Sub Code: Thunderbolt fault | Fault Name: Scheduled FMS Activity Missed Timing Requirement | Date and Time: 2032-06-18 11:58:18 AM | Module Temperature: 39 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 50 | Application Data: Deadline miss` Background service - 65562;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 419 | UUID: 42e0e24d-dfa2-4539-b4b3-9c9a5fd2f17d]`
* **NODE_A** [Fault History]: Oss semaphore failure (Code: 6029)
  * *Details:* Serial Number: 420 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6029 | Fault Code: 6029 | Sub Code: Thunderbolt fault | Fault Name: Oss semaphore failure | Date and Time: 2032-06-18 11:58:18 AM | Module Temperature: 40 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 100 | Application Data: wait semaphore failed in deos 653 - 6 ;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 420 | UUID: c2ab9f74-79e8-4820-8d53-02f43d5f38c2]`

**[11:58:19]**
* **NODE_A** [Fault History]: Oss semaphore failure (Code: 6029)
  * *Details:* Serial Number: 421 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6029 | Fault Code: 6029 | Sub Code: Thunderbolt fault | Fault Name: Oss semaphore failure | Date and Time: 2032-06-18 11:58:19 AM | Module Temperature: 40 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 100 | Application Data: wait semaphore failed in deos 653 - 6 ;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 421 | UUID: 90a6df6d-0742-4313-a14e-61eda33410df]`
* **NODE_A** [Fault History]: Scheduled FMS Activity Missed Timing Requirement (Code: 6000)
  * *Details:* Serial Number: 422 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6000 | Fault Code: 6000 | Sub Code: Thunderbolt fault | Fault Name: Scheduled FMS Activity Missed Timing Requirement | Date and Time: 2032-06-18 11:58:19 AM | Module Temperature: 40 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 50 | Application Data: Deadline miss` Background service - 65561;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 422 | UUID: b2cedefa-8206-4861-963c-6e424a4eaf2f]`
* **NODE_A** [Software Event]: Software Event: Master spare identifier
  * *Details:* Data Identifier: Master spare identifier | Data Format: Format fixed str | Left FMS node: Master | Dual: Single | [Event identifier: 68 | FMS node position: Operational master spare Changed]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 6 | UUID: dbc35f58-bb54-4f98-8d81-ee69f4d4c9b5]`

**[11:58:20]**
* **NODE_A** [Fault History]: Oss semaphore failure (Code: 6029)
  * *Details:* Serial Number: 423 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6029 | Fault Code: 6029 | Sub Code: Thunderbolt fault | Fault Name: Oss semaphore failure | Date and Time: 2032-06-18 11:58:20 AM | Module Temperature: 40 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 100 | Application Data: wait semaphore failed in deos 653 - 6 ;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 423 | UUID: 9b4513f1-8e1c-4b77-8726-300e2a898e6f]`
* **NODE_C** [Software Event]: Software Event: Master spare identifier
  * *Details:* Data Identifier: Master spare identifier | Data Format: Format fixed str | Left FMS node: Master | Right FMS node: Spare | Dual: Single | [Event identifier: 68 | FMS node position: Operational master spare Changed]
  * *Citation:* `[Source: NODE_C_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 289 | UUID: 45f2c2fc-782f-41d1-b4e6-f679f749bc67]`

**[11:58:21]**
* **NODE_A** [Fault History]: Oss semaphore failure (Code: 6029)
  * *Details:* Serial Number: 424 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6029 | Fault Code: 6029 | Sub Code: Thunderbolt fault | Fault Name: Oss semaphore failure | Date and Time: 2032-06-18 11:58:21 AM | Module Temperature: 40 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 100 | Application Data: wait semaphore failed in deos 653 - 6 ;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 424 | UUID: e0742dff-e3ce-4e5e-9b10-bc103de2365f]`

**[11:58:22]**
* **NODE_A** [Fault History]: Oss semaphore failure (Code: 6029)
  * *Details:* Serial Number: 425 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6029 | Fault Code: 6029 | Sub Code: Thunderbolt fault | Fault Name: Oss semaphore failure | Date and Time: 2032-06-18 11:58:22 AM | Module Temperature: 40 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 100 | Application Data: wait semaphore failed in deos 653 - 6 ;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 425 | UUID: 0af88b1d-f7ff-4963-9179-e805a959edbd]`

**[11:58:23]**
* **NODE_A** [Fault History]: Oss semaphore failure (Code: 6029)
  * *Details:* Serial Number: 426 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6029 | Fault Code: 6029 | Sub Code: Thunderbolt fault | Fault Name: Oss semaphore failure | Date and Time: 2032-06-18 11:58:23 AM | Module Temperature: 39 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 100 | Application Data: wait semaphore failed in deos 653 - 6 ;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 426 | UUID: 739985d9-9169-4de6-a10a-8fe6f7115903]`

**[11:58:24]**
* **NODE_A** [Fault History]: Oss semaphore failure (Code: 6029)
  * *Details:* Serial Number: 427 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6029 | Fault Code: 6029 | Sub Code: Thunderbolt fault | Fault Name: Oss semaphore failure | Date and Time: 2032-06-18 11:58:24 AM | Module Temperature: 40 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 100 | Application Data: wait semaphore failed in deos 653 - 6 ;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 427 | UUID: 44259e2e-40ea-43b5-9299-12fb1a8e1314]`
* **NODE_A** [Operator Interaction]: Operator Interaction Event
  * *Details:* Dual mode: Dual | Master status: Master | Functional position: Captain | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 342.997986 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [Fault/Event: Cold Start Due To A Re-Synch On The Receiver]
  * *Citation:* `[Source: NODE_A_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 7 | UUID: 4c93ca93-876e-458a-ac43-a826fafd31ed]`

**[11:58:25]**
* **NODE_C** [State Transition]: State Transition: Master status -> Spare
  * *Details:* [Master status: Spare | Dual mode: Single | Opposite fms ok: Unstable | Other dual fms node position: FMS node left | Standby fms node position: FMS node invalid | Functional position: First officer]
  * *Citation:* `[Source: NODE_C_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 110 | UUID: aeb5fd89-aec2-4648-a6ca-7f19da047af8]`

**[11:58:26]**
* **NODE_C** [State Transition]: State Transition: Master status -> Spare
  * *Details:* [Master status: Spare | Dual mode: Single | Opposite fms ok: Not ok | Other dual fms node position: FMS node left | Standby fms node position: FMS node invalid | Functional position: First officer]
  * *Citation:* `[Source: NODE_C_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 111 | UUID: 0b63186d-b77b-4926-8f00-333bbf85761a]`

**[11:58:34]**
* **NODE_C** [State Transition]: State Transition: Master status -> Master
  * *Details:* [Master status: Master | Dual mode: Single | Opposite fms ok: Not ok | Other dual fms node position: FMS node left | Standby fms node position: FMS node invalid | Functional position: First officer]
  * *Citation:* `[Source: NODE_C_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 112 | UUID: 5c18f26c-9eb4-40b2-b776-5f13f0f83491]`

**[11:58:40]**
* **NODE_C** [Software Event]: Software Event: Master spare identifier
  * *Details:* Data Identifier: Master spare identifier | Data Format: Format fixed str | Right FMS node: Master | Dual: Single | [Event identifier: 68 | FMS node position: Operational master spare Changed]
  * *Citation:* `[Source: NODE_C_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 290 | UUID: e4b3390c-d2a5-4e20-9e5b-8647f57efcfc]`

**[11:58:55]**
* **NODE_B** [Fault History]: Oss loading failure (Code: 6052)
  * *Details:* Serial Number: 262 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6052 | Fault Code: 6052 | Sub Code: Thunderbolt fault | Fault Name: Oss loading failure | Date and Time: 2032-06-18 11:58:55 AM | Module Temperature: 37 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Initializing | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 100 | Application Data: Failed to load library in Deos 653 - Libpssl dtf manager so.so 11 11;
  * *Citation:* `[Source: NODE_B_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 262 | UUID: edac0fc7-2fd0-4862-a11e-d12bdd925c7d]`

**[11:58:56]**
* **NODE_B** [Operator Interaction]: Operator Interaction Event
  * *Details:* Dual mode: Single | Master status: Standby | Functional position: Captain | Calibrated airspeed data: 30.000000 | Message: No displayable fields
  * *Citation:* `[Source: NODE_B_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 21 | UUID: eca5891a-1bd9-4344-bdc8-267794adfa21]`

**[11:58:57]**
* **NODE_B** [Fault History] (x4 occurrences collapsed): Oss bind failure (Code: 6035)
  * *Details:* Serial Number: 263 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6035 | Fault Code: 6035 | Sub Code: Thunderbolt fault | Fault Name: Oss bind failure | Date and Time: 2032-06-18 11:58:57 AM | Module Temperature: 36 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Ready | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 100 | Application Data: Client Cb not found in deos 653 - -933180756;
  * *Citation:* `[Source: NODE_B_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 263 | UUID: 1b8f4039-e4b3-414b-b80a-032ea40c0660]`
* **NODE_B** [Fault History] (x6 occurrences collapsed): Oss task client failure (Code: 6024)
  * *Details:* Serial Number: 267 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6024 | Fault Code: 6024 | Sub Code: Thunderbolt fault | Fault Name: Oss task client failure | Date and Time: 2032-06-18 11:58:57 AM | Module Temperature: 37 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Ready | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 22 | Application Data: Task Client not found;
  * *Citation:* `[Source: NODE_B_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 267 | UUID: 667ada33-4477-4c80-ac67-3d6833f1f50f]`
* **NODE_B** [Operator Interaction] (x2 occurrences collapsed): Operator Interaction Event
  * *Details:* Dual mode: Single | Master status: Master | Functional position: Captain | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 342.999573 | Magnetic track: 66.049805 | [FMS Operational Event: clear altitude | FMS node source: Standby]
  * *Citation:* `[Source: NODE_B_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 22 | UUID: 0b9201c7-a9d3-423b-8996-836a4dc11214]`
* **NODE_B** [Software Event]: Software Event: Operational startup mode identifier
  * *Details:* Data Identifier: Operational startup mode identifier | Data Format: Format fixed str | Left FMS node: Spare | Dual: Single | [Event identifier: 68 | Operational startup mode: Operational startup cold]
  * *Citation:* `[Source: NODE_B_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 53 | UUID: 17a39d10-0290-4020-823d-407344e09e64]`
* **NODE_B** [Software Event]: Software Event: Dual mode identifier
  * *Details:* Data Identifier: Dual mode identifier | Data Format: Format fixed str | Left FMS node: Spare | Dual: Single | [Event identifier: 68 | Operational dual mode: Operational dual mode Changed]
  * *Citation:* `[Source: NODE_B_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 54 | UUID: 636ce9d7-0d1a-4982-997a-3da4bfc553a1]`
* **NODE_B** [Software Event]: Software Event: Operational powerup identifier
  * *Details:* Data Identifier: Operational powerup identifier | Data Format: Format fixed str | Left FMS node: Spare | Dual: Single | [Event identifier: 68 | Operational powerup: Operational powerup normal]
  * *Citation:* `[Source: NODE_B_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 55 | UUID: c89ff871-5635-42da-a863-f7f47eb3ec10]`
* **NODE_B** [State Transition]: State Transition: Master status -> Standby
  * *Details:* [Master status: Standby | Dual mode: Single | Opposite fms ok: Unknown | Other dual fms node position: FMS node right | Standby fms node position: FMS node invalid | Functional position: Captain]
  * *Citation:* `[Source: NODE_B_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 16 | UUID: 153da3af-db11-44ca-a77f-b79ae8a1e4d1]`
* **NODE_B** [State Transition]: State Transition: Master status -> Master
  * *Details:* [Master status: Master | Dual mode: Single | Opposite fms ok: Unknown | Other dual fms node position: FMS node right | Standby fms node position: FMS node invalid | Functional position: Captain]
  * *Citation:* `[Source: NODE_B_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 17 | UUID: 1850eaaa-f869-4c0a-afcb-24ce4b7b2021]`
* **NODE_C** [Operator Interaction]: Operator Interaction Event
  * *Details:* Dual mode: Single | Master status: Spare | Functional position: First officer | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 342.999908 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [FMS Operational Event: redisplay | FMS node source: Captain | Event value: 131091]
  * *Citation:* `[Source: NODE_C_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 745 | UUID: b80cabca-6fcf-4003-926c-b2d6f642b99e]`
* **NODE_C** [State Transition]: State Transition: Master status -> Spare
  * *Details:* [Master status: Spare | Dual mode: Single | Opposite fms ok: Not ok | Other dual fms node position: FMS node center | Standby fms node position: FMS node invalid | Functional position: First officer]
  * *Citation:* `[Source: NODE_C_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 113 | UUID: 4691afe1-1f53-4fe6-ad89-9651dc05d21a]`

**[11:58:58]**
* **NODE_B** [Fault History]: Scheduled FMS Activity Missed Timing Requirement (Code: 6000)
  * *Details:* Serial Number: 273 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6000 | Fault Code: 6000 | Sub Code: Thunderbolt fault | Fault Name: Scheduled FMS Activity Missed Timing Requirement | Date and Time: 2032-06-18 11:58:58 AM | Module Temperature: 37 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 50 | Application Data: Deadline miss` Background service - 4259867;
  * *Citation:* `[Source: NODE_B_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 273 | UUID: 1cb22d12-04bc-4195-b408-8d297ebd1d13]`
* **NODE_B** [Operator Interaction]: Operator Interaction Event
  * *Details:* Dual mode: Single | Master status: Master | Functional position: Captain | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 343.000153 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [FMS Operational Event: no phase change | FMS node source: Standby | Event value: 65540]
  * *Citation:* `[Source: NODE_B_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 24 | UUID: 5b3d56fc-dac6-46ab-940f-b2adee96f35d]`
* **NODE_B** [State Transition]: State Transition: Master status -> Master
  * *Details:* [Master status: Master | Dual mode: Single | Opposite fms ok: Unstable | Other dual fms node position: FMS node right | Standby fms node position: FMS node invalid | Functional position: Captain]
  * *Citation:* `[Source: NODE_B_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 18 | UUID: a3f387b0-c254-4dc3-9aa6-a9cdb29fd690]`
* **NODE_C** [State Transition]: State Transition: Master status -> Spare
  * *Details:* [Master status: Spare | Dual mode: Single | Opposite fms ok: Unstable | Other dual fms node position: FMS node center | Standby fms node position: FMS node invalid | Functional position: First officer]
  * *Citation:* `[Source: NODE_C_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 114 | UUID: 75ea33fc-5c02-4a3b-920f-5385b1f83c16]`

**[11:58:59]**
* **NODE_B** [Fault History] (x2 occurrences collapsed): Scheduled FMS Activity Missed Timing Requirement (Code: 6000)
  * *Details:* Serial Number: 274 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6000 | Fault Code: 6000 | Sub Code: Thunderbolt fault | Fault Name: Scheduled FMS Activity Missed Timing Requirement | Date and Time: 2032-06-18 11:58:59 AM | Module Temperature: 37 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 50 | Application Data: Deadline miss` Background service - 4259858;
  * *Citation:* `[Source: NODE_B_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 274 | UUID: 0515b4c4-1e74-4e31-8465-bdfdf7db6085]`
* **NODE_B** [Fault History]: Oss semaphore failure (Code: 6029)
  * *Details:* Serial Number: 276 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6029 | Fault Code: 6029 | Sub Code: Thunderbolt fault | Fault Name: Oss semaphore failure | Date and Time: 2032-06-18 11:58:59 AM | Module Temperature: 36 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 100 | Application Data: wait semaphore failed in deos 653 - 6 ;
  * *Citation:* `[Source: NODE_B_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 276 | UUID: 63cd0756-f863-48c1-beda-81fbbed717d5]`
* **NODE_B** [Software Event]: Software Event: S pad message identifier l
  * *Details:* Data Identifier: S pad message identifier l | Data Format: Format one unsign 32 | Left FMS node: Spare | Dual: Single | [L message identifier: Please wait]
  * *Citation:* `[Source: NODE_B_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 56 | UUID: 7c4308c6-cbe9-4330-b856-ec4b70c7749c]`
* **NODE_B** [Software Event]: Software Event: S pad message identifier r
  * *Details:* Data Identifier: S pad message identifier r | Data Format: Format one unsign 32 | Left FMS node: Spare | Dual: Single | [R message identifier: Please wait]
  * *Citation:* `[Source: NODE_B_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 57 | UUID: 2780bf29-318b-4ee8-b902-627e1694c7a0]`
* **NODE_B** [State Transition]: State Transition: Master status -> Master
  * *Details:* [Master status: Master | Dual mode: Single | Opposite fms ok: Ok | Other dual fms node position: FMS node right | Standby fms node position: FMS node invalid | Functional position: Captain]
  * *Citation:* `[Source: NODE_B_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 19 | UUID: daa92134-1f4c-453c-a16b-762918762065]`
* **NODE_C** [State Transition]: State Transition: Master status -> Spare
  * *Details:* [Master status: Spare | Dual mode: Single | Opposite fms ok: Ok | Other dual fms node position: FMS node center | Standby fms node position: FMS node invalid | Functional position: First officer]
  * *Citation:* `[Source: NODE_C_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 115 | UUID: 5e746a0c-12f3-41c8-b614-6812922d43f2]`

**[11:59:00]**
* **NODE_B** [Fault History]: Oss semaphore failure (Code: 6029)
  * *Details:* Serial Number: 277 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6029 | Fault Code: 6029 | Sub Code: Thunderbolt fault | Fault Name: Oss semaphore failure | Date and Time: 2032-06-18 11:59:00 AM | Module Temperature: 37 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 100 | Application Data: wait semaphore failed in deos 653 - 6 ;
  * *Citation:* `[Source: NODE_B_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 277 | UUID: 17303e6c-8315-44a2-a65e-bb1d7080d9fa]`

**[11:59:01]**
* **NODE_B** [Fault History]: Oss semaphore failure (Code: 6029)
  * *Details:* Serial Number: 278 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6029 | Fault Code: 6029 | Sub Code: Thunderbolt fault | Fault Name: Oss semaphore failure | Date and Time: 2032-06-18 11:59:01 AM | Module Temperature: 37 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 100 | Application Data: wait semaphore failed in deos 653 - 6 ;
  * *Citation:* `[Source: NODE_B_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 278 | UUID: e1935b24-d39b-476a-9039-f06f322e071c]`

**[11:59:02]**
* **NODE_B** [Fault History]: Oss semaphore failure (Code: 6029)
  * *Details:* Serial Number: 279 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6029 | Fault Code: 6029 | Sub Code: Thunderbolt fault | Fault Name: Oss semaphore failure | Date and Time: 2032-06-18 11:59:02 AM | Module Temperature: 36 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 100 | Application Data: wait semaphore failed in deos 653 - 6 ;
  * *Citation:* `[Source: NODE_B_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 279 | UUID: 9784f594-0c12-47bf-9a61-cef56b532a07]`
* **NODE_B** [Software Event]: Software Event: Master spare identifier
  * *Details:* Data Identifier: Master spare identifier | Data Format: Format fixed str | Center FMS node: Master | Dual: Single | [Event identifier: 68 | FMS node position: Operational master spare Changed]
  * *Citation:* `[Source: NODE_B_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 58 | UUID: 131ee2c5-428a-4ed6-9c78-f6aac92b4c89]`

**[11:59:03]**
* **NODE_B** [Fault History]: Oss semaphore failure (Code: 6029)
  * *Details:* Serial Number: 280 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6029 | Fault Code: 6029 | Sub Code: Thunderbolt fault | Fault Name: Oss semaphore failure | Date and Time: 2032-06-18 11:59:03 AM | Module Temperature: 37 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 100 | Application Data: wait semaphore failed in deos 653 - 6 ;
  * *Citation:* `[Source: NODE_B_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 280 | UUID: 29fddcd9-f13f-4b56-bc90-d7fc1de1ff3e]`
* **NODE_C** [Software Event]: Software Event: Master spare identifier
  * *Details:* Data Identifier: Master spare identifier | Data Format: Format fixed str | Center FMS node: Master | Right FMS node: Spare | Dual: Single | [Event identifier: 68 | FMS node position: Operational master spare Changed]
  * *Citation:* `[Source: NODE_C_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 291 | UUID: 7dfbaa1a-00ee-43a4-98c7-a52d588ed3e1]`

**[11:59:04]**
* **NODE_B** [Fault History]: Scheduled FMS Activity Missed Timing Requirement (Code: 6000)
  * *Details:* Serial Number: 281 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6000 | Fault Code: 6000 | Sub Code: Thunderbolt fault | Fault Name: Scheduled FMS Activity Missed Timing Requirement | Date and Time: 2032-06-18 11:59:04 AM | Module Temperature: 37 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 50 | Application Data: Deadline miss` Background service - 4259866;
  * *Citation:* `[Source: NODE_B_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 281 | UUID: 98fc868f-99b3-440d-855f-fb80b681c957]`
* **NODE_B** [Fault History]: Oss semaphore failure (Code: 6029)
  * *Details:* Serial Number: 282 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6029 | Fault Code: 6029 | Sub Code: Thunderbolt fault | Fault Name: Oss semaphore failure | Date and Time: 2032-06-18 11:59:04 AM | Module Temperature: 36 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 100 | Application Data: wait semaphore failed in deos 653 - 6 ;
  * *Citation:* `[Source: NODE_B_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 282 | UUID: 0459d6ed-6411-4173-8a7d-03fddfeec779]`

**[11:59:05]**
* **NODE_B** [Fault History]: Oss semaphore failure (Code: 6029)
  * *Details:* Serial Number: 283 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6029 | Fault Code: 6029 | Sub Code: Thunderbolt fault | Fault Name: Oss semaphore failure | Date and Time: 2032-06-18 11:59:05 AM | Module Temperature: 37 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 100 | Application Data: wait semaphore failed in deos 653 - 6 ;
  * *Citation:* `[Source: NODE_B_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 283 | UUID: e8985a71-a00a-42f1-8242-85bfc2516d1f]`

**[11:59:06]**
* **NODE_B** [Operator Interaction]: Operator Interaction Event
  * *Details:* Dual mode: Dual | Master status: Master | Functional position: Captain | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 343.002319 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [Fault/Event: Cold Start Due To A Re-Synch On The Receiver]
  * *Citation:* `[Source: NODE_B_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 25 | UUID: c9045f3a-70d1-4f6d-8c0c-04cbca6822fc]`

**[11:59:07]**
* **NODE_C** [State Transition]: State Transition: Master status -> Spare
  * *Details:* [Master status: Spare | Dual mode: Single | Opposite fms ok: Unstable | Other dual fms node position: FMS node center | Standby fms node position: FMS node invalid | Functional position: First officer]
  * *Citation:* `[Source: NODE_C_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 116 | UUID: bbf9c547-040b-41c3-89a6-2ef937d70bba]`

**[11:59:08]**
* **NODE_C** [State Transition]: State Transition: Master status -> Spare
  * *Details:* [Master status: Spare | Dual mode: Single | Opposite fms ok: Not ok | Other dual fms node position: FMS node center | Standby fms node position: FMS node invalid | Functional position: First officer]
  * *Citation:* `[Source: NODE_C_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 117 | UUID: ea8f29bd-99f8-49f9-9cb8-c2040c9dce3d]`

**[11:59:16]**
* **NODE_C** [State Transition]: State Transition: Master status -> Master
  * *Details:* [Master status: Master | Dual mode: Single | Opposite fms ok: Not ok | Other dual fms node position: FMS node center | Standby fms node position: FMS node invalid | Functional position: First officer]
  * *Citation:* `[Source: NODE_C_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 118 | UUID: 58589037-ba5f-4093-b399-859d17586d94]`

**[11:59:22]**
* **NODE_C** [Software Event]: Software Event: Master spare identifier
  * *Details:* Data Identifier: Master spare identifier | Data Format: Format fixed str | Right FMS node: Master | Dual: Single | [Event identifier: 68 | FMS node position: Operational master spare Changed]
  * *Citation:* `[Source: NODE_C_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 292 | UUID: 43e64f54-4f74-4a5d-8770-1da7f85a0ee2]`

**[11:59:34]**
* **NODE_A** [Fault History] (x2 occurrences collapsed): Background Service Identity Failure (Code: 6025)
  * *Details:* Serial Number: 428 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6025 | Fault Code: 6025 | Sub Code: Thunderbolt fault | Fault Name: Background Service Identity Failure | Date and Time: 2032-06-18 11:59:34 AM | Module Temperature: 39 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Initializing | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 35 | Application Data: get current process id failure 653;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 428 | UUID: cec44666-e854-4b43-a052-b0dbaa26057b]`

**[11:59:35]**
* **NODE_A** [Fault History] (x2 occurrences collapsed): Background Service Identity Failure (Code: 6025)
  * *Details:* Serial Number: 430 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6025 | Fault Code: 6025 | Sub Code: Thunderbolt fault | Fault Name: Background Service Identity Failure | Date and Time: 2032-06-18 11:59:35 AM | Module Temperature: 41 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Initializing | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 35 | Application Data: get current process id failure 653;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 430 | UUID: 005e36f0-6af2-4d12-a765-19baadb4d052]`
* **NODE_A** [Fault History]: Oss loading failure (Code: 6052)
  * *Details:* Serial Number: 432 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6052 | Fault Code: 6052 | Sub Code: Thunderbolt fault | Fault Name: Oss loading failure | Date and Time: 2032-06-18 11:59:35 AM | Module Temperature: 41 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Initializing | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 100 | Application Data: Failed to load library in Deos 653 - Libpssl dtf manager so.so 11 11;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 432 | UUID: 1ed0b269-3419-4133-ac69-8fe7b4f268f6]`
* **NODE_A** [Fault History] (x2 occurrences collapsed): Background Service Identity Failure (Code: 6025)
  * *Details:* Serial Number: 433 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6025 | Fault Code: 6025 | Sub Code: Thunderbolt fault | Fault Name: Background Service Identity Failure | Date and Time: 2032-06-18 11:59:35 AM | Module Temperature: 40 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Initializing | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 35 | Application Data: get current process id failure 653;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 433 | UUID: a5a10a99-8a13-43ba-b6dd-6b8eae7d10e0]`

**[11:59:36]**
* **NODE_A** [Operator Interaction]: Operator Interaction Event
  * *Details:* Dual mode: Dual | Master status: Master | Functional position: Captain | Calibrated airspeed data: 30.000000 | Message: No displayable fields
  * *Citation:* `[Source: NODE_A_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 8 | UUID: 313b05e3-36b3-4348-b798-22914f9e9790]`

**[11:59:37]**
* **NODE_A** [Fault History] (x8 occurrences collapsed): Oss bind failure (Code: 6035)
  * *Details:* Serial Number: 435 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6035 | Fault Code: 6035 | Sub Code: Thunderbolt fault | Fault Name: Oss bind failure | Date and Time: 2032-06-18 11:59:37 AM | Module Temperature: 40 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Ready | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 100 | Application Data: Client Cb not found in deos 653 - -933180756;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 435 | UUID: b1646fe0-1c5d-4884-9556-eff611fe1c1d]`
* **NODE_A** [Fault History] (x6 occurrences collapsed): Oss task client failure (Code: 6024)
  * *Details:* Serial Number: 443 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6024 | Fault Code: 6024 | Sub Code: Thunderbolt fault | Fault Name: Oss task client failure | Date and Time: 2032-06-18 11:59:37 AM | Module Temperature: 40 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Ready | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 22 | Application Data: Task Client not found;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 443 | UUID: c3f8fbf7-d3e4-4c7a-85e0-d904c03d9088]`
* **NODE_A** [Operator Interaction]: Operator Interaction Event
  * *Details:* Dual mode: Dual | Master status: Master | Functional position: Captain | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 342.999634 | Magnetic track: 66.049805 | [FMS Operational Event: redisplay | FMS node source: Standby]
  * *Citation:* `[Source: NODE_A_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 9 | UUID: e9811ca4-1fa4-4beb-96d8-b1fb6467f921]`
* **NODE_A** [Software Event]: Software Event: Operational startup mode identifier
  * *Details:* Data Identifier: Operational startup mode identifier | Data Format: Format fixed str | Left FMS node: Spare | Dual: Dual | [Event identifier: 68 | Operational startup mode: Operational startup cold]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 7 | UUID: 498aaaf9-0403-4816-bfe8-f9f8da1009ab]`
* **NODE_A** [Software Event]: Software Event: Operational powerup identifier
  * *Details:* Data Identifier: Operational powerup identifier | Data Format: Format fixed str | Left FMS node: Spare | Dual: Dual | [Event identifier: 68 | Operational powerup: Operational powerup normal]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 8 | UUID: c990d703-febf-4d0c-a51e-629f41ab681b]`
* **NODE_A** [State Transition]: State Transition: Master status -> Master
  * *Details:* [Master status: Master | Dual mode: Dual | Opposite fms ok: Unknown | Other dual fms node position: FMS node right | Standby fms node position: FMS node invalid | Functional position: Captain]
  * *Citation:* `[Source: NODE_A_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 8 | UUID: acf3091d-5acd-4f3f-a2cf-ce0e67c7ef65]`
* **NODE_C** [Operator Interaction]: Operator Interaction Event
  * *Details:* Dual mode: Single | Master status: Spare | Functional position: First officer | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 342.999420 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [FMS Operational Event: redisplay | FMS node source: Captain | Event value: 131072]
  * *Citation:* `[Source: NODE_C_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 746 | UUID: 02f931f1-053e-49cc-aa74-4702899418e3]`
* **NODE_C** [State Transition]: State Transition: Master status -> Spare
  * *Details:* [Master status: Spare | Dual mode: Single | Opposite fms ok: Not ok | Other dual fms node position: FMS node left | Standby fms node position: FMS node invalid | Functional position: First officer]
  * *Citation:* `[Source: NODE_C_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 119 | UUID: c642cd4d-0d76-42e0-baae-a17fc6fc1211]`

**[11:59:38]**
* **NODE_A** [Fault History]: Oss semaphore failure (Code: 6029)
  * *Details:* Serial Number: 449 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6029 | Fault Code: 6029 | Sub Code: Thunderbolt fault | Fault Name: Oss semaphore failure | Date and Time: 2032-06-18 11:59:38 AM | Module Temperature: 40 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 100 | Application Data: wait semaphore failed in deos 653 - 6 ;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 449 | UUID: a123dacf-36ec-4b8f-af82-903dc0516544]`
* **NODE_A** [State Transition]: State Transition: Master status -> Master
  * *Details:* [Master status: Master | Dual mode: Dual | Opposite fms ok: Unstable | Other dual fms node position: FMS node right | Standby fms node position: FMS node invalid | Functional position: Captain]
  * *Citation:* `[Source: NODE_A_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 9 | UUID: b5361eaa-f635-4800-9578-891a94f13ee8]`
* **NODE_C** [State Transition]: State Transition: Master status -> Spare
  * *Details:* [Master status: Spare | Dual mode: Single | Opposite fms ok: Unstable | Other dual fms node position: FMS node left | Standby fms node position: FMS node invalid | Functional position: First officer]
  * *Citation:* `[Source: NODE_C_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 120 | UUID: e8684684-7bf7-4687-9e35-ebb081137693]`

**[11:59:39]**
* **NODE_A** [Fault History]: Oss task client failure (Code: 6024)
  * *Details:* Serial Number: 450 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6024 | Fault Code: 6024 | Sub Code: Thunderbolt fault | Fault Name: Oss task client failure | Date and Time: 2032-06-18 11:59:39 AM | Module Temperature: 40 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 22 | Application Data: Task Client not found;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 450 | UUID: b7bc57aa-4f37-4a26-90b6-bb3827c14c12]`
* **NODE_A** [Fault History]: Oss semaphore failure (Code: 6029)
  * *Details:* Serial Number: 451 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6029 | Fault Code: 6029 | Sub Code: Thunderbolt fault | Fault Name: Oss semaphore failure | Date and Time: 2032-06-18 11:59:39 AM | Module Temperature: 40 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 100 | Application Data: wait semaphore failed in deos 653 - 6 ;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 451 | UUID: 21f2c8d7-e240-4220-8d3c-4db407987561]`
* **NODE_A** [Fault History] (x3 occurrences collapsed): Scheduled FMS Activity Missed Timing Requirement (Code: 6000)
  * *Details:* Serial Number: 452 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6000 | Fault Code: 6000 | Sub Code: Thunderbolt fault | Fault Name: Scheduled FMS Activity Missed Timing Requirement | Date and Time: 2032-06-18 11:59:39 AM | Module Temperature: 39 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 50 | Application Data: Deadline miss` Background service - 1114128;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 452 | UUID: 4387045e-e782-4858-8d6a-b780aaf4f6ca]`
* **NODE_A** [Software Event]: Software Event: S pad message identifier l
  * *Details:* Data Identifier: S pad message identifier l | Data Format: Format one unsign 32 | Left FMS node: Spare | Dual: Dual | [L message identifier: Please wait]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 9 | UUID: 1084694b-e749-40de-a757-46ec53fd2033]`
* **NODE_A** [Software Event]: Software Event: S pad message identifier r
  * *Details:* Data Identifier: S pad message identifier r | Data Format: Format one unsign 32 | Left FMS node: Spare | Dual: Dual | [R message identifier: Please wait]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 10 | UUID: 21577337-66ff-468d-9a8c-0b4c3dd86521]`
* **NODE_A** [State Transition]: State Transition: Master status -> Master
  * *Details:* [Master status: Master | Dual mode: Dual | Opposite fms ok: Ok | Other dual fms node position: FMS node right | Standby fms node position: FMS node invalid | Functional position: Captain]
  * *Citation:* `[Source: NODE_A_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 10 | UUID: c9aa64fe-23cf-4ad1-9cb7-8c3fb3da6e57]`
* **NODE_C** [State Transition]: State Transition: Master status -> Spare
  * *Details:* [Master status: Spare | Dual mode: Single | Opposite fms ok: Ok | Other dual fms node position: FMS node left | Standby fms node position: FMS node invalid | Functional position: First officer]
  * *Citation:* `[Source: NODE_C_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 121 | UUID: f5197a5d-c9fe-40ad-b4a8-b79a96cf1310]`

**[11:59:40]**
* **NODE_A** [Fault History]: Scheduled FMS Activity Missed Timing Requirement (Code: 6000)
  * *Details:* Serial Number: 455 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6000 | Fault Code: 6000 | Sub Code: Thunderbolt fault | Fault Name: Scheduled FMS Activity Missed Timing Requirement | Date and Time: 2032-06-18 11:59:40 AM | Module Temperature: 40 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 50 | Application Data: Deadline miss` Background service - 1114138;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 455 | UUID: ec59f95e-d63a-40db-8764-129f8e29bb9c]`

**[11:59:43]**
* **NODE_A** [Software Event]: Software Event: Master spare identifier
  * *Details:* Data Identifier: Master spare identifier | Data Format: Format fixed str | Left FMS node: Master | Right FMS node: Spare | Dual: Dual | [Event identifier: 68 | FMS node position: Operational master spare Changed]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 11 | UUID: f8cf7749-7d07-40e9-a9a2-2428aaa59963]`
* **NODE_C** [Software Event]: Software Event: Master spare identifier
  * *Details:* Data Identifier: Master spare identifier | Data Format: Format fixed str | Left FMS node: Master | Right FMS node: Spare | Dual: Single | [Event identifier: 68 | FMS node position: Operational master spare Changed]
  * *Citation:* `[Source: NODE_C_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 293 | UUID: 468b2ec7-b7fc-4b50-82aa-066fb240f511]`

**[11:59:44]**
* **NODE_C** [Operator Interaction]: Operator Interaction Event
  * *Details:* Dual mode: Dual | Master status: Spare | Functional position: First officer | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 343.000458 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [Fault/Event: Cold Start Due To A Re-Synch On The Receiver]
  * *Citation:* `[Source: NODE_C_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 747 | UUID: 397e832b-12d5-4fe0-9f36-1e2979219ab5]`

**[11:59:45]**
* **NODE_C** [Fault History]: Na (Code: 0)
  * *Details:* Serial Number: 243 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Sub Code: Thunderbolt fault | Fault Name: Na | Date and Time: 2032-06-18 11:59:45 AM | Current Recovery Type: No Recovery Action | Module State: Ms unequipped e | Context State: Cs not equipped e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: Power Loss | Fault Exception: False | Extended Record: False | Application Data: ;
  * *Citation:* `[Source: NODE_C_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 243 | UUID: a3e3569b-dbe6-4a8e-88da-ee916e9f6575]`

**[11:59:46]**
* **NODE_A** [State Transition]: State Transition: Master status -> Master
  * *Details:* [Master status: Master | Dual mode: Dual | Opposite fms ok: Unstable | Other dual fms node position: FMS node right | Standby fms node position: FMS node invalid | Functional position: Captain]
  * *Citation:* `[Source: NODE_A_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 11 | UUID: e3e21e36-1e09-433c-85cf-ec9c0b0ebe73]`

**[11:59:47]**
* **NODE_A** [Fault History]: Application error (Code: 6001)
  * *Details:* Serial Number: 456 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6001 | Fault Code: 6001 | Sub Code: Thunderbolt fault | Fault Name: Application error | Date and Time: 2032-06-18 11:59:47 AM | Module Temperature: 39 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: Fr context shutdown e | Module State: Operational | Context State: Cs fault recovery e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: True | Extended Record: True | Application Data Size: 372 | Application Data: @x};P?;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 456 | UUID: 06933891-63b4-435d-a300-788c36177b4a]`
* **NODE_A** [State Transition]: State Transition: Master status -> Master
  * *Details:* [Master status: Master | Dual mode: Dual | Opposite fms ok: Not ok | Other dual fms node position: FMS node right | Standby fms node position: FMS node invalid | Functional position: Captain]
  * *Citation:* `[Source: NODE_A_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 12 | UUID: 47e4834f-df88-46f5-a2e5-274d748ec6b1]`

**[11:59:48]**
* **NODE_A** [Fault History] (x2 occurrences collapsed): Application error (Code: 6001)
  * *Details:* Serial Number: 457 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6001 | Fault Code: 6001 | Sub Code: Thunderbolt fault | Fault Name: Application error | Date and Time: 2032-06-18 11:59:48 AM | Module Temperature: 39 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: Fr context shutdown e | Module State: Operational | Context State: Cs fault recovery e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: True | Extended Record: True | Application Data Size: 192 | Application Data: @x};
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 457 | UUID: 19ba97bc-7890-4ed5-b716-1f94eb91420d]`

**[12:00:17]**
* **NODE_B** [Fault History]: Oss loading failure (Code: 6052)
  * *Details:* Serial Number: 284 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6052 | Fault Code: 6052 | Sub Code: Thunderbolt fault | Fault Name: Oss loading failure | Date and Time: 2032-06-18 12:00:17 PM | Module Temperature: 36 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Initializing | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 100 | Application Data: Failed to load library in Deos 653 - Libpssl dtf manager so.so 11 11;
  * *Citation:* `[Source: NODE_B_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 284 | UUID: 6a03823a-e7d7-46d2-a7d7-e897c57af78f]`

**[12:00:18]**
* **NODE_B** [Operator Interaction]: Operator Interaction Event
  * *Details:* Dual mode: Dual | Master status: Master | Functional position: Captain | Calibrated airspeed data: 30.000000 | Message: No displayable fields
  * *Citation:* `[Source: NODE_B_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 26 | UUID: 8794b807-22dc-4c32-b1fa-89326026950e]`

**[12:00:19]**
* **NODE_B** [Operator Interaction]: Operator Interaction Event
  * *Details:* Dual mode: Dual | Master status: Master | Functional position: Captain | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 343.003113 | Magnetic track: 66.049805 | [FMS Operational Event: redisplay | FMS node source: Standby]
  * *Citation:* `[Source: NODE_B_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 27 | UUID: 223cc910-0a5d-44e4-b731-d4b4f40d448b]`
* **NODE_B** [Software Event]: Software Event: Operational startup mode identifier
  * *Details:* Data Identifier: Operational startup mode identifier | Data Format: Format fixed str | Left FMS node: Spare | Dual: Dual | [Event identifier: 68 | Operational startup mode: Operational startup cold]
  * *Citation:* `[Source: NODE_B_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 59 | UUID: 7b01c5ad-734f-4807-bce8-4a507eeaea24]`
* **NODE_B** [Software Event]: Software Event: Operational powerup identifier
  * *Details:* Data Identifier: Operational powerup identifier | Data Format: Format fixed str | Left FMS node: Spare | Dual: Dual | [Event identifier: 68 | Operational powerup: Operational powerup normal]
  * *Citation:* `[Source: NODE_B_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 60 | UUID: 47a5cff9-5334-4a2a-8131-f8e1cb5f1b1c]`
* **NODE_B** [State Transition]: State Transition: Master status -> Master
  * *Details:* [Master status: Master | Dual mode: Dual | Opposite fms ok: Unknown | Other dual fms node position: FMS node right | Standby fms node position: FMS node invalid | Functional position: Captain]
  * *Citation:* `[Source: NODE_B_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 20 | UUID: 8b0aa447-f1fb-4efc-a1be-fc5e415905fc]`

**[12:00:20]**
* **NODE_B** [Fault History]: Oss semaphore failure (Code: 6029)
  * *Details:* Serial Number: 285 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6029 | Fault Code: 6029 | Sub Code: Thunderbolt fault | Fault Name: Oss semaphore failure | Date and Time: 2032-06-18 12:00:20 PM | Module Temperature: 37 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 100 | Application Data: wait semaphore failed in deos 653 - 6 ;
  * *Citation:* `[Source: NODE_B_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 285 | UUID: 950fa78e-9830-4cff-ac8d-129ae26047d2]`
* **NODE_B** [State Transition]: State Transition: Master status -> Master
  * *Details:* [Master status: Master | Dual mode: Dual | Opposite fms ok: Not ok | Other dual fms node position: FMS node right | Standby fms node position: FMS node invalid | Functional position: Captain]
  * *Citation:* `[Source: NODE_B_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 21 | UUID: 00e84385-645c-4747-959f-1e2a540a1d95]`

**[12:00:21]**
* **NODE_B** [Fault History]: Scheduled FMS Activity Missed Timing Requirement (Code: 6000)
  * *Details:* Serial Number: 286 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6000 | Fault Code: 6000 | Sub Code: Thunderbolt fault | Fault Name: Scheduled FMS Activity Missed Timing Requirement | Date and Time: 2032-06-18 12:00:21 PM | Module Temperature: 37 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 50 | Application Data: Deadline miss` Background service - 5308442;
  * *Citation:* `[Source: NODE_B_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 286 | UUID: fd339ce9-c40c-4a32-9dd1-c0c55797006b]`

**[12:00:23]**
* **NODE_B** [Software Event]: Software Event: Data link comm master identifier
  * *Details:* Data Identifier: Data link comm master identifier | Data Format: Format fixed str | Left FMS node: Spare | Dual: Dual | [Event identifier: 68 | Data link comm master status log: Data link comm slave to master]
  * *Citation:* `[Source: NODE_B_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 61 | UUID: b0f0678c-5ce1-4596-bb96-858f800b4d8f]`

**[12:00:24]**
* **NODE_B** [Software Event]: Software Event: Master spare identifier
  * *Details:* Data Identifier: Master spare identifier | Data Format: Format fixed str | Center FMS node: Master | Right FMS node: Spare | Dual: Dual | [Event identifier: 68 | FMS node position: Operational master spare Changed]
  * *Citation:* `[Source: NODE_B_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 62 | UUID: 1c12e4f8-a1de-4078-91a1-d98361f03b16]`

**[12:00:27]**
* **NODE_B** [Operator Interaction] (x4 occurrences collapsed): Operator Interaction Event
  * *Details:* Dual mode: Single | Master status: Master | Functional position: Captain | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 343.002716 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [FMS Operational Event: clear altitude | FMS node source: Standby | Event value: 65536]
  * *Citation:* `[Source: NODE_B_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 28 | UUID: 8c77aba5-8811-4695-91d5-705e77c69f89]`
* **NODE_B** [Software Event]: Software Event: Dual mode identifier
  * *Details:* Data Identifier: Dual mode identifier | Data Format: Format fixed str | Center FMS node: Master | Right FMS node: Spare | Dual: Single | [Event identifier: 68 | Operational dual mode: Operational dual mode Changed]
  * *Citation:* `[Source: NODE_B_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 63 | UUID: c855a25a-8204-4329-9a17-a046d51c7b92]`
* **NODE_B** [State Transition]: State Transition: Master status -> Master
  * *Details:* [Master status: Master | Dual mode: Single | Opposite fms ok: Not ok | Other dual fms node position: FMS node right | Standby fms node position: FMS node invalid | Functional position: Captain]
  * *Citation:* `[Source: NODE_B_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 22 | UUID: 4414de3f-2f81-4bff-a3b4-90d1e56098b9]`

**[12:00:28]**
* **NODE_B** [Fault History] (x2 occurrences collapsed): Scheduled FMS Activity Missed Timing Requirement (Code: 6000)
  * *Details:* Serial Number: 287 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6000 | Fault Code: 6000 | Sub Code: Thunderbolt fault | Fault Name: Scheduled FMS Activity Missed Timing Requirement | Date and Time: 2032-06-18 12:00:28 PM | Module Temperature: 37 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 50 | Application Data: Deadline miss` Background service - 5308434;
  * *Citation:* `[Source: NODE_B_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 287 | UUID: d89353d0-407b-4e61-a38c-4f3fff7fe83c]`
* **NODE_B** [Operator Interaction] (x2 occurrences collapsed): Operator Interaction Event
  * *Details:* Dual mode: Single | Master status: Master | Functional position: Captain | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 343.002563 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [FMS Operational Event: clear altitude | FMS node source: Standby | Event value: 65540]
  * *Citation:* `[Source: NODE_B_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 32 | UUID: d426732f-3407-4abb-bf62-d774d8d62258]`

**[12:00:29]**
* **NODE_B** [Operator Interaction]: Operator Interaction Event
  * *Details:* Dual mode: Single | Master status: Master | Functional position: Captain | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 343.002411 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [FMS Operational Event: no phase change | FMS node source: Standby | Event value: 65540]
  * *Citation:* `[Source: NODE_B_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 34 | UUID: 09477934-2fc1-4b48-b73e-2a778c553def]`

**[12:00:30]**
* **NODE_B** [Fault History] (x2 occurrences collapsed): Scheduled FMS Activity Missed Timing Requirement (Code: 6000)
  * *Details:* Serial Number: 289 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6000 | Fault Code: 6000 | Sub Code: Thunderbolt fault | Fault Name: Scheduled FMS Activity Missed Timing Requirement | Date and Time: 2032-06-18 12:00:30 PM | Module Temperature: 36 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 50 | Application Data: Deadline miss` Background service - 5308441;
  * *Citation:* `[Source: NODE_B_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 289 | UUID: 8a9248f6-fb2d-4751-ad56-b13504e7d482]`

**[12:00:32]**
* **NODE_B** [Software Event]: Software Event: Master spare identifier
  * *Details:* Data Identifier: Master spare identifier | Data Format: Format fixed str | Center FMS node: Master | Dual: Single | [Event identifier: 68 | FMS node position: Operational master spare Changed]
  * *Citation:* `[Source: NODE_B_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 64 | UUID: 908c0997-e96b-4484-8d00-c8afa84867c4]`

**[12:00:33]**
* **NODE_B** [Software Event]: Software Event: S pad message identifier l
  * *Details:* Data Identifier: S pad message identifier l | Data Format: Format one unsign 32 | Center FMS node: Master | Dual: Single | [L message identifier: Navigation primary lost]
  * *Citation:* `[Source: NODE_B_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 65 | UUID: 19d134f3-7644-41f3-917a-0f994a088f6c]`
* **NODE_B** [Software Event]: Software Event: S pad message identifier r
  * *Details:* Data Identifier: S pad message identifier r | Data Format: Format one unsign 32 | Center FMS node: Master | Dual: Single | [R message identifier: Navigation primary lost]
  * *Citation:* `[Source: NODE_B_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 66 | UUID: e47057be-3f89-4344-9040-0939918dfe8b]`

**[12:00:38]**
* **NODE_B** [Software Event]: Software Event: S pad message identifier l
  * *Details:* Data Identifier: S pad message identifier l | Data Format: Format one unsign 32 | Center FMS node: Master | Dual: Single | [L message identifier: Navigation primary]
  * *Citation:* `[Source: NODE_B_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 67 | UUID: ce583a12-9382-498d-8b86-b5711c99dfa8]`
* **NODE_B** [Software Event]: Software Event: S pad message identifier r
  * *Details:* Data Identifier: S pad message identifier r | Data Format: Format one unsign 32 | Center FMS node: Master | Dual: Single | [R message identifier: Navigation primary]
  * *Citation:* `[Source: NODE_B_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 68 | UUID: 5d58eecc-ad1a-40cf-9a95-5d2f24b3fd68]`

**[12:00:39]**
* **NODE_B** [Fault History]: Navigation Data Coordination Activity Failure (Code: 11)
  * *Details:* Serial Number: 291 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 12925 | Fault Code: 11 | Sub Code: 109 | Fault Name: Navigation Data Coordination Activity Failure | Date and Time: 2032-06-18 12:00:39 PM | Module Temperature: 37 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 8 | Application Data: ?~J;
  * *Citation:* `[Source: NODE_B_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 291 | UUID: 1b28db4b-014a-44f4-a0ca-c600a53d6f5a]`
* **NODE_B** [Software Event]: Software Event: Opc configuration data identifier
  * *Details:* Data Identifier: Opc configuration data identifier | Data Format: Format opc configuration data | Center FMS node: Master | Dual: Single | [Identifier: Configuration data | Performance custo 3: False | Performance custo 2: False | Performance custo 1: False | Operational data link datalink: True | Air traffic service enable: True | Kilogram enable: True | Metric enable: True | Display trajectory: 1 | Grid mora enable: True | I4d rta enable: False | Radio navigation 2 installed: True | Aim disable: True | No radio navigation on board: False | Passenger count enable: True | Fls enable: True | To securization enable: True | No ap fd mda mdh disconnect: True | To derate enable: True | Climb derate enable: False | Fnl des enable: True | Cda enable: 1 | Cpdb opc enable: False | Vor2 dme2 on board: True | Rnp function enable: True | Leg sequencing monitoring enable: True | Resync check enable: True | To securization 2 enable: True | Sbas enable: True | Sls enable: True | Jfgw display on mfd enable: True | Acr 2 on board: False | Vertical display enable: True | FMS trjctry on vd enable: True | Mora on vd enable: True | Msa on vd enable: True | Etoc enable: True | Freeze scale on vd enable: False | Fls axis on vd enable: True | Aess twsf trjctry enable: True | Auto derate climb enable: True | Polar navigation enabled: True | Back beam approach en: True | FMS platform type 1: True | FMS platform type 2: True | FMS platform type 3: False | FMS platform type 4: False | FMS engine manuf 1: False | FMS engine manuf 2: True | FMS engine manuf 3: False | FMS engine type 1: False | FMS engine type 2: True | FMS engine type 3: False | FMS engine type 4: False | FMS engine type 5: False | Takeoff rnp: 1.000000 | Gps approach rnp: 0.300000 | Precision approach rnp: 0.500000 | Nonprecision approach rnp: 0.500000 | Terminal rnp: 1.000000 | Enroute rnp: 2.000000 | Oceanic rnp: 2.000000 | Takeoff tla: 110.991997 | Takeoff hal: 1.000000 | Approach hal: 0.300000 | Terminal hal: 1.000000 | Enroute hal: 2.000000 | Oceanic hal: 2.000000 | Tail number 32: .F-Wzht | Tail number 16: Zht | Tail number 8: T | Configuration data version: [Redacted Payload] | Opc integrity validation: 61]
  * *Citation:* `[Source: NODE_B_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 69 | UUID: 22288f33-b7f0-47c1-bc3e-d46fd2c6bb07]`
* **NODE_B** [Software Event]: Software Event: Sys status identifier
  * *Details:* Data Identifier: Sys status identifier | Data Format: Format sys status | Center FMS node: Master | Dual: Single | [Identifier: Sys | Platform family: A350 | Air frame ident: A350 | FMS node physical position: Center | Engine ident: Trent | Engine manufact: 2 | Opsys pn: Hnp5dxcl01xea01 | Ndb pn: Abv2601l01 | Ami database pn: Hnp40 | Database Reference: [Removed]: Hnp56xcd06xha08 | Cpdb pn: Not loaded]
  * *Citation:* `[Source: NODE_B_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 70 | UUID: 8e2bab45-f69f-43f9-8899-1451d66f49c0]`

**[12:00:55]**
* **NODE_C** [Fault History]: Oss loading failure (Code: 6052)
  * *Details:* Serial Number: 244 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6052 | Fault Code: 6052 | Sub Code: Thunderbolt fault | Fault Name: Oss loading failure | Date and Time: 2032-06-18 12:00:55 PM | Module Temperature: 38 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Initializing | Last Context Reset Count: 5 | Last Context Reset Reason: Fr context shutdown e | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 100 | Application Data: Failed to load library in Deos 653 - Libpssl dtf manager so.so 11 11;
  * *Citation:* `[Source: NODE_C_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 244 | UUID: 84bea0af-868f-4783-ab47-13fe85b490b4]`

**[12:00:56]**
* **NODE_C** [Operator Interaction]: Operator Interaction Event
  * *Details:* Dual mode: Dual | Master status: Spare | Functional position: First officer | Calibrated airspeed data: 30.000000 | Message: No displayable fields
  * *Citation:* `[Source: NODE_C_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 748 | UUID: 9b32447b-7b68-48b1-9546-d1533b807b68]`

**[12:00:57]**
* **NODE_C** [Software Event]: Software Event: Operational startup mode identifier
  * *Details:* Data Identifier: Operational startup mode identifier | Data Format: Format fixed str | Left FMS node: Spare | Dual: Dual | [Event identifier: 68 | Operational startup mode: Operational startup cold]
  * *Citation:* `[Source: NODE_C_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 294 | UUID: 5cc0f7f1-1559-405d-9ac1-eed1b777fc20]`
* **NODE_C** [Software Event]: Software Event: Operational powerup identifier
  * *Details:* Data Identifier: Operational powerup identifier | Data Format: Format fixed str | Left FMS node: Spare | Dual: Dual | [Event identifier: 68 | Operational powerup: Operational powerup normal]
  * *Citation:* `[Source: NODE_C_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 295 | UUID: deea4a24-53b2-4fb2-ba78-bd33542ed3a3]`
* **NODE_C** [State Transition]: State Transition: Master status -> Spare
  * *Details:* [Master status: Spare | Dual mode: Dual | Opposite fms ok: Unknown | Other dual fms node position: FMS node left | Standby fms node position: FMS node invalid | Functional position: First officer]
  * *Citation:* `[Source: NODE_C_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 122 | UUID: e02da6f6-a0de-46b2-b8dc-475d2866f47a]`

**[12:00:58]**
* **NODE_C** [Software Event]: Software Event: Dual mode identifier
  * *Details:* Data Identifier: Dual mode identifier | Data Format: Format fixed str | Left FMS node: Spare | Dual: Single | [Event identifier: 68 | Operational dual mode: Operational dual mode Changed]
  * *Citation:* `[Source: NODE_C_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 296 | UUID: 8645da7c-d5ef-48ab-8713-f287d3d5076f]`
* **NODE_C** [State Transition] (x2 occurrences collapsed): State Transition: Master status -> Spare
  * *Details:* [Master status: Spare | Dual mode: Single | Opposite fms ok: Unknown | Other dual fms node position: FMS node center | Standby fms node position: FMS node invalid | Functional position: First officer]
  * *Citation:* `[Source: NODE_C_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 123 | UUID: 9dab38b5-c2ff-4e39-88ba-203525ca301e]`

**[12:00:59]**
* **NODE_A** [Fault History]: Oss loading failure (Code: 6052)
  * *Details:* Serial Number: 459 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6052 | Fault Code: 6052 | Sub Code: Thunderbolt fault | Fault Name: Oss loading failure | Date and Time: 2032-06-18 12:00:59 PM | Module Temperature: 40 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Initializing | Last Context Reset Reason: Fr context shutdown e | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 100 | Application Data: Failed to load library in Deos 653 - Libpssl dtf manager so.so 11 11;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 459 | UUID: 0ff49ae1-bcea-45d8-bded-aa09404b95f0]`
* **NODE_A** [Fault History]: Cpdb opc not not enabled (Code: 6)
  * *Details:* Serial Number: 460 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 11643 | Fault Code: 6 | Sub Code: 107 | Fault Name: Cpdb opc not not enabled | Date and Time: 2032-06-18 12:00:59 PM | Module Temperature: 39 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Initializing | Last Context Reset Reason: Fr context shutdown e | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 8 | Application Data: ?~J;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 460 | UUID: d0972d1d-76a9-4aa4-971f-381e3b279a67]`
* **NODE_A** [Operator Interaction]: Operator Interaction Event
  * *Details:* Dual mode: Single | Master status: Master | Functional position: Captain | Calibrated airspeed data: 30.000000 | Message: No displayable fields
  * *Citation:* `[Source: NODE_A_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 10 | UUID: b4668375-7ba2-4123-bb8a-0ad510e76fe6]`
* **NODE_B** [Fault History]: Scheduled FMS Activity Missed Timing Requirement (Code: 6000)
  * *Details:* Serial Number: 292 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6000 | Fault Code: 6000 | Sub Code: Thunderbolt fault | Fault Name: Scheduled FMS Activity Missed Timing Requirement | Date and Time: 2032-06-18 12:00:59 PM | Module Temperature: 36 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 50 | Application Data: Deadline miss` Background service - 5308432;
  * *Citation:* `[Source: NODE_B_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 292 | UUID: 7e6e7b25-8e6b-416e-96ab-f2e62494be00]`
* **NODE_B** [Software Event]: Software Event: S pad message identifier l
  * *Details:* Data Identifier: S pad message identifier l | Data Format: Format one unsign 32 | Center FMS node: Master | Dual: Single | [L message identifier: Please wait]
  * *Citation:* `[Source: NODE_B_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 71 | UUID: f7254e0b-d5da-4d77-b2b7-593d4bbd402a]`
* **NODE_B** [Software Event]: Software Event: S pad message identifier r
  * *Details:* Data Identifier: S pad message identifier r | Data Format: Format one unsign 32 | Center FMS node: Master | Dual: Single | [R message identifier: Please wait]
  * *Citation:* `[Source: NODE_B_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 72 | UUID: 0be1987d-df6f-48f2-91b8-5ab9ad7138c6]`
* **NODE_C** [State Transition]: State Transition: Master status -> Spare
  * *Details:* [Master status: Spare | Dual mode: Single | Opposite fms ok: Ok | Other dual fms node position: FMS node center | Standby fms node position: FMS node invalid | Functional position: First officer]
  * *Citation:* `[Source: NODE_C_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 125 | UUID: 738bf80b-4a85-4fa0-b329-bc87378422ef]`

**[12:01:00]**
* **NODE_A** [Fault History] (x4 occurrences collapsed): Oss bind failure (Code: 6035)
  * *Details:* Serial Number: 461 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6035 | Fault Code: 6035 | Sub Code: Thunderbolt fault | Fault Name: Oss bind failure | Date and Time: 2032-06-18 12:01:00 PM | Module Temperature: 40 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Ready | Last Context Reset Reason: Fr context shutdown e | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 100 | Application Data: Client Cb not found in deos 653 - -933180756;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 461 | UUID: 05c12bd7-0fde-45a7-bdf6-42934df536ac]`
* **NODE_A** [Fault History]: Oss task client failure (Code: 6024)
  * *Details:* Serial Number: 465 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6024 | Fault Code: 6024 | Sub Code: Thunderbolt fault | Fault Name: Oss task client failure | Date and Time: 2032-06-18 12:01:00 PM | Module Temperature: 40 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Ready | Last Context Reset Reason: Fr context shutdown e | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 22 | Application Data: Task Client not found;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 465 | UUID: 18b4f99b-5587-4d6d-9be3-60dadb7a576b]`
* **NODE_A** [Fault History]: Ndb out of date (Code: 5)
  * *Details:* Serial Number: 466 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 11311 | Fault Code: 5 | Sub Code: 31 | Fault Name: Ndb out of date | Date and Time: 2032-06-18 12:01:00 PM | Module Temperature: 40 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: Fr context shutdown e | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 8 | Application Data: ?~J;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 466 | UUID: d1f4cec3-a917-49bf-b7c7-04461557904a]`
* **NODE_A** [Fault History]: Oss task client failure (Code: 6024)
  * *Details:* Serial Number: 467 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6024 | Fault Code: 6024 | Sub Code: Thunderbolt fault | Fault Name: Oss task client failure | Date and Time: 2032-06-18 12:01:00 PM | Module Temperature: 40 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: Fr context shutdown e | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 22 | Application Data: Task Client not found;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 467 | UUID: 4630dab6-8df7-4cef-ab22-2738491ecd56]`
* **NODE_A** [Fault History]: Error during start process (Code: 9)
  * *Details:* Serial Number: 468 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 12315 | Fault Code: 9 | Sub Code: 11 | Fault Name: Error during start process | Date and Time: 2032-06-18 12:01:00 PM | Module Temperature: 40 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: Fr context shutdown e | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 8 | Application Data: ?~J;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 468 | UUID: 83720c1d-fd32-496d-857f-a377e0904e43]`
* **NODE_A** [Fault History]: Oss task client failure (Code: 6024)
  * *Details:* Serial Number: 469 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6024 | Fault Code: 6024 | Sub Code: Thunderbolt fault | Fault Name: Oss task client failure | Date and Time: 2032-06-18 12:01:00 PM | Module Temperature: 39 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: Fr context shutdown e | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 22 | Application Data: Task Client not found;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 469 | UUID: e1cf4d0d-fcc8-4fc1-9890-62eba8e9cd0b]`
* **NODE_A** [Software Event]: Software Event: Operational startup mode identifier
  * *Details:* Data Identifier: Operational startup mode identifier | Data Format: Format fixed str | Left FMS node: Spare | Dual: Single | [Event identifier: 68 | Operational startup mode: Operational startup cold]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 12 | UUID: 6e482546-7abe-4444-bf8f-1731bfd4ef8a]`
* **NODE_A** [Software Event]: Software Event: Dual mode identifier
  * *Details:* Data Identifier: Dual mode identifier | Data Format: Format fixed str | Left FMS node: Spare | Dual: Single | [Event identifier: 68 | Operational dual mode: Operational dual mode Changed]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 13 | UUID: 08ae4861-a192-402c-8225-7a18a1706363]`
* **NODE_A** [Software Event]: Software Event: Operational powerup identifier
  * *Details:* Data Identifier: Operational powerup identifier | Data Format: Format fixed str | Left FMS node: Spare | Dual: Single | [Event identifier: 68 | Operational powerup: Operational powerup normal]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 14 | UUID: d9f41de9-54b1-44ab-8500-7f5fd24e3ff9]`
* **NODE_A** [State Transition]: State Transition: Master status -> Master
  * *Details:* [Master status: Master | Dual mode: Single | Opposite fms ok: Unknown | Other dual fms node position: FMS node invalid | Standby fms node position: FMS node invalid | Functional position: Standby]
  * *Citation:* `[Source: NODE_A_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 13 | UUID: d820f4bf-23b0-4d72-88e9-8d47c6027193]`
* **NODE_C** [Software Event]: Software Event: S pad message identifier l
  * *Details:* Data Identifier: S pad message identifier l | Data Format: Format one unsign 32 | Left FMS node: Spare | Dual: Single | [L message identifier: Please wait]
  * *Citation:* `[Source: NODE_C_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 297 | UUID: 7412e422-b934-4469-ad06-32dcdd221120]`
* **NODE_C** [Software Event]: Software Event: S pad message identifier r
  * *Details:* Data Identifier: S pad message identifier r | Data Format: Format one unsign 32 | Left FMS node: Spare | Dual: Single | [R message identifier: Please wait]
  * *Citation:* `[Source: NODE_C_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 298 | UUID: 7595f880-00ec-441c-92cd-a8722d850bca]`
* **NODE_C** [State Transition]: State Transition: Master status -> Spare
  * *Details:* [Master status: Spare | Dual mode: Single | Opposite fms ok: Ok | Other dual fms node position: FMS node center | Standby fms node position: FMS node left | Functional position: First officer]
  * *Citation:* `[Source: NODE_C_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 126 | UUID: 9bff0239-0b75-4712-8e8e-5ed48a39bcf0]`

**[12:01:01]**
* **NODE_A** [Fault History] (x3 occurrences collapsed): Oss task client failure (Code: 6024)
  * *Details:* Serial Number: 470 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6024 | Fault Code: 6024 | Sub Code: Thunderbolt fault | Fault Name: Oss task client failure | Date and Time: 2032-06-18 12:01:01 PM | Module Temperature: 39 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: Fr context shutdown e | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 22 | Application Data: Task Client not found;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 470 | UUID: b23622ac-eef0-4b38-868c-d648af54621c]`
* **NODE_A** [State Transition]: State Transition: Master status -> Standby
  * *Details:* [Master status: Standby | Dual mode: Single | Opposite fms ok: Unknown | Other dual fms node position: FMS node invalid | Standby fms node position: FMS node invalid | Functional position: Standby]
  * *Citation:* `[Source: NODE_A_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 14 | UUID: 95e07009-74e3-4a51-b395-6d8bf43cca75]`
* **NODE_C** [State Transition] (x2 occurrences collapsed): State Transition: Master status -> Spare
  * *Details:* [Master status: Spare | Dual mode: Single | Opposite fms ok: Ok | Other dual fms node position: FMS node center | Standby fms node position: FMS node center | Functional position: First officer]
  * *Citation:* `[Source: NODE_C_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 127 | UUID: dbf018ba-1fae-43cb-bbb7-19d95c660295]`

**[12:01:02]**
* **NODE_A** [Fault History]: Error during start process (Code: 9)
  * *Details:* Serial Number: 473 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 12315 | Fault Code: 9 | Sub Code: 11 | Fault Name: Error during start process | Date and Time: 2032-06-18 12:01:02 PM | Module Temperature: 40 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: Fr context shutdown e | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 8 | Application Data: ?~J;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 473 | UUID: 56d5a0f8-9f63-459c-b4c1-e01da92009dd]`
* **NODE_A** [Fault History]: Scheduled FMS Activity Missed Timing Requirement (Code: 6000)
  * *Details:* Serial Number: 474 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6000 | Fault Code: 6000 | Sub Code: Thunderbolt fault | Fault Name: Scheduled FMS Activity Missed Timing Requirement | Date and Time: 2032-06-18 12:01:02 PM | Module Temperature: 40 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: Fr context shutdown e | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 50 | Application Data: Deadline miss` Background service - 2162715;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 474 | UUID: 59540186-b9ac-4621-b277-bb54c69fc527]`
* **NODE_A** [Operator Interaction] (x2 occurrences collapsed): Operator Interaction Event
  * *Details:* Dual mode: Single | Master status: Master | Functional position: Captain | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 343.002075 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [FMS Operational Event: clear altitude | FMS node source: Standby]
  * *Citation:* `[Source: NODE_A_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 11 | UUID: e2eec84d-3a55-4b1a-b03e-4890eb4c9dd5]`
* **NODE_A** [State Transition]: State Transition: Master status -> Standby
  * *Details:* [Master status: Standby | Dual mode: Single | Opposite fms ok: Not ok | Other dual fms node position: FMS node invalid | Standby fms node position: FMS node invalid | Functional position: Standby]
  * *Citation:* `[Source: NODE_A_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 15 | UUID: fc6f2808-13b8-4fc4-9d41-7fbe44651ef0]`
* **NODE_A** [State Transition]: State Transition: Master status -> Master
  * *Details:* [Master status: Master | Dual mode: Single | Opposite fms ok: Not ok | Other dual fms node position: FMS node invalid | Standby fms node position: FMS node invalid | Functional position: Captain]
  * *Citation:* `[Source: NODE_A_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 16 | UUID: d2043691-e60e-41e7-9794-d269bbfc5285]`
* **NODE_C** [Aircraft State]: Aircraft State Update
  * *Details:* [Ndb selected cycle: 1 | Ils mode: 17 | Previous leg terminator: 4 | Active leg terminator: 2 | Current lateral leg Sequence: -1417659838 | Next lateral leg Sequence: -1935671229 | Gross weight: 160045.109375 | Cost index: 201326657 | Track: 12946.814453 | FMS button push39: 1792 | Simsoft data: 1610612736 | Software fault address: 537264290 | Last in: 2 | First in: 16 | Right bite trc history: 6]
  * *Citation:* `[Source: NODE_C_Aircraft_State_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 4 | UUID: 1c06e319-7c4e-4892-9d9d-d5ff0a017ba5]`
* **NODE_C** [Fault History]: Resync reciever restart (Code: 6)
  * *Details:* Serial Number: 245 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 11606 | Fault Code: 6 | Sub Code: 70 | Fault Name: Resync reciever restart | Date and Time: 2032-06-18 12:01:02 PM | Module Temperature: 39 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Count: 5 | Last Context Reset Reason: Fr context shutdown e | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 8 | Application Data: ?~J;
  * *Citation:* `[Source: NODE_C_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 245 | UUID: cc3cfbc7-966b-455b-8d77-2ad316d12809]`
* **NODE_C** [Operator Interaction]: Operator Interaction Event
  * *Details:* Dual mode: Single | Master status: Spare | Functional position: First officer | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 343.001770 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [Fault/Event: Dual Resynch Aborted]
  * *Citation:* `[Source: NODE_C_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 749 | UUID: 60a84fa0-9110-4b98-ac3a-a37f6c2ca219]`
* **NODE_C** [State Transition] (x3 occurrences collapsed): State Transition: Master status -> Spare
  * *Details:* [Master status: Spare | Dual mode: Single | Opposite fms ok: Unstable | Other dual fms node position: FMS node left | Standby fms node position: FMS node center | Functional position: First officer]
  * *Citation:* `[Source: NODE_C_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 129 | UUID: 41afba37-3eb4-4b18-8aed-668234afed29]`

**[12:01:03]**
* **NODE_A** [Operator Interaction] (x3 occurrences collapsed): Operator Interaction Event
  * *Details:* Dual mode: Single | Master status: Master | Functional position: Captain | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 343.002075 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [FMS Operational Event: Vertical Guidance Sequence Changed | FMS node source: Standby | Event value: 65540]
  * *Citation:* `[Source: NODE_A_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 13 | UUID: 3a1eb45a-900a-4e02-a62a-c85e66be2a66]`
* **NODE_A** [State Transition] (x2 occurrences collapsed): State Transition: Master status -> Master
  * *Details:* [Master status: Master | Dual mode: Single | Opposite fms ok: Not ok | Other dual fms node position: FMS node right | Standby fms node position: FMS node invalid | Functional position: Captain]
  * *Citation:* `[Source: NODE_A_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 17 | UUID: f9e5de7d-e6c4-4d92-bb91-649fa02e39f6]`
* **NODE_C** [State Transition]: State Transition: Master status -> Spare
  * *Details:* [Master status: Spare | Dual mode: Single | Opposite fms ok: Ok | Other dual fms node position: FMS node left | Standby fms node position: FMS node invalid | Functional position: First officer]
  * *Citation:* `[Source: NODE_C_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 132 | UUID: b7478949-018e-4388-a60d-6ef5611af50f]`

**[12:01:04]**
* **NODE_A** [Fault History]: Scheduled FMS Activity Missed Timing Requirement (Code: 6000)
  * *Details:* Serial Number: 475 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6000 | Fault Code: 6000 | Sub Code: Thunderbolt fault | Fault Name: Scheduled FMS Activity Missed Timing Requirement | Date and Time: 2032-06-18 12:01:04 PM | Module Temperature: 39 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: Fr context shutdown e | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 50 | Application Data: Deadline miss` Background service - 2162704;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 475 | UUID: 56d29d86-3e80-45e7-bed6-205802d3c988]`
* **NODE_A** [Fault History]: Oss semaphore failure (Code: 6029)
  * *Details:* Serial Number: 476 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6029 | Fault Code: 6029 | Sub Code: Thunderbolt fault | Fault Name: Oss semaphore failure | Date and Time: 2032-06-18 12:01:04 PM | Module Temperature: 40 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: Fr context shutdown e | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 100 | Application Data: wait semaphore failed in deos 653 - 6 ;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 476 | UUID: 892e04d1-e41f-4fc9-94ff-90f1d20b4d58]`
* **NODE_A** [Software Event]: Software Event: S pad message identifier l
  * *Details:* Data Identifier: S pad message identifier l | Data Format: Format one unsign 32 | Left FMS node: Spare | Dual: Single | [L message identifier: Please wait]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 15 | UUID: 1a76b3b2-db2f-47a9-8c68-08d990f4d3bc]`
* **NODE_A** [Software Event]: Software Event: S pad message identifier r
  * *Details:* Data Identifier: S pad message identifier r | Data Format: Format one unsign 32 | Left FMS node: Spare | Dual: Single | [R message identifier: Please wait]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 16 | UUID: abb3867e-edc8-441c-81f9-2672be535c20]`
* **NODE_A** [State Transition]: State Transition: Master status -> Master
  * *Details:* [Master status: Master | Dual mode: Single | Opposite fms ok: Ok | Other dual fms node position: FMS node right | Standby fms node position: FMS node invalid | Functional position: Captain]
  * *Citation:* `[Source: NODE_A_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 19 | UUID: 06db16fc-042e-4ef0-9082-70bc80aacf16]`

**[12:01:05]**
* **NODE_A** [Fault History]: Oss semaphore failure (Code: 6029)
  * *Details:* Serial Number: 477 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6029 | Fault Code: 6029 | Sub Code: Thunderbolt fault | Fault Name: Oss semaphore failure | Date and Time: 2032-06-18 12:01:05 PM | Module Temperature: 40 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: Fr context shutdown e | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 100 | Application Data: wait semaphore failed in deos 653 - 6 ;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 477 | UUID: fa2047ee-607c-4eb9-b5cc-7b0efed0c80a]`
* **NODE_C** [Fault History]: Navigation Data Coordination Activity Failure (Code: 11)
  * *Details:* Serial Number: 246 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 12925 | Fault Code: 11 | Sub Code: 109 | Fault Name: Navigation Data Coordination Activity Failure | Date and Time: 2032-06-18 12:01:05 PM | Module Temperature: 39 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Count: 5 | Last Context Reset Reason: Fr context shutdown e | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 8 | Application Data: ?~J;
  * *Citation:* `[Source: NODE_C_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 246 | UUID: affe9146-f40f-46c2-b75e-d15b42491ac6]`

**[12:01:06]**
* **NODE_A** [Fault History]: Oss semaphore failure (Code: 6029)
  * *Details:* Serial Number: 478 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6029 | Fault Code: 6029 | Sub Code: Thunderbolt fault | Fault Name: Oss semaphore failure | Date and Time: 2032-06-18 12:01:06 PM | Module Temperature: 39 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: Fr context shutdown e | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 100 | Application Data: wait semaphore failed in deos 653 - 6 ;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 478 | UUID: 4624f412-2f60-4a61-8eea-3dfd6371c66c]`
* **NODE_A** [Fault History]: Scheduled FMS Activity Missed Timing Requirement (Code: 6000)
  * *Details:* Serial Number: 479 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6000 | Fault Code: 6000 | Sub Code: Thunderbolt fault | Fault Name: Scheduled FMS Activity Missed Timing Requirement | Date and Time: 2032-06-18 12:01:06 PM | Module Temperature: 40 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: Fr context shutdown e | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 50 | Application Data: Deadline miss` Background service - 2162714;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 479 | UUID: 31e4c24b-6beb-42da-9ac9-72c38982852b]`

**[12:01:07]**
* **NODE_A** [Fault History]: Oss semaphore failure (Code: 6029)
  * *Details:* Serial Number: 480 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6029 | Fault Code: 6029 | Sub Code: Thunderbolt fault | Fault Name: Oss semaphore failure | Date and Time: 2032-06-18 12:01:07 PM | Module Temperature: 40 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: Fr context shutdown e | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 100 | Application Data: wait semaphore failed in deos 653 - 6 ;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 480 | UUID: d7174c5f-8044-4463-9aa5-a20b9c44e06c]`
* **NODE_A** [Fault History]: Scheduled FMS Activity Missed Timing Requirement (Code: 6000)
  * *Details:* Serial Number: 481 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6000 | Fault Code: 6000 | Sub Code: Thunderbolt fault | Fault Name: Scheduled FMS Activity Missed Timing Requirement | Date and Time: 2032-06-18 12:01:07 PM | Module Temperature: 40 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: Fr context shutdown e | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 50 | Application Data: Deadline miss` Background service - 2162713;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 481 | UUID: 8547793b-6be1-4b6b-9aec-e6576348f47e]`
* **NODE_A** [Fault History]: Oss semaphore failure (Code: 6029)
  * *Details:* Serial Number: 482 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6029 | Fault Code: 6029 | Sub Code: Thunderbolt fault | Fault Name: Oss semaphore failure | Date and Time: 2032-06-18 12:01:07 PM | Module Temperature: 39 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: Fr context shutdown e | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 100 | Application Data: wait semaphore failed in deos 653 - 6 ;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 482 | UUID: b5b7e688-5900-4054-a7bc-8c641e85e8a3]`
* **NODE_A** [Software Event]: Software Event: Master spare identifier
  * *Details:* Data Identifier: Master spare identifier | Data Format: Format fixed str | Left FMS node: Master | Dual: Single | [Event identifier: 68 | FMS node position: Operational master spare Changed]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 17 | UUID: 1c3fb8ec-18ec-4731-be86-f932e5d21bfb]`
* **NODE_A** [Software Event]: Software Event: Flight display cp identifier
  * *Details:* Data Identifier: Flight display cp identifier | Data Format: Format flight display cp | Left FMS node: Master | Dual: Single | [Scale: 160.000000 | Mode: Plan]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 18 | UUID: 3df77782-d383-4a52-b16e-201cf0ba0e1f]`
* **NODE_C** [Software Event]: Software Event: Master spare identifier
  * *Details:* Data Identifier: Master spare identifier | Data Format: Format fixed str | Left FMS node: Master | Right FMS node: Spare | Dual: Single | [Event identifier: 68 | FMS node position: Operational master spare Changed]
  * *Citation:* `[Source: NODE_C_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 299 | UUID: 02cf6f51-24e2-490f-8475-91fe489e4192]`

**[12:01:08]**
* **NODE_A** [Fault History]: Oss semaphore failure (Code: 6029)
  * *Details:* Serial Number: 483 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6029 | Fault Code: 6029 | Sub Code: Thunderbolt fault | Fault Name: Oss semaphore failure | Date and Time: 2032-06-18 12:01:08 PM | Module Temperature: 40 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: Fr context shutdown e | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 100 | Application Data: wait semaphore failed in deos 653 - 6 ;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 483 | UUID: 3bdf186f-2e09-45de-ba90-864c5b0fa3c6]`

**[12:01:09]**
* **NODE_A** [Fault History]: Oss semaphore failure (Code: 6029)
  * *Details:* Serial Number: 484 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6029 | Fault Code: 6029 | Sub Code: Thunderbolt fault | Fault Name: Oss semaphore failure | Date and Time: 2032-06-18 12:01:09 PM | Module Temperature: 39 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: Fr context shutdown e | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 100 | Application Data: wait semaphore failed in deos 653 - 6 ;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 484 | UUID: a3a28966-deb4-403c-b282-7b6ad5439a10]`

**[12:01:10]**
* **NODE_A** [Fault History]: Oss semaphore failure (Code: 6029)
  * *Details:* Serial Number: 485 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6029 | Fault Code: 6029 | Sub Code: Thunderbolt fault | Fault Name: Oss semaphore failure | Date and Time: 2032-06-18 12:01:10 PM | Module Temperature: 40 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: Fr context shutdown e | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 100 | Application Data: wait semaphore failed in deos 653 - 6 ;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 485 | UUID: d6ae9725-ea44-4c54-8315-ea49e6fc8eb1]`

**[12:01:11]**
* **NODE_A** [Fault History]: Oss semaphore failure (Code: 6029)
  * *Details:* Serial Number: 486 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6029 | Fault Code: 6029 | Sub Code: Thunderbolt fault | Fault Name: Oss semaphore failure | Date and Time: 2032-06-18 12:01:11 PM | Module Temperature: 40 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: Fr context shutdown e | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 100 | Application Data: wait semaphore failed in deos 653 - 6 ;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 486 | UUID: 44fd0f1b-78ba-4915-854c-dbda9a5504ba]`

**[12:01:13]**
* **NODE_A** [Fault History]: Oss semaphore failure (Code: 6029)
  * *Details:* Serial Number: 487 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6029 | Fault Code: 6029 | Sub Code: Thunderbolt fault | Fault Name: Oss semaphore failure | Date and Time: 2032-06-18 12:01:13 PM | Module Temperature: 39 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: Fr context shutdown e | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 100 | Application Data: wait semaphore failed in deos 653 - 6 ;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 487 | UUID: 924ab05f-22a7-4946-885f-a38271bcb7e0]`

**[12:01:17]**
* **NODE_C** [Software Event]: Software Event: Opc configuration data identifier
  * *Details:* Data Identifier: Opc configuration data identifier | Data Format: Format opc configuration data | Left FMS node: Master | Right FMS node: Spare | Dual: Single | [Identifier: Configuration data | Performance custo 3: False | Performance custo 2: False | Performance custo 1: False | Operational data link datalink: True | Air traffic service enable: True | Kilogram enable: True | Metric enable: True | Display trajectory: 1 | Grid mora enable: True | I4d rta enable: False | Radio navigation 2 installed: True | Aim disable: True | No radio navigation on board: False | Passenger count enable: True | Fls enable: True | To securization enable: True | No ap fd mda mdh disconnect: True | To derate enable: True | Climb derate enable: False | Fnl des enable: True | Cda enable: 1 | Cpdb opc enable: False | Vor2 dme2 on board: True | Rnp function enable: True | Leg sequencing monitoring enable: True | Resync check enable: True | To securization 2 enable: True | Sbas enable: True | Sls enable: True | Jfgw display on mfd enable: True | Acr 2 on board: False | Vertical display enable: True | FMS trjctry on vd enable: True | Mora on vd enable: True | Msa on vd enable: True | Etoc enable: True | Freeze scale on vd enable: False | Fls axis on vd enable: True | Aess twsf trjctry enable: True | Auto derate climb enable: True | Polar navigation enabled: True | Back beam approach en: True | FMS platform type 1: True | FMS platform type 2: True | FMS platform type 3: False | FMS platform type 4: False | FMS engine manuf 1: False | FMS engine manuf 2: True | FMS engine manuf 3: False | FMS engine type 1: False | FMS engine type 2: True | FMS engine type 3: False | FMS engine type 4: False | FMS engine type 5: False | Takeoff rnp: 1.000000 | Gps approach rnp: 0.300000 | Precision approach rnp: 0.500000 | Nonprecision approach rnp: 0.500000 | Terminal rnp: 1.000000 | Enroute rnp: 2.000000 | Oceanic rnp: 2.000000 | Takeoff tla: 110.991997 | Takeoff hal: 1.000000 | Approach hal: 0.300000 | Terminal hal: 1.000000 | Enroute hal: 2.000000 | Oceanic hal: 2.000000 | Tail number 32: .F-Wzht | Tail number 16: Zht | Tail number 8: T | Configuration data version: [Redacted Payload] | Opc integrity validation: 61]
  * *Citation:* `[Source: NODE_C_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 300 | UUID: f68ab076-2126-4a77-a4a0-cdf93b320537]`

**[12:01:18]**
* **NODE_C** [Software Event]: Software Event: Sys status identifier
  * *Details:* Data Identifier: Sys status identifier | Data Format: Format sys status | Left FMS node: Master | Right FMS node: Spare | Dual: Single | [Identifier: Sys | Platform family: A350 | Air frame ident: A350 | FMS node physical position: Right | Engine ident: Trent | Engine manufact: 2 | Opsys pn: Hnp5dxcl01xea01 | Ndb pn: Abv2601l01 | Ami database pn: Hnp40 | Database Reference: [Removed]: Hnp56xcd06xha08 | Cpdb pn: Not loaded]
  * *Citation:* `[Source: NODE_C_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 301 | UUID: f45191bb-34d2-4982-a074-40681de46360]`

**[12:01:20]**
* **NODE_A** [Fault History]: Navigation Data Coordination Activity Failure (Code: 11)
  * *Details:* Serial Number: 488 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 12925 | Fault Code: 11 | Sub Code: 109 | Fault Name: Navigation Data Coordination Activity Failure | Date and Time: 2032-06-18 12:01:20 PM | Module Temperature: 40 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: Fr context shutdown e | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 8 | Application Data: ?~J;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 488 | UUID: 733ddab1-6ee4-4afc-9db3-e686bb2fec03]`
* **NODE_A** [Software Event]: Software Event: Opc configuration data identifier
  * *Details:* Data Identifier: Opc configuration data identifier | Data Format: Format opc configuration data | Left FMS node: Master | Dual: Single | [Identifier: Configuration data | Performance custo 3: False | Performance custo 2: False | Performance custo 1: False | Operational data link datalink: True | Air traffic service enable: True | Kilogram enable: True | Metric enable: True | Display trajectory: 1 | Grid mora enable: True | I4d rta enable: False | Radio navigation 2 installed: True | Aim disable: True | No radio navigation on board: False | Passenger count enable: True | Fls enable: True | To securization enable: True | No ap fd mda mdh disconnect: True | To derate enable: True | Climb derate enable: False | Fnl des enable: True | Cda enable: 1 | Cpdb opc enable: False | Vor2 dme2 on board: True | Rnp function enable: True | Leg sequencing monitoring enable: True | Resync check enable: True | To securization 2 enable: True | Sbas enable: True | Sls enable: True | Jfgw display on mfd enable: True | Acr 2 on board: False | Vertical display enable: True | FMS trjctry on vd enable: True | Mora on vd enable: True | Msa on vd enable: True | Etoc enable: True | Freeze scale on vd enable: False | Fls axis on vd enable: True | Aess twsf trjctry enable: True | Auto derate climb enable: True | Polar navigation enabled: True | Back beam approach en: True | FMS platform type 1: True | FMS platform type 2: True | FMS platform type 3: False | FMS platform type 4: False | FMS engine manuf 1: False | FMS engine manuf 2: True | FMS engine manuf 3: False | FMS engine type 1: False | FMS engine type 2: True | FMS engine type 3: False | FMS engine type 4: False | FMS engine type 5: False | Takeoff rnp: 1.000000 | Gps approach rnp: 0.300000 | Precision approach rnp: 0.500000 | Nonprecision approach rnp: 0.500000 | Terminal rnp: 1.000000 | Enroute rnp: 2.000000 | Oceanic rnp: 2.000000 | Takeoff tla: 110.991997 | Takeoff hal: 1.000000 | Approach hal: 0.300000 | Terminal hal: 1.000000 | Enroute hal: 2.000000 | Oceanic hal: 2.000000 | Tail number 32: .F-Wzht | Tail number 16: Zht | Tail number 8: T | Configuration data version: [Redacted Payload] | Opc integrity validation: 61]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 19 | UUID: 3e738eb4-71d2-4be9-ad90-9de5ec6102fa]`
* **NODE_A** [Software Event]: Software Event: Sys status identifier
  * *Details:* Data Identifier: Sys status identifier | Data Format: Format sys status | Left FMS node: Master | Dual: Single | [Identifier: Sys | Platform family: A350 | Air frame ident: A350 | FMS node physical position: Left | Engine ident: Trent | Engine manufact: 2 | Opsys pn: Hnp5dxcl01xea01 | Ndb pn: Abv2601l01 | Ami database pn: Hnp40 | Database Reference: [Removed]: Hnp56xcd06xha08 | Cpdb pn: Not loaded]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 20 | UUID: 0dd721b2-7b2d-40dc-a2d3-f532bc8af5b3]`

**[12:01:41]**
* **NODE_A** [Fault History] (x2 occurrences collapsed): Na (Code: 0)
  * *Details:* Serial Number: 489 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Sub Code: Thunderbolt fault | Fault Name: Na | Date and Time: 2032-06-18 12:01:41 PM | Current Recovery Type: No Recovery Action | Module State: Ms unequipped e | Context State: Cs not equipped e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: Power Loss | Fault Exception: False | Extended Record: False | Application Data: ;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 489 | UUID: 43727ba0-c5fb-498a-afdc-a5ee7f980cc2]`
* **NODE_A** [Operator Interaction]: Operator Interaction Event
  * *Details:* Dual mode: Dual | Master status: Master | Functional position: Captain | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 342.998749 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [Fault/Event: Cold Start Due To A Re-Synch On The Receiver]
  * *Citation:* `[Source: NODE_A_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 16 | UUID: 04c27f9a-efa2-4728-9314-f28fcfa18834]`
* **NODE_C** [State Transition]: State Transition: Master status -> Spare
  * *Details:* [Master status: Spare | Dual mode: Single | Opposite fms ok: Unstable | Other dual fms node position: FMS node left | Standby fms node position: FMS node invalid | Functional position: First officer]
  * *Citation:* `[Source: NODE_C_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 133 | UUID: 4a3f3ead-99c8-46d6-9b2d-9aa5ec99ea54]`

**[12:01:42]**
* **NODE_C** [State Transition]: State Transition: Master status -> Spare
  * *Details:* [Master status: Spare | Dual mode: Single | Opposite fms ok: Not ok | Other dual fms node position: FMS node left | Standby fms node position: FMS node invalid | Functional position: First officer]
  * *Citation:* `[Source: NODE_C_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 134 | UUID: f111253d-0ca4-43db-998c-d6ec84809307]`

**[12:01:51]**
* **NODE_C** [State Transition]: State Transition: Master status -> Master
  * *Details:* [Master status: Master | Dual mode: Single | Opposite fms ok: Not ok | Other dual fms node position: FMS node left | Standby fms node position: FMS node invalid | Functional position: First officer]
  * *Citation:* `[Source: NODE_C_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 135 | UUID: 6de4ca1c-f92f-4016-bd95-dd731143baa2]`

**[12:01:57]**
* **NODE_C** [Software Event]: Software Event: Master spare identifier
  * *Details:* Data Identifier: Master spare identifier | Data Format: Format fixed str | Right FMS node: Master | Dual: Single | [Event identifier: 68 | FMS node position: Operational master spare Changed]
  * *Citation:* `[Source: NODE_C_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 302 | UUID: b9a0b08d-3a2e-438d-abac-6fbe32091aef]`

**[12:02:12]**
* **NODE_B** [Fault History]: Oss loading failure (Code: 6052)
  * *Details:* Serial Number: 293 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6052 | Fault Code: 6052 | Sub Code: Thunderbolt fault | Fault Name: Oss loading failure | Date and Time: 2032-06-18 12:02:12 PM | Module Temperature: 38 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Initializing | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 100 | Application Data: Failed to load library in Deos 653 - Libpssl dtf manager so.so 11 11;
  * *Citation:* `[Source: NODE_B_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 293 | UUID: 2e89192d-66d1-4725-ba92-f149180253f9]`

**[12:02:14]**
* **NODE_B** [Fault History]: Error during start process (Code: 9)
  * *Details:* Serial Number: 294 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 12315 | Fault Code: 9 | Sub Code: 11 | Fault Name: Error during start process | Date and Time: 2032-06-18 12:02:14 PM | Module Temperature: 37 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 8 | Application Data: ?~J;
  * *Citation:* `[Source: NODE_B_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 294 | UUID: ca681854-225e-48e3-80fc-4960ea13bf3f]`
* **NODE_C** [State Transition]: State Transition: Master status -> Master
  * *Details:* [Master status: Master | Dual mode: Single | Opposite fms ok: Not ok | Other dual fms node position: FMS node left | Standby fms node position: FMS node center | Functional position: First officer]
  * *Citation:* `[Source: NODE_C_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 136 | UUID: 321ec35a-77c7-4d80-8203-bfdc57393977]`

**[12:02:20]**
* **NODE_C** [Software Event]: Software Event: Master spare identifier
  * *Details:* Data Identifier: Master spare identifier | Data Format: Format fixed str | Center FMS node: Standby | Right FMS node: Master | Dual: Single | [Event identifier: 68 | FMS node position: Operational master spare Changed]
  * *Citation:* `[Source: NODE_C_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 303 | UUID: c1c33d0c-c8cd-4c2a-8cf0-e7900e5a836d]`

**[12:02:34]**
* **NODE_B** [Fault History]: Navigation Data Coordination Activity Failure (Code: 11)
  * *Details:* Serial Number: 295 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 12925 | Fault Code: 11 | Sub Code: 109 | Fault Name: Navigation Data Coordination Activity Failure | Date and Time: 2032-06-18 12:02:34 PM | Module Temperature: 36 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 8 | Application Data: ?~J;
  * *Citation:* `[Source: NODE_B_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 295 | UUID: 911aba04-2a28-4be1-98a1-49270810c084]`

**[12:02:52]**
* **NODE_A** [Fault History]: Oss loading failure (Code: 6052)
  * *Details:* Serial Number: 491 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6052 | Fault Code: 6052 | Sub Code: Thunderbolt fault | Fault Name: Oss loading failure | Date and Time: 2032-06-18 12:02:52 PM | Module Temperature: 40 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Initializing | Last Context Reset Reason: Fr context shutdown e | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 100 | Application Data: Failed to load library in Deos 653 - Libpssl dtf manager so.so 11 11;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 491 | UUID: e3a68837-31d4-4cc9-a82f-f89dc54c2c0b]`

**[12:02:53]**
* **NODE_A** [Operator Interaction]: Operator Interaction Event
  * *Details:* Dual mode: Dual | Master status: Master | Functional position: Captain | Calibrated airspeed data: 30.000000 | Message: No displayable fields
  * *Citation:* `[Source: NODE_A_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 17 | UUID: cd256b95-078e-4a50-a52e-370d576644b0]`

**[12:02:54]**
* **NODE_A** [Operator Interaction]: Operator Interaction Event
  * *Details:* Dual mode: Dual | Master status: Master | Functional position: Captain | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 342.997498 | Magnetic track: 66.049805 | [FMS Operational Event: redisplay | FMS node source: Standby]
  * *Citation:* `[Source: NODE_A_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 18 | UUID: 954759d3-d93c-4095-afb4-debb0d1ae972]`
* **NODE_A** [Software Event]: Software Event: Operational startup mode identifier
  * *Details:* Data Identifier: Operational startup mode identifier | Data Format: Format fixed str | Left FMS node: Spare | Dual: Dual | [Event identifier: 68 | Operational startup mode: Operational startup cold]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 21 | UUID: 1265ef2e-eaba-4594-9148-98722e465f60]`
* **NODE_A** [Software Event]: Software Event: Operational powerup identifier
  * *Details:* Data Identifier: Operational powerup identifier | Data Format: Format fixed str | Left FMS node: Spare | Dual: Dual | [Event identifier: 68 | Operational powerup: Operational powerup normal]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 22 | UUID: 69199cfb-9fee-4c6c-acb6-3a5cb419a8b7]`
* **NODE_A** [State Transition] (x2 occurrences collapsed): State Transition: Master status -> Master
  * *Details:* [Master status: Master | Dual mode: Dual | Opposite fms ok: Unknown | Other dual fms node position: FMS node right | Standby fms node position: FMS node invalid | Functional position: Captain]
  * *Citation:* `[Source: NODE_A_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 20 | UUID: 2d013c0b-7b0c-4bf7-8d47-af8ed5a2a840]`
* **NODE_C** [Fault History] (x2 occurrences collapsed): Exception unknown error (Code: 2)
  * *Details:* Serial Number: 247 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 10514 | Fault Code: 2 | Sub Code: 2 | Fault Name: Exception unknown error | Date and Time: 2032-06-18 12:02:54 PM | Module Temperature: 38 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: Fr context shutdown e | Module State: Operational | Context State: Cs fault recovery e | Last Context Reset Count: 5 | Last Context Reset Reason: Fr context shutdown e | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 8 | Application Data: ?~J;
  * *Citation:* `[Source: NODE_C_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 247 | UUID: f6a0461d-a38a-4a96-ba1c-d44969a368ab]`

**[12:02:55]**
* **NODE_A** [State Transition]: State Transition: Master status -> Master
  * *Details:* [Master status: Master | Dual mode: Dual | Opposite fms ok: Not ok | Other dual fms node position: FMS node right | Standby fms node position: FMS node center | Functional position: Captain]
  * *Citation:* `[Source: NODE_A_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 22 | UUID: 4534a1be-f650-42f3-8f3a-cea9b5b01e09]`

**[12:02:56]**
* **NODE_A** [Fault History]: Scheduled FMS Activity Missed Timing Requirement (Code: 6000)
  * *Details:* Serial Number: 492 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6000 | Fault Code: 6000 | Sub Code: Thunderbolt fault | Fault Name: Scheduled FMS Activity Missed Timing Requirement | Date and Time: 2032-06-18 12:02:56 PM | Module Temperature: 40 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: Fr context shutdown e | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 50 | Application Data: Deadline miss` Background service - 3211290;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 492 | UUID: 6a808863-add4-4bef-a601-cf305d30f466]`

**[12:02:58]**
* **NODE_A** [Software Event]: Software Event: Data link comm master identifier
  * *Details:* Data Identifier: Data link comm master identifier | Data Format: Format fixed str | Left FMS node: Spare | Dual: Dual | [Event identifier: 68 | Data link comm master status log: Data link comm slave to master]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 23 | UUID: 085fdc35-1756-4933-8fe0-2d92497ea900]`

**[12:03:00]**
* **NODE_A** [Software Event]: Software Event: Master spare identifier
  * *Details:* Data Identifier: Master spare identifier | Data Format: Format fixed str | Left FMS node: Master | Center FMS node: Standby | Right FMS node: Spare | Dual: Dual | [Event identifier: 68 | FMS node position: Operational master spare Changed]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 24 | UUID: 79d0ffe5-f267-4422-9178-354dddc36386]`

**[12:03:03]**
* **NODE_A** [Fault History]: Scheduled FMS Activity Missed Timing Requirement (Code: 6000)
  * *Details:* Serial Number: 493 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6000 | Fault Code: 6000 | Sub Code: Thunderbolt fault | Fault Name: Scheduled FMS Activity Missed Timing Requirement | Date and Time: 2032-06-18 12:03:03 PM | Module Temperature: 40 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: Fr context shutdown e | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 50 | Application Data: Deadline miss` Background service - 3211291;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 493 | UUID: b63491db-f5e3-4bbc-b808-835ba9ecba9e]`
* **NODE_A** [Software Event]: Software Event: Dual mode identifier
  * *Details:* Data Identifier: Dual mode identifier | Data Format: Format fixed str | Left FMS node: Master | Center FMS node: Standby | Right FMS node: Spare | Dual: Single | [Event identifier: 68 | Operational dual mode: Operational dual mode Changed]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 25 | UUID: 3420a362-e316-48d5-8606-26782559212b]`
* **NODE_A** [State Transition]: State Transition: Master status -> Master
  * *Details:* [Master status: Master | Dual mode: Single | Opposite fms ok: Not ok | Other dual fms node position: FMS node right | Standby fms node position: FMS node center | Functional position: Captain]
  * *Citation:* `[Source: NODE_A_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 23 | UUID: 0a66b574-7d7f-427c-bff7-53fb6c00b482]`

**[12:03:04]**
* **NODE_A** [Fault History]: Scheduled FMS Activity Missed Timing Requirement (Code: 6000)
  * *Details:* Serial Number: 494 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6000 | Fault Code: 6000 | Sub Code: Thunderbolt fault | Fault Name: Scheduled FMS Activity Missed Timing Requirement | Date and Time: 2032-06-18 12:03:04 PM | Module Temperature: 40 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: Fr context shutdown e | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 50 | Application Data: Deadline miss` Background service - 3211282;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 494 | UUID: b312f15b-66a6-4688-b81e-d42e4ae1e623]`
* **NODE_A** [Operator Interaction] (x6 occurrences collapsed): Operator Interaction Event
  * *Details:* Dual mode: Single | Master status: Master | Functional position: Captain | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 342.998047 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [FMS Operational Event: clear altitude | FMS node source: Standby | Event value: 65536]
  * *Citation:* `[Source: NODE_A_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 19 | UUID: 74045a9a-fe35-49ba-a8e5-2650398a2ee8]`

**[12:03:05]**
* **NODE_A** [Operator Interaction]: Operator Interaction Event
  * *Details:* Dual mode: Single | Master status: Master | Functional position: Captain | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 342.998505 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [FMS Operational Event: no phase change | FMS node source: Standby | Event value: 65540]
  * *Citation:* `[Source: NODE_A_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 25 | UUID: ba55c156-542f-4fb0-b231-3d1214804d9f]`

**[12:03:06]**
* **NODE_A** [Fault History] (x2 occurrences collapsed): Scheduled FMS Activity Missed Timing Requirement (Code: 6000)
  * *Details:* Serial Number: 495 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6000 | Fault Code: 6000 | Sub Code: Thunderbolt fault | Fault Name: Scheduled FMS Activity Missed Timing Requirement | Date and Time: 2032-06-18 12:03:06 PM | Module Temperature: 40 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: Fr context shutdown e | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 50 | Application Data: Deadline miss` Background service - 3211289;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 495 | UUID: 38084696-ce5f-48d8-9270-196a8de31c21]`

**[12:03:09]**
* **NODE_A** [Software Event]: Software Event: Master spare identifier
  * *Details:* Data Identifier: Master spare identifier | Data Format: Format fixed str | Left FMS node: Master | Center FMS node: Standby | Dual: Single | [Event identifier: 68 | FMS node position: Operational master spare Changed]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 26 | UUID: 9a341253-67b8-4810-a134-b6f44eabb8fb]`

**[12:03:14]**
* **NODE_A** [Fault History]: Navigation Data Coordination Activity Failure (Code: 11)
  * *Details:* Serial Number: 497 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 12925 | Fault Code: 11 | Sub Code: 109 | Fault Name: Navigation Data Coordination Activity Failure | Date and Time: 2032-06-18 12:03:14 PM | Module Temperature: 41 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: Fr context shutdown e | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 8 | Application Data: ?~J;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 497 | UUID: 8848af1c-68fb-467f-a927-15bc824579f3]`
