# **DMA Human Memory Builder: User Guide**

Welcome to the DMA Human Memory Builder\! This tool is designed to help you create structured, machine-readable memory payloads for your SoulChain, capturing key moments, insights, and feelings in a format that can be easily processed and archived.

### **How to Use**

Simply fill out the form fields below to create a comprehensive memory entry. The more details you provide, the richer the memory will be.

1. **What do you want to remember?** (Required)  
   * In this box, write a detailed account of the memory. This is the core content of your memory entry. It can be a thought, a reflection, a conversation, or a detailed event.  
2. **Short summary** (Optional)  
   * Provide a brief summary of the memory. If you leave this blank, the app will automatically generate one using the first 100 characters of your main content.  
3. **Tags** (Optional)  
   * Enter keywords or labels to categorize your memory. Use a comma to separate each tag. Examples include insight, a-ha-moment, discussion, bug-fix.  
4. **Emotional Tone**  
   * Select the button that best represents the emotional tone of this memory. This helps to provide emotional context and weighting.  
5. **Importance**  
   * Use the slider to rate the importance of this memory on a scale of 1 to 10\. A rating of 1 means "Not Important" and a rating of 10 means "Highly Important." The app converts this to a score between 0.0 and 1.0 in the final file.

### **Generating the JSON File**

Once you have filled out the fields, click the **"Generate Memory JSON"** button. The application will:

* Validate that you have entered content in the required field.  
* Construct a JSON object with all the information you provided.  
* Automatically prompt a download of a .json file to your computer. The file will be named human\_memory\_payload\_\[timestamp\].json.

This file is now ready to be added to your SoulChain.
