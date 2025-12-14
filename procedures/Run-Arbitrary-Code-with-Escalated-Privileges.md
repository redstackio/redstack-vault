---
tags:
  - privilege-escalation
  - arbitrary-execution
  - root-access
type: procedure
tools:
  - '[[tools/npm]]'
tactics:
  - '[[Privilege Escalation]]'
commands: []
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:28:44.398Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 8cc24ab4-5e7e-4642-8987-2487c8debbb0
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---
# Run-Arbitrary-Code-with-Escalated-Privileges

## Summary

This procedure executes attacker-controlled Node.js code via the onload-script, achieving RCE with user or root privileges based on the npm invocation.

## Description

The onload-script runs in the npm process, allowing arbitrary Node.js operations like file I/O, network calls, or shell spawns. If sudo npm is used, this escalates to root, enabling persistence or data exfiltration. Discovered via source analysis, it's exploitable in tutorials or infected repos.

## Requirements

1. onload-script executed
2. Node.js modules available
3. Target privileges (user/root)

## Defense

Defensive measures and detection strategies:

- Principle of least privilege for npm/sudo
- Monitor for anomalous file/network activity from npm processes
- Patch to newer npm versions without this feature

## Objectives

1. Perform arbitrary actions as the npm user
2. Escalate to root if sudo triggered
3. Achieve persistent access or data theft

## Instructions

### Step 1: Define Payload in Script

**Context**: Embed desired code in the Node.js script referenced by onload-script.

No command; example script content: `require('child_process').exec('whoami > /tmp/escalated.txt');`

> Expected: File written with user/root identity.

### Step 2: Verify Execution

**Context**: After npm run, check payload effects.

**Command** (Check output):
```bash
cat /tmp/pwned.txt
```

> Confirms execution. Expected output: User or root ID.

### Step 3: Escalate Impact

**Context**: Use root for high-impact actions like installing backdoors.

No command; script can run `exec('apt install -y malicious-pkg');` if root.

> Expected: System changes as root.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[Exploitation for Privilege Escalation]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/npm]]

## Tags

- [[privilege-escalation]]
- [[rce]]
