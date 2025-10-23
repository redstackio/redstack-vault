---
id: 484ddb2e-2549-4b48-9c4a-045002eaacad
name: Filter Users
type: command
executor: bash
data: (user.otherMails -any (_ -contains "vendor")) -and (user.userType -eq "guest")
output: null
created_at: '2023-04-06T03:56:15.788446+00:00'
updated_at: '2023-04-10T20:19:31.729228+00:00'
---

# Filter Users

```bash
(user.otherMails -any (_ -contains "vendor")) -and (user.userType -eq "guest")
```


