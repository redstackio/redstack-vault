---
id: cd90d2a0-8b45-46ff-a75f-9d861768dc56
type: code
language: SQL
verified: false
created_at: '2023-04-06T03:56:33.116049+00:00'
updated_at: '2023-04-10T20:22:05.854264+00:00'
---

# Code Snippet cd90d2a0

**Language**: SQL

```sql
select xmlagg(xmlrow(table_schema)) from sysibm.tables -- returns all in one xml-formatted string
select xmlagg(xmlrow(table_schema)) from (select distinct(table_schema) from sysibm.tables) -- Same but without repeated elements
select xml2clob(xmelement(name t, table_schema)) from sysibm.tables -- returns all in one xml-formatted string (v8). May need CAST(xml2clob(… AS varchar(500)) to display the result.
```
