---
id: 840894eb-5777-4380-8448-9db1588fdd3a
name: Check PowerShell version
type: command
executor: bash
data: REG QUERY "HKLM\SOFTWARE\Microsoft\PowerShell\1\PowerShellEngine" /v PowerShellVersion
output: null
created_at: '2023-04-06T03:56:29.377707+00:00'
updated_at: '2023-04-10T20:37:39.789164+00:00'
---

# Check PowerShell version

```bash
REG QUERY "HKLM\SOFTWARE\Microsoft\PowerShell\1\PowerShellEngine" /v PowerShellVersion
```


