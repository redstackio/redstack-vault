---
id: ca768299-4b1e-48f8-b5a9-0f68456191d0
name: Update registry value
type: command
executor: bash
data: REG ADD HKLM\SOFTWARE\Policies\Microsoft\Windows\LocationAndSensors /v DisableLocation
  /t REG_DWORD /d 1 /f
output: null
created_at: '2023-04-06T03:56:15.139951+00:00'
updated_at: '2023-04-10T20:19:38.041975+00:00'
---

# Update registry value

```bash
REG ADD HKLM\SOFTWARE\Policies\Microsoft\Windows\LocationAndSensors /v DisableLocation /t REG_DWORD /d 1 /f
```
