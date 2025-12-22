---
id: 7c4d3978-e1fb-4770-8a51-6930fa568c50
name: DB2-Version-Extraction-SQL-Queries
type: code
language: sql
verified: true
created_at: '2023-04-06T03:56:32.535594+00:00'
updated_at: '2023-04-10T20:21:57.272722+00:00'
platforms:
  - Database
  - DB2
tags:
  - db2
  - version
  - recon
validated: true
---

# DB2-Version-Extraction-SQL-Queries

## Code

```sql
select versionnumber, version_timestamp from sysibm.sysversions;
select service_level from table(sysproc.env_get_inst_info()) as instanceinfo
select getvariable('sysibm.version') from sysibm.sysdummy1 -- (v8+)
select prod_release,installed_prod_fullname from table(sysproc.env_get_prod_info()) as productinfo
select service_level,bld_level from sysibmadm.env_inst_info
```

## Description

This SQL code snippet contains a series of queries to extract comprehensive version, service level, build, and product information from an IBM DB2 database. It targets system tables and functions to gather reconnaissance data without modifying the database.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | No variables; direct queries | N/A |

## Usage

Execute these queries sequentially in a DB2 SQL client or via an injection vector during a penetration test. Start with the versionnumber query for quick identification, then proceed to detailed instance and product info. Useful in red team engagements targeting database servers to map vulnerabilities.

## Detection

- Audit logs showing SELECTs on SYSIBM.SYSVERSIONS, SYSPROC.ENV_GET_INST_INFO(), or SYSIBMADM.ENV_INST_INFO.
- Anomalous query patterns from non-admin users accessing administrative views.
- Intrusion detection signatures for version enumeration in SQL traffic.

## Related

- [[procedures/Extract-DB2-Database-Version-Information]]
