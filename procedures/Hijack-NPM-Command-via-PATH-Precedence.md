---
id: proc-npm-path-hijack
tags:
  - path-hijacking
  - privilege-escalation
  - npm
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/copy-node-to-npm]]'
  - '[[commands/run-npm-command]]'
verified: false
platforms:
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Registry Run Keys - Startup Folder]]'
updated_at: '2025-12-14T17:29:09.964Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Registry Run Keys - Startup Folder]]'
---
# Hijack-NPM-Command-via-PATH-Precedence

## Summary

This procedure demonstrates local privilege escalation by having an unprivileged user drop a malicious executable (e.g., renamed node.exe as npm.exe) into the writable Node.js directory, hijacking the 'npm' command due to Windows PATH and file extension precedence (.exe over .cmd).

## Description

After Node.js installation to a writable PATH directory, unprivileged users can place files there. The legitimate npm is a .cmd script, but a .exe with the same name takes precedence. When a privileged user runs 'npm', the malicious exe executes with their privileges, potentially escalating from standard to admin. This targets any PATH-dependent Node tools.

## Requirements

1. Node.js installed to writable C:\tools (from prior procedure)
2. Unprivileged local user account
3. Privileged user account for execution
4. Access to node.exe for demo (or custom malicious payload)

## Defense

Defensive measures and detection strategies:

- Remove write access to installation directories post-install
- Monitor file creations in PATH directories via Sysmon (Event ID 11 with Image as PATH dir)
- Enforce execution policies restricting unsigned exes in system paths
- Use integrity checks on Node binaries and audit PATH runs

## Objectives

1. Place malicious file in writable PATH as low-priv user
2. Trigger execution with high-priv user via command invocation
3. Achieve code execution/escalation

## Instructions

### Step 1: Create Unprivileged User

**Context**: Set up a standard user without admin rights for exploitation.

**Instructions**: Use Computer Management or `net user lowpriv Password123 /add` and `net localgroup Users lowpriv /add` as admin.

> Expected output: User created; log in as lowpriv to verify no admin.

### Step 2: Drop Malicious Executable

**Context**: As unprivileged user, copy or create npm.exe in C:\tools to hijack.

**Command** ([[commands/copy-node-to-npm]]):
```cmd
copy C:\tools\node.exe C:\tools\npm.exe
```

> Copies node.exe to npm.exe. Expected output: 1 file(s) copied; npm.exe now in path.

### Step 3: Execute Hijacked Command

**Context**: Switch to privileged user and run 'npm' to trigger hijack.

**Command** ([[commands/run-npm-command]]):
```cmd
npm
```

> Runs npm, prioritizing malicious exe. Expected output: Node REPL shell (demo) or payload execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[Registry Run Keys - Startup Folder]]

### Sub-Techniques


## Commands Used

- [[commands/copy-node-to-npm]]
- [[commands/run-npm-command]]

## Tools Used


## Tags

- path-hijacking
- windows
- escalation
