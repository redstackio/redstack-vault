---
id: proc-trigger-snap-rce
tags:
  - rce
  - dynamic-linker-hijacking
type: procedure
tools:
  - '[[tools/snap]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/run-chromium-from-malicious-dir]]'
  - '[[commands/write-test-file-in-container]]'
  - '[[commands/read-test-file-in-container]]'
verified: false
platforms:
  - Linux
  - Ubuntu
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Dynamic Linker Hijacking]]'
updated_at: '2025-12-14T17:23:23.839Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Dynamic Linker Hijacking]]'
---
# Trigger-RCE-in-Snap-Application

## Summary

Execute a vulnerable snap application from the malicious cwd to hijack the dynamic linker, loading a fake libc.so.6 and running an RCE payload inside the snap container, allowing read/write to non-hidden home files.

## Description

Snapcraft's wrapper scripts set LD_LIBRARY_PATH to an empty string, causing ld.so to search the cwd and subdirs like 'tls' for libraries. Placing a malicious libc.so.6 (crafted with make_libc.py) in 'tls' leads to code execution when the app (e.g., Chromium) dlopen's libraries. Initial impact is confined to user home (no dotfiles), but enables further escalation. Scenarios include running media in VLC or building Docker images.

## Requirements

1. Malicious directory prepared with 'tls/libc.so.6'
2. Vulnerable snap installed (e.g., 'chromium' via snap)
3. User execution privileges

## Defense

Defensive measures and detection strategies:

- Update to Snapcraft 4.4.4+ which sets explicit LD_LIBRARY_PATH
- Restrict snap apps from running in untrusted directories
- Monitor strace for unusual library loads from cwd

## Objectives

1. Achieve RCE inside snap container
2. Confirm payload execution via file operations
3. Set stage for container escape

## Instructions

### Step 1: Launch Snap App from Malicious CWD

**Context**: Trigger library hijacking by running the app.

**Command** ([[commands/run-chromium-from-malicious-dir]]):
```bash
chromium
```

> Loads malicious libc.so.6 from 'tls', executes payload. Expected output: 'Got code execution running as itszn inside snap container!'.

### Step 2: Write Test File in Container

**Context**: Demonstrate RCE by writing to home.

**Command** ([[commands/write-test-file-in-container]]):
```bash
echo 'Hello from snap code exec' > /home/itszn/pwned
```

> Creates 'pwned' file. No output on success.

### Step 3: Read Test File to Verify

**Context**: Confirm write access.

**Command** ([[commands/read-test-file-in-container]]):
```bash
cat /home/itszn/pwned
```

> Outputs 'Hello from snap code exec'.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Dynamic Linker Hijacking]] Dynamic Linker Search Order Hijacking

### Sub-Techniques


## Commands Used

- [[commands/run-chromium-from-malicious-dir]]
- [[commands/write-test-file-in-container]]
- [[commands/read-test-file-in-container]]

## Tools Used

- [[tools/snap]]

## Tags

- rce
- dynamic-linker-hijacking
