---
id: 6ed79a12-5c79-4caa-b259-8914ff6f6bdd
type: code
language: SQL
verified: true
created_at: '2023-04-06T03:56:37.018191+00:00'
updated_at: '2023-04-10T20:24:31.294791+00:00'
tags:
  - sqli
  - sqlite
  - schema-extraction
platforms:
  - Database
validated: true
---

# SQLite-Query-Table-Creation-SQL-with-Pagination

## Code

```sql
SELECT sql FROM sqlite_master WHERE type!='meta' AND sql NOT NULL AND name ='table_name' LIMIT X+1 OFFSET X
```

## Description

This SQL query retrieves the creation statement (CREATE TABLE SQL) for a specific table from the sqlite_master system table, excluding metadata tables. It uses LIMIT and OFFSET for pagination, making it suitable for integer-based SQL injection scenarios where large result sets need to be handled incrementally. The query focuses on non-null SQL definitions to ensure valid table schemas are returned.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| table_name | Name of the target table to query | users |
| X (in LIMIT X+1) | Number of rows to return (e.g., for pagination count) | 5 |
| X (in OFFSET X) | Starting offset for pagination | 0 |

## Usage

Inject this query into a vulnerable SQLite-backed application parameter, such as a search field: ' OR [query]--. Use it during database schema enumeration in SQL injection attacks to fetch table structures one at a time. Paginate by incrementing the OFFSET value in subsequent requests to avoid response size limits.

## Detection

- Monitor for queries accessing sqlite_master, which is unusual for normal application traffic.
- Look for patterns involving LIMIT/OFFSET in user inputs, indicating enumeration attempts.
- Enable SQL logging to capture full query strings and flag system table access.

## Related

- [[procedures/SQLite-Column-Name-Extraction-via-SQL-Injection]]
