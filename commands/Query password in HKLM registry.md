---
id: 0bb64de1-00c0-4056-bf12-c71da73861e8
name: Query password in HKLM registry
type: command
executor: bash
data: reg query HKLM /f password /t REG_SZ /s
output: null
created_at: '2023-04-06T03:56:29.010782+00:00'
updated_at: '2023-04-10T20:37:47.338666+00:00'
---

# Query password in HKLM registry

```bash
reg query HKLM /f password /t REG_SZ /s
```


