---
type: code
language: sql
verified: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Oracle Database
tags:
  - oracle-sql
  - discovery
  - enumeration
validated: true
---

# Oracle-SQL-Database-Enumeration-Queries

## Code

```sql
SELECT global_name FROM global_name;
SELECT name FROM V$DATABASE;
SELECT instance_name FROM V$INSTANCE;
SELECT SYS.DATABASE_NAME FROM DUAL;
```

## Description

This SQL code snippet contains a sequence of four queries designed to enumerate essential Oracle database identifiers: the global name, local database name, instance name, and system database name. It is intended for use in reconnaissance during penetration testing, particularly via SQL injection vectors, to map the target's database infrastructure without requiring complex tooling.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | This is a static set of queries with no variables; adapt for injection by wrapping in UNION or stacked statements. | N/A |

## Usage

Execute the queries sequentially in a SQL client like sqlplus after gaining database access, or inject them into vulnerable web parameters using techniques like union-based SQLi (e.g., `' UNION SELECT global_name FROM global_name--`). In automated tools like sqlmap, reference as custom payloads for Oracle targets. This snippet is reusable in procedures focusing on Oracle discovery.

## Detection

- Audit logs showing SELECT against V$ views or DUAL with SYS functions from unprivileged users.
- Web application logs indicating injection attempts with these exact query patterns.
- Intrusion detection signatures for SQLi payloads containing 'V$DATABASE', 'V$INSTANCE', or 'SYS.DATABASE_NAME'.

## Related

- [[procedures/Oracle-SQL-Database-Name-Enumeration]]
- [[tools/sqlplus]] (for execution)
