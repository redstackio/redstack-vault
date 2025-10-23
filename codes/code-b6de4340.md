---
id: b6de4340-747f-454d-84f9-e9454333f1ac
type: code
language: ps1
verified: false
created_at: '2023-04-06T03:56:25.112963+00:00'
updated_at: '2023-04-10T20:34:07.181527+00:00'
---

# Code Snippet b6de4340

**Language**: ps1

```ps1
SCMKit.exe -s gitlab -m createpat -c userName:password -u https://gitlab.something.local -o targetUserName
SCMKit.exe -s gitlab -m createpat -c apikey -u https://gitlab.something.local -o targetUserName
SCMKit.exe -s gitlab -m removepat -c userName:password -u https://gitlab.something.local -o patID
SCMKit.exe -s gitlab -m listpat -c userName:password -u https://gitlab.something.local -o targetUser
SCMKit.exe -s gitlab -m listpat -c apikey -u https://gitlab.something.local -o targetUser
```


