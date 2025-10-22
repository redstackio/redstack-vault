---
id: ada87028-3471-4379-8793-a303a5fe63d2
name: List column names and types for 'sometable'
type: command
executor: bash
data: SELECT master..syscolumns.name, TYPE_NAME(master..syscolumns.xtype) FROM master..syscolumns,
  master..sysobjects WHERE master..syscolumns.id=master..sysobjects.id AND master..sysobjects.name='sometable';
  -- list column names and types for master..sometable
output: null
created_at: '2023-04-06T03:56:33.676028+00:00'
updated_at: '2023-04-10T20:22:44.531078+00:00'
---

# List column names and types for 'sometable'

```bash
SELECT master..syscolumns.name, TYPE_NAME(master..syscolumns.xtype) FROM master..syscolumns, master..sysobjects WHERE master..syscolumns.id=master..sysobjects.id AND master..sysobjects.name='sometable'; -- list column names and types for master..sometable
```
