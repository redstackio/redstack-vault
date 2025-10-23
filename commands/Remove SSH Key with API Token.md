---
id: d48c5d55-79d8-4db1-9905-da69ed818092
name: Remove SSH Key with API Token
type: command
executor: bash
data: SCMKit.exe -s gitlab -m removesshkey -c apiToken -u https://gitlab.something.local
  -o sshKeyID
output: null
created_at: '2023-04-06T03:56:25.113763+00:00'
updated_at: '2023-04-10T20:34:07.180628+00:00'
---

# Remove SSH Key with API Token

```bash
SCMKit.exe -s gitlab -m removesshkey -c apiToken -u https://gitlab.something.local -o sshKeyID
```


