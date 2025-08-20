# **DMA: Single Voice & Tone Schema**

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
