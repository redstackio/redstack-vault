---
id: b656467b-e640-4edc-adbd-4485168f413b
name: Git List a Git Repository's Commit Messages
type: command
executor: bash
data: git log --all
output: "root@kali:~# git log --all\ncommit 766c5f1a2f95e117244d9128bff7a579ca1d4968\
  \ (HEAD -> master, origin/master)\nAuthor: bob <bob@corp.net>\nDate:   Sat Oct 29\
  \ 12:01:40 2018 +0530\n\n    changed auth\n\ncommit c130757dbbefdb3af3966fbd5ca273496180dc913\n\
  Author: bob <bob@corp.net>\nDate:   Sat Oct 29 11:56:32 2018 +0530\n\n    added\
  \ mysql"
created_at: '2019-10-16T22:13:26.097794+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[Git]]'
---

# Git List a Git Repository's Commit Messages

```bash
git log --all
```

## Expected Output

```
root@kali:~# git log --all
commit 766c5f1a2f95e117244d9128bff7a579ca1d4968 (HEAD -> master, origin/master)
Author: bob <bob@corp.net>
Date:   Sat Oct 29 12:01:40 2018 +0530

    changed auth

commit c130757dbbefdb3af3966fbd5ca273496180dc913
Author: bob <bob@corp.net>
Date:   Sat Oct 29 11:56:32 2018 +0530

    added mysql
```


