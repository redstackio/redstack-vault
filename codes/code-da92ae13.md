---
id: da92ae13-d234-4ccb-a4f9-679adbc9fd6b
type: code
language: ps1
verified: false
created_at: '2023-04-06T03:56:25.113402+00:00'
updated_at: '2023-04-10T20:34:07.181527+00:00'
---

# Code Snippet da92ae13

**Language**: ps1

```ps1
SCMKit.exe -s gitlab -m createsshkey -c userName:password -u https://gitlab.something.local -o "ssh public key"
SCMKit.exe -s gitlab -m createsshkey -c apiToken -u https://gitlab.something.local -o "ssh public key"
SCMKit.exe -s gitlab -m listsshkey -c userName:password -u https://github.something.local
SCMKit.exe -s gitlab -m listsshkey -c apiToken -u https://github.something.local
SCMKit.exe -s gitlab -m removesshkey -c userName:password -u https://gitlab.something.local -o sshKeyID
SCMKit.exe -s gitlab -m removesshkey -c apiToken -u https://gitlab.something.local -o sshKeyID
```
