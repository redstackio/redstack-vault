---
id: 31339e97-348e-43ba-a624-37b84554cf88
name: postgresql-query-users-privileges
type: code
language: SQL
verified: true
created_at: '2023-04-06T03:56:35.568934+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Database
tags:
  - postgresql
  - enumeration
validated: true
---

# postgresql-query-users-privileges

## Code

```sql
SELECT usename, usecreatedb, usesuper, usecatupd FROM pg_user
```

## Description

This SQL code snippet queries the pg_user system table in PostgreSQL to enumerate all database users and their core privileges, including superuser status and database creation rights. It is a foundational reconnaissance tool in privilege escalation scenarios, helping identify accounts for further exploitation.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | No variables; direct query | N/A |

## Usage

Execute this code within a psql session after connecting to the target database, or inject it via a vulnerable application endpoint. Use the output to target superusers (usesuper=true) for credential attacks or role assumptions. Integrate into procedures like database enumeration during lateral movement.

## Detection

- Monitor PostgreSQL logs for queries accessing pg_user or pg_roles.
- Alert on anomalous SELECT statements from low-privilege users.
- Use database firewalls to restrict access to system catalogs.

## Related

- [[procedures/PostgreSQL-Privilege-Escalation-via-User-Enumeration]]
- [[commands/postgresql-list-users-and-privileges]]
