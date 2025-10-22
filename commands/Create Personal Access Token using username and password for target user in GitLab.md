---
id: ed957dcd-8d54-4cca-b2a6-edded50ede1e
name: Create Personal Access Token using username and password for target user in
  GitLab
type: command
executor: bash
data: SCMKit.exe -s gitlab -m createpat -c userName:password -u https://gitlab.something.local
  -o targetUserName
output: null
created_at: '2023-04-06T03:56:25.113036+00:00'
updated_at: '2023-04-10T20:34:07.180628+00:00'
---

# Create Personal Access Token using username and password for target user in GitLab

```bash
SCMKit.exe -s gitlab -m createpat -c userName:password -u https://gitlab.something.local -o targetUserName
```
