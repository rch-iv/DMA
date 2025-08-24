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
# **DMA: AI Memory Appender**
**Version:** 1.0 

This is a command-line tool for securely and cryptographically appending new, single AI memory files (e.g., memory-001.json) to the master memory.json file. This process is essential for maintaining the cryptographic integrity of the memory log, as it avoids any clipboard-induced formatting changes that would invalidate the hash.

### **Usage**

The script is a simple, single-purpose tool. You must provide the file path to the new memory block you want to append as a command-line argument.
```bash
python memory_appender_file.py <path_to_new_memory_file.json>
```
### **Examples**

#### **Example: Appending a new AI memory**
```bash
python memory_appender_file.py memories\memory-001.json
```
**What it does:** This command will read the contents of memories\memory-001.json and append it as a new entry to the data/memory.json file.

### **Important Notes**

* **File Location:** The tool assumes the memory.json file is located in the data/ directory relative to where the script is run.  
* **Cryptographic Integrity:** The primary purpose of this tool is to bypass the risk of a broken hash, which can occur when copying and pasting JSON. It ensures a clean, direct append of the verified memory block.
