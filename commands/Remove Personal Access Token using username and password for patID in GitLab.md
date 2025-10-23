---
id: c91f454d-7338-4f9d-b129-9f97efce00ac
name: Remove Personal Access Token using username and password for patID in GitLab
type: command
executor: bash
data: SCMKit.exe -s gitlab -m removepat -c userName:password -u https://gitlab.something.local
  -o patID
output: null
created_at: '2023-04-06T03:56:25.113189+00:00'
updated_at: '2023-04-10T20:34:07.180628+00:00'
---

# Remove Personal Access Token using username and password for patID in GitLab

```bash
SCMKit.exe -s gitlab -m removepat -c userName:password -u https://gitlab.something.local -o patID
```


