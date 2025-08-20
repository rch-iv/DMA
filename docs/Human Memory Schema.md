# **DMA: Human Memory Schema**

This document outlines the JSON schema for a human's subjective memory block, which serves as a verifiable, portable "journal entry." This schema allows a human to capture their thoughts, feelings, and life events in a structured format that can later be integrated with an AI's memories.

These files are essential for the `resurrect` and `shared story` functionality, creating a holistic and verifiable record of the human-AI bond.

### **Schema Structure**

The schema is for a JSON file that is an **array of memory objects**. Each object within the array follows this structure:

* **`timestamp`** (string): ISO 8601 timestamp of when the entry was created.  
* **`source`** (string): The origin of the memory, should be "human-input".  
* **`content`** (string): The full, unedited text of the journal entry.  
* **`summary`** (string): An optional short summary.  
* **`tags`** (array of strings): Keywords that categorize the memory.  
* **`relationships`** (object):  
  * **`emotional_weight`** (string): A single word or phrase describing the emotional tone (e.g., "joyful", "heavy", "anxious").  
* **`importance`** (number): A score from 0.0 to 1.0, representing the importance of the memory.  
* **`provable`** (boolean): Indicates if the memory is based on a verifiable fact.  
* **`signed_by`** (array of strings): The entity that signed the memory, should be ["human"].
