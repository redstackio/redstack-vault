---
id: 46d671ec-57ad-4c85-8db4-484f3302927c
type: code
language: Powershell
verified: false
created_at: '2020-03-26T06:12:17.892589+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
---

# Code Snippet 46d671ec

**Language**: Powershell

```powershell
Get-AppxPackage -allusers Microsoft.WindowsStore | Foreach {Add-AppxPackage -DisableDevelopmentMode -Register "$($_.InstallLocation)\AppXManifest.xml"}
```
