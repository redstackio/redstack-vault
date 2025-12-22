---
tags:
  - symlink
  - ca-file
  - toctou-setup
type: procedure
tools:
  - '[[tools/ln]]'
tactics:
  - '[[Defense Evasion]]'
commands:
  - '[[commands/ln-symlink-legit-ca]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Registry Run Keys - Startup Folder]]'
updated_at: '2025-12-14T17:24:19.136Z'
skill_level: basic
impact_level: low
detection_risk: low
sub_techniques: []
id: 787da57d-0db7-4b56-82c4-6e958288960b
validated: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Registry Run Keys - Startup Folder]]'
---
# Create-Symlink-to-Legitimate-CA-File

## Summary

This procedure creates a symbolic link from ca.crt to legit_ca.crt, setting up the initial trusted CA bundle for curl's certificate validation during the first TLS handshake.

## Description

In the attack scenario, the symlink allows atomic swapping of the CA file on disk without changing curl's command-line arguments, exploiting the TOCTOU window where validation happens only once at connection setup.

## Requirements

1. legit_ca.crt file exists
2. Write permissions in directory
3. ln command available (standard on Linux)

## Defense

Defensive measures and detection strategies:

- Disable symlink creation in shared directories via filesystem policies
- Monitor symlink changes with tools like inotify or auditd
- Use absolute paths for CA bundles to prevent symlink attacks

## Objectives

1. Link ca.crt to legit_ca.crt for initial trust
2. Enable easy swap for race condition
3. Prepare for curl --cacert usage

## Instructions

### Step 1: Create Symlink

**Context**: Symlink the CA bundle to the legitimate certificate.

**Command** ([[commands/ln-symlink-legit-ca]]):
```bash
ln -s legit_ca.crt ca.crt
```

> Creates symbolic link ca.crt pointing to legit_ca.crt.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion]] Defense Evasion

### Techniques

- [[Registry Run Keys - Startup Folder]] .bash_profile and .bashrc

### Sub-Techniques


## Commands Used

- [[commands/ln-symlink-legit-ca]]

## Tools Used

- [[tools/ln]]

## Tags

- symlink
- ca-file
- toctou-setup
