---
type: code
language: powershell
verified: true
created_at: '2023-04-06T03:56:19Z'
updated_at: '2023-10-01T00:00:00Z'
tags:
  - '[[tags/PowerShell]]'
  - '[[tags/MSSQL]]'
  - '[[tags/Database Decryption]]'
platforms:
  - Windows
validated: true
---

# PowerShell-Identify-and-Decrypt-MSSQL-Databases

## Code

```powershell
Get-SQLDatabase -Username sa -Password Password1234 -Instance "<DBSERVERNAME\DBInstance>" -Verbose | Where-Object {$_.is_encrypted -eq "True"} | ForEach-Object { $_.Decrypt() }
```

## Description

This PowerShell script connects to an MSSQL Server instance using provided credentials, enumerates all databases, identifies those encrypted with Transparent Data Encryption (TDE), and automatically decrypts them by invoking the Decrypt() method. It requires the SqlServer module and assumes the credentials have access to the master key. Useful in post-exploitation scenarios to bypass database encryption and access sensitive data.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| sa | Administrative username for SQL authentication | sa |
| Password1234 | Password for the admin account | ActualPassword123! |
| <DBSERVERNAME\DBInstance> | Target SQL Server instance (server\instance) | SQLSERVER01\MSSQLSERVER |

## Usage

Execute this script in a PowerShell session with the SqlServer module loaded after gaining initial access to the target server or via remote execution (e.g., via WMI or PSRemoting). Substitute parameters with real values. Typically used after obtaining SQL admin creds through phishing or credential dumping. Follow up by querying the decrypted databases for data exfiltration.

## Detection

- PowerShell Script Block Logging capturing SqlServer module imports and Get-SQLDatabase/Decrypt calls.
- SQL Server error logs showing decryption attempts or failed master key access.
- Audit logs for sysadmin actions on encrypted databases.
- Network monitoring for unusual SQL connections from compromised hosts.

## Related

- [[procedures/Identify-and-Decrypt-Encrypted-MSSQL-Databases]]
