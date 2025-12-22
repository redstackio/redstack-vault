---
type: command
executor: powershell
data: >-
  Get-SQLAgentJob -Instance "<DBSERVERNAME\DBInstance>" -username sa -Password
  Password1234 -Verbose
output: null
platforms:
  - Windows
  - SQL Server
tags:
  - discovery
  - mssql
  - powershell
verified: true
validated: true
---

# mssql-get-sqlagentjob-powershell

## Command

```powershell
Get-SQLAgentJob -Instance "<DBSERVERNAME\DBInstance>" -username sa -Password Password1234 -Verbose
```

## Description

This PowerShell cmdlet uses the SqlServer module to retrieve SQL Server Agent job details from a remote instance. Useful for scripted enumeration in Windows environments.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -Instance | SQL Server instance name (e.g., SERVER\SQLEXPRESS) | Yes |
| -username | SQL login username | Yes |
| -Password | Plaintext password (use SecureString in production) | Yes |
| -Verbose | Enables detailed output | No |

## Examples

### Basic Usage

```powershell
Get-SQLAgentJob -Instance "SERVER\DEFAULT" -username sa -Password Password1234
```

### Advanced Usage

With output formatting:

```powershell
Get-SQLAgentJob -Instance "SERVER\DEFAULT" -username sa -Password Password1234 | Format-Table Name, Enabled, Description -AutoSize
```

## Expected Output

List of Job objects:

```
Name                Enabled Description
----                ------- -----------
Weekly Backup Job   True    Automated backups
Data Export Task    True    Exports data to file
```

Verbose adds connection logs.

## Related

- [[procedures/Enumerate-MSSQL-Server-Agent-Jobs]]
- [[commands/mssql-select-job-details-from-sysjobs-and-sysjobsteps]]
