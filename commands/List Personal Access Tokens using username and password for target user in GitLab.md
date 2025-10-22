---
id: 4ccd87f6-3267-4acd-8c6f-e86f1931f6a0
name: List Personal Access Tokens using username and password for target user in GitLab
type: command
executor: bash
data: SCMKit.exe -s gitlab -m listpat -c userName:password -u https://gitlab.something.local
  -o targetUser
output: null
created_at: '2023-04-06T03:56:25.113299+00:00'
updated_at: '2023-04-10T20:34:07.180628+00:00'
---

# List Personal Access Tokens using username and password for target user in GitLab

```bash
SCMKit.exe -s gitlab -m listpat -c userName:password -u https://gitlab.something.local -o targetUser
```
