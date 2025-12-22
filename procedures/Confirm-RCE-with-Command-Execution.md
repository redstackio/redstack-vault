---
tags:
  - rce
  - execution
  - linux
  - file-read
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Linux
techniques:
  - '[[Unix Shell]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: dd9fd0aa-41fa-4a36-97e2-a69c213892d4
created_at: '2025-12-14T17:23:28.136Z'
updated_at: '2025-12-14T17:23:28.136Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Unix Shell]]'
---
# Confirm-RCE-with-Command-Execution

## Summary

This procedure verifies successful RCE in the Jenkins instance by executing system commands to identify the operating system and read sensitive files, confirming control over the environment.

## Description

Following deserialization exploitation, attackers can leverage the RCE to run shell commands on the Linux host (Debian 7 in this case). This includes querying OS details with uname and extracting user data from /etc/passwd, demonstrating compromise of the CI server and potential access to build slaves, though limited to non-sensitive testing tasks.

## Requirements

1. Established RCE session from prior exploitation
2. Knowledge of target OS for command crafting
3. Ability to inject or chain commands via payloads

## Defense

Defensive measures and detection strategies:

- Implement command logging and anomaly detection in Jenkins (e.g., via plugins)
- Use containerization or least-privilege for CI agents to limit command impact
- Monitor for unexpected file reads or OS queries in logs

## Objectives

1. Validate RCE by executing diagnostic commands
2. Extract sensitive information like user lists
3. Assess further compromise potential on slaves

## Instructions

### Step 1: Execute OS Identification Command

**Context**: Run a command to confirm the Linux distribution and version.

**Command** (Embedded in RCE payload):
```bash
uname -a
```

> Output shows Linux kernel details, confirming Debian 7 environment.

### Step 2: Read Sensitive File

**Context**: Access system files to demonstrate file read capabilities.

**Command** (Embedded in RCE payload):
```bash
cat /etc/passwd
```

> Returns user account listings, verifying arbitrary file access.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Unix Shell]]

### Sub-Techniques

- None

## Commands Used

- None (embedded in payloads)

## Tools Used

- None

## Tags

- [[rce]]
- [[Execution]]
- [[linux]]
- [[file-read]]
