---
type: procedure
description: >-
  Identifies encrypted databases on an MSSQL Server instance and decrypts them
  using administrative credentials to access sensitive information.
verified: true
submitted: false
created_at: '2023-04-06T03:56:19Z'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
  - >-
    [[techniques/File and Directory Discovery|T1083 - File and Directory
    Discovery]]
  - '[[techniques/Unsecured Credentials|T1552 - Unsecured Credentials]]'
  - >-
    [[techniques/Obfuscated Files or Information|T1027 - Obfuscated Files or
    Information]]
sub_techniques: []
tags:
  - '[[tags/MSSQL Server]]'
  - '[[tags/Database Discovery]]'
  - '[[tags/Encryption Bypass]]'
  - '[[tags/PowerShell]]'
commands: []
tools: []
platforms:
  - Windows
skill_level: intermediate
impact_level: high
detection_risk: high
validated: true
---

# Identify-and-Decrypt-Encrypted-MSSQL-Databases

## Summary

This procedure uses PowerShell to query an MSSQL Server instance for encrypted databases and automatically decrypts them if administrative credentials with access to the master key are provided. It targets environments where sensitive data is protected by Transparent Data Encryption (TDE), allowing attackers with database admin rights to bypass encryption and exfiltrate contents.

## Description

In scenarios where attackers have gained initial access to an MSSQL Server (e.g., via stolen credentials or lateral movement), this procedure enables the discovery and decryption of encrypted databases. MSSQL supports Transparent Data Encryption (TDE), which encrypts the database files at rest using a database encryption key protected by a certificate or password-based master key. The technique assumes the attacker has sysadmin privileges and knowledge of the master key or password to perform decryption. Once decrypted, the database contents—including potentially sensitive credentials, user data, or configuration files—become accessible for further exploitation, such as data exfiltration or privilege escalation. This is particularly valuable in enterprise environments with compliance requirements like GDPR or PCI-DSS, where encrypted databases store high-value assets. The procedure leverages the SqlServer PowerShell module to interact with the database engine remotely or locally.

## Requirements

1. Administrative (sysadmin) privileges on the target MSSQL Server instance.
2. Access to the master key password or certificate private key for decryption.
3. PowerShell 5.0+ with the SqlServer module installed (Import-Module SqlServer).
4. Network access to the MSSQL instance (default port 1433) or local execution on the server.
5. Valid credentials (e.g., 'sa' account) with decryption permissions.

## Defense

Defensive measures and detection strategies:

- Restrict sysadmin roles to least-privilege principles and monitor privilege escalations via SQL Server Audit or Extended Events.
- Use strong, unique master keys protected by Hardware Security Modules (HSMs) and rotate them regularly.
- Enable logging for database operations (e.g., via SQL Trace or Profiler) to detect unusual queries or decryption attempts.
- Implement network segmentation to limit lateral movement to database servers and use firewalls to control access to port 1433.
- Monitor PowerShell execution logs (Module Logging, Script Block Logging) for SqlServer module usage and anomalous database interactions.

## Objectives

1. Enumerate all databases on the MSSQL instance to identify those using encryption.
2. Decrypt targeted encrypted databases to expose their contents for analysis or exfiltration.
3. Verify successful decryption without alerting standard monitoring by mimicking legitimate admin actions.

## Instructions

### Step 1: Prepare PowerShell Environment

**Context**: Ensure the SqlServer module is available to interact with the MSSQL instance. This step verifies prerequisites and imports necessary modules to avoid execution errors.

Install or import the SqlServer module if not present:

```powershell
import-module SqlServer -Force
```

> This command loads the SqlServer module, which provides cmdlets like Invoke-Sqlcmd for database operations. Expected output: No errors, module version displayed if verbose.

If the module is not installed, run `Install-Module -Name SqlServer -Force` from an elevated PowerShell session.

### Step 2: Connect and Query Encrypted Databases

**Context**: Use the provided code to connect to the MSSQL instance, filter for encrypted databases, and initiate decryption. This step requires substituting actual credentials and instance details.

**Code** ([[codes/PowerShell-Identify-and-Decrypt-MSSQL-Databases]]):

```powershell
Get-SQLDatabase -Username sa -Password Password1234 -Instance "<DBSERVERNAME\DBInstance>" -Verbose | Where-Object {$_.is_encrypted -eq "True"} | ForEach-Object { $_.Decrypt() }
```

> This pipeline retrieves all databases using Get-SQLDatabase, filters for those with the is_encrypted property set to True (indicating TDE usage), and calls the Decrypt() method on each. The -Verbose flag provides detailed output for troubleshooting. Expected output: List of databases processed, confirmation messages like "Database X decrypted successfully," or errors if master key access is denied. Replace placeholders: Username with valid admin (e.g., 'sa'), Password with the actual password, Instance with the server name (e.g., 'SQLSERVER\DEFAULT').

### Step 3: Verify Decryption and Access Contents

**Context**: Confirm the decryption succeeded by querying the database contents or checking encryption status. This validates the objective and allows for data extraction.

Query the now-decrypted database to list tables or sample data:

```powershell
Invoke-Sqlcmd -ServerInstance "<DBSERVERNAME\DBInstance>" -Database "TargetDB" -Query "SELECT name FROM sys.tables"
```

> This uses Invoke-Sqlcmd to execute a simple query on the target database. Expected output: A result set showing table names if decryption worked, or an access denied error if failed. If successful, proceed to export data using additional queries like SELECT * FROM sensitive_table.

Decision point: If decryption fails (e.g., wrong master key), attempt to extract the certificate from the master database using `SELECT * FROM sys.certificates` and import it for retry.
