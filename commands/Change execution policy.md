---
id: 42b3a626-15d2-4ce7-a5f7-063e054a851c
name: Change execution policy
type: command
executor: bash
data: 'Set-Executionpolicy -Scope CurrentUser -ExecutionPolicy UnRestricted

  Set-ExecutionPolicy Bypass -Scope Process'
output: null
created_at: '2023-04-06T03:56:23.962728+00:00'
updated_at: '2023-04-10T20:37:00.767168+00:00'
---

# Change execution policy

```bash
Set-Executionpolicy -Scope CurrentUser -ExecutionPolicy UnRestricted
Set-ExecutionPolicy Bypass -Scope Process
```
