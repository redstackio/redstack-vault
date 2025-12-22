---
tags:
  - rce
  - command-injection
  - asp
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
updated_at: '2025-12-14T17:23:41.450Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 13a47983-cb10-434b-b039-51ee2e4d2f74
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Windows Command Shell]]'
---
# Execute-Commands-via-Uploaded-ASP-Shell

## Summary

This procedure triggers the uploaded ASP shell to execute arbitrary Windows commands passed via a URL parameter, achieving remote code execution (RCE) and allowing attackers to run system commands like directory listings or further exploitation.

## Description

Once the ASP shell is uploaded to '/savefiles/poc.asp', accessing it with '?cmd=<command>' invokes the WScript.Shell to run 'cmd /c <command>' without input sanitization, leading to command injection. The target is a Windows IIS server; expected outcomes include command output display in the browser, confirming RCE and potential for lateral movement or data exfiltration.

## Requirements

1. Successful upload from previous procedure
2. Direct access to '/savefiles/poc.asp' (readable/executable by IIS)
3. Knowledge of Windows commands for testing

## Defense

Defensive measures and detection strategies:

- Disable or restrict WScript.Shell usage in ASP scripts
- Implement parameter validation and output encoding to prevent injection
- Monitor IIS logs for suspicious requests to uploaded files (e.g., ?cmd= patterns) and anomalous ASP executions

## Objectives

1. Verify RCE by executing test commands
2. Gather server information via output
3. Escalate to full system compromise

## Instructions

### Step 1: Access Shell with Test Command

**Context**: Trigger the shell to run a directory listing.

Visit 'https://target.com/savefiles/poc.asp?cmd=dir' in a browser.

> The ASP executes [[commands/windows-cmd-c]] with [[commands/windows-dir]], displaying folder contents and server vars like server_name.

### Step 2: Execute Advanced Commands

**Context**: Run more commands to explore the system.

Append other commands, e.g., '?cmd=whoami' or '?cmd=systeminfo'.

> Expected output: Command results rendered as HTML, confirming unsanitized execution.

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
- [[command-injection]]
- [[asp]]
