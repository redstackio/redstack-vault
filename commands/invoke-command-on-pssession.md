---
id: 9930fb81-7ed4-4858-acb2-391f051c3b46
name: invoke-command-on-pssession
type: command
executor: powershell
data: 'Invoke-Command -Session $session -ScriptBlock { $_SCRIPT_BLOCK }'
output: null
created_at: '2023-04-06T03:56:31.141374+00:00'
updated_at: '2023-04-10T20:37:59.190248+00:00'
platforms:
  - Windows
tags:
  - pssession
  - execution
verified: true
validated: true
---

# invoke-command-on-pssession

## Command

```powershell
Invoke-Command -Session $session -ScriptBlock { $_SCRIPT_BLOCK }
```

## Description

Executes a script block on an existing PSSession for remote command execution without entering interactive mode. Ideal for scripted or automated tasks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $session | PSSession object from New-PSSession | Yes |
| $_SCRIPT_BLOCK | PowerShell code to execute remotely (e.g., { whoami }) | Yes |

## Examples

### Basic Usage

```powershell
Invoke-Command -Session $session -ScriptBlock { whoami }
```

### With Variable Set

```powershell
Invoke-Command -Session $session -ScriptBlock { $test = 1 }
Invoke-Command -Session $session -ScriptBlock { $test }
```

### From File

```powershell
Invoke-Command -Session $session -FilePath C:\Scripts\Task.ps1
```

## Expected Output

DOMAIN\username

(or value from script, e.g., 1)

## Related

- [[procedures/windows-powershell-remoting-with-pssession]]
- [[commands/new-pssession]]
