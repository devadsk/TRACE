# Incident Cluster: cluster-28d5f74c
**Date:** 2032-06-18
**Duration:** 09:00:00 to 09:01:28
**Nodes Involved:** NODE_A, NODE_C
**Total Events:** 13 (Filtered from 13 raw logs)

## Timeline Transcript

**[09:00:00]**
* **NODE_A** [Software Event]: Software Event: S pad message identifier l
  * *Details:* Data Identifier: S pad message identifier l | Data Format: Format one unsign 32 | Left FMS node: Master | Center FMS node: Standby | Right FMS node: Spare | Dual: Dual | [L message identifier: Navigation primary]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 27 | UUID: 8b12e8c3-937e-4ecb-91c2-451a68e664d8]`

**[09:00:31]**
* **NODE_A** [Operator Interaction]: Navigation Database Refresh Cycle
  * *Details:* Dual mode: Dual | Master status: Master | Functional position: Captain | Latitude: 43.619164 | Longitude: 1.371921 | Altitude: 511.995605 | Magnetic track: -37.380981 | Calibrated airspeed data: 35.000000 | Flight plan source - high: Active | Flight plan source - low: ActPrimary | Display system source: Operator interaction display system right | [Operator Interaction Event: Navigation Database Refresh Cycle | Event status: Operator interaction entered | Event value: 17826343]
  * *Citation:* `[Source: NODE_A_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 15 | UUID: 675e178f-7e11-4cb5-9198-c92aa465c74c]`
* **NODE_A** [Software Event]: Software Event: Operator interaction event identifier
  * *Details:* Data Identifier: Operator interaction event identifier | Data Format: Format operator interaction event | Left FMS node: Master | Center FMS node: Standby | Right FMS node: Spare | Dual: Dual | [Event identifier: Navigation Database Refresh Cycle | Source fms node: First officer]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 28 | UUID: fe5eed1f-b34e-4347-b507-47eb7fed05e5]`
* **NODE_C** [Operator Interaction]: Navigation Database Refresh Cycle
  * *Details:* Dual mode: Dual | Master status: Spare | Functional position: First officer | Latitude: 43.619164 | Longitude: 1.371921 | Altitude: 511.995514 | Magnetic track: -37.380981 | Calibrated airspeed data: 35.000000 | Flight plan source - high: Active | Flight plan source - low: ActPrimary | Display system source: Operator interaction display system right | [Operator Interaction Event: Navigation Database Refresh Cycle | Event status: Operator interaction entered | Event value: 17826343]
  * *Citation:* `[Source: NODE_C_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 17 | UUID: 028cf4f9-5ee4-408a-8b38-da9fe99f125f]`
* **NODE_C** [Software Event]: Software Event: Operator interaction event identifier
  * *Details:* Data Identifier: Operator interaction event identifier | Data Format: Format operator interaction event | Left FMS node: Master | Center FMS node: Standby | Right FMS node: Spare | Dual: Dual | [Event identifier: Navigation Database Refresh Cycle | Source fms node: First officer]
  * *Citation:* `[Source: NODE_C_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 28 | UUID: 5155c5b5-d3f9-45b4-b4aa-c370d0c05e19]`
* **NODE_C** [Software Event]: Software Event: S pad message identifier l
  * *Details:* Data Identifier: S pad message identifier l | Data Format: Format one unsign 32 | Left FMS node: Master | Center FMS node: Standby | Right FMS node: Spare | Dual: Dual | [L message identifier: Navigation primary]
  * *Citation:* `[Source: NODE_C_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 29 | UUID: 5cae596f-baca-4b86-af6d-788684675d1f]`

**[09:00:32]**
* **NODE_A** [Operator Interaction]: Operator Interaction Event
  * *Details:* Dual mode: Dual | Master status: Master | Functional position: Captain | Latitude: 43.619164 | Longitude: 1.371921 | Altitude: 511.995270 | Magnetic track: -37.380981 | Calibrated airspeed data: 35.000000 | [FMS Operational Event: Vertical Guidance Sequence Changed | FMS node source: Standby | Event value: 17826305]
  * *Citation:* `[Source: NODE_A_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 16 | UUID: fef99cfd-c490-47f2-b43b-c720a9058ae9]`
* **NODE_C** [Operator Interaction]: Operator Interaction Event
  * *Details:* Dual mode: Dual | Master status: Spare | Functional position: First officer | Latitude: 43.619164 | Longitude: 1.371921 | Altitude: 511.995117 | Magnetic track: -37.380981 | Calibrated airspeed data: 35.000000 | [FMS Operational Event: Vertical Guidance Sequence Changed | FMS node source: Standby | Event value: 17826305]
  * *Citation:* `[Source: NODE_C_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 18 | UUID: 6c5b37c2-eb69-44e9-8af8-22e2f713a2d2]`

**[09:00:33]**
* **NODE_A** [Software Event]: Software Event: Lnav identifier
  * *Details:* Data Identifier: Lnav identifier | Data Format: Format fixed str | Left FMS node: Master | Center FMS node: Standby | Right FMS node: Spare | Dual: Dual | [Event identifier: 68 | L navigation status: L navigation hdg]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 29 | UUID: ad3e2a81-107e-4c84-833f-6f4b78a309f6]`
* **NODE_C** [Software Event]: Software Event: Lnav identifier
  * *Details:* Data Identifier: Lnav identifier | Data Format: Format fixed str | Left FMS node: Master | Center FMS node: Standby | Right FMS node: Spare | Dual: Dual | [Event identifier: 68 | L navigation status: L navigation hdg]
  * *Citation:* `[Source: NODE_C_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 30 | UUID: 9c74f569-f16a-4887-bddd-54a51cf5c24c]`

**[09:01:21]**
* **NODE_C** [Software Event]: Software Event: Dual mode identifier
  * *Details:* Data Identifier: Dual mode identifier | Data Format: Format fixed str | Left FMS node: Master | Center FMS node: Standby | Right FMS node: Spare | Dual: Single | [Event identifier: 68 | Operational dual mode: Operational dual mode Changed]
  * *Citation:* `[Source: NODE_C_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 31 | UUID: 864cc738-4a69-413b-ae93-75b2e7398c9b]`

**[09:01:22]**
* **NODE_C** [Software Event]: Software Event: Data link comm master identifier
  * *Details:* Data Identifier: Data link comm master identifier | Data Format: Format fixed str | Left FMS node: Master | Center FMS node: Standby | Right FMS node: Spare | Dual: Single | [Event identifier: 68 | Data link comm master status log: Data link comm slave to master]
  * *Citation:* `[Source: NODE_C_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 32 | UUID: 6c4e19fb-3c5e-4d58-b9d8-40191be60f8a]`

**[09:01:28]**
* **NODE_C** [Software Event]: Software Event: Master spare identifier
  * *Details:* Data Identifier: Master spare identifier | Data Format: Format fixed str | Right FMS node: Master | Dual: Single | [Event identifier: 68 | FMS node position: Operational master spare Changed]
  * *Citation:* `[Source: NODE_C_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 33 | UUID: 2839019f-41ec-4a9e-b922-d9ba318e8106]`
