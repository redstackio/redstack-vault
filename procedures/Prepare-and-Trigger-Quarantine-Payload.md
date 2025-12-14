---
id: prepare-quarantine-payload
tags:
  - av-trigger
  - eicar
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/mkdir-create-eicar-folder]]'
  - '[[commands/echo-write-eicar-string]]'
verified: false
platforms:
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Windows Command Shell]]'
updated_at: '2025-12-14T17:29:44.756Z'
skill_level: intermediate
impact_level: low
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Windows Command Shell]]'
---
# Prepare-and-Trigger-Quarantine-Payload

## Summary

This procedure sets up and triggers the Acronis True Image Antivirus detection by creating a folder and writing an EICAR test file, simulating a threat to initiate the quarantine process.

## Description

In a local Windows environment with Acronis True Image AV enabled, create a target directory and populate it with the standard EICAR test string in a batch file. This triggers the AV to detect it as malware, prompting for quarantine. The approach exploits the brief window during detection to prepare for subsequent modification, ultimately leading to privilege escalation via redirected restores. Prerequisites include local command execution rights and AV real-time scanning active.

## Requirements

1. Windows OS with NTFS (for later junctions)
2. Acronis True Image AV installed and scanning enabled
3. Low-privileged user access to execute commands

## Defense

Defensive measures and detection strategies:

- Enable strict AV policies to prevent file modifications during detection
- Monitor for EICAR test file creations via file integrity monitoring
- Log and alert on unusual batch file writes in user directories

## Objectives

1. Trigger AV quarantine workflow
2. Prepare payload location for modification
3. Simulate threat without real malware

## Instructions

### Step 1: Create Target Folder

**Context**: Establishes the directory that will hold the initial payload file.

**Command** ([[commands/mkdir-create-eicar-folder]]):
```cmd
mkdir %userprofile%\Desktop\eicar
```

> This command uses the Windows mkdir to create a new folder named 'eicar' on the desktop, leveraging the %userprofile% environment variable for the current user's path. Expected output: 'Directory created successfully' or no error.

### Step 2: Write EICAR String to Batch File

**Context**: Creates the file that AV will detect as a threat.

**Command** ([[commands/echo-write-eicar-string]]):
```cmd
echo|set /p="X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*" > %userprofile%\Desktop\eicar\eicar.bat
```

> This uses echo with set /p to output the EICAR string without a newline, redirecting to eicar.bat. AV detects it immediately. Expected output: File created, AV alert appears.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Windows Command Shell]] Windows Command Shell

### Sub-Techniques

-

## Commands Used

- [[commands/mkdir-create-eicar-folder]]
- [[commands/echo-write-eicar-string]]

## Tools Used

-

## Tags

- av-trigger
- eicar
