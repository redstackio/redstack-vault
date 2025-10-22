---
id: 50b0b2d4-f5ba-47b2-ab15-698be26b828c
type: code
language: ps1
verified: false
created_at: '2023-04-06T03:56:32.295911+00:00'
updated_at: '2023-04-10T20:21:04.818355+00:00'
---

# Code Snippet 50b0b2d4

**Language**: ps1

```ps1
# Gathering project id
select @@project_id

# Gathering all dataset names
select schema_name from INFORMATION_SCHEMA.SCHEMATA

# Gathering data from specific project id & dataset
select * from `project_id.dataset_name.table_name`
```
