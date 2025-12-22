---
id: 341790fd-9034-4aeb-a700-62ebd6c554d4
name: db2-select-versionnumber-and-timestamp
type: command
executor: sql
data: 'select versionnumber, version_timestamp from sysibm.sysversions;'
output: null
created_at: '2023-04-06T03:56:32.535683+00:00'
updated_at: '2023-04-10T20:21:57.272196+00:00'
platforms:
  - Database
  - DB2
tags:
  - db2
  - version
  - recon
verified: true
validated: true
---

# db2-select-versionnumber-and-timestamp

## Command

```sql
select versionnumber, version_timestamp from sysibm.sysversions;
```

## Description

This SQL command queries the SYSIBM.SYSVERSIONS system table in DB2 to retrieve the database version number and the timestamp when that version was built. Use this during reconnaissance to identify the base DB2 version for vulnerability research.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Pure SELECT query; no parameters needed | N/A |

## Examples

### Basic Usage

```sql
select versionnumber, version_timestamp from sysibm.sysversions;
```

### Usage in db2 CLI

Connect to the database first with `db2 connect to DBNAME`, then execute the query.

## Expected Output

```
VERSIONNUMBER                VERSION_TIMESTAMP
----------------------------- --------------------------
SQL11005                     2021-08-20-12.00.00.000000
```

A successful query returns a single row with the version string (e.g., SQL11005 for DB2 11.5) and a timestamp indicating the build date.

## Related

- [[procedures/Extract-DB2-Database-Version-Information]]
