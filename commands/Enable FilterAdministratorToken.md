---
id: 359ae4a0-5f47-41a2-b084-ac3d8c50bd5a
name: Enable FilterAdministratorToken
type: command
executor: bash
data: reg add HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v FilterAdministratorToken
  /t REG_DWORD /f /d 1
output: null
created_at: '2023-04-06T03:56:30.837586+00:00'
updated_at: '2023-04-10T20:37:57.936960+00:00'
---

# Enable FilterAdministratorToken

```bash
reg add HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v FilterAdministratorToken /t REG_DWORD /f /d 1
```
