# Incident Cluster: cluster-2cbd6097
**Date:** 2032-06-18
**Duration:** 13:20:33 to 13:21:31
**Nodes Involved:** NODE_A, NODE_C
**Total Events:** 27 (Filtered from 29 raw logs)

## Timeline Transcript

**[13:20:33]**
* **NODE_C** [Software Event]: Software Event: Autopilot identifier a350
  * *Details:* Data Identifier: Autopilot identifier a350 | Data Format: Format fixed str | Left FMS node: Master | Right FMS node: Spare | Dual: Dual | Latitude: 51.419777 | Longitude: 6.572720 | Altitude: 2870.024658 | [Event identifier: 68 | Autopilot data: Auto pilot 1 is off]
  * *Citation:* `[Source: NODE_C_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 106 | UUID: 87d8aee3-0b00-45e4-8ba1-2f04711a381d]`

**[13:20:34]**
* **NODE_A** [Software Event]: Software Event: Autopilot identifier a350
  * *Details:* Data Identifier: Autopilot identifier a350 | Data Format: Format fixed str | Left FMS node: Master | Right FMS node: Spare | Dual: Dual | Latitude: 51.419796 | Longitude: 6.572608 | Altitude: 2870.011475 | [Event identifier: 68 | Autopilot data: Auto pilot 1 is off]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 281 | UUID: e166d365-d84a-4378-9de8-0fb4bf9deb2a]`

**[13:20:56]**
* **NODE_A** [Software Event]: Software Event: S pad message identifier l
  * *Details:* Data Identifier: S pad message identifier l | Data Format: Format one unsign 32 | Left FMS node: Master | Right FMS node: Spare | Dual: Dual | [L message identifier: New crz altitude]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 282 | UUID: ebf36c2d-3d1f-4a1e-a040-2323036f2463]`
* **NODE_C** [Software Event]: Software Event: S pad message identifier l
  * *Details:* Data Identifier: S pad message identifier l | Data Format: Format one unsign 32 | Left FMS node: Master | Right FMS node: Spare | Dual: Dual | [L message identifier: New crz altitude]
  * *Citation:* `[Source: NODE_C_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 107 | UUID: 856c6d97-b351-4705-9387-ec0dc34b2170]`
* **NODE_C** [Software Event]: Software Event: S pad message identifier r
  * *Details:* Data Identifier: S pad message identifier r | Data Format: Format one unsign 32 | Left FMS node: Master | Right FMS node: Spare | Dual: Dual | [R message identifier: New crz altitude]
  * *Citation:* `[Source: NODE_C_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 108 | UUID: b1e93ab0-43a2-4902-bcd2-def2807745b6]`
* **NODE_C** [Software Event]: Software Event: Flap tomconf identifier
  * *Details:* Data Identifier: Flap tomconf identifier | Data Format: Format str 44 | Left FMS node: Master | Right FMS node: Spare | Dual: Dual | [Flaps position data: Flaps Position: 2]
  * *Citation:* `[Source: NODE_C_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 109 | UUID: d90d9728-d5ef-4614-b2ee-4221fd4d8f40]`

**[13:20:57]**
* **NODE_A** [Software Event]: Software Event: Flap tomconf identifier
  * *Details:* Data Identifier: Flap tomconf identifier | Data Format: Format str 44 | Left FMS node: Master | Right FMS node: Spare | Dual: Dual | [Flaps position data: Flaps Position: 2]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 283 | UUID: fcc8f39e-4906-4cdc-bbce-e7d0afcf9148]`
* **NODE_A** [Software Event]: Software Event: S pad message identifier r
  * *Details:* Data Identifier: S pad message identifier r | Data Format: Format one unsign 32 | Left FMS node: Master | Right FMS node: Spare | Dual: Dual | [R message identifier: New crz altitude]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 284 | UUID: fe848ab0-b4f8-48a2-805b-6ed6c72c4d32]`

**[13:20:58]**
* **NODE_A** [Software Event]: Software Event: Air ground identifier
  * *Details:* Data Identifier: Air ground identifier | Data Format: Format fixed str | Left FMS node: Master | Right FMS node: Spare | Dual: Dual | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 2870.011475 | [Event identifier: 68 | Air ground status: 49]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 285 | UUID: 40c97ec3-1207-4132-b43d-3867c96ea7e7]`
* **NODE_C** [Software Event]: Software Event: Air ground identifier
  * *Details:* Data Identifier: Air ground identifier | Data Format: Format fixed str | Left FMS node: Master | Right FMS node: Spare | Dual: Dual | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 2870.024658 | [Event identifier: 68 | Air ground status: 49]
  * *Citation:* `[Source: NODE_C_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 110 | UUID: 3c0acd5d-7d0c-4aa0-9e5e-238039b7d173]`

**[13:21:01]**
* **NODE_C** [Software Event]: Software Event: Nose gear identifier
  * *Details:* Data Identifier: Nose gear identifier | Data Format: Format fixed str | Left FMS node: Master | Right FMS node: Spare | Dual: Dual | [Event identifier: 68 | Main gear out: Nose gear is down]
  * *Citation:* `[Source: NODE_C_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 111 | UUID: 6ec95e55-cfba-4fe0-afe9-3725e8463210]`

**[13:21:02]**
* **NODE_A** [Software Event]: Software Event: Nose gear identifier
  * *Details:* Data Identifier: Nose gear identifier | Data Format: Format fixed str | Left FMS node: Master | Right FMS node: Spare | Dual: Dual | [Event identifier: 68 | Main gear out: Nose gear is down]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 286 | UUID: f1b422ff-9f0a-44f8-bcf2-dc86e1fc97e8]`
* **NODE_C** [Software Event]: Software Event: Selection vertical speed identifier
  * *Details:* Data Identifier: Selection vertical speed identifier | Data Format: Format one float 32 | Left FMS node: Master | Right FMS node: Spare | Dual: Dual
  * *Citation:* `[Source: NODE_C_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 112 | UUID: a4dcc60e-50e0-4747-b8ae-3b532e1d41d4]`
* **NODE_C** [Software Event]: Software Event: Selection speed identifier
  * *Details:* Data Identifier: Selection speed identifier | Data Format: Format one float 32 | Left FMS node: Master | Right FMS node: Spare | Dual: Dual | [Selection speed: 140.179398]
  * *Citation:* `[Source: NODE_C_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 113 | UUID: 1596a310-7044-4675-a902-677344547d1e]`

**[13:21:03]**
* **NODE_A** [Software Event]: Software Event: Selection speed identifier
  * *Details:* Data Identifier: Selection speed identifier | Data Format: Format one float 32 | Left FMS node: Master | Right FMS node: Spare | Dual: Dual | [Selection speed: 140.179398]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 287 | UUID: d5f5781d-fd83-4814-a165-77676cc570b2]`

**[13:21:12]**
* **NODE_C** [Software Event]: Software Event: Selection altitude identifier
  * *Details:* Data Identifier: Selection altitude identifier | Data Format: Format one float 32 | Left FMS node: Master | Right FMS node: Spare | Dual: Dual | [Selected altitude data: 440.000000]
  * *Citation:* `[Source: NODE_C_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 114 | UUID: 6eb9a954-18d6-4bf7-8d21-91fd582cbe5d]`
* **NODE_C** [Software Event]: Software Event: Selection heading identifier
  * *Details:* Data Identifier: Selection heading identifier | Data Format: Format one float 32 | Left FMS node: Master | Right FMS node: Spare | Dual: Dual | [Selection heading: 66.000000]
  * *Citation:* `[Source: NODE_C_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 115 | UUID: 56017bd0-e75f-47f0-8ef1-01351c2109a8]`

**[13:21:13]**
* **NODE_A** [Software Event]: Software Event: Selection altitude identifier
  * *Details:* Data Identifier: Selection altitude identifier | Data Format: Format one float 32 | Left FMS node: Master | Right FMS node: Spare | Dual: Dual | [Selected altitude data: 440.000000]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 288 | UUID: f8bd420f-b455-488e-b13a-5a5d30f7a754]`
* **NODE_A** [Software Event]: Software Event: Selection heading identifier
  * *Details:* Data Identifier: Selection heading identifier | Data Format: Format one float 32 | Left FMS node: Master | Right FMS node: Spare | Dual: Dual | [Selection heading: 66.000000]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 289 | UUID: 10784247-3d08-46da-b448-4845218d7afb]`

**[13:21:29]**
* **NODE_C** [Operator Interaction] (x2 occurrences collapsed): Operator Interaction Event
  * *Details:* Dual mode: Dual | Master status: Spare | Functional position: First officer | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 2870.024658 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [FMS Operational Event: phase change | FMS node source: Standby | Event value: 65547]
  * *Citation:* `[Source: NODE_C_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 52 | UUID: efab87c7-d68f-4edc-817d-567fddbdd2d6]`

**[13:21:30]**
* **NODE_A** [Operator Interaction] (x2 occurrences collapsed): Operator Interaction Event
  * *Details:* Dual mode: Dual | Master status: Master | Functional position: Captain | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 2870.011475 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [FMS Operational Event: phase change | FMS node source: Standby | Event value: 65547]
  * *Citation:* `[Source: NODE_A_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 240 | UUID: 60894bbb-8691-48d9-b3d6-9003796dbb81]`
* **NODE_A** [Software Event]: Software Event: Flight phase identifier
  * *Details:* Data Identifier: Flight phase identifier | Data Format: Format fixed str | Left FMS node: Master | Right FMS node: Spare | Dual: Dual | [Event identifier: 68 | Flight phase previous: Approach | Flight phase current: Done]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 290 | UUID: 95f8f9f7-d2bf-42f1-a39e-090da9160975]`
* **NODE_C** [Operator Interaction]: Operator Interaction Event
  * *Details:* Dual mode: Dual | Master status: Spare | Functional position: First officer | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 2870.024658 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [FMS Operational Event: Vertical Guidance Sequence Changed | FMS node source: Standby | Event value: 65539]
  * *Citation:* `[Source: NODE_C_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 54 | UUID: 8d95f5a9-9ecb-4ab3-b5c3-faad6139240a]`
* **NODE_C** [Software Event]: Software Event: Flight phase identifier
  * *Details:* Data Identifier: Flight phase identifier | Data Format: Format fixed str | Left FMS node: Master | Right FMS node: Spare | Dual: Dual | [Event identifier: 68 | Flight phase previous: Approach | Flight phase current: Done]
  * *Citation:* `[Source: NODE_C_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 116 | UUID: f4e70758-a8f4-4d34-8471-bf7c8aad2ff4]`

**[13:21:31]**
* **NODE_A** [Operator Interaction]: Operator Interaction Event
  * *Details:* Dual mode: Dual | Master status: Master | Functional position: Captain | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 2870.011475 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [FMS Operational Event: Vertical Guidance Sequence Changed | FMS node source: Standby | Event value: 65539]
  * *Citation:* `[Source: NODE_A_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 242 | UUID: f0fdbbe6-008d-465f-b8fb-632f80a5afa2]`
* **NODE_A** [Software Event]: Software Event: Lnav identifier
  * *Details:* Data Identifier: Lnav identifier | Data Format: Format fixed str | Left FMS node: Master | Right FMS node: Spare | Dual: Dual | [Event identifier: 68 | L navigation status: L navigation hdg]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 291 | UUID: 4f139b76-8e05-49ea-81c3-8b7e41b94529]`
* **NODE_C** [Software Event]: Software Event: Lnav identifier
  * *Details:* Data Identifier: Lnav identifier | Data Format: Format fixed str | Left FMS node: Master | Right FMS node: Spare | Dual: Dual | [Event identifier: 68 | L navigation status: L navigation hdg]
  * *Citation:* `[Source: NODE_C_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 117 | UUID: 9d4dfa87-09b9-43a2-be17-8d3dd1ab46b8]`
