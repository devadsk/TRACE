# Incident Cluster: cluster-9e50cb97
**Date:** 2032-06-18
**Duration:** 09:14:25 to 09:15:20
**Nodes Involved:** NODE_C
**Total Events:** 27 (Filtered from 37 raw logs)

## Timeline Transcript

**[09:14:25]**
* **NODE_C** [Fault History]: Scheduled FMS Activity Missed Timing Requirement (Code: 6000)
  * *Details:* Serial Number: 77 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6000 | Fault Code: 6000 | Sub Code: Thunderbolt fault | Fault Name: Scheduled FMS Activity Missed Timing Requirement | Date and Time: 2032-06-18 09:14:25 AM | Module Temperature: 38 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 50 | Application Data: Deadline miss` Background service - 65563;
  * *Citation:* `[Source: NODE_C_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 77 | UUID: c2c2da4c-048d-454f-9049-bfd2dd66f022]`
* **NODE_C** [Operator Interaction] (x2 occurrences collapsed): Operator Interaction Event
  * *Details:* Dual mode: Single | Master status: Master | Functional position: First officer | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 212.000977 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [FMS Operational Event: clear altitude | FMS node source: Captain | Event value: 17826345]
  * *Citation:* `[Source: NODE_C_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 6 | UUID: a7bd382e-99dc-485c-9d3d-782afb60eaab]`

**[09:14:26]**
* **NODE_C** [Operator Interaction]: Operator Interaction Event
  * *Details:* Dual mode: Single | Master status: Master | Functional position: First officer | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 212.000839 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [FMS Operational Event: no phase change | FMS node source: Captain | Event value: 131076]
  * *Citation:* `[Source: NODE_C_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 8 | UUID: 486a6c3e-1049-40c4-89f9-922a0b9a4b0f]`

**[09:14:28]**
* **NODE_C** [Software Event]: Software Event: Selection altitude identifier
  * *Details:* Data Identifier: Selection altitude identifier | Data Format: Format one float 32 | Right FMS node: Master | Dual: Single | [Selected altitude data: 18000.000000]
  * *Citation:* `[Source: NODE_C_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 12 | UUID: 8da0397e-56ca-447b-b907-84974590ef74]`

**[09:14:48]**
* **NODE_C** [Operator Interaction]: Operator interaction enter origin
  * *Details:* Dual mode: Single | Master status: Master | Functional position: First officer | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 212.002243 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | Flight plan source - high: Active | Flight plan source - low: ActPrimary | Display system source: Operator interaction display system right | [Operator Interaction Event: Operator interaction enter origin | Event status: Operator interaction entered | Event value: 131083 | Airport Identifier: Eddf | Airport Latitude: 500159.90 | Airport Longitude: 83413.63]
  * *Citation:* `[Source: NODE_C_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 9 | UUID: 6a38dc4b-f9b3-4d40-9c56-6fb4851d5a24]`
* **NODE_C** [Operator Interaction] (x2 occurrences collapsed): Operator Interaction Event
  * *Citation:* `[Source: NODE_C_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 10 | UUID: 87bb50e7-691b-4cf1-979e-83735031a631]`
* **NODE_C** [Software Event] (x2 occurrences collapsed): Software Event: Operator interaction event identifier
  * *Details:* Data Identifier: Operator interaction event identifier | Data Format: Format operator interaction event | Right FMS node: Master | Dual: Single | [Event identifier: Operator interaction enter origin | Source fms node: First officer]
  * *Citation:* `[Source: NODE_C_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 13 | UUID: d462ebba-8d70-4ed7-8937-bf4fee98a85a]`

**[09:14:49]**
* **NODE_C** [Software Event]: Software Event: S pad message identifier l
  * *Details:* Data Identifier: S pad message identifier l | Data Format: Format one unsign 32 | Right FMS node: Master | Dual: Single | [L message identifier: Check data base cycle]
  * *Citation:* `[Source: NODE_C_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 15 | UUID: 462dffc2-eb04-43cf-93ba-7f49b03c6504]`
* **NODE_C** [Software Event]: Software Event: S pad message identifier r
  * *Details:* Data Identifier: S pad message identifier r | Data Format: Format one unsign 32 | Right FMS node: Master | Dual: Single | [R message identifier: Check data base cycle]
  * *Citation:* `[Source: NODE_C_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 16 | UUID: c9c84d23-d134-4406-9727-0cbeff4e0942]`

**[09:14:50]**
* **NODE_C** [Operator Interaction]: Operator interaction enter destination
  * *Details:* Dual mode: Single | Master status: Master | Functional position: First officer | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 212.002121 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | Flight plan source - high: Active | Flight plan source - low: ActPrimary | Display system source: Operator interaction display system right | [Operator Interaction Event: Operator interaction enter destination | Event status: Operator interaction entered | Event value: 131110 | Airport Identifier: Eddf | Airport Latitude: 500159.90 | Airport Longitude: 83413.63]
  * *Citation:* `[Source: NODE_C_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 12 | UUID: 4b4fbbf4-71bf-4b59-ae0f-5337886203d9]`
* **NODE_C** [Operator Interaction]: Operator Interaction Event
  * *Citation:* `[Source: NODE_C_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 13 | UUID: 47060121-2f12-4496-8904-f9701c9e3a16]`
* **NODE_C** [Software Event]: Software Event: Operator interaction event identifier
  * *Details:* Data Identifier: Operator interaction event identifier | Data Format: Format operator interaction event | Right FMS node: Master | Dual: Single | [Event identifier: Operator interaction enter destination | Source fms node: First officer]
  * *Citation:* `[Source: NODE_C_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 17 | UUID: 4cec842b-c823-4a7a-9c49-3edd4f97a1b6]`

**[09:14:51]**
* **NODE_C** [Operator Interaction] (x2 occurrences collapsed): Operator Interaction Event
  * *Details:* Dual mode: Single | Master status: Master | Functional position: First officer | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 212.002090 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [FMS Operational Event: Vertical Guidance Sequence Changed | FMS node source: Captain | Event value: 17826347]
  * *Citation:* `[Source: NODE_C_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 14 | UUID: fe514c28-fa85-482b-9fd9-30fb1a1d66b4]`
* **NODE_C** [Software Event] (x2 occurrences collapsed): Software Event: Operator interaction event identifier
  * *Details:* Data Identifier: Operator interaction event identifier | Data Format: Format operator interaction event | Right FMS node: Master | Dual: Single | [Event identifier: Operator interaction enter destination | Source fms node: First officer]
  * *Citation:* `[Source: NODE_C_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 18 | UUID: 9b134df2-5a5f-496c-b8a9-dd1f7daa643d]`

**[09:15:13]**
* **NODE_C** [Operator Interaction]: Operator interaction enter approach
  * *Details:* Dual mode: Single | Master status: Master | Functional position: First officer | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 211.997635 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | Flight plan source - high: Active | Flight plan source - low: ActPrimary | Display system source: Operator interaction display system right | [Operator Interaction Event: Operator interaction enter approach | Event status: Operator interaction entered | Event value: 131110 | Airport Identifier: 25L | Airport Latitude: 500224.15 | Airport Longitude: 83511.48]
  * *Citation:* `[Source: NODE_C_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 16 | UUID: 10b06ce3-0ecc-4fee-91fb-fcd58f945151]`
* **NODE_C** [Operator Interaction]: Operator Interaction Event
  * *Citation:* `[Source: NODE_C_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 17 | UUID: 06f9046c-f56c-4fbd-8224-e70b23faebd3]`
* **NODE_C** [Software Event]: Software Event: Operator interaction event identifier
  * *Details:* Data Identifier: Operator interaction event identifier | Data Format: Format operator interaction event | Right FMS node: Master | Dual: Single | [Event identifier: Operator interaction enter approach | Source fms node: First officer]
  * *Citation:* `[Source: NODE_C_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 20 | UUID: 8e0dcf5b-a22b-46e3-9f70-f19408d0b446]`

**[09:15:20]**
* **NODE_C** [Fault History]: Scheduled FMS Activity Missed Timing Requirement (Code: 6000)
  * *Details:* Serial Number: 78 | Report Name: Fault repository 01 Public FMS Artifact | Context Identifier: 6 | Encoded Fault: 6000 | Fault Code: 6000 | Sub Code: Thunderbolt fault | Fault Name: Scheduled FMS Activity Missed Timing Requirement | Date and Time: 2032-06-18 09:15:20 AM | Module Temperature: 38 | Member System Equipment Identifier: 540 | Member System Destination Identifier: 1 | Current Recovery Type: No Recovery Action | Module State: Operational | Context State: Cs executing e | Last Context Reset Reason: No Recovery Action | Last Module Reset Reason: FMS Service Restart | Fault Exception: False | Extended Record: False | Application Data Size: 50 | Application Data: Deadline miss` Background service - 65554;
  * *Citation:* `[Source: NODE_C_FAULT_REPOSITORY_01_1_Decoded_report.html | Seq: 78 | UUID: 7872b6ef-0597-4636-a958-242db28a7d55]`
* **NODE_C** [Operator Interaction]: Operator interaction enter arrival procedure
  * *Details:* Dual mode: Single | Master status: Master | Functional position: First officer | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 211.997223 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | Flight plan source - high: Temporary Efb | Flight plan source - low: TmpyPrimary | Display system source: Operator interaction display system right | [Operator Interaction Event: Operator interaction enter arrival procedure | Event status: Operator interaction entered | Event value: 17826314]
  * *Citation:* `[Source: NODE_C_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 18 | UUID: e79d78b7-96d0-4767-aab9-20f748bdf69f]`
* **NODE_C** [Operator Interaction]: Operator Interaction Event
  * *Citation:* `[Source: NODE_C_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 19 | UUID: 8d006316-f6ed-495f-8e45-36faa8d4ec35]`
* **NODE_C** [Operator Interaction]: Operator interaction flight plan orient destination event
  * *Details:* Dual mode: Single | Master status: Master | Functional position: First officer | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 211.997467 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | Flight plan source - high: Temporary Efb | Flight plan source - low: TmpyPrimary | Display system source: Operator interaction display system right | [Operator Interaction Event: Operator interaction flight plan orient destination event | Event status: Operator interaction entered | Event value: 26477068]
  * *Citation:* `[Source: NODE_C_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 20 | UUID: d7a558bb-ca8b-4ca5-85ab-22182c8fb9f1]`
* **NODE_C** [Operator Interaction]: Operator Interaction Event
  * *Citation:* `[Source: NODE_C_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 21 | UUID: 4060f29d-f712-46a9-9e96-19f39ed62837]`
* **NODE_C** [Operator Interaction]: Operator interaction initialize offset data
  * *Details:* Dual mode: Single | Master status: Master | Functional position: First officer | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 211.995972 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | Flight plan source - high: Temporary Efb | Flight plan source - low: TmpyPrimary | Display system source: Operator interaction display system right | [Operator Interaction Event: Operator interaction initialize offset data | Event status: Operator interaction entered | Event value: 26477139]
  * *Citation:* `[Source: NODE_C_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 22 | UUID: b23db76f-164d-4e77-9d07-2645541050ac]`
* **NODE_C** [Operator Interaction] (x2 occurrences collapsed): Operator Interaction Event
  * *Details:* Dual mode: Single | Master status: Master | Functional position: First officer | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 211.995972 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [Fix ident: Debhi]
  * *Citation:* `[Source: NODE_C_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 23 | UUID: d6c21743-436c-4edd-a191-25b55b2866d1]`
* **NODE_C** [Operator Interaction]: Operator interaction initialize offset data
  * *Details:* Dual mode: Single | Master status: Master | Functional position: First officer | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 211.998688 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | Flight plan source - high: Temporary Efb | Flight plan source - low: TmpyPrimary | Display system source: Operator interaction display system right | [Operator Interaction Event: Operator interaction initialize offset data | Event status: Operator interaction entered | Event value: 26477346]
  * *Citation:* `[Source: NODE_C_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 25 | UUID: 256b103f-140b-4d55-9bed-2538bc7d1030]`
* **NODE_C** [Operator Interaction] (x2 occurrences collapsed): Operator Interaction Event
  * *Details:* Dual mode: Single | Master status: Master | Functional position: First officer | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 211.998688 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [Fix ident: Debhi]
  * *Citation:* `[Source: NODE_C_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 26 | UUID: 3bfdede2-395a-487e-aa2d-fd5f8691af35]`
* **NODE_C** [Software Event] (x4 occurrences collapsed): Software Event: Operator interaction event identifier
  * *Details:* Data Identifier: Operator interaction event identifier | Data Format: Format operator interaction event | Right FMS node: Master | Dual: Single | [Event identifier: Operator interaction enter arrival procedure | Source fms node: First officer]
  * *Citation:* `[Source: NODE_C_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 21 | UUID: 12140df9-3482-4306-b285-88677b28c786]`
