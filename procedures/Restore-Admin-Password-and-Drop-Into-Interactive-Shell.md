---
tags:
  - persistence
  - interactive-shell
type: procedure
tools:
  - '[[tools/Python3]]'
  - '[[tools/post_auth_nosqli.py]]'
tactics:
  - '[[Persistence]]'
commands:
  - '[[commands/python3-post-auth-nosqli]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:46:14.803Z'
skill_level: intermediate
impact_level: critical
detection_risk: high
sub_techniques: []
id: b0e7b782-a33b-4c12-ae28-a5aeab383bdc
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Restore-Admin-Password-and-Drop-Into-Interactive-Shell

## Summary

This procedure uses the RCE webhook to restore the original admin password and establish an interactive shell for persistent access.

## Description

Via webhook JS, execute commands to reset the password back using the API, then spawn a reverse shell or interactive prompt. Ensures stealth by cleaning up changes. Requires RCE access. Outcome: Persistent server control without traces.

## Requirements

1. Active RCE via webhook
2. Original password known or recoverable
3. Shell payload ready

## Defense

Defensive measures and detection strategies:

- Monitor for password changes via RCE
- Detect reverse shells or anomalous processes
- Implement process monitoring tools like Falco
- Regularly audit admin accounts

## Objectives

1. Clean up takeover traces
2. Maintain interactive access
3. Verify full compromise

## Instructions

### Step 1: Restore Password and Spawn Shell

**Context**: Use webhook to reset password and drop shell.

**Command** ([[commands/python3-post-auth-nosqli]]):
```bash
python3 post_auth_nosqli.py -u attacker -p attacker 'http://localhost:3000'
```

> Script executes cleanup and shell via webhook. Expected output: Interactive shell prompt, e.g., allowing further commands.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/python3-post-auth-nosqli]]

## Tools Used

- [[tools/Python3]]
- [[tools/post_auth_nosqli.py]]

## Tags

- persistence
- interactive-shell
