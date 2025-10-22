---
id: aeef471a-ae9e-487c-98b2-18aeed78312a
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:26.392983+00:00'
updated_at: '2023-04-10T20:37:04.889627+00:00'
---

# Code Snippet aeef471a

**Language**: Powershell

```powershell
PowerView PS C:\> Get-AppLockerPolicy -Effective | select -ExpandProperty RuleCollections
PowerView PS C:\> Get-AppLockerPolicy -effective -xml
Get-ChildItem -Path HKLM:\SOFTWARE\Policies\Microsoft\Windows\SrpV2\Exe # (Keys: Appx, Dll, Exe, Msi and Script
```
