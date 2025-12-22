---
id: 1cffbfab-ce62-4e65-8505-df68fdd64c3e
name: DB2-Configuration-Parameters-Queries
type: code
language: SQL
verified: true
created_at: '2023-04-06T03:56:33.204800+00:00'
updated_at: '2023-04-10T20:22:01.200909+00:00'
platforms:
  - Linux
tags:
  - database
  - db2
  - configuration
  - sql
validated: true
---

# DB2-Configuration-Parameters-Queries

## Code

```sql
select dbpartitionnum, name, value from sysibmadm.dbcfg where name like 'auto_%' -- Requires priv. Retrieve the automatic maintenance settings in the database configuration that are stored in memory for all database partitions.
select name, deferred_value, dbpartitionnum from sysibmadm.dbcfg -- Requires priv. Retrieve all the database configuration parameters values stored on disk for all database partitions.
```

## Description

This SQL code snippet contains two queries to extract DB2 configuration parameters: the first retrieves in-memory automatic maintenance settings across partitions, and the second fetches all disk-stored parameters including deferred values. It is used in database discovery to uncover sensitive details like credentials and policies after gaining query execution access.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | The queries are fixed; no variables. Substitute partition filters if needed (e.g., add WHERE dbpartitionnum = 0). | N/A |

## Usage

Execute these queries via a DB2 client (e.g., db2 command) or inject into a vulnerable web application. Run the first for quick maintenance insights, then the second for full config dump. Parse output for sensitive data like authentication settings.

## Detection

- Database logs showing SELECT on sysibmadm.dbcfg from unauthorized sessions.
- Anomalous query patterns with LIKE 'auto_%' or full table scans.
- Increased access to administrative views without legitimate admin activity.

## Related

- [[procedures/DB2-Configuration-Parameters-Retrieval]]
