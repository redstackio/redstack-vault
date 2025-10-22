---
id: e115f5ec-c7a7-42cc-a5c6-26cc1aebc795
name: Select all table schemas in one xml-formatted string
type: command
executor: bash
data: select xmlagg(xmlrow(table_schema)) from sysibm.tables -- returns all in one
  xml-formatted string
output: null
created_at: '2023-04-06T03:56:33.116094+00:00'
updated_at: '2023-04-10T20:22:05.851680+00:00'
---

# Select all table schemas in one xml-formatted string

```bash
select xmlagg(xmlrow(table_schema)) from sysibm.tables -- returns all in one xml-formatted string
```
