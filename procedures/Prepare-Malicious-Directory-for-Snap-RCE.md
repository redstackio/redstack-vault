---
id: proc-prepare-malicious-dir
tags:
  - rce-setup
  - poc-extraction
type: procedure
tools:
  - '[[tools/tar]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/extract-snap-escape-poc]]'
  - '[[commands/change-to-malicious-directory]]'
  - '[[commands/list-directory-contents]]'
verified: false
platforms:
  - Linux
  - Ubuntu
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Remote File Copy]]'
updated_at: '2025-12-14T17:23:23.841Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Remote File Copy]]'
---
# Prepare-Malicious-Directory-for-Snap-RCE

## Summary

This procedure sets up an attacker-controlled current working directory by extracting a POC archive containing decoy files and a 'tls' subdirectory with a malicious libc.so.6 library, priming the environment for dynamic linker hijacking in Snapcraft apps.

## Description

The vulnerability relies on running snap apps from a directory where the attacker can place libraries that the dynamic linker (ld.so) will load due to empty LD_LIBRARY_PATH in the snap's bash wrapper scripts. The POC archive includes a fake file (e.g., 'amazing-movie.mp4') to lure the user into running the app from this directory, along with the malicious library generated via make_libc.py. This step is prerequisite for triggering RCE and applies to scenarios like media playback (VLC) or web browsing (Chromium).

## Requirements

1. POC archive 'snap-escape.tar.gz' available, containing malicious libraries
2. Local file write access on the target Ubuntu system
3. Tar utility installed (standard on Linux)

## Defense

Defensive measures and detection strategies:

- Monitor for unusual archive extractions in user directories
- Enforce snap app execution from trusted paths via policy
- Audit LD_LIBRARY_PATH in snap wrappers post-4.4.4

## Objectives

1. Establish malicious cwd with hijackable libraries
2. Verify setup without alerting the user
3. Prepare for app execution trigger

## Instructions

### Step 1: Extract POC Archive

**Context**: Unpack the tar.gz to place malicious files in the filesystem.

**Command** ([[commands/extract-snap-escape-poc]]):
```bash
tar xfvz snap-escape
```

> Extracts files including 'amazing-movie.mp4', 'README.txt', and 'tls' directory with malicious libc.so.6. Expected output: Directory listing during extraction.

### Step 2: Change to Extracted Directory

**Context**: Set the cwd to the malicious directory for library loading.

**Command** ([[commands/change-to-malicious-directory]]):
```bash
cd snap-escape
```

> Changes prompt to 'itszn@ubuntu:snap-escape$'. No output beyond prompt change.

### Step 3: Verify Directory Contents

**Context**: Confirm malicious files are in place.

**Command** ([[commands/list-directory-contents]]):
```bash
ls
```

> Lists 'total 8', '-rw-rw-r-- amazing-movie.mp4', '-rw-rw-r-- README.txt', 'drwxrwxr-x tls'. Success if 'tls' directory present.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Remote File Copy]] Ingress Tool Transfer

### Sub-Techniques


## Commands Used

- [[commands/extract-snap-escape-poc]]
- [[commands/change-to-malicious-directory]]
- [[commands/list-directory-contents]]

## Tools Used

- [[tools/tar]]

## Tags

- rce-setup
- poc-extraction
