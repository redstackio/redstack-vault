---
id: b6fd1d66-20aa-4086-88f8-c0320a90e115
type: code
language: powershell
verified: true
created_at: '2023-04-06T03:56:20.683206+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - mssql
  - trustworthy
  - privilege-escalation
validated: true
---

# invoke-sql-audit-priv-trustworthy-check

## Code

```powershell
Invoke-SQLAuditPrivTrustworthy -Instance "<DBSERVERNAME\DBInstance>" -Exploit -Verbose 

SELECT name as database_name, SUSER_NAME(owner_sid) AS database_owner, is_trustworthy_on AS TRUSTWORTHY from sys.databases
```

## Description

This code snippet uses a PowerShell function to audit an MSSQL instance for trustworthy database vulnerabilities and executes a SQL query to enumerate databases with the TRUSTWORTHY property enabled. It helps identify configurations allowing potential privilege escalation through cross-database access.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| <DBSERVERNAME\DBInstance> | Target SQL Server instance name | SERVER\SQLEXPRESS |

## Usage

Load the required PowerShell module for SQL audits, replace the instance placeholder, and execute in a PowerShell session with SQL connectivity. Use in red team engagements after initial SQL access to map escalation paths. Follow with exploitation if TRUSTWORTHY=1 is found.

## Detection

- Monitor SQL Server error logs for xp_* procedure calls or unusual sys.databases queries.
- Enable PowerShell logging (Module, ScriptBlock) to detect Invoke-SQL* executions.
- Audit for ALTER DATABASE TRUSTWORTHY changes and anomalous SELECT from system views.

## Related

- [[procedures/Identify-Trustworthy-Databases-in-MSSQL]]
