---
id: 2ede9e0c-1660-4526-8d1a-08008d1a38f7
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:28.589446+00:00'
updated_at: '2023-04-10T20:37:36.294286+00:00'
---

# Code Snippet 2ede9e0c

**Language**: Powershell

```powershell
wmic logicaldisk get caption || fsutil fsinfo drives
wmic logicaldisk get caption,description,providername
Get-PSDrive | where {$_.Provider -like "Microsoft.PowerShell.Core\FileSystem"}| ft Name,Root
```
