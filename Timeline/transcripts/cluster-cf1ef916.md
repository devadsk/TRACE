# Incident Cluster: cluster-cf1ef916
**Date:** 2032-06-18
**Duration:** 11:55:18 to 11:56:48
**Nodes Involved:** NODE_A, NODE_B, NODE_C
**Total Events:** 23 (Filtered from 29 raw logs)

## Timeline Transcript

**[11:55:18]**
* **NODE_C** [Operator Interaction] (x2 occurrences collapsed): Operator Interaction Event
  * *Details:* Dual mode: Dual | Master status: Spare | Functional position: First officer | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 342.998962 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [Fault/Event: Performance Defined Event | Event value: 3]
  * *Citation:* `[Source: NODE_C_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 728 | UUID: 85e558c5-812e-4cd8-ad99-0a76e5eddf6d]`

**[11:55:44]**
* **NODE_C** [State Transition]: State Transition: Master status -> Spare
  * *Details:* [Master status: Spare | Dual mode: Dual | Opposite fms ok: Unstable | Other dual fms node position: FMS node left | Standby fms node position: FMS node center | Functional position: First officer]
  * *Citation:* `[Source: NODE_C_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 96 | UUID: 17ce1285-97f4-4464-8d34-f0199b50c8da]`

**[11:55:45]**
* **NODE_C** [State Transition]: State Transition: Master status -> Spare
  * *Details:* [Master status: Spare | Dual mode: Dual | Opposite fms ok: Not ok | Other dual fms node position: FMS node left | Standby fms node position: FMS node center | Functional position: First officer]
  * *Citation:* `[Source: NODE_C_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 97 | UUID: e78080d6-30fb-4908-a3e3-fa70a43202dc]`

**[11:55:47]**
* **NODE_A** [Fault History] (x2 occurrences collapsed): Na (Code: 0)
  * *Details:* Serial Number: 361 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Sub Code: Thunderbolt fault | Fault Name: Na | Date and Time: 2032-06-18 11:55:47 AM | Current Recovery Type: No Recovery Action | Module State: Ms unequipped e | Context State: Cs not equipped e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: Power Loss | Fault Exception: False | Extended Record: False | Application Data: ;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 361 | UUID: 6912db2d-2131-46fd-9883-3cb3aa8de2de]`

**[11:55:50]**
* **NODE_B** [Software Event]: Software Event: Master spare identifier
  * *Details:* Data Identifier: Master spare identifier | Data Format: Format fixed str | Center FMS node: Standby | Right FMS node: Spare | Dual: Single | [Event identifier: 68 | FMS node position: Operational master spare Changed]
  * *Citation:* `[Source: NODE_B_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 51 | UUID: d2eaa36c-9f34-4198-b542-b8ffe405ed67]`

**[11:55:51]**
* **NODE_C** [Software Event]: Software Event: Dual mode identifier
  * *Details:* Data Identifier: Dual mode identifier | Data Format: Format fixed str | Left FMS node: Master | Center FMS node: Standby | Right FMS node: Spare | Dual: Single | [Event identifier: 68 | Operational dual mode: Operational dual mode Changed]
  * *Citation:* `[Source: NODE_C_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 282 | UUID: 92ec6916-faef-4fcf-8b26-88036f0f9d59]`
* **NODE_C** [Software Event]: Software Event: Data link comm master identifier
  * *Details:* Data Identifier: Data link comm master identifier | Data Format: Format fixed str | Left FMS node: Master | Center FMS node: Standby | Right FMS node: Spare | Dual: Single | [Event identifier: 68 | Data link comm master status log: Data link comm slave to master]
  * *Citation:* `[Source: NODE_C_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 283 | UUID: dcc09c11-d2d8-4fd1-8438-869937d80f08]`
* **NODE_C** [State Transition]: State Transition: Master status -> Spare
  * *Details:* [Master status: Spare | Dual mode: Single | Opposite fms ok: Not ok | Other dual fms node position: FMS node left | Standby fms node position: FMS node center | Functional position: First officer]
  * *Citation:* `[Source: NODE_C_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 98 | UUID: 75e7dfde-fc89-4c6f-b50b-47e785d5be97]`

**[11:55:54]**
* **NODE_C** [State Transition]: State Transition: Master status -> Master
  * *Details:* [Master status: Master | Dual mode: Single | Opposite fms ok: Not ok | Other dual fms node position: FMS node left | Standby fms node position: FMS node center | Functional position: First officer]
  * *Citation:* `[Source: NODE_C_State_Transition_Buffer_Log_6_Custom_Log_Decoded_Report.html | Seq: 99 | UUID: a137a98c-8bc5-407f-b6c7-79c08461b2df]`

**[11:55:58]**
* **NODE_C** [Operator Interaction] (x2 occurrences collapsed): Operator Interaction Event
  * *Details:* Dual mode: Single | Master status: Master | Functional position: First officer | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 342.999664 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [Fault/Event: Performance Defined Event | Event value: 4]
  * *Citation:* `[Source: NODE_C_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 730 | UUID: 9b357c82-d29b-40a2-aafd-282b5584dcff]`

**[11:55:59]**
* **NODE_C** [Software Event]: Software Event: Master spare identifier
  * *Details:* Data Identifier: Master spare identifier | Data Format: Format fixed str | Center FMS node: Standby | Right FMS node: Master | Dual: Single | [Event identifier: 68 | FMS node position: Operational master spare Changed]
  * *Citation:* `[Source: NODE_C_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 284 | UUID: f2275918-1ba7-48a8-b038-1ab0094a3bfe]`

**[11:56:00]**
* **NODE_B** [Software Event]: Software Event: Master spare identifier
  * *Details:* Data Identifier: Master spare identifier | Data Format: Format fixed str | Center FMS node: Standby | Right FMS node: Master | Dual: Single | [Event identifier: 68 | FMS node position: Operational master spare Changed]
  * *Citation:* `[Source: NODE_B_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 52 | UUID: c8761472-adbe-4ca1-a72f-107927bb0444]`
* **NODE_C** [Operator Interaction]: Operator interaction clear leg term
  * *Details:* Dual mode: Single | Master status: Master | Functional position: First officer | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 343.000061 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | Flight plan source - high: Active | Flight plan source - low: ActPrimary | Display system source: Operator interaction display system right | [Operator Interaction Event: Operator interaction clear leg term | Event status: Operator interaction entered | Event value: 131091]
  * *Citation:* `[Source: NODE_C_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 732 | UUID: 84465e3e-4ce8-4ae8-a9da-61a00ff02d05]`
* **NODE_C** [Operator Interaction] (x2 occurrences collapsed): Operator Interaction Event
  * *Details:* Dual mode: Single | Master status: Master | Functional position: First officer | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 343.000061 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [Fix ident: Pd05]
  * *Citation:* `[Source: NODE_C_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 733 | UUID: ab514dc6-af5f-46ef-ade2-7da06eae3f5e]`
* **NODE_C** [Software Event]: Software Event: Operator interaction event identifier
  * *Details:* Data Identifier: Operator interaction event identifier | Data Format: Format operator interaction event | Center FMS node: Standby | Right FMS node: Master | Dual: Single | [Event identifier: Operator interaction clear leg term | Source fms node: First officer]
  * *Citation:* `[Source: NODE_C_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 285 | UUID: b8027aeb-d7ca-4401-be18-c98e324cbc68]`

**[11:56:02]**
* **NODE_C** [Operator Interaction]: Operator interaction delete discon
  * *Details:* Dual mode: Single | Master status: Master | Functional position: First officer | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 343.000671 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | Flight plan source - high: Temporary Efb | Flight plan source - low: TmpyPrimary | Display system source: Operator interaction display system right | [Operator Interaction Event: Operator interaction delete discon | Event status: Operator interaction entered | Event value: 17826328]
  * *Citation:* `[Source: NODE_C_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 735 | UUID: e137d00f-d555-433d-95b2-85056c618b11]`
* **NODE_C** [Operator Interaction] (x2 occurrences collapsed): Operator Interaction Event
  * *Details:* Dual mode: Single | Master status: Master | Functional position: First officer | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 343.000671 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [Fix ident: Pd03]
  * *Citation:* `[Source: NODE_C_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 736 | UUID: 29429687-8836-4935-99b7-4f1ed30b89a0]`
* **NODE_C** [Software Event]: Software Event: Operator interaction event identifier
  * *Details:* Data Identifier: Operator interaction event identifier | Data Format: Format operator interaction event | Center FMS node: Standby | Right FMS node: Master | Dual: Single | [Event identifier: Operator interaction delete discon | Source fms node: First officer]
  * *Citation:* `[Source: NODE_C_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 286 | UUID: 884d80e1-795f-4eeb-91b6-57c97bea3176]`

**[11:56:04]**
* **NODE_C** [Operator Interaction]: Operator interaction insert temporary
  * *Details:* Dual mode: Single | Master status: Master | Functional position: First officer | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 343.000977 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | Flight plan source - high: Temporary Efb | Flight plan source - low: TmpyPrimary | Display system source: Operator interaction display system right | [Operator Interaction Event: Operator interaction insert temporary | Event status: Operator interaction entered | Event value: 26477192]
  * *Citation:* `[Source: NODE_C_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 738 | UUID: 32c9595b-b087-4a3b-8ad3-19ff1b7e6fd0]`
* **NODE_C** [Operator Interaction]: Operator Interaction Event
  * *Citation:* `[Source: NODE_C_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 739 | UUID: 11fe1289-93fb-4164-b769-6bd089a6ca6c]`
* **NODE_C** [Software Event]: Software Event: Operator interaction event identifier
  * *Details:* Data Identifier: Operator interaction event identifier | Data Format: Format operator interaction event | Center FMS node: Standby | Right FMS node: Master | Dual: Single | [Event identifier: Operator interaction insert temporary | Source fms node: First officer]
  * *Citation:* `[Source: NODE_C_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 287 | UUID: 02654b18-c51f-458f-be4b-6e568e9980a9]`

**[11:56:07]**
* **NODE_C** [Operator Interaction]: Operator Interaction Event
  * *Details:* Dual mode: Single | Master status: Master | Functional position: First officer | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 343.001556 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [FMS Operational Event: Performance Data Changed | FMS node source: Captain | Event value: 26477079]
  * *Citation:* `[Source: NODE_C_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 740 | UUID: 2439c6d0-9a50-4ab9-aed2-b5df0aae49bd]`

**[11:56:48]**
* **NODE_C** [Operator Interaction] (x2 occurrences collapsed): Operator Interaction Event
  * *Details:* Dual mode: Single | Master status: Master | Functional position: First officer | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 343.001678 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [Fault/Event: Performance Defined Event | Event value: 5]
  * *Citation:* `[Source: NODE_C_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 741 | UUID: 3a6000c3-acd5-4574-9567-1cdef3dabb1d]`
