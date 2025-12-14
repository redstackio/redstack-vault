---
id: proc-002
tags:
  - verification
  - file-check
  - baseline
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/ls-check-files]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:23:24.009Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Verify-Initial-File-Absence

## Summary

This procedure uses the ls command to list files in the current directory, confirming the absence of a target file like 'HACKED' before executing the exploit, establishing a clean baseline state.

## Description

In the context of reproducing the node-df RCE, this step verifies no artifacts from prior runs exist. It targets a Linux environment and ensures the exploitation can be measured by file creation. Prerequisites include a clean working directory post-module installation.

## Requirements

1. Linux shell access
2. Current directory is the project root
3. No prior exploitation artifacts

## Defense

Defensive measures and detection strategies:

- Monitor file system changes with tools like auditd
- Use integrity checking tools like AIDE to detect unexpected file creations
- Log all ls commands if in a monitored environment

## Objectives

1. Confirm 'HACKED' file does not exist initially
2. Establish baseline for post-exploitation verification
3. Ensure clean state for reproducible testing

## Instructions

### Step 1: List Directory Contents

**Context**: Check for the presence of any 'HACKED' file to confirm initial absence.

**Command** ([[commands/ls-check-files]]):
```bash
ls
```

> Lists files in the current directory. Expected output: No 'HACKED' in the listing.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[File and Directory Discovery]]

### Sub-Techniques


## Commands Used

- [[commands/ls-check-files]]

## Tools Used


## Tags

- verification
- file-check
- baseline
