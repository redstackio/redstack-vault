---
id: c3e024b7-d247-422e-864a-d03b193ea514
type: code
language: SQL
verified: false
created_at: '2023-04-06T03:56:33.675877+00:00'
updated_at: '2023-04-10T20:22:44.534394+00:00'
---

# Code Snippet c3e024b7

**Language**: SQL

```sql
SELECT name FROM syscolumns WHERE id = (SELECT id FROM sysobjects WHERE name = 'mytable'); -- for the current DB only
SELECT master..syscolumns.name, TYPE_NAME(master..syscolumns.xtype) FROM master..syscolumns, master..sysobjects WHERE master..syscolumns.id=master..sysobjects.id AND master..sysobjects.name='sometable'; -- list column names and types for master..sometable

SELECT table_catalog, column_name FROM information_schema.columns
```


