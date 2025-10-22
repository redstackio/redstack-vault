---
id: 2b61a395-7804-42fe-8f1b-07d07d61f108
name: Remove SSH Key with Username and Password
type: command
executor: bash
data: SCMKit.exe -s gitlab -m removesshkey -c userName:password -u https://gitlab.something.local
  -o sshKeyID
output: null
created_at: '2023-04-06T03:56:25.113704+00:00'
updated_at: '2023-04-10T20:34:07.180628+00:00'
---

# Remove SSH Key with Username and Password

```bash
SCMKit.exe -s gitlab -m removesshkey -c userName:password -u https://gitlab.something.local -o sshKeyID
```
