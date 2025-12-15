---
id: proc-trigger-shell-rce
tags:
  - rce
  - electron
  - shell-execution
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Desktop
  - Electron
  - Windows
  - macOS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Client Execution]]'
  - '[[Windows Command Shell]]'
updated_at: '2025-12-14T17:23:20.313Z'
skill_level: intermediate
impact_level: critical
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
  - '[[Windows Command Shell]]'
---
# Trigger-shell-openExternal-for-Arbitrary-Code-Execution

## Summary

This procedure finalizes the attack by triggering Electron's shell.openExternal with the malicious URL, resulting in arbitrary OS command execution on the victim's desktop machine.

## Description

Once the malicious URL is passed to openInternalVideoChatWindow, it flows directly to shell.openExternal at line 17 of internalVideoChatWindow.ts. This Electron API opens external resources but insecurely interprets certain schemes as OS commands, enabling RCE. The vulnerability is exploitable via the chain from XSS, affecting users with the desktop app running.

## Requirements

1. Malicious URL injected from prior procedure
2. Victim's Rocket.Chat-Desktop actively running
3. Target OS paths known for payload execution
4. No additional network access needed post-injection

## Defense

Defensive measures and detection strategies:

- Patch Electron apps to validate shell.openExternal inputs strictly
- Disable external URL handling in desktop configs
- Implement runtime monitoring for unexpected process spawns
- Use endpoint detection tools to alert on calc.exe or similar launches

## Objectives

1. Execute the injected URL via shell.openExternal
2. Achieve full RCE on the desktop OS
3. Demonstrate impact through observable command effects

## Instructions

### Step 1: Ensure API Invocation Triggers Shell Call

**Context**: The function call automatically passes the URL; no manual trigger needed beyond injection.

Verify in app source or debugging that line 17 executes:

```javascript
// Equivalent to: shell.openExternal(url);
```

> This happens synchronously upon API call if checks are bypassed.

### Step 2: Observe and Validate Execution

**Context**: Monitor the victim's machine for command effects.

On success, expect OS-level execution, e.g., application launch.

> Expected output: Target executable runs (e.g., calculator opens); check task manager or Activity Monitor for new processes.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploitation for Client Execution]]
- [[Windows Command Shell]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[rce]]
- [[electron]]
- [[shell-execution]]
