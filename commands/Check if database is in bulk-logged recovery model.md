---
id: 014fc421-7aa5-4cb8-87a1-48b537251f88
name: Check if database is in bulk-logged recovery model
type: command
executor: bash
data: 'USE master

  GO

  SELECT [name], [recovery_model_desc] FROM sys.databases WHERE [name] = ''database_name'''
output: null
created_at: '2023-04-06T03:56:33.914847+00:00'
updated_at: '2023-04-10T20:22:42.032361+00:00'
---

# Check if database is in bulk-logged recovery model

```bash
USE master
GO
SELECT [name], [recovery_model_desc] FROM sys.databases WHERE [name] = 'database_name'
```
