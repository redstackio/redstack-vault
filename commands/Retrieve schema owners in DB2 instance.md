---
id: a15f7b42-250a-469f-9985-7f66404c2cf7
name: Retrieve schema owners in DB2 instance
type: command
executor: bash
data: select distinct(definer) from syscat.schemata
output: null
created_at: '2023-04-06T03:56:32.616023+00:00'
updated_at: '2023-04-10T20:22:05.508378+00:00'
---

# Retrieve schema owners in DB2 instance

```bash
select distinct(definer) from syscat.schemata
```


