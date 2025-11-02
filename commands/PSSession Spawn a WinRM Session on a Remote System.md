---
id: 38405062-48cc-41f4-a7be-44f830a58308
name: PSSession Spawn a WinRM Session on a Remote System
type: command
executor: powershell
data: Enter-PSSession -$_TARGET
output: 'PS C:\Windows\system32\spool\drivers\color> Enter-PSSession dc-dev.dev.tesla.local

  [dc-dev.dev.tsla.local]: PS C:\Users\Administrator\Documents>'
created_at: '2020-07-07T04:30:50.322541+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[ps]]'
---

# PSSession Spawn a WinRM Session on a Remote System

```powershell
Enter-PSSession -$_TARGET
```

## Expected Output

```
PS C:\Windows\system32\spool\drivers\color> Enter-PSSession dc-dev.dev.tesla.local
[dc-dev.dev.tsla.local]: PS C:\Users\Administrator\Documents>
```


