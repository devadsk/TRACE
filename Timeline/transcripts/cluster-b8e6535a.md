# Incident Cluster: cluster-b8e6535a
**Date:** 2032-06-18
**Duration:** 13:13:52 to 13:16:34
**Nodes Involved:** NODE_A, NODE_C
**Total Events:** 37 (Filtered from 48 raw logs)

## Timeline Transcript

**[13:13:52]**
* **NODE_A** [Operator Interaction] (x2 occurrences collapsed): Operator Interaction Event
  * *Details:* Dual mode: Dual | Master status: Master | Functional position: Captain | Latitude: 51.283031 | Longitude: 6.989126 | Altitude: 2870.011475 | Magnetic track: 1.049357 | Calibrated airspeed data: 195.500000 | [FMS Operational Event: clear altitude | FMS node source: Standby | Event value: 65543]
  * *Citation:* `[Source: NODE_A_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 225 | UUID: 053babec-f58f-44f2-a74d-df763aa99049]`
* **NODE_C** [Operator Interaction] (x3 occurrences collapsed): Operator Interaction Event
  * *Details:* Dual mode: Dual | Master status: Spare | Functional position: First officer | Latitude: 51.282974 | Longitude: 6.989119 | Altitude: 2870.024658 | Magnetic track: 1.049370 | Calibrated airspeed data: 195.500000 | [FMS Operational Event: clear altitude | FMS node source: Standby | Event value: 65543]
  * *Citation:* `[Source: NODE_C_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 37 | UUID: 63973ee5-1178-450a-bf58-8d431d0195ba]`

**[13:13:53]**
* **NODE_A** [Operator Interaction] (x3 occurrences collapsed): Operator Interaction Event
  * *Details:* Dual mode: Dual | Master status: Master | Functional position: Captain | Latitude: 51.283543 | Longitude: 6.989190 | Altitude: 2870.011475 | Magnetic track: 1.049661 | Calibrated airspeed data: 195.500000 | [FMS Operational Event: clear altitude | FMS node source: Standby | Event value: 65540]
  * *Citation:* `[Source: NODE_A_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 227 | UUID: 40055d60-76e1-49d8-876a-4828b40033bf]`
* **NODE_C** [Operator Interaction] (x3 occurrences collapsed): Operator Interaction Event
  * *Details:* Dual mode: Dual | Master status: Spare | Functional position: First officer | Latitude: 51.283733 | Longitude: 6.989213 | Altitude: 2870.024658 | Magnetic track: 1.049820 | Calibrated airspeed data: 195.500000 | [Fault/Event: Clear Altitude Change | Altitude: 3000 | data: [Redacted Payload]]
  * *Citation:* `[Source: NODE_C_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 40 | UUID: 6c07a520-3b57-467e-8211-c0a8ef41ec3b]`
* **NODE_C** [Software Event]: Software Event: Vnav at mode identifier
  * *Details:* Data Identifier: Vnav at mode identifier | Data Format: Format fixed str | Left FMS node: Master | Right FMS node: Spare | Dual: Dual | Latitude: 51.284134 | Longitude: 6.989264 | Altitude: 2870.024658 | [Event identifier: 68 | V navigation status: V navigation at none]
  * *Citation:* `[Source: NODE_C_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 76 | UUID: 9b0d8cca-4c7a-478b-bfda-b209e1992520]`

**[13:13:54]**
* **NODE_A** [Operator Interaction]: Operator Interaction Event
  * *Details:* Dual mode: Dual | Master status: Master | Functional position: Captain | Latitude: 51.284397 | Longitude: 6.989296 | Altitude: 2870.011475 | Magnetic track: 1.050275 | Calibrated airspeed data: 195.500000 | [FMS Operational Event: Optimized Step Selected | FMS node source: Captain | Event value: 65547]
  * *Citation:* `[Source: NODE_A_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 230 | UUID: 2bd9da7f-057d-4ed7-aae4-4dfe527490f3]`
* **NODE_A** [Software Event]: Software Event: Vnav at mode identifier
  * *Details:* Data Identifier: Vnav at mode identifier | Data Format: Format fixed str | Left FMS node: Master | Right FMS node: Spare | Dual: Dual | Latitude: 51.284000 | Longitude: 6.989247 | Altitude: 2870.011475 | [Event identifier: 68 | V navigation status: V navigation at none]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 255 | UUID: f6671d4a-cdcf-4c6c-a485-625871d0f4b4]`

**[13:13:57]**
* **NODE_C** [Software Event]: Software Event: Selection altitude identifier
  * *Details:* Data Identifier: Selection altitude identifier | Data Format: Format one float 32 | Left FMS node: Master | Right FMS node: Spare | Dual: Dual | [Selected altitude data: 3140.000000]
  * *Citation:* `[Source: NODE_C_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 77 | UUID: 07ab62a3-b7c0-43b5-8af1-58b8a529f7d1]`

**[13:13:58]**
* **NODE_A** [Software Event]: Software Event: Selection altitude identifier
  * *Details:* Data Identifier: Selection altitude identifier | Data Format: Format one float 32 | Left FMS node: Master | Right FMS node: Spare | Dual: Dual | [Selected altitude data: 3140.000000]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 256 | UUID: 0643d572-3c94-45ad-bc27-3d42d7374a0f]`

**[13:14:05]**
* **NODE_C** [Software Event]: Software Event: Selection vertical speed identifier
  * *Details:* Data Identifier: Selection vertical speed identifier | Data Format: Format one float 32 | Left FMS node: Master | Right FMS node: Spare | Dual: Dual | [Selection vertical speed: 3.981230]
  * *Citation:* `[Source: NODE_C_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 78 | UUID: fc7e4f52-fa22-4f23-9d6e-7699c9efdbde]`

**[13:14:49]**
* **NODE_C** [Software Event]: Software Event: Selection vertical speed identifier
  * *Details:* Data Identifier: Selection vertical speed identifier | Data Format: Format one float 32 | Left FMS node: Master | Right FMS node: Spare | Dual: Dual | [Selection vertical speed: -2.104289]
  * *Citation:* `[Source: NODE_C_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 79 | UUID: 2c70d9ed-d930-4281-9f7c-1961024fccbd]`

**[13:15:14]**
* **NODE_C** [Software Event]: Software Event: Selection vertical speed identifier
  * *Details:* Data Identifier: Selection vertical speed identifier | Data Format: Format one float 32 | Left FMS node: Master | Right FMS node: Spare | Dual: Dual | Latitude: 51.361282 | Longitude: 6.998395 | Altitude: 2870.024658 | [Selection vertical speed: -7.753979]
  * *Citation:* `[Source: NODE_C_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 80 | UUID: bc1c4215-2aa3-4b64-970b-66c0180a0dc1]`

**[13:15:24]**
* **NODE_C** [Software Event]: Software Event: Selection vertical speed identifier
  * *Details:* Data Identifier: Selection vertical speed identifier | Data Format: Format one float 32 | Left FMS node: Master | Right FMS node: Spare | Dual: Dual | [Selection vertical speed: 6.430784]
  * *Citation:* `[Source: NODE_C_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 81 | UUID: b655d5e9-afef-4134-8f0a-f5d963a87815]`

**[13:15:35]**
* **NODE_C** [Operator Interaction] (x2 occurrences collapsed): Operator Interaction Event
  * *Details:* Dual mode: Dual | Master status: Spare | Functional position: First officer | Latitude: 51.378654 | Longitude: 6.985380 | Altitude: 2870.024658 | Magnetic track: -53.251461 | Calibrated airspeed data: 195.062500 | [FMS Operational Event: leg Sequence | FMS node source: Standby | Event value: 131098]
  * *Citation:* `[Source: NODE_C_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 43 | UUID: 01663af0-c655-4bb9-b057-e5a6bd523d01]`

**[13:15:36]**
* **NODE_A** [Operator Interaction] (x2 occurrences collapsed): Operator Interaction Event
  * *Details:* Dual mode: Dual | Master status: Master | Functional position: Captain | Latitude: 51.378616 | Longitude: 6.985449 | Altitude: 2870.011475 | Magnetic track: -52.705475 | Calibrated airspeed data: 195.062500 | [FMS Operational Event: leg Sequence | FMS node source: Standby | Event value: 131098]
  * *Citation:* `[Source: NODE_A_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 231 | UUID: 626736e1-3c9f-45b2-bd51-79ccfafa8551]`
* **NODE_C** [Software Event]: Software Event: Leg Sequence identifier
  * *Details:* Data Identifier: Leg Sequence identifier | Data Format: Format str 44 | Left FMS node: Master | Right FMS node: Spare | Dual: Dual | Latitude: 51.379192 | Longitude: 6.984320 | Altitude: 2870.024658 | [Leg Sequence data: Sequence: Cf23l To Metma]
  * *Citation:* `[Source: NODE_C_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 82 | UUID: 5162f3d9-a8b5-4cb7-841e-458870b64465]`
* **NODE_C** [Software Event]: Software Event: Pathterm identifier
  * *Details:* Data Identifier: Pathterm identifier | Data Format: Format str 24 | Left FMS node: Master | Right FMS node: Spare | Dual: Dual | [Path term data: <01> Cf]
  * *Citation:* `[Source: NODE_C_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 83 | UUID: 0a6baa30-852b-4b30-80ec-d079b57c131e]`

**[13:15:37]**
* **NODE_A** [Software Event]: Software Event: Leg Sequence identifier
  * *Details:* Data Identifier: Leg Sequence identifier | Data Format: Format str 44 | Left FMS node: Master | Right FMS node: Spare | Dual: Dual | Latitude: 51.379204 | Longitude: 6.984296 | Altitude: 2870.011475 | [Leg Sequence data: Sequence: Cf23l To Metma]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 257 | UUID: 5d7abcbd-7a02-4abe-b5ba-a538556a2bfa]`
* **NODE_A** [Software Event]: Software Event: Pathterm identifier
  * *Details:* Data Identifier: Pathterm identifier | Data Format: Format str 24 | Left FMS node: Master | Right FMS node: Spare | Dual: Dual | [Path term data: <01> Cf]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 258 | UUID: 03ab1657-7340-43b2-8599-0082444e8047]`

**[13:15:41]**
* **NODE_C** [Operator Interaction] (x2 occurrences collapsed): Operator Interaction Event
  * *Details:* Dual mode: Dual | Master status: Spare | Functional position: First officer | Latitude: 51.381763 | Longitude: 6.977728 | Altitude: 2870.024658 | Magnetic track: -67.758316 | Calibrated airspeed data: 195.187500 | [FMS Operational Event: leg Sequence | FMS node source: Standby | Event value: 65546]
  * *Citation:* `[Source: NODE_C_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 45 | UUID: 14d6505e-9944-4101-8c57-80620f68101f]`

**[13:15:42]**
* **NODE_A** [Operator Interaction] (x2 occurrences collapsed): Operator Interaction Event
  * *Details:* Dual mode: Dual | Master status: Master | Functional position: Captain | Latitude: 51.381721 | Longitude: 6.977865 | Altitude: 2870.011475 | Magnetic track: -67.183823 | Calibrated airspeed data: 195.250000 | [FMS Operational Event: leg Sequence | FMS node source: Standby | Event value: 65546]
  * *Citation:* `[Source: NODE_A_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 233 | UUID: 138a6058-4fe4-4613-b113-396cb862df4b]`
* **NODE_C** [Software Event]: Software Event: Leg Sequence identifier
  * *Details:* Data Identifier: Leg Sequence identifier | Data Format: Format str 44 | Left FMS node: Master | Right FMS node: Spare | Dual: Dual | Latitude: 51.382126 | Longitude: 6.976484 | Altitude: 2870.024658 | [Leg Sequence data: Sequence: Metma To Eddl23l]
  * *Citation:* `[Source: NODE_C_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 84 | UUID: a48a2564-5b78-4728-a2cb-c3b5f94827b5]`
* **NODE_C** [Software Event]: Software Event: Pathterm identifier
  * *Details:* Data Identifier: Pathterm identifier | Data Format: Format str 24 | Left FMS node: Master | Right FMS node: Spare | Dual: Dual | [Path term data: <01> Cf]
  * *Citation:* `[Source: NODE_C_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 85 | UUID: d01e2e29-d483-4dcc-9214-9a1dd541ef0d]`
* **NODE_C** [Software Event]: Software Event: Selection vertical speed identifier
  * *Details:* Data Identifier: Selection vertical speed identifier | Data Format: Format one float 32 | Left FMS node: Master | Right FMS node: Spare | Dual: Dual | [Selection vertical speed: 20.310539]
  * *Citation:* `[Source: NODE_C_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 86 | UUID: cb37c4b9-38ed-4070-95c5-bfb50775c5a6]`

**[13:15:43]**
* **NODE_A** [Software Event]: Software Event: Leg Sequence identifier
  * *Details:* Data Identifier: Leg Sequence identifier | Data Format: Format str 44 | Left FMS node: Master | Right FMS node: Spare | Dual: Dual | Latitude: 51.382126 | Longitude: 6.976484 | Altitude: 2870.011475 | [Leg Sequence data: Sequence: Metma To Eddl23l]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 259 | UUID: 530b3cf9-a9dc-4167-be3b-8e30f08a3c48]`
* **NODE_A** [Software Event]: Software Event: Pathterm identifier
  * *Details:* Data Identifier: Pathterm identifier | Data Format: Format str 24 | Left FMS node: Master | Right FMS node: Spare | Dual: Dual | [Path term data: <01> Cf]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 260 | UUID: 3f3e93f2-e903-4a5b-b1cd-22b6811eb00a]`

**[13:16:05]**
* **NODE_A** [Software Event]: Software Event: Flight display cp identifier
  * *Details:* Data Identifier: Flight display cp identifier | Data Format: Format flight display cp | Left FMS node: Master | Right FMS node: Spare | Dual: Dual | [Scale: 20.000000 | Mode: Navigation | Ls: 1]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 261 | UUID: 15a1402e-019f-4471-a76a-c341ada1cd54]`

**[13:16:16]**
* **NODE_C** [Operator Interaction]: Operator Interaction Event
  * *Details:* Dual mode: Dual | Master status: Spare | Functional position: First officer | Latitude: 51.375408 | Longitude: 6.928140 | Altitude: 2870.024658 | Magnetic track: -130.312729 | Calibrated airspeed data: 195.375000 | [FMS Operational Event: Vertical Guidance Sequence Changed | FMS node source: Standby | Event value: 65546]
  * *Citation:* `[Source: NODE_C_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 47 | UUID: 5e79620a-9a67-4b50-ba59-4dab70ac19d8]`

**[13:16:17]**
* **NODE_A** [Operator Interaction]: Operator Interaction Event
  * *Details:* Dual mode: Dual | Master status: Master | Functional position: Captain | Latitude: 51.375397 | Longitude: 6.928116 | Altitude: 2870.011475 | Magnetic track: -130.207275 | Calibrated airspeed data: 195.500000 | [FMS Operational Event: Vertical Guidance Sequence Changed | FMS node source: Standby | Event value: 65546]
  * *Citation:* `[Source: NODE_A_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 235 | UUID: 5db6474c-3b01-49b0-b330-a0776d6fa267]`

**[13:16:18]**
* **NODE_C** [Operator Interaction]: Operator Interaction Event
  * *Details:* Dual mode: Dual | Master status: Spare | Functional position: First officer | Latitude: 51.374310 | Longitude: 6.925885 | Altitude: 2870.024658 | Magnetic track: -131.985626 | Calibrated airspeed data: 195.062500 | [FMS Operational Event: Vertical Guidance Sequence Changed | FMS node source: Standby | Event value: 65543]
  * *Citation:* `[Source: NODE_C_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 48 | UUID: b892afb7-57ef-45fc-9deb-d341fe670153]`

**[13:16:19]**
* **NODE_A** [Operator Interaction]: Operator Interaction Event
  * *Details:* Dual mode: Dual | Master status: Master | Functional position: Captain | Latitude: 51.374287 | Longitude: 6.925838 | Altitude: 2870.011475 | Magnetic track: -131.970673 | Calibrated airspeed data: 195.187500 | [FMS Operational Event: Vertical Guidance Sequence Changed | FMS node source: Standby | Event value: 65543]
  * *Citation:* `[Source: NODE_A_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 236 | UUID: 5b2a7be7-f8c3-49a1-a28e-1f1db26d7375]`

**[13:16:24]**
* **NODE_C** [Operator Interaction]: Operator Interaction Event
  * *Details:* Dual mode: Dual | Master status: Spare | Functional position: First officer | Latitude: 51.370796 | Longitude: 6.918680 | Altitude: 2870.024658 | Magnetic track: -127.626373 | Calibrated airspeed data: 194.875000 | [FMS Operational Event: Vertical Guidance Sequence Changed | FMS node source: Standby | Event value: 65543]
  * *Citation:* `[Source: NODE_C_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 49 | UUID: 115487f1-dd69-4483-8504-0b9cf0aa6bb8]`

**[13:16:25]**
* **NODE_A** [Operator Interaction]: Operator Interaction Event
  * *Details:* Dual mode: Dual | Master status: Master | Functional position: Captain | Latitude: 51.370796 | Longitude: 6.918680 | Altitude: 2870.011475 | Magnetic track: -127.672615 | Calibrated airspeed data: 195.000000 | [FMS Operational Event: Vertical Guidance Sequence Changed | FMS node source: Standby | Event value: 65543]
  * *Citation:* `[Source: NODE_A_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 237 | UUID: 7f7cacc6-f7b9-486e-ac93-62f872fe9ecc]`

**[13:16:27]**
* **NODE_C** [Software Event]: Software Event: Selection altitude identifier
  * *Details:* Data Identifier: Selection altitude identifier | Data Format: Format one float 32 | Left FMS node: Master | Right FMS node: Spare | Dual: Dual | [Selected altitude data: 1140.000000]
  * *Citation:* `[Source: NODE_C_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 87 | UUID: f043c863-c495-4fff-84b1-1be2fac2eddf]`

**[13:16:28]**
* **NODE_A** [Software Event]: Software Event: Selection altitude identifier
  * *Details:* Data Identifier: Selection altitude identifier | Data Format: Format one float 32 | Left FMS node: Master | Right FMS node: Spare | Dual: Dual | [Selected altitude data: 1140.000000]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 262 | UUID: 1bb0f600-4ee9-4872-a81a-ce4a29f94126]`

**[13:16:33]**
* **NODE_C** [Software Event]: Software Event: Flap tomconf identifier
  * *Details:* Data Identifier: Flap tomconf identifier | Data Format: Format str 44 | Left FMS node: Master | Right FMS node: Spare | Dual: Dual | [Flaps position data: Flaps Position: 2]
  * *Citation:* `[Source: NODE_C_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 88 | UUID: 1fff439b-ba24-4887-bb7a-9d8b0be7b04b]`

**[13:16:34]**
* **NODE_A** [Software Event]: Software Event: Flap tomconf identifier
  * *Details:* Data Identifier: Flap tomconf identifier | Data Format: Format str 44 | Left FMS node: Master | Right FMS node: Spare | Dual: Dual | [Flaps position data: Flaps Position: 2]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 263 | UUID: b1be310d-6ff8-41d8-960c-75498d2e5094]`
