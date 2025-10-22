---
id: 2aca5e72-9d06-4fbb-9689-e9ef6f54399d
name: Query Windows Autologin settings
type: command
executor: bash
data: reg query \"HKLM\SOFTWARE\Microsoft\Windows NT\Currentversion\Winlogon\"
output: null
created_at: '2023-04-06T03:56:29.010423+00:00'
updated_at: '2023-04-10T20:37:47.338666+00:00'
---

# Query Windows Autologin settings

```bash
reg query \"HKLM\SOFTWARE\Microsoft\Windows NT\Currentversion\Winlogon\"
```
