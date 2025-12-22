---
id: 1f9aa9d8-1075-468c-9a6c-7834e9529b39
name: psexec-spawn-powershell-as-system
type: command
executor: command_prompt
data: PsExec.exe -accepteula \\$_TARGET powershell.exe
output: |-
  C:\Tools\Sysinternals>PsExec.exe -accepteula \\$_TARGET powershell.exe

  PsExec v2.2 - Execute processes remotely
  Copyright (C) 2001-2016 Mark Russinovich
  Sysinternals - www.sysinternals.com
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Windows
tags:
  - privilege-escalation
  - execution
verified: true
validated: true
---

# psexec-spawn-powershell-as-system

## Command

```command_prompt
PsExec.exe -accepteula \$_TARGET powershell.exe
```

## Description

This command uses PsExec to execute PowerShell as the SYSTEM user on a target Windows machine, typically the local system for privilege escalation. It creates a temporary service to run the process with elevated privileges, opening a new console window.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET | Target hostname or '.' for local machine (e.g., 'WS01' or '.') | Yes |
| -accepteula | Automatically accepts the End User License Agreement on first run | Yes (first time) |
| powershell.exe | The executable to launch (can be replaced with cmd.exe for a command prompt) | Yes |

## Examples

### Basic Usage

For local escalation:

```command_prompt
PsExec.exe -accepteula \\. powershell.exe
```

### Advanced Usage

For remote execution (requires admin shares accessible):

```command_prompt
PsExec.exe -accepteula \\WS01 powershell.exe
```

## Expected Output

```
C:\Tools\Sysinternals>PsExec.exe -accepteula \\WS01 powershell.exe

PsExec v2.2 - Execute processes remotely
Copyright (C) 2001-2016 Mark Russinovich
Sysinternals - www.sysinternals.com

Starting PowerShell on WS01...
The command completed successfully.

[New PowerShell window opens as SYSTEM]
PS C:\Windows\system32> whoami
nt authority\system
```

A new PowerShell window will spawn, and running 'whoami' confirms SYSTEM privileges.

## Related

- [[procedures/Escalate-Administrator-to-SYSTEM-Windows]]
- [[tools/PsExec]]
