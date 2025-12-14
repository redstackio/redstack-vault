---
tags:
  - verification
  - system
type: procedure
tools:
  - '[[tools/cmd-exe]]'
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/whoami-check-privileges]]'
platforms:
  - Windows
techniques:
  - '[[T1087.001]]'
skill_level: low
impact_level: high
detection_risk: low
sub_techniques: []
id: a315e3a9-80fa-444d-a352-faf7e31378e5
created_at: '2025-12-14T17:29:44.273Z'
updated_at: '2025-12-14T17:29:44.273Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[T1087.001]]'
---
# Verify SYSTEM Privilege Escalation

## Summary

This procedure confirms the success of the DLL hijacking by checking the current user context in the elevated shell, ensuring execution as NT AUTHORITY\SYSTEM.

## Description

After the malicious DLL loads, it typically spawns a new cmd.exe under SYSTEM. Running whoami validates the escalation, allowing further actions like rootkit installation.

## Requirements

1. Elevated cmd.exe spawned from payload
2. Access to run basic commands

## Defense

Defensive measures and detection strategies:

- Monitor for unexpected SYSTEM processes
- Use EDR to detect DLL load anomalies
- Audit privilege changes

## Objectives

1. Confirm SYSTEM privileges
2. Validate exploit success
3. Enable post-exploitation

## Instructions

### Step 1: Access Elevated Shell

**Context**: Use the popped-up cmd.exe from the DLL payload.

No command; the shell appears automatically.

> If no popup, check running processes for anomalies.

### Step 2: Check User Context

**Context**: Execute whoami to verify escalation.

**Command** ([[commands/whoami-check-privileges]]):

```cmd
whoami
```

> Expected output: 'nt authority\system' indicates success.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[T1087.001]] Account Discovery: Local Account

### Sub-Techniques


## Commands Used

- [[commands/whoami-check-privileges]]

## Tools Used

- [[tools/cmd-exe]]

## Tags

- [[verification]]
- [[system]]
