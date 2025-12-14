---
id: proc-uuid-5
tags:
  - xss-shell
  - interaction
type: procedure
tools:
  - '[[tools/netcat]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/javascript-alert-shell-test]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:43.727Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Establish and Interact with XSS Shell

## Summary

This procedure simulates victim interaction by having them visit the malicious link, connecting the XSS shell, and demonstrates sending JS commands via the netcat listener for control.

## Description

Once the victim loads the page, the payload connects to the listener. Attacker inputs JS like alerts or document.cookie theft, piped through nc to execute in victim browser. Enables cookie theft, redirects, etc. Outcome: Full JS REPL in browser context.

## Requirements

1. Active listener from previous step
2. Malicious URL shared via phishing
3. JS commands prepared

## Defense

Defensive measures and detection strategies:

- User training on suspicious links
- Endpoint detection for anomalous browser behavior
- Session token binding to prevent theft

## Objectives

1. Confirm shell connection
2. Execute test commands
3. Expand to data exfil

## Instructions

### Step 1: Trigger Victim Connection

**Context**: Victim visits crafted URL, payload loads external script connecting to nc.

**Command** (No direct; monitor listener):

Watch nc output for connection.

> Expected: Logs like 'connect to [IP] from [victim] 55730'.

### Step 2: Send Test Command

**Context**: Input JS at prompt to verify execution.

**Command** ([[commands/javascript-alert-shell-test]]):

At prompt: alert('Shell')

```bash
# Piped via nc loop
echo "alert('Shell')" | nc -vvlp 533
```

> Victim sees alert 'Shell'. Success: Command executes remotely.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/javascript-alert-shell-test]]

## Tools Used

- [[tools/netcat]]

## Tags

- [[shell]]
- [[Execution]]
