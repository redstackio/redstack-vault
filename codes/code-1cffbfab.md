---
id: 1cffbfab-ce62-4e65-8505-df68fdd64c3e
type: code
language: SQL
verified: false
created_at: '2023-04-06T03:56:33.204800+00:00'
updated_at: '2023-04-10T20:22:01.200909+00:00'
---

# Code Snippet 1cffbfab

**Language**: SQL

```sql
select dbpartitionnum, name, value from sysibmadm.dbcfg where name like 'auto_%' -- Requires priv. Retrieve the automatic maintenance settings in the database configuration that are stored in memory for all database partitions.
select name, deferred_value, dbpartitionnum from sysibmadm.dbcfg -- Requires priv. Retrieve all the database configuration parameters values stored on disk for all database partitions.
```
