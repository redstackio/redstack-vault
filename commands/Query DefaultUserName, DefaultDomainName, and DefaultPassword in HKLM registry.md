---
id: eb6f41f7-6abc-4e74-a44e-9ef62c7e3f19
name: Query DefaultUserName, DefaultDomainName, and DefaultPassword in HKLM registry
type: command
executor: bash
data: reg query \"HKLM\SOFTWARE\Microsoft\Windows NT\Currentversion\Winlogon\" 2>nul
  | findstr \"DefaultUserName DefaultDomainName DefaultPassword\"
output: null
created_at: '2023-04-06T03:56:29.010525+00:00'
updated_at: '2023-04-10T20:37:47.338666+00:00'
---

# Query DefaultUserName, DefaultDomainName, and DefaultPassword in HKLM registry

```bash
reg query \"HKLM\SOFTWARE\Microsoft\Windows NT\Currentversion\Winlogon\" 2>nul | findstr \"DefaultUserName DefaultDomainName DefaultPassword\"
```


