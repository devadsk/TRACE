# Incident Cluster: cluster-30f7fbe5
**Date:** 2032-06-18
**Duration:** 10:11:09 to 10:12:05
**Nodes Involved:** NODE_A, NODE_B, NODE_C
**Total Events:** 42 (Filtered from 55 raw logs)

## Timeline Transcript

**[10:11:09]**
* **NODE_C** [Software Event]: Software Event: Flight display cp identifier
  * *Details:* Data Identifier: Flight display cp identifier | Data Format: Format flight display cp | Left FMS node: Master | Center FMS node: Standby | Right FMS node: Spare | Dual: Dual | [Scale: 40.000000 | Mode: Plan | Route data: 1 | Waypoints: 1 | Cust wpts: 1 | Mora: 1]
  * *Citation:* `[Source: NODE_C_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 98 | UUID: d963dc25-de83-47f6-aa8a-977c57572b01]`

**[10:11:25]**
* **NODE_A** [Operator Interaction]: Operator interaction string new waypoint
  * *Details:* Dual mode: Dual | Master status: Master | Functional position: Captain | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 211.999344 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | Flight plan source - high: Active | Flight plan source - low: ActPrimary | Display system source: Operator interaction display system right | [Operator Interaction Event: Operator interaction string new waypoint | Event status: Operator interaction entered | Event value: 131098 | Airport Identifier: Bobix | Airport Latitude: -173026.02 | Airport Longitude: -1494005.01]
  * *Citation:* `[Source: NODE_A_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 242 | UUID: ae6cc2a1-eeff-433c-b04f-5585fe8621bb]`
* **NODE_A** [Operator Interaction] (x2 occurrences collapsed): Operator Interaction Event
  * *Details:* Dual mode: Dual | Master status: Master | Functional position: Captain | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 211.999344 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [Fix ident: Ovini]
  * *Citation:* `[Source: NODE_A_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 243 | UUID: 2e7be7b4-af77-4a18-b96f-b9aa706a378a]`
* **NODE_A** [Software Event]: Software Event: Operator interaction event identifier
  * *Details:* Data Identifier: Operator interaction event identifier | Data Format: Format operator interaction event | Left FMS node: Master | Center FMS node: Standby | Right FMS node: Spare | Dual: Dual | [Event identifier: Operator interaction string new waypoint | Source fms node: First officer]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 97 | UUID: 90f9adc1-475d-4d18-bfd9-7cbe8add866e]`

**[10:11:26]**
* **NODE_A** [Operator Interaction]: Operator Interaction Event
  * *Details:* Dual mode: Dual | Master status: Master | Functional position: Captain | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 211.999237 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [FMS Operational Event: Optimized Step Selected | FMS node source: Captain | Event value: 17826333]
  * *Citation:* `[Source: NODE_A_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 245 | UUID: 912e39da-26b6-4ac0-9081-ba5b4558fdf2]`

**[10:11:27]**
* **NODE_A** [Operator Interaction] (x2 occurrences collapsed): Operator Interaction Event
  * *Details:* Dual mode: Dual | Master status: Master | Functional position: Captain | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 211.999161 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [FMS Operational Event: Performance Data Changed | FMS node source: Standby | Event value: 131098]
  * *Citation:* `[Source: NODE_A_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 246 | UUID: b2ce4bb5-08e2-452b-8a50-b983f100f668]`
* **NODE_C** [Operator Interaction]: Operator interaction string new waypoint
  * *Details:* Dual mode: Dual | Master status: Spare | Functional position: First officer | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 211.999298 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | Flight plan source - high: Active | Flight plan source - low: ActPrimary | Display system source: Operator interaction display system right | [Operator Interaction Event: Operator interaction string new waypoint | Event status: Operator interaction entered | Event value: 131098 | Airport Identifier: Bobix | Airport Latitude: -173026.02 | Airport Longitude: -1494005.01]
  * *Citation:* `[Source: NODE_C_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 244 | UUID: 4ce6b640-df96-4689-886d-9d381b371ac2]`
* **NODE_C** [Operator Interaction] (x3 occurrences collapsed): Operator Interaction Event
  * *Details:* Dual mode: Dual | Master status: Spare | Functional position: First officer | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 211.999298 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [Fix ident: Ovini]
  * *Citation:* `[Source: NODE_C_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 245 | UUID: d8e4e038-4d3f-42ab-98c3-8fe4dbcbd3f4]`
* **NODE_C** [Software Event]: Software Event: Operator interaction event identifier
  * *Details:* Data Identifier: Operator interaction event identifier | Data Format: Format operator interaction event | Left FMS node: Master | Center FMS node: Standby | Right FMS node: Spare | Dual: Dual | [Event identifier: Operator interaction string new waypoint | Source fms node: First officer]
  * *Citation:* `[Source: NODE_C_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 99 | UUID: 269ee473-4bac-4464-b392-9f5ed37032eb]`

**[10:11:28]**
* **NODE_A** [Operator Interaction]: Operator interaction insert temporary
  * *Details:* Dual mode: Dual | Master status: Master | Functional position: Captain | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 211.998947 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | Flight plan source - high: Temporary Efb | Flight plan source - low: TmpyPrimary | Display system source: Operator interaction display system right | [Operator Interaction Event: Operator interaction insert temporary | Event status: Operator interaction entered | Event value: 131091]
  * *Citation:* `[Source: NODE_A_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 248 | UUID: 9017ec31-9af9-44db-8bfb-7c0bd57c7de5]`
* **NODE_A** [Operator Interaction]: Operator Interaction Event
  * *Citation:* `[Source: NODE_A_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 249 | UUID: 80f177fe-7147-4409-a238-92be1787792d]`
* **NODE_A** [Software Event]: Software Event: Operator interaction event identifier
  * *Details:* Data Identifier: Operator interaction event identifier | Data Format: Format operator interaction event | Left FMS node: Master | Center FMS node: Standby | Right FMS node: Spare | Dual: Dual | [Event identifier: Operator interaction insert temporary | Source fms node: First officer]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 98 | UUID: 4da0b034-3b50-4dd8-913e-a723e0593ace]`
* **NODE_C** [Operator Interaction] (x2 occurrences collapsed): Operator Interaction Event
  * *Details:* Dual mode: Dual | Master status: Spare | Functional position: First officer | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 211.999146 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [FMS Operational Event: Performance Data Changed | FMS node source: Standby | Event value: 131098]
  * *Citation:* `[Source: NODE_C_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 248 | UUID: ab9dc0dc-032f-4f35-9d34-7290115cefbe]`

**[10:11:29]**
* **NODE_A** [Operator Interaction]: Operator Interaction Event
  * *Details:* Dual mode: Dual | Master status: Master | Functional position: Captain | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 211.998871 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [FMS Operational Event: Optimized Step Selected | FMS node source: Captain | Event value: 26477079]
  * *Citation:* `[Source: NODE_A_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 250 | UUID: 47385e6b-fedb-4580-9a01-36069bba7ea0]`
* **NODE_A** [Software Event]: Software Event: Operator interaction event identifier
  * *Details:* Data Identifier: Operator interaction event identifier | Data Format: Format operator interaction event | Left FMS node: Master | Center FMS node: Standby | Right FMS node: Spare | Dual: Dual | [Event identifier: Operator interaction insert temporary | Source fms node: First officer]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 99 | UUID: 4aa61474-af15-47b1-a275-f3da87cf75c9]`
* **NODE_C** [Operator Interaction]: Operator interaction insert temporary
  * *Details:* Dual mode: Dual | Master status: Spare | Functional position: First officer | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 211.998886 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | Flight plan source - high: Temporary Efb | Flight plan source - low: TmpyPrimary | Display system source: Operator interaction display system right | [Operator Interaction Event: Operator interaction insert temporary | Event status: Operator interaction entered | Event value: 131091]
  * *Citation:* `[Source: NODE_C_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 250 | UUID: 116b0802-e2e7-437a-a5ab-9f16c342f5a0]`
* **NODE_C** [Operator Interaction]: Operator Interaction Event
  * *Citation:* `[Source: NODE_C_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 251 | UUID: 36fb2227-6342-4a5f-8c4e-65ea3f9bd8f8]`
* **NODE_C** [Software Event]: Software Event: Operator interaction event identifier
  * *Details:* Data Identifier: Operator interaction event identifier | Data Format: Format operator interaction event | Left FMS node: Master | Center FMS node: Standby | Right FMS node: Spare | Dual: Dual | [Event identifier: Operator interaction insert temporary | Source fms node: First officer]
  * *Citation:* `[Source: NODE_C_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 100 | UUID: 6162ebb4-3198-473c-a32b-5ba5b1a2d612]`

**[10:11:30]**
* **NODE_C** [Operator Interaction]: Operator Interaction Event
  * *Details:* Dual mode: Dual | Master status: Spare | Functional position: First officer | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 211.998840 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [FMS Operational Event: Optimized Step Selected | FMS node source: Captain | Event value: 26477079]
  * *Citation:* `[Source: NODE_C_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 252 | UUID: 064643b8-6b59-48f2-b2e6-86158fed8014]`
* **NODE_C** [Software Event]: Software Event: Operator interaction event identifier
  * *Details:* Data Identifier: Operator interaction event identifier | Data Format: Format operator interaction event | Left FMS node: Master | Center FMS node: Standby | Right FMS node: Spare | Dual: Dual | [Event identifier: Operator interaction insert temporary | Source fms node: First officer]
  * *Citation:* `[Source: NODE_C_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 101 | UUID: b181facd-73ad-4b0d-85d2-bd49d2c413c1]`

**[10:11:33]**
* **NODE_A** [Fault History]: Rnp legs transmitter io (Code: 6)
  * *Details:* Serial Number: 181 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 11629 | Fault Code: 6 | Sub Code: 93 | Fault Name: Rnp legs transmitter io | Date and Time: 2032-06-18 10:11:33 AM | Module Temperature: 40 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 8 | Application Data: ?~J;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 181 | UUID: bcc26667-b72a-4c96-a2c4-3b62ae485c68]`

**[10:11:35]**
* **NODE_B** [Fault History]: Rnp integrity validation receiver timeout (Code: 6)
  * *Details:* Serial Number: 143 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 11633 | Fault Code: 6 | Sub Code: 97 | Fault Name: Rnp integrity validation receiver timeout | Date and Time: 2032-06-18 10:11:35 AM | Module Temperature: 36 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 8 | Application Data: ?~J;
  * *Citation:* `[Source: NODE_B_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 143 | UUID: 328b71d2-4ff4-44e2-b842-93caa403b378]`

**[10:11:56]**
* **NODE_A** [Operator Interaction]: Operator interaction string new waypoint
  * *Details:* Dual mode: Dual | Master status: Master | Functional position: Captain | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 211.999664 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | Flight plan source - high: Active | Flight plan source - low: ActPrimary | Display system source: Operator interaction display system right | [Operator Interaction Event: Operator interaction string new waypoint | Event status: Operator interaction entered | Event value: 131098 | Airport Identifier: Mosma | Airport Latitude: -171936.83 | Airport Longitude: -1495037.59]
  * *Citation:* `[Source: NODE_A_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 251 | UUID: 9d488312-a7be-4d65-bce5-ab43d43c9213]`
* **NODE_A** [Operator Interaction] (x2 occurrences collapsed): Operator Interaction Event
  * *Details:* Dual mode: Dual | Master status: Master | Functional position: Captain | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 211.999664 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [Fix ident: Bobix]
  * *Citation:* `[Source: NODE_A_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 252 | UUID: 0e0c3cbd-7c7c-49c4-974e-57cca2da278c]`
* **NODE_A** [Software Event]: Software Event: Operator interaction event identifier
  * *Details:* Data Identifier: Operator interaction event identifier | Data Format: Format operator interaction event | Left FMS node: Master | Center FMS node: Standby | Right FMS node: Spare | Dual: Dual | [Event identifier: Operator interaction string new waypoint | Source fms node: First officer]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 100 | UUID: 13185fe5-e7ff-4c86-b8a0-33382ec3903b]`

**[10:11:57]**
* **NODE_A** [Operator Interaction]: Operator Interaction Event
  * *Details:* Dual mode: Dual | Master status: Master | Functional position: Captain | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 211.999573 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [FMS Operational Event: Optimized Step Selected | FMS node source: Captain | Event value: 17826333]
  * *Citation:* `[Source: NODE_A_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 254 | UUID: 9c776e43-b2cd-4fd8-bbaf-cd7c004faf92]`

**[10:11:58]**
* **NODE_A** [Operator Interaction] (x3 occurrences collapsed): Operator Interaction Event
  * *Details:* Dual mode: Dual | Master status: Master | Functional position: Captain | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 211.999451 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [FMS Operational Event: Performance Data Changed | FMS node source: Standby | Event value: 131098]
  * *Citation:* `[Source: NODE_A_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 255 | UUID: 95e0d163-8993-40c1-b289-98d179f440de]`
* **NODE_C** [Operator Interaction]: Operator interaction string new waypoint
  * *Details:* Dual mode: Dual | Master status: Spare | Functional position: First officer | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 211.999649 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | Flight plan source - high: Active | Flight plan source - low: ActPrimary | Display system source: Operator interaction display system right | [Operator Interaction Event: Operator interaction string new waypoint | Event status: Operator interaction entered | Event value: 131098 | Airport Identifier: Mosma | Airport Latitude: -171936.83 | Airport Longitude: -1495037.59]
  * *Citation:* `[Source: NODE_C_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 253 | UUID: 9b18519d-b058-4524-857b-3c27d2d4d914]`
* **NODE_C** [Operator Interaction] (x3 occurrences collapsed): Operator Interaction Event
  * *Details:* Dual mode: Dual | Master status: Spare | Functional position: First officer | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 211.999649 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [Fix ident: Bobix]
  * *Citation:* `[Source: NODE_C_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 254 | UUID: ed8ef946-944f-448c-875f-c9a7370f7314]`
* **NODE_C** [Software Event]: Software Event: Operator interaction event identifier
  * *Details:* Data Identifier: Operator interaction event identifier | Data Format: Format operator interaction event | Left FMS node: Master | Center FMS node: Standby | Right FMS node: Spare | Dual: Dual | [Event identifier: Operator interaction string new waypoint | Source fms node: First officer]
  * *Citation:* `[Source: NODE_C_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 102 | UUID: 9f3246cf-f5cd-4001-96a8-78c6a86f00ca]`

**[10:11:59]**
* **NODE_A** [Operator Interaction]: Operator interaction insert temporary
  * *Details:* Dual mode: Dual | Master status: Master | Functional position: Captain | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 211.999451 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | Flight plan source - high: Temporary Efb | Flight plan source - low: TmpyPrimary | Display system source: Operator interaction display system right | [Operator Interaction Event: Operator interaction insert temporary | Event status: Operator interaction entered | Event value: 131098]
  * *Citation:* `[Source: NODE_A_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 258 | UUID: 70877f03-005e-4f91-9796-cae487532de5]`
* **NODE_A** [Operator Interaction] (x2 occurrences collapsed): Operator Interaction Event
  * *Citation:* `[Source: NODE_A_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 259 | UUID: e1e34486-0765-4b08-8cc0-3bd66954d4be]`
* **NODE_A** [Software Event] (x2 occurrences collapsed): Software Event: Operator interaction event identifier
  * *Details:* Data Identifier: Operator interaction event identifier | Data Format: Format operator interaction event | Left FMS node: Master | Center FMS node: Standby | Right FMS node: Spare | Dual: Dual | [Event identifier: Operator interaction insert temporary | Source fms node: First officer]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 101 | UUID: b3fb6f45-58e8-49b9-a174-60eae4dc7996]`
* **NODE_C** [Operator Interaction] (x2 occurrences collapsed): Operator Interaction Event
  * *Details:* Dual mode: Dual | Master status: Spare | Functional position: First officer | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 211.999420 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [FMS Operational Event: Performance Data Changed | FMS node source: Standby | Event value: 131098]
  * *Citation:* `[Source: NODE_C_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 257 | UUID: 8af06a90-4c8b-40ef-9cdc-3f28b386410e]`

**[10:12:00]**
* **NODE_C** [Operator Interaction]: Operator Interaction Event
  * *Details:* Dual mode: Dual | Master status: Spare | Functional position: First officer | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 211.999451 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [FMS Operational Event: Optimized Step Selected | FMS node source: Captain | Event value: 131091]
  * *Citation:* `[Source: NODE_C_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 259 | UUID: dd1b6aa5-f69a-4615-9a63-258ce6de7046]`
* **NODE_C** [Operator Interaction]: Operator interaction insert temporary
  * *Details:* Dual mode: Dual | Master status: Spare | Functional position: First officer | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 211.999451 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | Flight plan source - high: Temporary Efb | Flight plan source - low: TmpyPrimary | Display system source: Operator interaction display system right | [Operator Interaction Event: Operator interaction insert temporary | Event status: Operator interaction entered | Event value: 131098]
  * *Citation:* `[Source: NODE_C_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 260 | UUID: 0a4ebe93-1b17-4b36-9c7c-99d8b272c30d]`
* **NODE_C** [Operator Interaction]: Operator Interaction Event
  * *Citation:* `[Source: NODE_C_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 261 | UUID: c590d2ce-7ed0-45ba-82d5-46ffdf770ebf]`
* **NODE_C** [Software Event]: Software Event: Operator interaction event identifier
  * *Details:* Data Identifier: Operator interaction event identifier | Data Format: Format operator interaction event | Left FMS node: Master | Center FMS node: Standby | Right FMS node: Spare | Dual: Dual | [Event identifier: Operator interaction insert temporary | Source fms node: First officer]
  * *Citation:* `[Source: NODE_C_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 103 | UUID: 9b372408-e248-4e13-a5ba-8c211def66fc]`

**[10:12:01]**
* **NODE_C** [Operator Interaction]: Operator Interaction Event
  * *Details:* Dual mode: Dual | Master status: Spare | Functional position: First officer | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 211.999466 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [FMS Operational Event: Optimized Step Selected | FMS node source: Captain | Event value: 26477079]
  * *Citation:* `[Source: NODE_C_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 262 | UUID: 434e06ac-9255-4f57-9c8e-1834cd4f28d0]`
* **NODE_C** [Software Event]: Software Event: Operator interaction event identifier
  * *Details:* Data Identifier: Operator interaction event identifier | Data Format: Format operator interaction event | Left FMS node: Master | Center FMS node: Standby | Right FMS node: Spare | Dual: Dual | [Event identifier: Operator interaction insert temporary | Source fms node: First officer]
  * *Citation:* `[Source: NODE_C_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 104 | UUID: 6ea7c20d-5c76-4b4a-aff6-b41c3c2a6b41]`

**[10:12:04]**
* **NODE_A** [Fault History]: Rnp legs transmitter io (Code: 6)
  * *Details:* Serial Number: 182 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 11629 | Fault Code: 6 | Sub Code: 93 | Fault Name: Rnp legs transmitter io | Date and Time: 2032-06-18 10:12:04 AM | Module Temperature: 40 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 8 | Application Data: ?~J;
  * *Citation:* `[Source: NODE_A_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 182 | UUID: 3702e7be-d037-4375-b99c-17ecc5373711]`

**[10:12:05]**
* **NODE_B** [Fault History]: Rnp integrity validation receiver timeout (Code: 6)
  * *Details:* Serial Number: 144 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 11633 | Fault Code: 6 | Sub Code: 97 | Fault Name: Rnp integrity validation receiver timeout | Date and Time: 2032-06-18 10:12:05 AM | Module Temperature: 37 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 8 | Application Data: ?~J;
  * *Citation:* `[Source: NODE_B_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 144 | UUID: 3d0c2301-f74c-4817-aa8b-c7b6a28088b7]`
