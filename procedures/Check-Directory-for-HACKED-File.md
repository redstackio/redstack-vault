---
id: proc-002
tags:
  - verification
  - windows
  - file-check
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/list-directory-windows]]'
verified: false
platforms:
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:23:20.594Z'
skill_level: beginner
impact_level: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Check-Directory-for-HACKED-File

## Summary

This procedure uses the Windows dir command to list directory contents and verify the presence or absence of the HACKED.txt file, used before and after exploitation to confirm RCE success.

## Description

In the context of exploiting the treekill vulnerability, this procedure checks the current working directory for the indicator file created by the injected command. It is run twice: once to ensure the file does not exist initially, and again to confirm creation post-exploitation. This validates the command injection without requiring additional tools.

## Requirements

1. Windows command prompt access
2. Current directory where PoC will run

## Defense

Defensive measures and detection strategies:

- Monitor file system changes with tools like Sysmon
- Log unexpected file creations in working directories
- Use antivirus to scan for suspicious .txt files

## Objectives

1. Confirm absence of HACKED.txt pre-exploit
2. Verify presence post-exploit
3. Validate RCE outcome

## Instructions

### Step 1: List Directory Contents

**Context**: Display files in the current directory to check for HACKED.txt.

**Command** ([[commands/list-directory-windows]]):
```bash
dir
```

> This lists all files and directories. Pre-exploit, HACKED.txt should not appear; post-exploit, it should be listed with size 7 bytes containing "HACKED".

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[File and Directory Discovery]] File and Directory Discovery

### Sub-Techniques


## Commands Used

- [[commands/list-directory-windows]]

## Tools Used


## Tags

- windows-cmd
- file-discovery
- verification
