---
id: 6ce6afe9-980e-4a6f-b2f5-ec0eb57f3bae
name: Create SSH Key with API Token
type: command
executor: bash
data: SCMKit.exe -s gitlab -m createsshkey -c apiToken -u https://gitlab.something.local
  -o "ssh public key"
output: null
created_at: '2023-04-06T03:56:25.113542+00:00'
updated_at: '2023-04-10T20:34:07.180628+00:00'
---

# Create SSH Key with API Token

```bash
SCMKit.exe -s gitlab -m createsshkey -c apiToken -u https://gitlab.something.local -o "ssh public key"
```
