---
id: 2f9f9dff-df16-42da-9f0c-0962b4c89290
name: Find Administrative users logged in across the domain – default group = Domain
  Admins
type: command
executor: bash
data: 'Invoke-UserHunter -Threads 15 -NoPing [-GroupName “Enterprise Admins”]

  Invoke-UserHunter -Threads 20 -GroupName "Domain Admins" -SearchForest -CheckAccess

  '
output: null
created_at: '2020-07-14T18:21:07.164382+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Find Administrative users logged in across the domain – default group = Domain Admins

```bash
Invoke-UserHunter -Threads 15 -NoPing [-GroupName “Enterprise Admins”]
Invoke-UserHunter -Threads 20 -GroupName "Domain Admins" -SearchForest -CheckAccess

```


