---
id: 92e5efb0-1b09-49c0-a688-5eca0ba1a572
name: Create Personal Access Token using API key for target user in GitLab
type: command
executor: bash
data: SCMKit.exe -s gitlab -m createpat -c apikey -u https://gitlab.something.local
  -o targetUserName
output: null
created_at: '2023-04-06T03:56:25.113145+00:00'
updated_at: '2023-04-10T20:34:07.180628+00:00'
---

# Create Personal Access Token using API key for target user in GitLab

```bash
SCMKit.exe -s gitlab -m createpat -c apikey -u https://gitlab.something.local -o targetUserName
```
