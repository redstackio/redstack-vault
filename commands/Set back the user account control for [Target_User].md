---
id: 1f236e6f-3192-4ddd-8fe6-45ef260b3162
name: Set back the user account control for [Target_User]
type: command
executor: bash
data: $ bloodyAD.py --host [DC IP] -d [DOMAIN] -u [AttackerUser] -p [MyPassword] setUserAccountControl
  [Target_User] 0x400000 False
output: null
created_at: '2023-04-06T03:56:06.701492+00:00'
updated_at: '2023-04-10T20:26:07.517652+00:00'
---

# Set back the user account control for [Target_User]

```bash
$ bloodyAD.py --host [DC IP] -d [DOMAIN] -u [AttackerUser] -p [MyPassword] setUserAccountControl [Target_User] 0x400000 False
```
