---
id: c7d3b46f-703a-4e01-a3c6-a401c55f2473
type: code
language: SQL
verified: false
created_at: '2023-04-06T03:56:32.615817+00:00'
updated_at: '2023-04-10T20:22:05.509537+00:00'
---

# Code Snippet c7d3b46f

**Language**: SQL

```sql
select distinct(authid) from sysibmadm.privileges -- This command retrieves a list of all authorized users in the DB2 instance.
select grantee from syscat.dbauth -- This command retrieves a list of all users with database-level privileges, but the results may be incomplete.
select distinct(definer) from syscat.schemata -- This command retrieves a list of all schema owners in the DB2 instance.
select distinct(grantee) from sysibm.systabauth -- This command retrieves a list of all users with table-level privileges, and it provides more accurate results than the previous command.
```


