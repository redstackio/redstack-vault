---
id: ca61b053-3596-46f0-b8ed-f4ba39e71c00
type: code
language: SQL
verified: false
created_at: '2023-04-06T03:56:35.305118+00:00'
updated_at: '2023-04-10T20:23:12.139738+00:00'
---

# Code Snippet ca61b053

**Language**: SQL

```sql
exec dbms_java.grant_permission('SCOTT', 'SYS:java.io.FilePermission','<<ALL FILES>>','execute');
exec dbms_java.grant_permission('SCOTT','SYS:java.lang.RuntimePermission', 'writeFileDescriptor', '');
exec dbms_java.grant_permission('SCOTT','SYS:java.lang.RuntimePermission', 'readFileDescriptor', '');
```
