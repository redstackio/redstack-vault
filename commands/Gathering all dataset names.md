---
id: cbd92e7c-d358-48f5-b781-16cd48f21011
name: Gathering all dataset names
type: command
executor: bash
data: select schema_name from INFORMATION_SCHEMA.SCHEMATA
output: null
created_at: '2023-04-06T03:56:32.296105+00:00'
updated_at: '2023-04-10T20:21:04.820574+00:00'
---

# Gathering all dataset names

```bash
select schema_name from INFORMATION_SCHEMA.SCHEMATA
```
