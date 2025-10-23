---
id: 94abac2e-51df-4ef0-86c4-7dce72eceb00
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:08.936517+00:00'
updated_at: '2023-04-10T20:20:58.743576+00:00'
---

# Code Snippet 94abac2e

**Language**: Powershell

```powershell
$ git clone https://github.com/cyberark/SkyArk
$ powershell -ExecutionPolicy Bypass -NoProfile
PS C> Import-Module .\SkyArk.ps1 -force
PS C> Start-AWStealth

or in the Cloud Console

PS C> IEX (New-Object Net.WebClient).DownloadString('https://raw.githubusercontent.com/cyberark/SkyArk/master/AWStealth/AWStealth.ps1')  
PS C> Scan-AWShadowAdmins
```


