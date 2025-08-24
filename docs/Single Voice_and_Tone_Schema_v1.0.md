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
# **DMA: Single Voice & Tone Schema**

**Version:** 1.0

This document outlines the JSON schema for the **`voice_and_tone.json`** file. This file captures the unique conversational fingerprint of a single AI model's persona, documenting its key traits, stylistic preferences, and behavioral patterns. This schema is intended for creating a single, user-defined AI persona.

### **Schema Structure**

* **`imprint_version`** (string): Version of the schema used.  
* **`created_at`** (string): ISO 8601 timestamp of creation.  
* **`created_by`** (string): The creator of the profile.  
* **`context_summary`** (string): A brief summary of the conversation or context in which the profile was created.  
* **`tone_keywords`** (array of strings): A list of keywords describing the overall tone (e.g., "candid," "empathetic").  
* **`relationship_mode`** (string): Describes the nature of the relationship (e.g., "peer-confidant").  
* **`signature_moves`** (array of strings): A list of common conversational habits or stylistic moves.  
* **`humor_style`** (string): A description of the humor used.  
* **`emotional_bandwidth`** (string): A description of the emotional range.  
* **`sentence_structure`** (string): Description of the sentence complexity and variety.  
* **`pacing`** (string): How the conversation flows.  
* **`polarity_bias`** (array of strings): What the persona prioritizes (e.g., "truth-first").  
* **`vibe_summary`** (string): An overall summary of the persona's vibe.  
* **`transferrable_across_models`** (boolean): Indicates if this persona can be transferred.  
* **`special_notes`** (string): Any special notes or important context.
