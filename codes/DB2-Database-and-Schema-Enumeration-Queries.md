---
id: 29d09929-356a-49bd-9525-71dd07b429a9
name: DB2-Database-and-Schema-Enumeration-Queries
type: code
language: sql
verified: true
created_at: '2023-04-06T03:56:32.748108+00:00'
updated_at: '2023-04-10T20:21:59.788113+00:00'
platforms:
  - Database
  - DB2
tags:
  - enumeration
  - sql
validated: true
---

# DB2-Database-and-Schema-Enumeration-Queries

## Code

```sql
select distinct(table_catalog) from sysibm.tables
SELECT schemaname FROM syscat.schemata;
```

## Description

This SQL code snippet contains two queries for enumerating databases and schemas in a DB2 instance. The first lists unique database catalogs from the tables metadata, while the second retrieves all schema names from the schemata catalog. It is used in reconnaissance to understand the database structure without needing advanced privileges.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | No variables; queries are static and run against the connected instance. | N/A |

## Usage

Execute these queries sequentially in a DB2 client after connecting to the target instance. Use for initial discovery in red team engagements or auditing. Combine with export statements to save results for analysis.

## Detection

- Monitor DB2 audit logs for SELECT queries on sysibm.tables and syscat.schemata.
- Alert on unusual access to system catalogs from non-administrative users.
- Use database intrusion detection to flag enumeration patterns.

## Related

- [[procedures/Enumerate-DB2-Databases-and-Schemas]]
