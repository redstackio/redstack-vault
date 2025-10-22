---
id: 9525b6c8-9c37-4d17-89b9-c49350c95a7c
name: Select all table schemas in one xml-formatted string without repeated elements
type: command
executor: bash
data: select xmlagg(xmlrow(table_schema)) from (select distinct(table_schema) from
  sysibm.tables) -- Same but without repeated elements
output: null
created_at: '2023-04-06T03:56:33.116167+00:00'
updated_at: '2023-04-10T20:22:05.851680+00:00'
---

# Select all table schemas in one xml-formatted string without repeated elements

```bash
select xmlagg(xmlrow(table_schema)) from (select distinct(table_schema) from sysibm.tables) -- Same but without repeated elements
```
