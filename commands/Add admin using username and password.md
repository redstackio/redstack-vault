---
id: e6766745-d912-4873-b915-27e3dfb3f9b0
name: Add admin using username and password
type: command
executor: bash
data: SCMKit.exe -s gitlab -m addadmin -c userName:password -u https://gitlab.something.local
  -o targetUserName
output: null
created_at: '2023-04-06T03:56:25.112804+00:00'
updated_at: '2023-04-10T20:34:07.180628+00:00'
---

# Add admin using username and password

```bash
SCMKit.exe -s gitlab -m addadmin -c userName:password -u https://gitlab.something.local -o targetUserName
```
