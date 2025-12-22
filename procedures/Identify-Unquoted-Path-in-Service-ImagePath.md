---
tags:
  - unquoted-path
  - vulnerability-identification
  - windows
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/reg-query-service-imagepath]]'
verified: false
platforms:
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:26:27.157Z'
sub_techniques: []
id: acfa8c4c-c120-46fe-b06e-98a22f535744
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Identify-Unquoted-Path-in-Service-ImagePath

## Summary

This procedure analyzes the ImagePath registry value of the Rockstar Game Library Service to detect the absence of quotation marks, which allows Windows to misparse paths with spaces and enables potential hijacking.

## Description

Windows services with unquoted ImagePath values are vulnerable because the system searches for the executable in every folder along the path segments separated by spaces. For example, a path like C:\Program Files\App\app.exe allows execution of C:\Program.exe if it exists. This procedure builds on registry examination to flag this issue, targeting the Rockstar service for local escalation scenarios.

## Requirements

1. Output from prior registry query
2. Basic scripting or manual inspection capability
3. Understanding of Windows path parsing rules

## Defense

Defensive measures and detection strategies:

- Audit service ImagePaths with tools like PowerShell's Get-Service
- Implement centralized configuration management to enforce quoting
- Log service start failures via Event Viewer (Event ID 7000/7024)

## Objectives

1. Confirm absence of quotes in ImagePath
2. Document the vulnerable path structure
3. Assess hijack potential based on path segments

## Instructions

### Step 1: Extract and Inspect Path

**Context**: Retrieve the ImagePath and check for enclosing double quotes.

**Command** ([[commands/reg-query-service-imagepath]]):
```cmd
reg query "HKLM\SYSTEM\CurrentControlSet\Services\RockstarService" /v ImagePath
```

> Inspect the output for quotes. If the path starts with the value without " around it, it's unquoted. Expected: Path like `C:\Program Files\...` without delimiters.

### Step 2: Validate Parsing Behavior

**Context**: Simulate Windows' search order by checking directory existence in segments.

**Command** ([[commands/dir-path-segments]]):
```cmd
dir /ad "C:\Program Files"
```

> Lists subdirectories; if writable, confirms potential for hijack. Success: Identifies exploitable segments before spaces.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[File and Directory Discovery]] File and Directory Discovery

### Sub-Techniques

-

## Commands Used

- [[commands/reg-query-service-imagepath]]
- [[commands/dir-path-segments]]

## Tools Used

-

## Tags

- [[path-analysis]]
- [[vulnerability-scan]]
