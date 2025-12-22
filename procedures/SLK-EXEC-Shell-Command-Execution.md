---
id: 7a9bce08-c2a1-4972-86e4-f40f8157cacc
name: SLK-EXEC-Shell-Command-Execution
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:23.348526+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[Execution]]'
techniques:
  - '[[Command-Line Interface]]'
sub_techniques: []
tags:
  - office-attacks
  - slk-exec
commands: []
platforms:
  - Windows
tools: []
validated: true
---

# SLK-EXEC-Shell-Command-Execution

## Summary

SLK-EXEC Shell Command Execution leverages the SLK-EXEC Microsoft Office add-in to run arbitrary shell commands on a Windows target system. This technique enables attackers to execute system-level commands through Office documents, facilitating objectives like information gathering, persistence, or further exploitation in environments where Office applications are in use.

## Description

SLK-EXEC is a third-party add-in for Microsoft Office that extends functionality by allowing custom script execution, including shell commands via the 'Execute Shell Command' feature. Attackers can embed a specialized macro script in an Office document (e.g., Excel or Word) that triggers upon opening, invoking the add-in to run a prepared batch file or command. This bypasses some execution policies since it originates from a trusted Office context. The technique is effective against users with local system access but limited direct command-line privileges. It maps to MITRE ATT&CK Execution tactic via Command and Scripting Interpreter, as it indirectly uses the system's command shell.

Target environment: Windows systems (7+) with Microsoft Office 2010+ and SLK-EXEC add-in installed and enabled. Delivery typically occurs via phishing emails with malicious Office attachments. Success depends on the add-in being permitted and the user opening the document without suspicion.

Expected outcomes: The specified shell command runs, with output directed to the console, a file, or further chained actions, providing the attacker with command execution capabilities.

## Requirements

1. Target Windows system with Microsoft Office installed and SLK-EXEC add-in enabled (requires administrative configuration to allow add-ins).
2. Local user access or social engineering to open the malicious Office document on the target.
3. A writable path on the target for the shell command file (e.g., c:\shell.cmd), accessible by the user context.

## Defense

Defensive measures and detection strategies:

- Disable SLK-EXEC and restrict all third-party Office add-ins via Group Policy (User Configuration > Administrative Templates > Microsoft Office > Security Settings).
- Monitor endpoint logs for Office processes (e.g., EXCEL.EXE, WINWORD.EXE) spawning child processes like CMD.EXE or POWERSHELL.EXE using tools like Sysmon or EDR solutions.
- Enforce high macro security levels in Office (File > Options > Trust Center > Macro Settings > Disable all macros with notification).
- Implement application control (e.g., AppLocker) to block unauthorized add-ins and script execution from Office contexts.
- Scan attachments for embedded macros and add-ins using antivirus/EDR with behavioral analysis.

## Objectives

1. Execute arbitrary shell commands on the target Windows system to run reconnaissance or payload delivery.
2. Access sensitive information, such as file listings or credential dumps, via command output.
3. Establish persistence by executing commands that create backdoors or scheduled tasks.
4. Chain to further attacks, like lateral movement or data exfiltration, through executed commands.

## Instructions

### Step 1: Prepare the Shell Command File

**Context**: On the target system or via prior access, create a simple batch file containing the desired shell command. This file serves as the payload executed by SLK-EXEC. For example, to perform directory enumeration, the file could contain 'dir > c:\output.txt' to log results for later retrieval. Why: This isolates the command logic, making it easier to customize without altering the macro.

Create the file at a known path, such as c:\shell.cmd, ensuring it matches the path specified in the macro.

### Step 2: Embed the SLK-EXEC Macro Script

**Context**: Craft and insert the SLK-EXEC macro into an Office document to automate command execution on open. The script sets up an auto-open event, executes the shell command via EEXEC, and halts to avoid further actions. Why: Auto-execution minimizes user interaction and detection risk.

**Code** ([[codes/SLK-EXEC-Execute-Shell-Command-Macro]]):

```
ID;P
O;E
NN;NAuto_open;ER101C1;KOut Flank;F
C;X1;Y101;K0;EEXEC("c:\shell.cmd")
C;X1;Y102;K0;EHALT()
E
```

Open Microsoft Office (e.g., Excel), insert the macro via the SLK-EXEC interface or VBA editor if compatible, and save the document as .xlsm or .docm. Test in a lab environment to verify the path resolution.

**Expected Output**: No visible output in Office; the shell command runs in the background. Check the shell file's output (e.g., c:\output.txt) for results.

### Step 3: Deliver and Trigger Execution

**Context**: Distribute the document to the target and ensure it opens, triggering the macro. Why: This completes the execution chain, achieving the objective with minimal footprint.

Deliver via email attachment or shared drive. Upon opening, the auto-open event fires, executing the shell command. If prompted, the user must enable content/add-ins.

**Expected Output**: Successful command execution, verifiable by the presence of command artifacts (e.g., created files, process logs). Failure indicators include macro disabled warnings or add-in errors.
