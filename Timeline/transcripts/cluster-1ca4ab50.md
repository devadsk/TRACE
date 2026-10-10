# Incident Cluster: cluster-1ca4ab50
**Date:** 2032-06-18
**Duration:** 12:32:05 to 12:35:20
**Nodes Involved:** NODE_A, NODE_B
**Total Events:** 60 (Filtered from 67 raw logs)

## Timeline Transcript

**[12:32:05]**
* **NODE_B** [Operator Interaction] (x2 occurrences collapsed): Operator Interaction Event
  * *Details:* Dual mode: Dual | Master status: Spare | Functional position: First officer | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 341.000549 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [FMS Operational Event: phase change | FMS node source: Standby | Event value: 17826481]
  * *Citation:* `[Source: NODE_B_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 51 | UUID: f59742a7-8efd-485d-a041-825190a3d69e]`

**[12:32:06]**
* **NODE_A** [Operator Interaction] (x2 occurrences collapsed): Operator Interaction Event
  * *Details:* Dual mode: Dual | Master status: Master | Functional position: Captain | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 341.001709 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [FMS Operational Event: phase change | FMS node source: Standby | Event value: 17826481]
  * *Citation:* `[Source: NODE_A_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 55 | UUID: 26656a17-ec7b-4b2b-957d-2af64240be82]`
* **NODE_A** [Software Event]: Software Event: Flight phase identifier
  * *Details:* Data Identifier: Flight phase identifier | Data Format: Format fixed str | Left FMS node: Master | Center FMS node: Spare | Dual: Dual | [Event identifier: 68 | Flight phase previous: Preflight | Flight phase current: Takeoff]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 46 | UUID: 880edc4c-8a68-4405-bf6b-7b54109f0604]`
* **NODE_B** [Operator Interaction]: Operator Interaction Event
  * *Details:* Dual mode: Dual | Master status: Spare | Functional position: First officer | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 341.000488 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [FMS Operational Event: Vertical Guidance Sequence Changed | FMS node source: Standby | Event value: 65539]
  * *Citation:* `[Source: NODE_B_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 53 | UUID: 8374969e-8419-4325-8701-91e701e94fde]`
* **NODE_B** [Software Event]: Software Event: Flight phase identifier
  * *Details:* Data Identifier: Flight phase identifier | Data Format: Format fixed str | Left FMS node: Master | Center FMS node: Spare | Dual: Dual | [Event identifier: 68 | Flight phase previous: Preflight | Flight phase current: Takeoff]
  * *Citation:* `[Source: NODE_B_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 53 | UUID: 45df3575-51d2-4f39-af9d-d741924c9dcc]`

**[12:32:07]**
* **NODE_A** [Operator Interaction]: Operator Interaction Event
  * *Details:* Dual mode: Dual | Master status: Master | Functional position: Captain | Latitude: 50.027630 | Longitude: 8.534528 | Altitude: 341.001648 | Magnetic track: 66.049805 | Calibrated airspeed data: 35.000000 | [FMS Operational Event: Vertical Guidance Sequence Changed | FMS node source: Standby | Event value: 65539]
  * *Citation:* `[Source: NODE_A_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 57 | UUID: c87ca30b-5d4a-4d28-bf04-14aad75111e0]`

**[12:32:09]**
* **NODE_B** [Software Event]: Software Event: Selection speed identifier
  * *Details:* Data Identifier: Selection speed identifier | Data Format: Format one float 32 | Left FMS node: Master | Center FMS node: Spare | Dual: Dual | [Selection speed: 150.000000]
  * *Citation:* `[Source: NODE_B_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 54 | UUID: e9460d1c-acf9-48ff-b954-e0a8e5951437]`

**[12:32:10]**
* **NODE_A** [Software Event]: Software Event: Selection speed identifier
  * *Details:* Data Identifier: Selection speed identifier | Data Format: Format one float 32 | Left FMS node: Master | Center FMS node: Spare | Dual: Dual | [Selection speed: 150.000000]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 47 | UUID: f1428c9d-08f5-4c70-98ba-70d0acd37ae9]`

**[12:32:20]**
* **NODE_B** [Software Event]: Software Event: Flight display cp identifier
  * *Details:* Data Identifier: Flight display cp identifier | Data Format: Format flight display cp | Left FMS node: Master | Center FMS node: Spare | Dual: Dual | [Scale: 20.000000 | Mode: Arc | Route data: 1 | Mora: 1]
  * *Citation:* `[Source: NODE_B_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 55 | UUID: a5effd0d-ecae-456b-9bf2-c1fbecca939b]`

**[12:32:28]**
* **NODE_B** [Software Event]: Software Event: Flight display cp identifier
  * *Details:* Data Identifier: Flight display cp identifier | Data Format: Format flight display cp | Left FMS node: Master | Center FMS node: Spare | Dual: Dual | [Scale: 20.000000 | Mode: Arc | Route data: 1 | Mora: 1 | Ls: 1]
  * *Citation:* `[Source: NODE_B_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 56 | UUID: a0724f97-955f-4a76-9001-df140fb0bf5f]`

**[12:32:32]**
* **NODE_B** [Operator Interaction]: Operator Interaction Event
  * *Details:* Dual mode: Dual | Master status: Spare | Functional position: First officer | Latitude: 50.029419 | Longitude: 8.542379 | Altitude: 358.407043 | Magnetic track: 68.192741 | Calibrated airspeed data: 104.375000 | [FMS Operational Event: Vertical Guidance Sequence Changed | FMS node source: Standby | Event value: 65543]
  * *Citation:* `[Source: NODE_B_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 54 | UUID: bad3cd8d-9d7f-46ec-8539-e1caf1faf8d7]`

**[12:32:33]**
* **NODE_A** [Operator Interaction]: Operator Interaction Event
  * *Details:* Dual mode: Dual | Master status: Master | Functional position: Captain | Latitude: 50.029423 | Longitude: 8.542409 | Altitude: 357.547882 | Magnetic track: 67.002777 | Calibrated airspeed data: 104.000000 | [FMS Operational Event: Vertical Guidance Sequence Changed | FMS node source: Standby | Event value: 65543]
  * *Citation:* `[Source: NODE_A_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 58 | UUID: c23abb87-3b1c-4e18-873b-00eb70661ec3]`

**[12:32:39]**
* **NODE_B** [Software Event]: Software Event: Selection vertical speed identifier
  * *Details:* Data Identifier: Selection vertical speed identifier | Data Format: Format one float 32 | Left FMS node: Master | Center FMS node: Spare | Dual: Dual | [Selection vertical speed: 49.585045]
  * *Citation:* `[Source: NODE_B_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 57 | UUID: 7b935c5a-e84a-4baa-b556-75d5cf03d4ea]`

**[12:32:40]**
* **NODE_A** [Software Event]: Software Event: Selection vertical speed identifier
  * *Details:* Data Identifier: Selection vertical speed identifier | Data Format: Format one float 32 | Left FMS node: Master | Center FMS node: Spare | Dual: Dual | [Selection vertical speed: 49.710514]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 48 | UUID: 8b329700-c073-43fe-9eb7-d92e6e278595]`

**[12:32:45]**
* **NODE_A** [Software Event]: Software Event: Air ground identifier
  * *Details:* Data Identifier: Air ground identifier | Data Format: Format fixed str | Left FMS node: Master | Center FMS node: Spare | Dual: Dual | Latitude: 50.032055 | Longitude: 8.554273 | Altitude: 378.348785 | [Event identifier: 68 | Air ground status: 50]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 49 | UUID: dbb58f76-51f2-4960-a805-b6afb2b79cae]`
* **NODE_B** [Software Event]: Software Event: Air ground identifier
  * *Details:* Data Identifier: Air ground identifier | Data Format: Format fixed str | Left FMS node: Master | Center FMS node: Spare | Dual: Dual | Latitude: 50.031971 | Longitude: 8.553883 | Altitude: 331.408905 | [Event identifier: 68 | Air ground status: 50]
  * *Citation:* `[Source: NODE_B_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 58 | UUID: 70bed264-e1e4-4d0a-98fb-9fec4c17fd07]`
* **NODE_B** [Software Event]: Software Event: Leg Sequence identifier
  * *Details:* Data Identifier: Leg Sequence identifier | Data Format: Format str 44 | Left FMS node: Master | Center FMS node: Spare | Dual: Dual | Latitude: 50.032028 | Longitude: 8.554142 | Altitude: 332.398529 | [Leg Sequence data: Sequence: Ppos To De07r]
  * *Citation:* `[Source: NODE_B_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 59 | UUID: 3376a4a0-1169-4918-87ac-375874ec9458]`
* **NODE_B** [Software Event]: Software Event: Pathterm identifier
  * *Details:* Data Identifier: Pathterm identifier | Data Format: Format str 24 | Left FMS node: Master | Center FMS node: Spare | Dual: Dual | [Path term data: <02> Df]
  * *Citation:* `[Source: NODE_B_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 60 | UUID: 0c24ec75-0344-46d0-8387-a0f58947e968]`

**[12:32:46]**
* **NODE_A** [Software Event]: Software Event: Leg Sequence identifier
  * *Details:* Data Identifier: Leg Sequence identifier | Data Format: Format str 44 | Left FMS node: Master | Center FMS node: Spare | Dual: Dual | Latitude: 50.032089 | Longitude: 8.554424 | Altitude: 379.659546 | [Leg Sequence data: Sequence: Ppos To De07r]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 50 | UUID: d5cac86e-82cf-4539-9959-e3fc65558feb]`
* **NODE_A** [Software Event]: Software Event: Pathterm identifier
  * *Details:* Data Identifier: Pathterm identifier | Data Format: Format str 24 | Left FMS node: Master | Center FMS node: Spare | Dual: Dual | [Path term data: <02> Df]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 51 | UUID: dae29e82-21a1-46ed-905c-d9d9bdf9ea39]`

**[12:32:50]**
* **NODE_B** [Software Event]: Software Event: Selection speed identifier
  * *Details:* Data Identifier: Selection speed identifier | Data Format: Format one float 32 | Left FMS node: Master | Center FMS node: Spare | Dual: Dual | [Selection speed: 161.343185]
  * *Citation:* `[Source: NODE_B_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 61 | UUID: 37a04d17-50be-4387-8909-82a11f457da6]`

**[12:32:53]**
* **NODE_A** [Software Event]: Software Event: Selection speed identifier
  * *Details:* Data Identifier: Selection speed identifier | Data Format: Format one float 32 | Left FMS node: Master | Center FMS node: Spare | Dual: Dual | [Selection speed: 161.185684]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 52 | UUID: 3b7f7653-ec2b-44fd-9830-8f4a696e1089]`
* **NODE_B** [Software Event]: Software Event: Autopilot identifier a350
  * *Details:* Data Identifier: Autopilot identifier a350 | Data Format: Format fixed str | Left FMS node: Master | Center FMS node: Spare | Dual: Dual | [Event identifier: 68 | Autopilot data: Auto pilot 1 is on]
  * *Citation:* `[Source: NODE_B_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 62 | UUID: 1f0bb783-12fa-4898-9ff3-2fa52bd42ba7]`

**[12:32:54]**
* **NODE_A** [Software Event]: Software Event: Autopilot identifier a350
  * *Details:* Data Identifier: Autopilot identifier a350 | Data Format: Format fixed str | Left FMS node: Master | Center FMS node: Spare | Dual: Dual | [Event identifier: 68 | Autopilot data: Auto pilot 1 is on]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 53 | UUID: ff98d31e-aeee-4b0e-a01f-8bf38d25191d]`

**[12:32:56]**
* **NODE_B** [Software Event]: Software Event: Nose gear identifier
  * *Details:* Data Identifier: Nose gear identifier | Data Format: Format fixed str | Left FMS node: Master | Center FMS node: Spare | Dual: Dual | [Event identifier: 68 | Main gear out: Nose gear is up]
  * *Citation:* `[Source: NODE_B_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 63 | UUID: b2d91e65-f0a2-483c-9fde-26630cd6774d]`

**[12:32:57]**
* **NODE_A** [Software Event]: Software Event: Nose gear identifier
  * *Details:* Data Identifier: Nose gear identifier | Data Format: Format fixed str | Left FMS node: Master | Center FMS node: Spare | Dual: Dual | [Event identifier: 68 | Main gear out: Nose gear is up]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 54 | UUID: 8318fdce-f190-4608-8727-06fa793aea62]`

**[12:33:02]**
* **NODE_B** [Software Event]: Software Event: Selection speed identifier
  * *Details:* Data Identifier: Selection speed identifier | Data Format: Format one float 32 | Left FMS node: Master | Center FMS node: Spare | Dual: Dual | [Selection speed: 165.800598]
  * *Citation:* `[Source: NODE_B_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 64 | UUID: a9287807-3c03-4bcb-ad5b-e8929322dfd7]`

**[12:33:09]**
* **NODE_A** [Software Event]: Software Event: Selection speed identifier
  * *Details:* Data Identifier: Selection speed identifier | Data Format: Format one float 32 | Left FMS node: Master | Center FMS node: Spare | Dual: Dual | [Selection speed: 168.528122]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 55 | UUID: ad9000f3-6df3-4199-a70d-518a5bf22903]`

**[12:33:12]**
* **NODE_B** [Software Event]: Software Event: Selection speed identifier
  * *Details:* Data Identifier: Selection speed identifier | Data Format: Format one float 32 | Left FMS node: Master | Center FMS node: Spare | Dual: Dual | [Selection speed: 169.726425]
  * *Citation:* `[Source: NODE_B_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 65 | UUID: 11070d4f-c3a4-4794-b0f3-907e80bca728]`

**[12:33:14]**
* **NODE_B** [Operator Interaction]: Operator Interaction Event
  * *Details:* Dual mode: Dual | Master status: Spare | Functional position: First officer | Latitude: 50.039261 | Longitude: 8.587166 | Altitude: 1545.482788 | Magnetic track: 66.672150 | Calibrated airspeed data: 170.187500 | [FMS Operational Event: leg Sequence | FMS node source: Standby | Event value: 65543]
  * *Citation:* `[Source: NODE_B_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 55 | UUID: eca3a975-53a9-4505-ac2f-d3df8ff230dc]`

**[12:33:15]**
* **NODE_A** [Operator Interaction] (x2 occurrences collapsed): Operator Interaction Event
  * *Details:* Dual mode: Dual | Master status: Master | Functional position: Captain | Latitude: 50.039268 | Longitude: 8.587190 | Altitude: 1537.950806 | Magnetic track: 65.498505 | Calibrated airspeed data: 170.187500 | [FMS Operational Event: leg Sequence | FMS node source: Standby | Event value: 65543]
  * *Citation:* `[Source: NODE_A_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 59 | UUID: 1ddfdd73-a89f-4d8c-bb6c-bfe2b75d6937]`
* **NODE_B** [Operator Interaction]: Operator Interaction Event
  * *Details:* Dual mode: Dual | Master status: Spare | Functional position: First officer | Latitude: 50.039433 | Longitude: 8.587864 | Altitude: 1574.505737 | Magnetic track: 66.605461 | Calibrated airspeed data: 170.312500 | [FMS Operational Event: Sequence confirm | FMS node source: Standby | Event value: 65537]
  * *Citation:* `[Source: NODE_B_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 56 | UUID: 93d2e000-66d9-4d87-a0c6-3fe959a392f9]`
* **NODE_B** [Software Event]: Software Event: Leg Sequence identifier
  * *Details:* Data Identifier: Leg Sequence identifier | Data Format: Format str 44 | Left FMS node: Master | Center FMS node: Spare | Dual: Dual | Latitude: 50.039490 | Longitude: 8.588097 | Altitude: 1582.496948 | [Leg Sequence data: Sequence: De07r To Df149]
  * *Citation:* `[Source: NODE_B_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 66 | UUID: a90eba59-c289-4b27-90de-0d39c508595b]`
* **NODE_B** [Software Event]: Software Event: Pathterm identifier
  * *Details:* Data Identifier: Pathterm identifier | Data Format: Format str 24 | Left FMS node: Master | Center FMS node: Spare | Dual: Dual | [Path term data: <01> Cf]
  * *Citation:* `[Source: NODE_B_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 67 | UUID: 41c58cbd-61e5-4687-bf83-8210d17d3d6a]`

**[12:33:16]**
* **NODE_A** [Software Event]: Software Event: Leg Sequence identifier
  * *Details:* Data Identifier: Leg Sequence identifier | Data Format: Format str 44 | Left FMS node: Master | Center FMS node: Spare | Dual: Dual | Latitude: 50.039551 | Longitude: 8.588352 | Altitude: 1589.299561 | [Leg Sequence data: Sequence: De07r To Df149]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 56 | UUID: 30c4a7a9-538c-43c6-b993-7767a4f2eb77]`
* **NODE_A** [Software Event]: Software Event: Pathterm identifier
  * *Details:* Data Identifier: Pathterm identifier | Data Format: Format str 24 | Left FMS node: Master | Center FMS node: Spare | Dual: Dual | [Path term data: <01> Cf]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 57 | UUID: f6fe43ec-e76c-4f1a-8412-9937219767cf]`

**[12:33:21]**
* **NODE_B** [Operator Interaction] (x2 occurrences collapsed): Operator Interaction Event
  * *Details:* Dual mode: Dual | Master status: Spare | Functional position: First officer | Latitude: 50.041309 | Longitude: 8.595422 | Altitude: 1875.395630 | Magnetic track: 65.844833 | Calibrated airspeed data: 171.500000 | [FMS Operational Event: phase change | FMS node source: Standby | Event value: 65546]
  * *Citation:* `[Source: NODE_B_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 57 | UUID: e4f35f48-f035-4cff-9a38-a25288e27667]`

**[12:33:22]**
* **NODE_A** [Operator Interaction] (x2 occurrences collapsed): Operator Interaction Event
  * *Details:* Dual mode: Dual | Master status: Master | Functional position: Captain | Latitude: 50.041298 | Longitude: 8.595375 | Altitude: 1873.486084 | Magnetic track: 64.651230 | Calibrated airspeed data: 171.437500 | [FMS Operational Event: phase change | FMS node source: Standby | Event value: 65546]
  * *Citation:* `[Source: NODE_A_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 61 | UUID: ce245653-b649-467d-aa40-64c10aa534a9]`
* **NODE_A** [Software Event]: Software Event: Flight phase identifier
  * *Details:* Data Identifier: Flight phase identifier | Data Format: Format fixed str | Left FMS node: Master | Center FMS node: Spare | Dual: Dual | Latitude: 50.041519 | Longitude: 8.596240 | Altitude: 1907.033813 | [Event identifier: 68 | Flight phase previous: Takeoff | Flight phase current: Climb]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 58 | UUID: 2cac9804-6b66-47da-808d-bf0a446a664e]`
* **NODE_B** [Software Event]: Software Event: Flight phase identifier
  * *Details:* Data Identifier: Flight phase identifier | Data Format: Format fixed str | Left FMS node: Master | Center FMS node: Spare | Dual: Dual | Latitude: 50.041485 | Longitude: 8.596100 | Altitude: 1902.385498 | [Event identifier: 68 | Flight phase previous: Takeoff | Flight phase current: Climb]
  * *Citation:* `[Source: NODE_B_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 68 | UUID: 4bc71170-d6eb-425f-bf7a-bc25d78d1194]`
* **NODE_B** [Software Event]: Software Event: Vnav at mode identifier
  * *Details:* Data Identifier: Vnav at mode identifier | Data Format: Format fixed str | Left FMS node: Master | Center FMS node: Spare | Dual: Dual | [Event identifier: 68 | V navigation status: V navigation at speed thrust]
  * *Citation:* `[Source: NODE_B_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 69 | UUID: f69242f0-0a4b-4c1a-a295-bcf131b1c680]`

**[12:33:24]**
* **NODE_A** [Software Event]: Software Event: Vnav at mode identifier
  * *Details:* Data Identifier: Vnav at mode identifier | Data Format: Format fixed str | Left FMS node: Master | Center FMS node: Spare | Dual: Dual | [Event identifier: 68 | V navigation status: V navigation at speed thrust]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 59 | UUID: 5020b988-7396-4339-8745-fdab5dc9f90f]`

**[12:33:26]**
* **NODE_A** [Software Event]: Software Event: Selection speed identifier
  * *Details:* Data Identifier: Selection speed identifier | Data Format: Format one float 32 | Left FMS node: Master | Center FMS node: Spare | Dual: Dual | [Selection speed: 171.813599]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 60 | UUID: ea613613-80cd-4c6b-9556-1dc30b1f000b]`

**[12:33:27]**
* **NODE_A** [Software Event]: Software Event: Flight display cp identifier
  * *Details:* Data Identifier: Flight display cp identifier | Data Format: Format flight display cp | Left FMS node: Master | Center FMS node: Spare | Dual: Dual | [Scale: 20.000000 | Mode: Plan]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 61 | UUID: ce6e83bd-f2b6-49ee-b651-fa16360e999a]`

**[12:34:08]**
* **NODE_B** [Software Event]: Software Event: Selection speed identifier
  * *Details:* Data Identifier: Selection speed identifier | Data Format: Format one float 32 | Left FMS node: Master | Center FMS node: Spare | Dual: Dual | [Selection speed: 216.671967]
  * *Citation:* `[Source: NODE_B_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 70 | UUID: f2adb52f-aae5-4b5e-96bc-ff6ae402c1ce]`

**[12:34:12]**
* **NODE_A** [Software Event]: Software Event: Selection speed identifier
  * *Details:* Data Identifier: Selection speed identifier | Data Format: Format one float 32 | Left FMS node: Master | Center FMS node: Spare | Dual: Dual | [Selection speed: 218.454178]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 62 | UUID: 66bf2acf-793d-4ad4-bffb-dedfbb58b74f]`

**[12:34:14]**
* **NODE_B** [Software Event]: Software Event: Selection speed identifier
  * *Details:* Data Identifier: Selection speed identifier | Data Format: Format one float 32 | Left FMS node: Master | Center FMS node: Spare | Dual: Dual | [Selection speed: 219.072540]
  * *Citation:* `[Source: NODE_B_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 71 | UUID: 5859d94d-4683-4fb7-b5a4-fa46f1cf6b81]`

**[12:34:15]**
* **NODE_A** [Software Event]: Software Event: Flap tomconf identifier
  * *Details:* Data Identifier: Flap tomconf identifier | Data Format: Format str 44 | Left FMS node: Master | Center FMS node: Spare | Dual: Dual | [Flaps position data: Flaps Position: 0]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 63 | UUID: 82c8d378-3b41-4ba8-8277-f4772470303e]`

**[12:34:32]**
* **NODE_A** [Software Event]: Software Event: Selection speed identifier
  * *Details:* Data Identifier: Selection speed identifier | Data Format: Format one float 32 | Left FMS node: Master | Center FMS node: Spare | Dual: Dual | Latitude: 50.068085 | Longitude: 8.692655 | Altitude: 3732.760742 | [Selection speed: 220.249130]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 64 | UUID: 66189284-9982-4080-8695-046926bb99bb]`

**[12:34:43]**
* **NODE_B** [Operator Interaction]: Operator Interaction Event
  * *Details:* Dual mode: Dual | Master status: Spare | Functional position: First officer | Latitude: 50.074306 | Longitude: 8.709422 | Altitude: 4226.446289 | Magnetic track: 47.057884 | Calibrated airspeed data: 220.062500 | [FMS Operational Event: leg Sequence | FMS node source: Standby | Event value: 65539]
  * *Citation:* `[Source: NODE_B_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 59 | UUID: 18f55d4b-b50e-49c3-9d32-9d34c56645ec]`

**[12:34:44]**
* **NODE_A** [Operator Interaction] (x2 occurrences collapsed): Operator Interaction Event
  * *Details:* Dual mode: Dual | Master status: Master | Functional position: Captain | Latitude: 50.074375 | Longitude: 8.709551 | Altitude: 4217.387695 | Magnetic track: 46.090424 | Calibrated airspeed data: 220.062500 | [FMS Operational Event: leg Sequence | FMS node source: Standby | Event value: 65539]
  * *Citation:* `[Source: NODE_A_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 63 | UUID: e661394a-8b83-4d42-8b91-7c52184c6053]`
* **NODE_B** [Operator Interaction] (x2 occurrences collapsed): Operator Interaction Event
  * *Details:* Dual mode: Dual | Master status: Spare | Functional position: First officer | Latitude: 50.074745 | Longitude: 8.710213 | Altitude: 4248.446777 | Magnetic track: 45.829025 | Calibrated airspeed data: 220.062500 | [FMS Operational Event: Vertical Guidance Sequence Changed | FMS node source: Standby | Event value: 65537]
  * *Citation:* `[Source: NODE_B_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 60 | UUID: b70122bd-bd77-48b6-b95d-e64c482a8a6c]`
* **NODE_B** [Software Event]: Software Event: Leg Sequence identifier
  * *Details:* Data Identifier: Leg Sequence identifier | Data Format: Format str 44 | Left FMS node: Master | Center FMS node: Spare | Dual: Dual | Latitude: 50.074875 | Longitude: 8.710439 | Altitude: 4251.461914 | [Leg Sequence data: Sequence: Df149 To Mefto]
  * *Citation:* `[Source: NODE_B_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 72 | UUID: 07487281-6e88-4009-b94e-668838e38b56]`
* **NODE_B** [Software Event]: Software Event: Pathterm identifier
  * *Details:* Data Identifier: Pathterm identifier | Data Format: Format str 24 | Left FMS node: Master | Center FMS node: Spare | Dual: Dual | [Path term data: <10> Tf]
  * *Citation:* `[Source: NODE_B_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 73 | UUID: fad06a02-9b15-4f16-ae9f-9608deed1e95]`

**[12:34:45]**
* **NODE_A** [Operator Interaction]: Operator Interaction Event
  * *Details:* Dual mode: Dual | Master status: Master | Functional position: Captain | Latitude: 50.075497 | Longitude: 8.711478 | Altitude: 4278.707520 | Magnetic track: 42.642006 | Calibrated airspeed data: 220.000000 | [FMS Operational Event: Sequence confirm | FMS node source: Standby | Event value: 65543]
  * *Citation:* `[Source: NODE_A_FM_CI_BPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 65 | UUID: ed9d3130-a5fa-4342-9d87-28c33dadccb6]`
* **NODE_A** [Software Event]: Software Event: Leg Sequence identifier
  * *Details:* Data Identifier: Leg Sequence identifier | Data Format: Format str 44 | Left FMS node: Master | Center FMS node: Spare | Dual: Dual | Latitude: 50.075035 | Longitude: 8.710714 | Altitude: 4254.262695 | [Leg Sequence data: Sequence: Df149 To Mefto]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 65 | UUID: ee67b061-6b9a-4e30-a046-d92973cdf105]`
* **NODE_A** [Software Event]: Software Event: Pathterm identifier
  * *Details:* Data Identifier: Pathterm identifier | Data Format: Format str 24 | Left FMS node: Master | Center FMS node: Spare | Dual: Dual | [Path term data: <10> Tf]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 66 | UUID: 2769c797-1312-4c69-857d-316708807c74]`

**[12:35:14]**
* **NODE_B** [Software Event]: Software Event: Selection speed identifier
  * *Details:* Data Identifier: Selection speed identifier | Data Format: Format one float 32 | Left FMS node: Master | Center FMS node: Spare | Dual: Dual | [Selection speed: 248.602615]
  * *Citation:* `[Source: NODE_B_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 74 | UUID: ff4909aa-edb3-4478-b4a5-70674181ac65]`

**[12:35:18]**
* **NODE_A** [Software Event]: Software Event: Selection speed identifier
  * *Details:* Data Identifier: Selection speed identifier | Data Format: Format one float 32 | Left FMS node: Master | Center FMS node: Spare | Dual: Dual | [Selection speed: 250.211487]
  * *Citation:* `[Source: NODE_A_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 67 | UUID: ee60c3f3-b296-4702-8605-3084222f1d84]`

**[12:35:20]**
* **NODE_B** [Software Event]: Software Event: Selection speed identifier
  * *Details:* Data Identifier: Selection speed identifier | Data Format: Format one float 32 | Left FMS node: Master | Center FMS node: Spare | Dual: Dual | [Selection speed: 250.982788]
  * *Citation:* `[Source: NODE_B_FM_LBPQ_Log_6_Custom_Log_Decoded_Report.html | Seq: 75 | UUID: 15f8de89-4744-4c75-8d0c-5581d7c4bf5b]`
