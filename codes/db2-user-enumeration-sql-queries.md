---
id: c7d3b46f-703a-4e01-a3c6-a401c55f2473
name: db2-user-enumeration-sql-queries
type: code
language: sql
verified: true
created_at: '2023-04-06T03:56:32.615817+00:00'
updated_at: '2023-04-10T20:22:05.509537+00:00'
platforms:
  - Database
  - DB2
tags:
  - db2
  - enumeration
  - users
  - privileges
validated: true
---

# db2-user-enumeration-sql-queries

## Code

```sql
select distinct(authid) from sysibmadm.privileges -- This command retrieves a list of all authorized users in the DB2 instance.
select grantee from syscat.dbauth -- This command retrieves a list of all users with database-level privileges, but the results may be incomplete.
select distinct(definer) from syscat.schemata -- This command retrieves a list of all schema owners in the DB2 instance.
select distinct(grantee) from sysibm.systabauth -- This command retrieves a list of all users with table-level privileges, and it provides more accurate results than the previous command.
```

## Description

This SQL code snippet contains a series of queries designed to enumerate users and their privileges in a DB2 database. It combines instance-level authorized users, database privilege grantees, schema owners, and table privilege holders into a single reference set. Each query targets specific DB2 system views to build a comprehensive user access map without modifying the database.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| N/A | No variables; these are static SQL queries | N/A |

## Usage

Execute these queries sequentially in a DB2 client (e.g., via `db2` command line after connecting to the database) during reconnaissance to gather user intelligence. Start with the authorized users query for a broad list, then refine with schema and privilege-specific ones. Combine outputs in a tool like Excel for analysis. Useful in scenarios where initial database access is obtained via injection or weak credentials.

## Detection

- Monitor DB2 audit logs for queries accessing sysibmadm.privileges, syscat.dbauth, syscat.schemata, or sysibm.systabauth.
- Alert on unusual SELECT patterns from administrative views by non-admin users.
- Use DB2's trusted context or fine-grained auditing to flag enumeration attempts.

## Related

- [[procedures/DB2-User-Enumeration]]
- [[commands/db2-select-authorized-users]]
