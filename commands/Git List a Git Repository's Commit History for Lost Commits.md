---
id: 852c3413-e5fa-4358-b750-f9b4682838a5
name: Git List a Git Repository's Commit History for Lost Commits
type: command
executor: bash
data: git reflog -p
output: 'root@kali:~# git reflog -p | grep password

  -spring.datasource.password=secretpassword'
created_at: '2019-10-16T22:13:26.108552+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Git List a Git Repository's Commit History for Lost Commits

```bash
git reflog -p
```

## Expected Output

```
root@kali:~# git reflog -p | grep password
-spring.datasource.password=secretpassword
```
