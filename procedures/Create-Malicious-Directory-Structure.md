---
id: proc-create-dir-structure
tags:
  - dll-hijacking
  - persistence
type: procedure
tools:
  - '[[tools/Process-Monitor]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/mkdir-create-path]]'
verified: false
platforms:
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[DLL Search Order Hijacking]]'
updated_at: '2025-12-14T17:30:27.119Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[DLL Search Order Hijacking]]'
---
# Create-Malicious-Directory-Structure

## Summary

This procedure creates a directory tree on the Windows C: drive that mimics a non-existent path Burp Suite attempts to load DLLs from, such as a variant of 'C:\Program Files\...\amd64', exploiting default permissions to position for hijacking.

## Description

Burp Suite (Java version) on Windows tries to load DLLs like sunec.dll from paths that don't exist, such as those under 'C:\Program Files' (space causes potential %20 encoding issues in logs). Low-priv users can create these due to writable C:\. Use Process Monitor to identify exact failed load paths first. Outcome: Attacker-controlled directory ready for DLL placement, leading to hijack on app startup.

## Requirements

1. Low-priv user session with C:\ write access
2. Knowledge of target DLL path from Process Monitor (e.g., C:\Program Files\Java\...\amd64)
3. Command Prompt access

## Defense

Defensive measures and detection strategies:

- Harden C:\ permissions: Remove write access for standard users via NTFS ACLs
- Use Sysmon to log file/directory creations on root (Event ID 11)
- Application whitelisting to prevent unsigned DLL loads

## Objectives

1. Replicate vulnerable load path
2. Ensure path is writable and hidden from casual inspection
3. Validate with Process Monitor for exact match

## Instructions

### Step 1: Identify Target Path

**Context**: Use Process Monitor to observe Burp Suite's failed DLL loads and note the exact non-existent path.

Launch [[tools/Process-Monitor]] and filter for Burp process; start Burp briefly to capture loads.

> Look for 'NAME NOT FOUND' errors for DLLs like sunec.dll under C:\Program Files\...\amd64. Expected: Path details for recreation.

### Step 2: Build Directory Tree

**Context**: Create nested directories matching the observed path.

Execute [[commands/mkdir-create-path]] to build the structure:

```cmd
mkdir "C:\Program Files\Java\jre1.8.0_xxx\bin\server\amd64"
```

> Replace 'jre1.8.0_xxx' with observed version. Expected output: Directories created without errors. Verify with `dir C:\Program Files`.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[DLL Search Order Hijacking]]

### Sub-Techniques


## Commands Used

- [[commands/mkdir-create-path]]

## Tools Used

- [[tools/Process-Monitor]]

## Tags

- dll-hijacking
- persistence

