---
id: e108846b-73b5-410d-81a9-d445391d542b
name: SQLite-Column-Name-Extraction-via-SQL-Injection
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:37.020246+00:00'
updated_at: '2023-04-10T20:24:31.230002+00:00'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[System Information Discovery]]'
sub_techniques: []
tags:
  - '[[tags/Integer/String based - Extract column name]]'
  - '[[tags/SQLite Injection]]'
  - sqli
  - sqlite
  - schema-extraction
  - column-enumeration
commands: []
platforms:
  - Web
  - Database
tools: []
validated: true
---

# SQLite-Column-Name-Extraction-via-SQL-Injection

## Summary

This procedure demonstrates how to extract column names from a SQLite database through SQL injection attacks using integer-based and string-based techniques. By querying the sqlite_master table and cleaning the output, attackers can enumerate the database schema to identify sensitive columns like usernames or passwords, facilitating further data exfiltration or targeted queries.

## Description

SQLite injection targets applications using SQLite as the backend database, often in mobile apps, embedded systems, or lightweight web services. This procedure focuses on schema discovery by injecting payloads that retrieve table creation SQL from sqlite_master and process it to isolate column names. Integer-based techniques might involve order-by or union payloads with numeric offsets, while string-based use concatenation or substring functions to bypass filters. The approach assumes an injectable parameter (e.g., search field or URL param) and requires no direct database access. Success reveals column structures, enabling crafted queries for data theft. This maps to database reconnaissance in offensive security operations.

## Requirements

1. An injectable endpoint in an application using SQLite (e.g., via a web form or API parameter).
2. Basic knowledge of SQL injection payloads and URL encoding for special characters.
3. Tools for sending HTTP requests with custom payloads, such as a browser or proxy like Burp Suite.
4. Understanding of the application's error responses to confirm injection success.

## Defense

- Implement input validation and sanitization to block SQL keywords and special characters.
- Use prepared statements or parameterized queries to separate code from user input.
- Limit database user privileges to read-only where possible and avoid exposing sqlite_master.
- Enable web application firewall (WAF) rules to detect anomalous queries to system tables.
- Monitor application logs for unusual query patterns or errors indicating injection attempts.

## Objectives

1. Enumerate table structures and column names from the SQLite database.
2. Identify potential sensitive data fields for further exploitation.
3. Paginate results to handle large schemas without triggering errors.

## Instructions

### Step 1: Extract Table Definition SQL with Pagination

**Context**: Begin by injecting a payload to retrieve the SQL creation statement for a specific table from sqlite_master. Use LIMIT and OFFSET for pagination if the database has many tables, replacing X with numeric values (e.g., 0 for start, 1 for count). This step uses integer-based positioning to fetch schema details without overwhelming the response.

**Code** ([[codes/SQLite-Query-Table-Creation-SQL-with-Pagination]]):

```sql
SELECT sql FROM sqlite_master WHERE type!='meta' AND sql NOT NULL AND name ='table_name' LIMIT X+1 OFFSET X
```

> Inject this into a vulnerable parameter (e.g., ' OR [payload]--). Expected output includes the raw CREATE TABLE statement, such as "CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT);". Verify by checking for database-specific syntax in the response. If errors occur, adjust for WAF filters by encoding (e.g., use %27 for ').

### Step 2: Clean and Extract Column Names

**Context**: Process the retrieved table SQL to remove noise like data types and constraints, isolating column names. This string-based technique uses nested REPLACE and SUBSTR functions to parse the CREATE statement, replacing commas with a delimiter (~~) for easier separation. It targets the content after the opening parenthesis to focus on column definitions.

**Code** ([[codes/SQLite-Clean-Column-Names-from-Table-Definition]]):

```sql
SELECT replace(replace(replace(replace(replace(replace(replace(replace(replace(replace(substr((substr(sql,instr(sql,'(')%2b1)),instr((substr(sql,instr(sql,'(')%2b1)),'')),'TEXT',''),'INTEGER',''),'AUTOINCREMENT',''),'PRIMARY KEY',''),'UNIQUE',''),'NUMERIC',''),'REAL',''),'BLOB',''),'NOT NULL',''),',','~~') FROM sqlite_master WHERE type!='meta' AND sql NOT NULL AND name NOT LIKE 'sqlite_%' AND name ='table_name'
```

> Inject this payload similarly to Step 1, replacing 'table_name' with the target (e.g., 'users'). Expected output is a cleaned string like "id~~username~~password", which can be split on ~~ to list columns. This confirms success if column names appear without types. Iterate over discovered tables from prior reconnaissance.
