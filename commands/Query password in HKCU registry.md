---
id: fca843b3-7ae0-4a9e-b823-724eff3b8eda
name: Query password in HKCU registry
type: command
executor: bash
data: reg query HKCU /f password /t REG_SZ /s
output: null
created_at: '2023-04-06T03:56:29.010860+00:00'
updated_at: '2023-04-10T20:37:47.338666+00:00'
---

# Query password in HKCU registry

```bash
reg query HKCU /f password /t REG_SZ /s
```


