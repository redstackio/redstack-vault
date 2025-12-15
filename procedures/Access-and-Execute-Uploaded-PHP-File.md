---
tags:
  - rce
  - php-execution
  - webshell
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Command-Line Interface]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:23:27.902Z'
sub_techniques:
  - '[[Python]]'
id: 939df041-a505-45f4-a7b8-bba4b9c3cce7
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Command-Line Interface]]'
  - '[[Exploit Public-Facing Application]]'
---
# Access-and-Execute-Uploaded-PHP-File

## Summary

This procedure triggers remote code execution by directly accessing the uploaded PHP file in the browser, exploiting its server-side interpretation.

## Description

Since the file is stored in a web-accessible directory and the server processes .php extensions, navigating to the URL causes the PHP code to run. This can execute system commands, leading to server compromise, data exfiltration, or defacement.

## Requirements

1. Copied full URL to uploaded file
2. Web browser
3. Payload designed for GET parameters if needed

## Defense

Defensive measures and detection strategies:

- Block execution of uploaded files via .htaccess or server config
- Validate and quarantine uploads
- WAF rules to detect direct access to upload paths

## Objectives

1. Invoke PHP interpreter on malicious script
2. Achieve code execution on server
3. Observe RCE output for confirmation

## Instructions

### Step 1: Paste URL in Browser

**Context**: Direct navigation to trigger execution.

Enter the copied URL into the address bar.

### Step 2: Append Parameters if Required

**Context**: Pass arguments to the payload.

For a system command shell, add ?cmd=ls or similar to the URL.

### Step 3: Observe Execution

**Context**: Verify RCE by checking response.

Press enter; look for output like directory listing or error if payload fails.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Command-Line Interface]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques

- [[Python]]

## Commands Used


## Tools Used


## Tags

- rce
- php-execution
