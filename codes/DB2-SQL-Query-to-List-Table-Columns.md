---
type: code
language: sql
verified: true
created_at: '2023-10-01T00:00:00.000000+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Databases
  - DB2
tags:
  - SQL-Injection
  - Payload
  - Database-Discovery
validated: true
---

# DB2-SQL-Query-to-List-Table-Columns

## Code

```sql
select name, tbname, coltype from sysibm.syscolumns -- also valid syscat and sysstat
```

## Description

This SQL code snippet is a payload for enumerating column metadata in a DB2 database via injection. It targets the sysibm.syscolumns system table to extract column names, parent table names, and data types, providing a schema overview essential for further exploitation like targeted data dumps.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| (None) | The query uses fixed system table references; customize by replacing 'sysibm.syscolumns' with 'syscat.columns' for schema-specific results | N/A |

## Usage

Inject this code into a vulnerable DB2-connected application parameter (e.g., after a ' UNION SELECT' or direct append with ';'). Observe the response for leaked metadata. Ideal for blind SQLi where full errors aren't visible—use substring extraction if needed (e.g., SUBSTR(name,1,1)). Commonly used in web app pentests after confirming DB2 backend via fingerprinting.

## Detection

- Database logs showing SELECT queries on system tables from application IPs.
- WAF alerts for SQL keywords like 'syscolumns' or 'coltype' in inputs.
- Anomalous response times or sizes indicating schema enumeration.
- Application logs with injection patterns (e.g., trailing comments '--').

## Related

- [[procedures/DB2-SQL-Injection-to-List-Table-Columns]]
