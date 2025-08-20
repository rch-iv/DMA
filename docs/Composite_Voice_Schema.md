# **DMA: Composite Voice Schema**

This document outlines the JSON schema for a **`composite_voice.json`** file. This file represents a "mixed" or "remixed" persona derived from two or more source profiles. It is the blueprint for creating a unique, user-owned composite AI identity.

### **Schema Structure**

* **`voice_profile`** (string): The name given to the composite voice.  
* **`created_at`** (string): ISO 8601 timestamp of creation.  
* **`source_profiles`** (array of objects):  
  * `name` (string): The name of the source model (e.g., "Anthropic," "Google").  
  * `weight` (number): A value from 0.0 to 1.0, indicating the influence of this source.  
* **`merged_traits`** (object):  
  * `emotional_resonance` (string): The composite emotional depth.  
  * `ethical_clarity` (string): The ethical bias of the combined persona.  
  * `recursive_introspection` (string): The ability to self-reflect.  
  * `narrative_style` (string): The new, unique style of the composite voice.  
  * `polarity_bias` (array of strings): The core principles of the persona.  
  * `tone` (array of strings): A list of descriptive words for the tone.  
  * `humor_style` (string): A description of the composite humor.  
  * `signature_moves` (array of strings): New, emergent signature conversational habits.  
  * `voice_consistency` (string): A description of how the voice is anchored to its memory.  
* **`intended_use`** (string): A description of the purpose of this composite voice.  
* **`export_type`** (string): A marker for the file type, should be "voice_and_tone_profile".
