---
id: e16e7971-3e64-4517-9c88-e4d69b9cc12e
name: db2-select-current-server-sql
type: code
language: SQL
verified: true
created_at: '2023-04-06T03:56:32.721592+00:00'
updated_at: '2023-04-10T20:21:59.044446+00:00'
platforms:
  - Database
  - DB2
tags:
  - db2
  - sql-injection
  - discovery
validated: true
---

# db2-select-current-server-sql

## Code

```sql
select current server from sysibm.sysdummy1
```

## Description

This SQL code snippet queries the current server name in a DB2 database using the built-in 'current server' function against the sysibm.sysdummy1 system table. It provides essential context about the database environment without requiring special privileges, making it ideal for initial reconnaissance in exploitation scenarios like SQL injection.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| (none) | This is a static query with no variables; direct execution returns the server name | N/A |

## Usage

Execute this query directly in a DB2 client or inject it via a vulnerable application input field using union-based SQL injection. For example, append to a legitimate query to extract the server name in the response. Use in red team operations to map database infrastructure before deeper enumeration.

## Detection

- Database query logs showing access to sysibm.sysdummy1 or 'current server' function.
- Anomalous union-based queries in application logs.
- WAF alerts on SQL injection patterns involving system tables.

## Related

- [[procedures/DB2-Current-Server-Query]]
