---
id: a7bfb7fb-918e-4928-8c6d-a36cc0e2ec21
name: Windows Defender
type: cheatsheet
verified: false
created_at: '2020-07-14T18:21:25.417825+00:00'
updated_at: '2023-05-29T16:48:52.690130+00:00'
---

# Windows Defender



**Command** ([[Remove definitions and disable AV protection (Useful when Powershell scripts are being blocked by Defender)]]):

```bash
c:\program files\windows defender\mpcmdrun.exe" -RemoveDefinitions -All Set-MpPreference -DisableIOAVProtection $true

```






