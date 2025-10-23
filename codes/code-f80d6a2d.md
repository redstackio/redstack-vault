---
id: f80d6a2d-fd73-457c-91cb-96b52f4177ca
type: code
language: SQL
verified: false
created_at: '2023-04-06T03:56:33.714212+00:00'
updated_at: '2023-04-10T20:22:43.828947+00:00'
---

# Code Snippet f80d6a2d

**Language**: SQL

```sql
SELECT name FROM master..sysobjects WHERE xtype = 'U'; -- use xtype = 'V' for views
SELECT name FROM someotherdb..sysobjects WHERE xtype = 'U';
SELECT master..syscolumns.name, TYPE_NAME(master..syscolumns.xtype) FROM master..syscolumns, master..sysobjects WHERE master..syscolumns.id=master..sysobjects.id AND master..sysobjects.name='sometable'; -- list column names and types for master..sometable

SELECT table_catalog, table_name FROM information_schema.columns
SELECT STRING_AGG(name, ', ') FROM master..sysobjects WHERE xtype = 'U'; -- Change delimiter value such as ', ' to anything else you want => trace_xe_action_map, trace_xe_event_map, spt_fallback_db, spt_fallback_dev, spt_fallback_usg, spt_monitor, MSreplication_options  (Only works in MSSQL 2017+)
```


