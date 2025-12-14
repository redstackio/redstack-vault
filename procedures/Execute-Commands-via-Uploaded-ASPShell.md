---
tags:
  - rce
  - command-execution
  - asp-shell
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/windows-dir]]'
  - '[[commands/windows-cmd-c]]'
verified: false
platforms:
  - Web
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Windows Command Shell]]'
updated_at: '2025-12-14T05:32:13.316Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: cddaa7ac-a65e-47d9-a295-0e3ec542b263
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Windows Command Shell]]'
---
# Execute-Commands-via-Uploaded-ASPShell

## Summary

This procedure demonstrates remote code execution by accessing an uploaded ASP shell on the target server and passing commands via URL parameters to run arbitrary Windows commands.

## Description

After uploading the malicious ASP file via null byte bypass, the shell at https://target/savefiles/poc.asp processes the 'cmd' parameter using WScript.Shell to execute commands and return output, compromising the IIS-hosted Windows server.

## Requirements

1. Successful upload of the ASP shell to a web-accessible path
2. Direct HTTP access to the shell URL
3. Knowledge of Windows commands for testing

## Defense

Defensive measures and detection strategies:

- Disable or restrict Classic ASP execution on IIS
- Monitor for suspicious GET/POST requests to uploaded files with query parameters like ?cmd=
- Implement least privilege for IIS application pools to limit command impact

## Objectives

1. Verify RCE by executing a simple directory listing
2. Demonstrate full command control on the server
3. Potentially escalate to system compromise

## Instructions

### Step 1: Access the Shell and Run Test Command

**Context**: Visit the uploaded shell URL with a command parameter to execute [[commands/windows-dir]].

**Command** ([[commands/windows-dir]]):

Append ?cmd=dir to the URL: https://target/savefiles/poc.asp?cmd=dir

> The ASP script runs the command via [[commands/windows-cmd-c]] and displays the directory listing in the response body.

### Step 2: Execute Arbitrary Commands

**Context**: Use the shell for further commands to confirm control.

**Command** ([[commands/windows-cmd-c]]):

https://target/savefiles/poc.asp?cmd=whoami

> Expected output: Identity of the running process (e.g., IIS user), indicating server access level.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Windows Command Shell]]

### Sub-Techniques


## Commands Used

- [[commands/windows-dir]]
- [[commands/windows-cmd-c]]

## Tools Used


## Tags

- [[rce]]
- [[command-execution]]
- [[asp-shell]]
