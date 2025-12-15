---
id: proc-verify-rce-tmp
tags:
  - rce-verification
  - file-write
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/ls-tmp-directory]]'
  - '[[commands/cat-tmp-alexb-says-hi]]'
verified: false
platforms:
  - Linux
  - Docker
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unix Shell]]'
updated_at: '2025-12-14T17:23:37.251Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Unix Shell]]'
---
# Verify-RCE-Execution-in-Tmp-Directory

## Summary

This procedure checks the /tmp directory for files written by the RCE payload, confirming successful command execution like uname -a in the exploited Chromium.

## Description

After running the headless shell, the payload executes system commands, leaving artifacts in /tmp. This verifies the RCE without full shell access. In Kibana context, it proves compromise of the container. Run inside the Docker container post-exploit.

## Requirements

1. Kibana container running post-exploit.
2. Access to bash inside container.
3. Knowledge of payload's file output (/tmp/alexb-says-hi).

## Defense

Defensive measures and detection strategies:

- Monitor /tmp for unexpected files with system info.
- Log file creation events in containers.
- Use immutable /tmp or monitoring tools like auditd.

## Objectives

1. Confirm payload execution.
2. Leak system information.
3. Validate RCE impact.

## Instructions

### Step 1: List Tmp Files

**Context**: Check for new files created by RCE.

**Command** ([[commands/ls-tmp-directory]]):
```bash
ls /tmp/
```

> Lists contents. Expected output: 'alexb-says-hi ks-script-esd4my7v ks-script-eusq_sc5' (new file present).

### Step 2: Read Output File

**Context**: View the contents written by payload.

**Command** ([[commands/cat-tmp-alexb-says-hi]]):
```bash
cat /tmp/alexb-says-hi
```

> Displays file. Expected output: 'Linux bd1b285e33b7 4.19.121-linuxkit #1 SMP Thu Jan 21 15:36:34 UTC 2021 x86_64 x86_64 x86_64 GNU/Linux'.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Unix Shell]] Unix Shell

### Sub-Techniques


## Commands Used

- [[commands/ls-tmp-directory]]
- [[commands/cat-tmp-alexb-says-hi]]

## Tools Used


## Tags

- rce-verification
- file-write
