---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
tags:
  - payload-creation
  - batch-script
type: procedure
tools:
  - '[[tools/malstaller-bat]]'
tactics:
  - '[[Privilege Escalation]]'
commands: []
verified: false
platforms:
  - Windows
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Bypass User Account Control]]'
updated_at: '2025-12-14T17:29:44.578Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Bypass User Account Control]]'
---
# Create-Malicious-Payload-for-Elevation

## Summary

This procedure creates a malicious batch script (`malstaller.bat`) that serves as the payload for elevated execution, such as replacing VeraCrypt binaries with malware in a proof-of-concept scenario.

## Description

In the context of the VeraCrypt UAC bypass, a limited admin user prepares a payload that will be executed with full privileges once the hijack is triggered. The script is placed on the desktop and customized for the user's environment. For PoC, it uses an existing executable like putty.exe renamed and copied to the VeraCrypt folder, then executed. This allows tampering with the installation, file deletion, or task scheduling.

## Requirements

1. Local write access to desktop
2. Windows environment with batch execution allowed
3. Knowledge of target installation path (e.g., C:\Program Files\VeraCrypt)

## Defense

Defensive measures and detection strategies:

- Monitor batch file creation in user directories with EDR tools
- Restrict execution of unsigned scripts via AppLocker or WDAC
- Audit file copies to privileged directories like Program Files

## Objectives

1. Prepare executable payload for privilege escalation
2. Ensure payload performs desired malicious actions (e.g., binary replacement)
3. Validate payload without elevation for syntax

## Instructions

### Step 1: Create the Batch Script

**Context**: Write the malstaller.bat file to handle the elevated execution, including copying and running a fake binary.

**Command** (Manual file creation):

Create `C:\Users\[Username]\Desktop\malstaller.bat` with content:

```batch
@echo off
copy "C:\path\to\putty.exe" "C:\Program Files\VeraCrypt\VeraCrypt2.exe"
"C:\Program Files\VeraCrypt\VeraCrypt2.exe"
```

> This copies putty.exe as a fake VeraCrypt executable and runs it. Replace paths as needed. Expected output: No console output if successful; verify by checking file existence.

### Step 2: Test Payload Syntax

**Context**: Ensure the script runs without errors in a non-elevated context.

**Command** ([[Run batch test]]):

```bash
malstaller.bat
```

> Run manually; expect syntax check without full execution if paths are invalid. Success: No error messages.
