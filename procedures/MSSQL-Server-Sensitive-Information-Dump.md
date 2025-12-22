---
id: 5df072de-e895-43df-9c17-62101bbc5771
name: MSSQL-Server-Sensitive-Information-Dump
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:19.997054+00:00'
updated_at: '2023-04-10T20:36:31.050161+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - >-
    [[techniques/System Information Discovery|T1082 - System Information
    Discovery]]
sub_techniques: []
tags:
  - '[[tags/Dump common information from server to files]]'
  - '[[tags/Identify Sensitive Information]]'
  - '[[tags/MSSQL Server]]'
commands:
  - '[[commands/invoke-sqldumpinfo-analyze-dump-verbose-csv]]'
platforms:
  - Windows
tools: []
validated: true
---

# MSSQL-Server-Sensitive-Information-Dump

## Summary

The MSSQL Server Sensitive Information Dump procedure identifies and extracts sensitive information from a target MSSQL server by leveraging SQL dump analysis to retrieve common server details, including usernames, passwords, and other credentials, writing them to files for further use in attacks like password spraying or credential stuffing.

## Description

This procedure targets MSSQL servers to perform discovery of sensitive data through dump file analysis. It uses PowerShell-based SQL commands to query and extract information from the server instance, focusing on crash dumps or diagnostic files that may contain exposed credentials. The technique is applicable in environments where an attacker has valid credentials or network access to the MSSQL instance. Expected outcomes include files containing extracted data that can pivot to lateral movement or privilege escalation. This aligns with reconnaissance and discovery phases in red team operations, providing actionable intelligence without requiring high privileges initially.

## Requirements

1. Valid credentials (username and password) for the target MSSQL server instance.
2. Network access to the MSSQL server (typically TCP port 1433 open).
3. PowerShell environment with SQL Server module or equivalent access to Invoke-SQLDumpInfo cmdlet.

## Defense

Defensive measures and detection strategies:

- Enforce strong, complex passwords for all MSSQL accounts and implement multi-factor authentication where possible.
- Restrict network access to the MSSQL server using firewalls, limiting connections to trusted IP ranges and requiring VPN for remote access.
- Enable and monitor MSSQL server logs (e.g., ERRORLOG, audit logs) for suspicious queries, failed logins, or unusual dump analysis attempts; integrate with SIEM for alerting on anomalous PowerShell executions.

## Objectives

1. Identify and extract sensitive information such as usernames and passwords from the MSSQL server.
2. Dump the data to local files for offline analysis and use in subsequent attacks.
3. Verify successful extraction to confirm the presence of exploitable credentials.

## Instructions

### Step 1: Analyze MSSQL Dump Files for Sensitive Information

**Context**: This step uses the Invoke-SQLDumpInfo cmdlet to retrieve and analyze dump files from the specified MSSQL instance, extracting details like credentials and server configuration. It provides verbose output and saves results to a CSV file for easy parsing. Run this from a machine with network access to the target, substituting the instance name with the actual target (e.g., SERVER\INSTANCE).

**Command** ([[commands/invoke-sqldumpinfo-analyze-dump-verbose-csv]]):
```powershell
Invoke-SQLDumpInfo -Verbose -Instance $_INSTANCE_NAME -csv $_OUTPUT_FILE
```

> The -Verbose flag enables detailed logging of the analysis process, helping identify any issues during extraction. The -Instance parameter targets the specific SQL Server instance (format: SERVER\INSTANCE). The -csv flag outputs results to a specified file path. Expected output includes a CSV file populated with server details, such as usernames, hashed passwords, and configuration data. If the dump contains sensitive info, it will be listed in columns like 'User', 'PasswordHash', and 'ServerInfo'. Verify by opening the CSV and checking for non-empty credential fields.
