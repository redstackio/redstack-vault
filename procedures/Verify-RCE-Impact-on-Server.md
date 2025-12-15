---
id: proc-verify-impact
tags:
  - verify
  - impact
  - file-write
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/execute-echo-file]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:23:50.163Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Verify-RCE-Impact-on-Server

## Summary

This procedure checks the GitLab server for artifacts created by the RCE payload, confirming arbitrary command execution and file write capabilities.

## Description

After triggering, the payload writes /tmp/ggg via echo command. Server access verifies persistence. This demonstrates full compromise potential, including escalation if gitlab-www has privileges. Prerequisites: RCE triggered; outcomes: Proof of server modification.

## Requirements

1. SSH or console access to GitLab server
2. Knowledge of payload commands
3. Triggered wiki render

## Defense

Defensive measures and detection strategies:

- Monitor /tmp for unexpected files
- Audit gitlab-www process for anomalous io.popen calls
- Implement file integrity monitoring (e.g., Tripwire)

## Objectives

1. Confirm file creation from payload
2. Assess compromise depth
3. Identify escalation paths

## Instructions

### Step 1: Check File Existence

**Context**: Locate the written file.

**Command** (Shell):
```bash
ls -la /tmp/ggg
```

> Lists file. Expected output: -rw-r--r-- 1 gitlab-www ... /tmp/ggg.

### Step 2: Inspect Content

**Context**: Verify payload execution.

**Command** (Shell):
```bash
cat /tmp/ggg
```

> Reads file. Expected output: 'vakzz'.

### Step 3: Relate to Payload

**Context**: Tie back to executed command.

**Command** ([[commands/execute-echo-file]]):
Embedded: execute('echo vakzz > /tmp/ggg')

> Confirms write via io.popen. Expected: File matches payload.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[File and Directory Discovery]] File and Directory Discovery

### Sub-Techniques


## Commands Used

- [[commands/execute-echo-file]]

## Tools Used


## Tags

- verify
- impact
- file-write
