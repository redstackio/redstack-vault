---
id: ebbfd331-774e-489d-8e09-06204b30b441
type: code
language: SQL
verified: true
created_at: '2023-04-06T03:56:34.943638+00:00'
updated_at: '2023-04-10T20:22:57.309257+00:00'
tags:
  - sql-injection
  - mysql
  - database-enumeration
platforms:
  - MySQL
validated: true
---

# MySQL-Extract-Table-Schemas-and-Names

## Code

```sql
SELECT json_arrayagg(concat_ws(0x3a,table_schema,table_name)) from INFORMATION_SCHEMA.TABLES;
```

## Description

This SQL code snippet queries the MySQL INFORMATION_SCHEMA.TABLES view to retrieve all database schemas and their table names, concatenating each pair with a colon separator and aggregating the results into a JSON array. It is designed for use in SQL injection attacks to efficiently enumerate database structure in scenarios where response size is limited, such as blind or union-based injections.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| 0x3a | Hex representation of the separator (colon) | 0x3a (fixed) |

(No user-substitutable variables; the query is self-contained.)

## Usage

Inject this query into a vulnerable SQL endpoint, such as a web application's input parameter (e.g., ?id=1'; [CODE HERE] -- ). It is typically used after confirming SQLi vulnerability to map the target database for further exploitation, like targeting specific tables for data exfiltration. In red team operations, deliver via tools like sqlmap or manual HTTP requests.

## Detection

- Monitor database logs for queries accessing INFORMATION_SCHEMA.TABLES or using json_arrayagg/concat_ws functions.
- Web application logs showing anomalous JSON responses in error/output fields.
- Intrusion detection signatures for SQLi payloads containing 'INFORMATION_SCHEMA' or hex separators like 0x3a.
- Rate of metadata queries exceeding normal application behavior.

## Related

- [[procedures/Extract-MySQL-Database-Schema-and-Table-Names-via-SQL-Injection]]
