---
id: fdcbda9b-fdf5-45c9-bbb4-56af437c61b7
name: DB2-Select-Tables-By-Column-Name
type: code
language: SQL
verified: true
created_at: '2023-04-06T03:56:32.836458+00:00'
updated_at: '2023-04-10T20:22:04.831292+00:00'
platforms:
  - Databases
  - DB2
tags:
  - SQL-Injection
  - Database-Enumeration
validated: true
---

# DB2-Select-Tables-By-Column-Name

## Code

```sql
select tbname from sysibm.syscolumns where name='username'
```

## Description

This SQL code snippet queries the DB2 sysibm.syscolumns system table to identify and list the names of tables (tbname) that include a specific column, such as 'username'. It is designed for use in SQL injection scenarios to perform database schema enumeration without direct administrative access.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| name='username' | The target column name to filter by (replace with desired column like 'password' or 'email') | name='credit_card' |

## Usage

Inject this query into a vulnerable DB2 input field, often via UNION SELECT or subquery techniques, e.g., "' UNION SELECT tbname FROM sysibm.syscolumns WHERE name='username'--". Execute through a web application or direct DB2 client. Use the output table names for further queries to extract data.

## Detection

- Monitor DB2 audit logs for queries accessing sysibm.syscolumns or syscat.columns.
- Detect anomalous UNION-based injections in application logs.
- Use intrusion detection systems to flag access to system catalogs from unprivileged users.
- Enable DB2's trusted context and row/column-level security to restrict schema queries.

## Related

- [[procedures/DB2-SQL-Injection-to-Find-Tables-by-Column-Name]]
