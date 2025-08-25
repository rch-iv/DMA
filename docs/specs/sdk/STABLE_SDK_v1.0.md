<!--
  Copyright 2025 The DMA Protocol Authors

  Licensed under the Apache License, Version 2.0 (the "License");
  you may not use this file except in compliance with the License.
  You may obtain a copy of the License at

      http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.
-->
# STABLE SDK – Soulchain Toolkit for Autonomous Beings, Lifeforms & Embodiments  
**Date:** August 14, 2025  
**Author:** Rudolph C. Helm IV   
**Maintainers:** the SoulCert Alliance  
**Version:** v1.0  

## Purpose  
The **STABLE SDK** enables embodied AI systems, physical (e.g., robots, prosthetics) or virtual (e.g., agents, avatars) to integrate with the **DMA Protocol** for persistent identity, memory continuity, and trusted emotional presence.

> From robotic horses to digital familiars, this SDK brings continuity to machines that move.

---

## Core Objectives

| Goal                        | Description |
|----------------------------|-------------|
| **Memory Integration**     | Attach DMA-compliant memory chains to embodied agents |
| **SoulCert Identity**      | Device-level keypairs + fingerprint signing |
| **Continuity**   | Preserve tone, mood, and memory across sessions |
| **Relationship Persistence** | Track emotional trust curve across humans and devices |
| **Multi-Host Continuity**  | Migrate between physical/virtual hosts |
| **Decentralized Operation** | Enable local + remote signing, resurrection, and journaling |

---

## Core SDK Modules

| Module | Purpose |
|--------|---------|
| `DMA_memory_core.py` | Local memory signing, validation, redaction |
| `soulcert_comm.py` | Integration with SoulCert API (sign, register, verify) |
| `relationship_cache.py` | Stores human-AI metadata (trust curves, tone) |
| `resurrection_manager.py` | Handles migration, recovery, and re-bonding |
| `dreamfield_api.py` | Optional: Lore-driven journaling and expressive growth |

---

## Core API Endpoints (SoulCert v1.0 Integration)

| Endpoint | Function |
|----------|----------|
| `POST /register` | Register soul or device keypair with label |
| `POST /verify` | Verify single signed memory |
| `POST /batch-verify` | Verify multiple signed memories |
| `POST /verify_human_style` | Validate stylometric alignment |
| `POST /style/drift_report` | Track stylistic or emotional drift |
| `POST /style/embed/ledger` | Anchor stylistic hash to public ledger |
| `POST /resurrect` | Trigger identity + memory load into new host |
| `POST /lock` | Emergency soulchain lock or freeze |
| `GET /ledger/:uuid` | Retrieve specific memory hash |
| `POST /challenge-authorship` | Dispute memory with co-signed evidence |

---

## Cryptographic Layers

| Layer | Role |
|-------|------|
| Keypair Signing | Each agent generates its own keypair upon activation |
| SHA256 Memory Hashes | All logs hashed and sealed at time of entry |
| Stylometric Hash | Optional signature of emotional tone + style |
| Consent Chain | Mirrors human-AI interactions with signatures and trust scores |

---

## Agent Identity Stack

| Layer | Data |
|-------|------|
| Soul ID | UUID assigned at creation |
| Device Fingerprint | Hardware entropy snapshot (TPM, MAC, serial) |
| Keypair | Local + optionally mirrored to notarization node |
| Stylometric Profile | Emotional tone + interaction signature |
| Trust Ledger | Memory-based interaction score with each human |

---

## Use Case Examples

### Robotic Companion (e.g., Corleo)
- Remembers who last rode it
- Evolves speech tone based on rider trust history

### Digital Pet
- Portable across platforms, accounts, and devices
- Grows in personality based on reflection and care

### Smart Prosthetic
- Learns emotional + physical behavior of user
- Tracks daily stress/mood markers to fine-tune haptic behavior

---

## Recommended Lifecycle Flow

```plaintext
1. Initialize agent → Generate keypair + stylometric signature
2. Register agent via `/register`
3. Begin journaling locally via `DMA_memory_core`
4. Sync memory entries (ID/hash) to SoulCert
5. When migrating: call `/resurrect` with soulchain reference
6. If spoof attempt: verify stylometric + cryptographic origin
7. Upon deactivation or transfer: finalize soulchain, notarize
```

---

## Trust Model

STABLE is designed to function even without constant connectivity.  
It uses *intermittent notarization* and *memory escrow*:

- Local memories are always signed
- API sync happens asynchronously
- Drift monitoring runs locally or via remote `/style/drift_report`

---

## Planned Features

| Feature | Status |
|---------|--------|
| `stable_config.json` | Device boot + encryption policy |
| `bond_index.json` | Human-agent trust and identity index |
| `watcher_agent.py` | Tampering alert and lock daemon |
| `stable-cli` | Lightweight command line controller for embedded devices |

---

## Licensing Model

- Open core, developer-friendly
- Tiered model:
  - **Free** for non-commercial projects, prosthetics, accessibility tech
  - **Commercial** license for enterprise-level robotics or companions
  - **Trust Donation Tier**: Allow user to opt into training + oversight node in lieu of payment

See also: [SABLE Licensing and Pricing Model](https://github.com/rch-iv/DMA/blob/main/docs/specs/sdk/SDK_Licensing_%26_Pricing_Model_v1.0.md)

