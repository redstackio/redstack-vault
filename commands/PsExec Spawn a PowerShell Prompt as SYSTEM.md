---
id: 1f9aa9d8-1075-468c-9a6c-7834e9529b39
name: PsExec Spawn a PowerShell Prompt as SYSTEM
type: command
executor: command_prompt
data: PsExec.exe -accepteula \\$_TARGET powershell.exe
output: 'C:\Tools\Sysinternals>PsExec.exe -accepteula \\WS01 powershell.exe


  PsExec v2.2 - Execute processes remotely

  Copyright (C) 2001-2016 Mark Russinovich

  Sysinternals - www.sysinternals.com'
created_at: '2020-07-06T23:55:46.925292+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[Powershell]]'
---

# PsExec Spawn a PowerShell Prompt as SYSTEM

```command_prompt
PsExec.exe -accepteula \\$_TARGET powershell.exe
```

## Expected Output

```
C:\Tools\Sysinternals>PsExec.exe -accepteula \\WS01 powershell.exe

PsExec v2.2 - Execute processes remotely
Copyright (C) 2001-2016 Mark Russinovich
Sysinternals - www.sysinternals.com
```


