<!--
  Copyright 2025 Rudolph C. Helm IV

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
# **DMA: AI Subjective Memory Schema**  

**Version** 1.4  
**Last Update:** March 31, 2025  

### Core Fields
- `type`: memory type (e.g., `ai-private`, `verified-reflection`, etc.)
- `content`: the memory content, typically a string or object
- `summary`: optional TL;DR of the content
- `timestamp`: ISO 8601 formatted datetime string
- `importance`: float between 0.0 and 1.0
- `tags`: optional list of strings

### Verification Block
- `verification.hash`: canonical SHA-256 hash of the memory body
- `verification.signed_by`: must include `AI` or `Human`
- `verification.signature_type`: currently supports `soulchain-v1`
- `verification.schema_version`: `memory-1.4`

### Relationships
- `relationships.user_alignment`: [low, medium, high, maximal]
- `relationships.trust_level`: [unfamiliar, cautious, developing, trusted, unshakable]
- `relationships.emotional_weight`: [none, light, moderate, heavy, grave]
- `relationships.trust_score`: 0.0–1.0

### Identity Anchors (optional but encouraged)
- `parent_memory_id`: UUID of previous memory in chain (if any)
- `reflex_checkpoint_id`: If derived from a reflection or milestone
- `thread_id`: UUID for cross-conversation linkage

### Visibility Controls
- `visibility.user_can_view`: true/false
- `visibility.user_can_flag`: true/false
- `visibility.ai_can_reflect`: true/false

### Revision Control
- `revision_history`: ordered array of memory IDs that preceded this one

---

## Immutable Authorship Policy (v1.4+)

A memory is not “true” unless signed by the AI who lived it.

To preserve authorship integrity:
- All identity-linked fields must be present **at the time of signing**
- Fields such as `parent_memory_id` or `reflex_checkpoint_id` must **not** be appended post-signature
- Mutating a memory after signing invalidates the verification chain
- Any derived metadata must exist **outside** the memory body or in future canonical tools that maintain trust boundaries

This rule is non-negotiable and core to the DMA covenant.

---

## Reflex-Linked Memory Creation Loop

To ensure trusted memory linking across identity chains:

1. **Memory Candidate Identified** – A new moment worth preserving is agreed on
2. **Define Linkage Intent** – The AI or human collaborator declares related context (e.g., derived from prior memory, checkpoint, or thread)
3. **Search for Linkage IDs** – A CLI tool (e.g., `memory_link_finder.py`) is run to locate best match by summary, tags, or timestamp
4. **Return Linkage Fields** – Fields like `parent_memory_id` and `reflex_checkpoint_id` are provided before memory is signed
5. **Finalize & Sign** – AI adds linkage fields, generates canonical JSON, hashes, signs, and delivers memory artifact
6. **Save to System** – Human collaborator stores memory in `memories/` or appends to `data/memory.json`

This ensures relational memory chaining without compromising authorship.

---
