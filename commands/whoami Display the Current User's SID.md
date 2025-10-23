---
id: 2f71f98f-c4e8-41a8-8152-8aa6aea41664
name: whoami Display the Current User's SID
type: command
executor: command_prompt
data: whoami.exe /name
output: 'C:\>whoami.exe /user


  USER INFORMATION

  ----------------


  User Name SID

  ========= =============================================

  dev\bob   S-1-5-21-1576920733-1301476157-954876328-1108'
created_at: '2020-07-20T22:27:56.254490+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# whoami Display the Current User's SID

```command_prompt
whoami.exe /name
```

## Expected Output

```
C:\>whoami.exe /user

USER INFORMATION
----------------

User Name SID
========= =============================================
dev\bob   S-1-5-21-1576920733-1301476157-954876328-1108
```


