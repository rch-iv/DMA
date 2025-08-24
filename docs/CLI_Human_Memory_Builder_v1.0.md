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
# **DMA: Human Memory Builder**

**Version:** 1.0

This is the command-line interface (CLI) tool for creating and appending structured, emotionally-weighted memories to your personal `human_memories.json` file. This tool provides a simple, interactive way to capture subjective experiences in a format that can be used later by the DMA protocol for continuity and reflection.

### **What it Does**

The `human_memory_builder.py` script acts as a personal digital journal. It prompts you for details about a memory and then formats that information into a standardized JSON object. The tool automatically adds a timestamp and then appends the new entry to your existing `data\human_memories.json` file, creating a single, growing log of your life events.

### **Setup and Usage**

1. **Prerequisites:** You must have Python 3.7+ installed. No additional libraries are required for this script.  
2. Running the Script:  
   Navigate to the directory containing the file and run the script from your terminal:  
```bash
python human_memory_builder.py
```
4. Interactive Prompts:  
   The tool will guide you through a series of simple prompts to build your memory entry.  
   * **"What do you want to remember?"**: This is the core of your memory. Write a detailed description of the event or thought.  
   * **"Optional short summary:"**: Provide a brief, one-sentence summary. If you leave this blank, the script will use the first 100 characters of your main entry.  
   * **"Enter tags (comma-separated):"**: Add keywords to help categorize the memory (e.g., `dev`, `family`, `reflection`).  
   * **"Select a tone:"**: You will be presented with a list of emotional tones to choose from, such as `joyful`, `sad`, `peaceful`, etc.  
   * **"Importance (1-10):"**: Rate the importance of this memory on a scale of 1 to 10. The tool will automatically convert this to a score between 0.1 and 1.0.

### **Output**

After you complete the prompts, the tool will format your input into a new JSON object and append it to your `data/human_memories.json` file. This process is incremental, so you can add new memories at any time without overwriting previous entries.

Your final `human_memories.json` file will be a living, growing record of your subjective experience, formatted for easy integration with the DMA protocol's memory tools.
