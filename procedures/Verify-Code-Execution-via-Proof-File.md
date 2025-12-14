---
tags:
  - rce
  - verification
  - proof
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/cat-rce-proof]]'
platforms:
  - Linux
  - POSIX
techniques:
  - '[[Exploitation for Client Execution]]'
  - '[[Dynamic Linker Hijacking]]'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
id: 9be81bd8-ca4c-40b2-b316-76f2c0038c3d
created_at: '2025-12-14T17:23:31.202Z'
updated_at: '2025-12-14T17:23:31.202Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
  - '[[Dynamic Linker Hijacking]]'
---
# Verify-Code-Execution-via-Proof-File

## Summary

Checks the contents of the proof file created by the RCE payload to confirm successful arbitrary code execution.

## Description

After curl loads the malicious library, the constructor runs 'id > /tmp/RCE_VIA_ENGINE'. This step reads the file to verify the output, proving RCE as the curl user in the POSIX environment.

## Requirements

1. /tmp/RCE_VIA_ENGINE created by prior RCE
2. Read access to /tmp

## Defense

Defensive measures and detection strategies:

- Monitor /tmp for unexpected files from 'id' or similar commands
- Alert on file creations in /tmp during curl executions
- Use SIEM to correlate library loads with file artifacts

## Objectives

1. Validate RCE success
2. Capture evidence of user context execution
3. Confirm payload efficacy

## Instructions

### Step 1: Display Proof File

**Context**: Read the file written by the system command to verify code ran.

**Command** ([[commands/cat-rce-proof]]):

```bash
cat /tmp/RCE_VIA_ENGINE
```

> Outputs the contents of the proof file. Expected: 'uid=1000(user) gid=1000(user) groups=...' indicating RCE.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploitation for Client Execution]]
- [[Dynamic Linker Hijacking]]

### Sub-Techniques


## Commands Used

- [[commands/cat-rce-proof]]

## Tools Used


## Tags

- [[rce]]
- [[verification]]
