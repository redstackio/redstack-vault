---
id: 49198249-9d17-440a-a7ec-5232bdbffe2c
name: Grant Java Permissions
type: command
executor: bash
data: 'exec dbms_java.grant_permission(''SCOTT'', ''SYS:java.io.FilePermission'',''<<ALL
  FILES>>'',''execute'');

  exec dbms_java.grant_permission(''SCOTT'',''SYS:java.lang.RuntimePermission'', ''writeFileDescriptor'',
  '''');

  exec dbms_java.grant_permission(''SCOTT'',''SYS:java.lang.RuntimePermission'', ''readFileDescriptor'',
  '''');'
output: null
created_at: '2023-04-06T03:56:35.305146+00:00'
updated_at: '2023-04-10T20:23:12.135207+00:00'
---

# Grant Java Permissions

```bash
exec dbms_java.grant_permission('SCOTT', 'SYS:java.io.FilePermission','<<ALL FILES>>','execute');
exec dbms_java.grant_permission('SCOTT','SYS:java.lang.RuntimePermission', 'writeFileDescriptor', '');
exec dbms_java.grant_permission('SCOTT','SYS:java.lang.RuntimePermission', 'readFileDescriptor', '');
```
