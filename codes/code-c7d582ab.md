---
id: c7d582ab-8e22-4dd9-9220-2c0d31e3af99
type: code
language: SQL
verified: false
created_at: '2023-04-06T03:56:20.332875+00:00'
updated_at: '2023-04-10T20:36:36.103615+00:00'
---

# Code Snippet c7d582ab

**Language**: SQL

```sql
-- can also be loaded from UNC path or Webdav
sp_addextendedproc 'xp_calc', 'C:\mydll\xp_calc.dll'
EXEC xp_calc
sp_dropextendedproc 'xp_calc'
```


