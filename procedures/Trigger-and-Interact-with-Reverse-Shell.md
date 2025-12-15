---
tags:
  - rce
  - shell-interaction
  - php-execution
type: procedure
tools:
  - '[[tools/netcat]]'
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
  - Linux
techniques:
  - '[[Python]]'
  - '[[Exploitation of Remote Services]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 48755590-e839-4e5f-8353-f20dd2f8d45e
created_at: '2025-12-14T17:24:08.459Z'
updated_at: '2025-12-14T17:24:08.459Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Python]]'
  - '[[Exploitation of Remote Services]]'
---
# Trigger-and-Interact-with-Reverse-Shell

## Summary

This procedure accesses the uploaded PHP file's URL to execute the reverse shell and interacts with the resulting remote shell for system control.

## Description

Accessing the file via its web URL triggers PHP execution on the server, initiating the reverse connection to the netcat listener. Once connected, the attacker gains a command shell, allowing navigation, file access, and further exploitation on the underlying system.

## Requirements

1. Uploaded shell.php with known URL
2. Active netcat listener on attacker's machine
3. Web access to the target CMS

## Defense

Defensive measures and detection strategies:

- Disable direct execution of uploaded files; route through non-executable paths
- Log web requests to uploaded files and alert on access to .php in user directories
- Endpoint detection for shell processes spawned from web contexts (e.g., via EDR tools)

## Objectives

1. Execute payload via HTTP request
2. Receive and verify shell connection
3. Perform post-exploitation actions

## Instructions

### Step 1: Access Uploaded File

**Context**: Trigger execution by requesting the file URL.

In the File Manager, click the properties link for shell.php or directly visit http://target.com/files/shell.php in a browser.

> Page may load blank or error, but payload executes in background.

### Step 2: Confirm Connection in Listener

**Context**: Observe incoming shell in netcat.

Switch to the netcat terminal; connection should establish.

> Displays remote host connection; provides shell prompt (e.g., $ or #).

### Step 3: Interact with Shell

**Context**: Execute commands on the remote system.

Run commands like 'id', 'pwd', or 'whoami' in the netcat session.

> Outputs confirm user context (e.g., web server user like www-data) and directory.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Python]]
- [[Exploitation of Remote Services]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/netcat]]

## Tags

- [[rce]]
- [[shell-interaction]]
- [[php-execution]]
