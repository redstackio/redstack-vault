---
id: 2c4bfc2e-6668-41ce-ab11-9bb3dae30a8c
name: Add Local Account Token Filter Policy
type: command
executor: bash
data: reg add HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v LocalAccountTokenFilterPolicy
  /t REG_DWORD /f /d 1
output: null
created_at: '2023-04-06T03:56:30.837490+00:00'
updated_at: '2023-04-10T20:37:57.936960+00:00'
---

# Add Local Account Token Filter Policy

```bash
reg add HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v LocalAccountTokenFilterPolicy /t REG_DWORD /f /d 1
```
