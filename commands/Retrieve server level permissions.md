---
id: 96955d9f-23f7-4e26-8511-a3071f8a7e7b
name: Retrieve server level permissions
type: command
executor: bash
data: select * from fn_my_permissions(null, 'server');
output: null
created_at: '2023-04-06T03:56:20.954736+00:00'
updated_at: '2023-04-10T20:36:33.554323+00:00'
---

# Retrieve server level permissions

```bash
select * from fn_my_permissions(null, 'server');
```
