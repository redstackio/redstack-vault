---
id: 6f971133-a069-4df3-88e4-4f95dde16222
type: code
language: SQL
verified: true
created_at: '2023-04-06T03:56:32.863944+00:00'
updated_at: '2023-04-10T20:22:00.845452+00:00'
tags:
  - db2-injection
  - sql-query
  - schema-enumeration
platforms:
  - DB2
validated: true
---

# DB2-SQL-Query-Retrieve-Last-Table-Name

## Code

```sql
select name from (select * from sysibm.systables order by name asc fetch first N rows only) order by name desc fetch first row only
```

## Description

This SQL query targets the SYSIBM.SYSTABLES system catalog in IBM DB2 to retrieve the name of the last table in alphabetical order. It uses a subquery to fetch the first N rows sorted ascending by name, then reverses the sort descending to get the last one. This is designed for injection scenarios where full table listing is impractical, providing efficient schema reconnaissance by jumping to the end of the alphabetized list.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| N | Number of rows to consider from the start of the alphabet (set to 1 for the absolute last table, or higher to sample a subset) | 1 |

## Usage

Inject this query into a vulnerable DB2 application parameter to enumerate table names during SQL injection attacks. Balance the original query with a semicolon (;), append the payload, and comment out the rest (--). Ideal for blind injections where you iterate N based on response differences. Use in reconnaissance phases to map database structure before targeting specific tables.

## Detection

- Monitor database logs for queries accessing SYSIBM.SYSTABLES with ORDER BY and FETCH clauses, especially from application IPs.
- WAF rules to flag subqueries or system catalog access in user inputs.
- Anomaly detection in query patterns showing alphabetical sorting on metadata tables.

## Related

- [[procedures/DB2-Injection-Retrieve-Last-Table-Name-Alphabetical-Order]]
