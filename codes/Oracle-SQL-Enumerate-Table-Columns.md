---
type: code
language: sql
verified: true
tags:
  - oracle
  - sqli
  - enumeration
platforms:
  - Database
  - Oracle
validated: true
---

# Oracle-SQL-Enumerate-Table-Columns

## Code

```sql
SELECT column_name FROM all_tab_columns WHERE table_name = 'blah';
SELECT column_name FROM all_tab_columns WHERE table_name = 'blah' and owner = 'foo';
```

## Description

This SQL code snippet contains two queries to enumerate column names from Oracle tables using the ALL_TAB_COLUMNS view. The first query retrieves columns for a table regardless of owner, while the second filters by a specific owner. It is designed for injection into vulnerable applications to perform database schema reconnaissance.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| table_name | The target table name | 'USERS' or 'blah' |
| owner | The schema owner (optional for first query) | 'HR' or 'foo' |

## Usage

Embed these queries in SQL injection payloads, such as UNION SELECT statements, to extract results via web responses. Use the first for broad enumeration and the second for precise schema targeting. Requires a confirmed SQLi vector.

## Detection

- Monitor application logs for queries accessing ALL_TAB_COLUMNS.
- WAF rules for UNION SELECT patterns or anomalous SELECT statements.
- Database audit trails showing access to metadata views by unexpected users.

## Related

- [[procedures/Oracle-SQL-Column-Enumeration]]
