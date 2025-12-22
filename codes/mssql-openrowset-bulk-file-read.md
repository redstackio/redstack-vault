---
id: 426daf60-8b7a-409f-b8a5-31ab00f4a2f3
name: mssql-openrowset-bulk-file-read
type: code
language: SQL
verified: true
created_at: '2023-04-06T03:56:33.915040+00:00'
updated_at: '2023-04-10T20:22:42.036386+00:00'
platforms:
  - Windows
tags:
  - mssql-injection
  - file-read
validated: true
---

# mssql-openrowset-bulk-file-read

## Code

```sql
-1 union select null,(select x from OpenRowset(BULK 'C:\Windows\win.ini',SINGLE_CLOB) R(x)),null,null
```

## Description

This SQL code snippet exploits SQL injection to read the contents of a Windows INI file (e.g., win.ini) using the OpenRowset function with BULK mode. It unions the file data into a query result, allowing extraction of configuration details like server paths or credentials in a database query response.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| 'C:\\Windows\\win.ini' | Full path to the target INI file on the Windows server | 'C:\\Windows\\system.ini' |

## Usage

Inject this payload into a vulnerable SQL query parameter (e.g., via a web form UNION SELECT). Requires the database to be in bulk-logged recovery mode. Use in reconnaissance to gather system config; deliver via tools like sqlmap or manual injection in Burp Suite.

## Detection

- Monitor for OpenRowset executions in SQL logs or Extended Events.
- Alert on BULK operations or UNION queries referencing file paths.
- Watch for recovery model changes preceding unusual SELECTs.

## Related

- [[procedures/MSSQL-Read-File-via-INI-Disclosure]]
- [[tools/sqlmap]]
