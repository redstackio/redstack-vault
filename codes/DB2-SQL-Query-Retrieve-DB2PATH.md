---
id: 8c63c1e1-c4fb-4768-8925-1fbf984361aa
type: code
language: SQL
verified: true
created_at: '2023-04-06T03:56:33.178227+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - Windows
  - Database
tags:
  - sql-injection
  - db2
  - database-enumeration
validated: true
---

# DB2-SQL-Query-Retrieve-DB2PATH

## Code

```sql
select * from sysibmadm.reg_variables where reg_var_name='DB2PATH' -- requires priv
```

## Description

This SQL query retrieves the DB2PATH environment variable from the DB2 system registry table sysibmadm.reg_variables. It filters for the specific variable name 'DB2PATH', which holds the installation path of the DB2 database files. The trailing comment (--) neutralizes any subsequent query parts in an injection scenario. This code is used in SQL injection attacks to enumerate database configuration for further exploitation.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| reg_var_name | The name of the registry variable to query | 'DB2PATH' |

(Note: No user-substitutable variables in this fixed query; adapt the WHERE clause for other variables if needed.)

## Usage

Inject this query via a vulnerable input point in a DB2-backed application, such as a web form, using UNION-based injection to append it to the original query. For example: `' UNION SELECT * FROM sysibmadm.reg_variables WHERE reg_var_name='DB2PATH' --`. Execute in the context of an authenticated or public-facing endpoint. Requires privileges to access sysibmadm tables; test in a lab environment first.

This code is referenced in the [[procedures/Retrieve-DB2PATH-via-SQL-Injection]] procedure for database path enumeration.

## Detection

- Monitor database logs for queries accessing sysibmadm.reg_variables or unusual SELECT statements with UNION/WHERE clauses targeting environment variables.
- Web application logs showing payloads with 'DB2PATH' or comment syntax (--).
- Anomalous error messages like privilege denial on registry access (DB21034E).
- Use intrusion detection systems to flag SQL injection patterns in traffic to DB2 ports (typically 50000).
