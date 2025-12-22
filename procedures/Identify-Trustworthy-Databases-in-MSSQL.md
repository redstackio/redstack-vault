---
id: 72004c31-779f-46e8-b727-a221d3587d4a
name: Identify-Trustworthy-Databases-in-MSSQL
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:20.690839+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - >-
    [[techniques/System Information Discovery|T1082 - System Information
    Discovery]]
sub_techniques: []
tags:
  - '[[tags/Find databases that have been configured as trustworthy]]'
  - '[[tags/MSSQL Server]]'
commands:
  - '[[commands/invoke-sql-audit-priv-xp-dirtree]]'
  - '[[commands/invoke-sql-audit-priv-xp-fileexist]]'
  - '[[commands/invoke-sql-unc-path-injection]]'
platforms:
  - Windows
  - MSSQL
tools: []
validated: true
---

# Identify-Trustworthy-Databases-in-MSSQL

## Summary

This procedure identifies Microsoft SQL Server (MSSQL) databases configured with the TRUSTWORTHY property set to ON, which enables cross-database ownership chaining and can allow code execution with elevated privileges. Attackers use this to discover vulnerable databases for privilege escalation. It combines PowerShell auditing commands with SQL queries to enumerate databases and test related SQL injection vulnerabilities like directory traversal and UNC path injection.

## Description

In MSSQL environments, the TRUSTWORTHY database option, when enabled, permits modules in one database to access objects in another without explicit permissions, potentially leading to privilege escalation if exploited via SQL injection or extended stored procedures. This procedure targets authenticated sessions on MSSQL instances to query the sys.databases view for the is_trustworthy_on flag and uses PowerShell modules (e.g., from SQL Server attack toolkits) to audit for exploitable configurations. It also incorporates tests for related vulnerabilities such as xp_dirtree for directory traversal, xp_fileexist for file checks, and UNC path injection, which can confirm audit privileges and enable further escalation. This is useful in post-exploitation scenarios where an attacker has SQL login access but seeks sysadmin privileges.

## Requirements

1. Authenticated access to the MSSQL instance (e.g., via SQL login with db_datareader or higher privileges).
2. PowerShell environment with SQL Server attack modules loaded (e.g., Invoke-SQL* functions from custom or open-source toolkits like PowerSploit extensions).
3. Network connectivity to the MSSQL server (default port 1433).
4. Basic knowledge of SQL Server system views and PowerShell execution policy allowing scripts.

## Defense

- Disable the TRUSTWORTHY option on all databases unless explicitly required for cross-database operations; use ALTER DATABASE SET TRUSTWORTHY OFF.
- Implement principle of least privilege: Restrict SQL logins to minimal roles and monitor for unusual queries against sys.databases.
- Enable SQL Server auditing for extended stored procedures (xp_dirtree, xp_fileexist) and UNC path usage; review logs for suspicious activity.
- Use database firewalls or proxies to block unauthorized extended procedure calls and inject anomalous SQL patterns via SIEM rules.

## Objectives

1. Enumerate MSSQL databases with TRUSTWORTHY enabled to identify escalation vectors.
2. Verify audit privileges through related SQL injection tests (directory traversal, file existence, UNC paths).
3. Gather evidence of vulnerable configurations for further exploitation or reporting.

## Instructions

### Step 1: Audit for Trustworthy Databases and Enumerate Properties

**Context**: Execute a PowerShell command to audit the SQL instance for trustworthy configurations and run a SQL query to list database names, owners, and TRUSTWORTHY status. This reveals databases vulnerable to privilege escalation via ownership chaining.

**Code** ([[codes/invoke-sql-audit-priv-trustworthy-check]]):

```sql
Invoke-SQLAuditPrivTrustworthy -Instance "<DBSERVERNAME\DBInstance>" -Exploit -Verbose 

SELECT name as database_name, SUSER_NAME(owner_sid) AS database_owner, is_trustworthy_on AS TRUSTWORTHY from sys.databases
```

> The Invoke-SQLAuditPrivTrustworthy command connects to the specified instance, checks for exploitable trustworthy settings, and generates verbose output on potential escalations. The subsequent SELECT query from sys.databases returns a table showing database details. Replace <DBSERVERNAME\DBInstance> with your target (e.g., "SERVER\SQLEXPRESS"). Expected output includes a report of vulnerable databases and a result set like: database_name | database_owner | TRUSTWORTHY (1 for ON, 0 for OFF). If TRUSTWORTHY is 1 for any database, it indicates a potential escalation path.

### Step 2: Test for Directory Traversal via xp_dirtree

**Context**: Use this command to check if the current user has privileges to execute xp_dirtree, an extended stored procedure that can be abused for directory listing and traversal, confirming audit-related escalation potential tied to trustworthy databases.

**Command** ([[commands/invoke-sql-audit-priv-xp-dirtree]]):

```powershell
Invoke-SQLAuditPrivXpDirtree
```

> This PowerShell function invokes xp_dirtree within the SQL context to enumerate directories. Run it after connecting to the instance. Expected output: A list of files and directories if successful, indicating privilege to perform traversal attacks. If it fails with permission errors, the user lacks necessary audit rights.

### Step 3: Test for UNC Path Injection

**Context**: Test for SQL injection via UNC paths, which can be used to access remote files or confirm network-based escalation when combined with trustworthy database access.

**Command** ([[commands/invoke-sql-unc-path-injection]]):

```powershell
Invoke-SQLUncPathInjection
```

> This command attempts UNC path access (e.g., \\attacker\share\file) to inject and retrieve remote content. Expected output: Contents of the targeted file or success confirmation if the injection works, highlighting network exposure. Failure indicates blocked UNC execution.

### Step 4: Test for File Existence via xp_fileexist

**Context**: Verify privileges for xp_fileexist, which checks file presence and can aid in reconnaissance or confirmation of local file access in escalation chains involving trustworthy databases.

**Command** ([[commands/invoke-sql-audit-priv-xp-fileexist]]):

```powershell
Invoke-SQLAuditPrivXpFileexist
```

> This PowerShell wrapper calls xp_fileexist on a target path. Expected output: Boolean or details on file existence (e.g., File exists: 1), confirming audit privileges. Use it to probe sensitive paths like boot.ini or config files.
