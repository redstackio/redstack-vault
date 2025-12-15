---
id: uuid-verify-admin
tags:
  - discovery
  - privilege-check
  - windows
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/net-session-verify-admin]]'
verified: false
platforms:
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[T1087.001]]'
updated_at: '2025-12-14T17:29:09.426Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[T1087.001]]'
---
# Verify Administrative Privileges

## Summary

This procedure confirms administrative privileges in the spawned command shell from the DLL payload using a simple network session check.

## Description

After DLL execution spawns cmd.exe, run 'net session' to test for admin rights: success shows no entries, failure shows access denied. This validates the hijacking led to elevation. Requires the elevated shell from prior steps. Outcome: Confirmation of admin access for further escalation.

## Requirements

1. Elevated cmd.exe from DLL payload
2. Windows environment

## Defense

Defensive measures and detection strategies:

- Log privilege checks in Event Viewer (Security log, Event ID 4672/4673)
- Use EDR to alert on net.exe usage in unexpected contexts
- Enforce least privilege to limit escalation impact

## Objectives

1. Validate elevation success
2. Prepare for next escalation steps
3. Detect potential failures early

## Instructions

### Step 1: Execute Privilege Check

**Context**: Run the command in the spawned elevated cmd.exe to verify admin rights.

**Command** ([[commands/net-session-verify-admin]]):

```cmd
net session
```

> If admin: "There are no entries in this list." If not: "Access denied."

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[T1087.001]]

### Sub-Techniques


## Commands Used

- [[commands/net-session-verify-admin]]

## Tools Used


## Tags

- [[Discovery]]
- [[privilege-check]]
- [[windows]]
