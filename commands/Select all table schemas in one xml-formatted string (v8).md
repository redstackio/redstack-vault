---
id: 614c7c08-1f5d-43e1-aab9-068ab1ba1446
name: Select all table schemas in one xml-formatted string (v8)
type: command
executor: bash
data: select xml2clob(xmelement(name t, table_schema)) from sysibm.tables -- returns
  all in one xml-formatted string (v8). May need CAST(xml2clob(… AS varchar(500))
  to display the result.
output: null
created_at: '2023-04-06T03:56:33.116214+00:00'
updated_at: '2023-04-10T20:22:05.851680+00:00'
---

# Select all table schemas in one xml-formatted string (v8)

```bash
select xml2clob(xmelement(name t, table_schema)) from sysibm.tables -- returns all in one xml-formatted string (v8). May need CAST(xml2clob(… AS varchar(500)) to display the result.
```


