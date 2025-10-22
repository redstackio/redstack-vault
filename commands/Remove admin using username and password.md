---
id: f1f7a8af-fb85-4608-88ab-15954b4150f3
name: Remove admin using username and password
type: command
executor: bash
data: SCMKit.exe -s gitlab -m removeadmin -c userName:password -u https://gitlab.something.local
  -o targetUserName
output: null
created_at: '2023-04-06T03:56:25.112916+00:00'
updated_at: '2023-04-10T20:34:07.180628+00:00'
---

# Remove admin using username and password

```bash
SCMKit.exe -s gitlab -m removeadmin -c userName:password -u https://gitlab.something.local -o targetUserName
```
