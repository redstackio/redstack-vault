---
id: 70eaa688-2ed2-497c-9d3a-5192453e5f35
name: Linux with username:password and ADCS module
type: command
executor: bash
data: rusthound -d domain.local -u 'user@domain.local' -p 'Password123' -o /tmp/adcs
  --adcs -z
output: null
created_at: '2023-04-06T03:56:02.119539+00:00'
updated_at: '2023-04-10T20:26:14.196507+00:00'
---

# Linux with username:password and ADCS module

```bash
rusthound -d domain.local -u 'user@domain.local' -p 'Password123' -o /tmp/adcs --adcs -z
```


