---
id: afdc525a-2245-4abc-be9e-c943f9f625f9
type: code
language: SQL
verified: false
created_at: '2023-04-06T03:56:20.431490+00:00'
updated_at: '2023-04-10T20:36:42.147021+00:00'
---

# Code Snippet afdc525a

**Language**: SQL

```sql
CREATE PROCEDURE [dbo].[cmd_exec] @execCommand NVARCHAR (4000) AS EXTERNAL NAME [my_assembly].[StoredProcedures].[cmd_exec];
GO
```
