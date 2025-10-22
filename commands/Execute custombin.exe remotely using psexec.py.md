---
id: 3393b395-7ae2-4396-9caf-466edb15bc03
name: Execute custombin.exe remotely using psexec.py
type: command
executor: bash
data: psexec.py Administrator:Password123@IP -service-name customservicename -remote-binary-name
  custombin.exe
output: null
created_at: '2023-04-06T03:56:30.905314+00:00'
updated_at: '2023-04-10T20:37:58.731576+00:00'
---

# Execute custombin.exe remotely using psexec.py

```bash
psexec.py Administrator:Password123@IP -service-name customservicename -remote-binary-name custombin.exe
```
