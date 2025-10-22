---
id: f0efef77-e1c3-4ac8-9d99-05afa56d3d46
name: Create SSH Key with Username and Password
type: command
executor: bash
data: SCMKit.exe -s gitlab -m createsshkey -c userName:password -u https://gitlab.something.local
  -o "ssh public key"
output: null
created_at: '2023-04-06T03:56:25.113514+00:00'
updated_at: '2023-04-10T20:34:07.180628+00:00'
---

# Create SSH Key with Username and Password

```bash
SCMKit.exe -s gitlab -m createsshkey -c userName:password -u https://gitlab.something.local -o "ssh public key"
```
