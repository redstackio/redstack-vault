---
id: abd68152-93d3-40f4-abb0-488cc92ca3ec
type: code
language: SQL
verified: false
created_at: '2023-04-06T03:56:37.018232+00:00'
updated_at: '2023-04-10T20:24:31.294791+00:00'
---

# Code Snippet abd68152

**Language**: SQL

```sql
SELECT replace(replace(replace(replace(replace(replace(replace(replace(replace(replace(substr((substr(sql,instr(sql,'(')%2b1)),instr((substr(sql,instr(sql,'(')%2b1)),'')),"TEXT",''),"INTEGER",''),"AUTOINCREMENT",''),"PRIMARY KEY",''),"UNIQUE",''),"NUMERIC",''),"REAL",''),"BLOB",''),"NOT NULL",''),",",'~~') FROM sqlite_master WHERE type!='meta' AND sql NOT NULL AND name NOT LIKE 'sqlite_%' AND name ='table_name'
```
