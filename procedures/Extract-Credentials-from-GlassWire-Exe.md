---
tags:
  - binary-analysis
  - credential-extraction
  - strings
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
platforms:
  - Windows
techniques:
  - '[[Credentials In Files]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: fc2bf017-154e-43b9-9b61-6fcb656f7faf
created_at: '2025-12-14T17:32:20.720Z'
updated_at: '2025-12-14T17:32:20.720Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Credentials In Files]]'
---
# Extract-Credentials-from-GlassWire-Exe

## Summary

This procedure details the analysis of the GlassWire.exe binary embedded in the setup installer to extract hardcoded Facebook App ID and Secret credentials stored in cleartext.

## Description

The GlassWire vulnerability stems from storing sensitive Facebook API credentials directly in the executable, making them accessible via decompilation, string extraction, or binary inspection tools. This targets Windows executables and assumes the attacker has the setup file, leading to potential unauthorized API access.

## Requirements

1. Downloaded GlassWireSetup.exe (version 1.1.26.0b)
2. Binary analysis tools like strings.exe (Windows Sysinternals) or a decompiler such as IDA Pro
3. Basic knowledge of executable file structure

## Defense

Defensive measures and detection strategies:

- Avoid hardcoding secrets in binaries; use environment variables or secure vaults
- Implement code signing and integrity checks on executables
- Scan binaries for exposed strings during development

## Objectives

1. Locate the embedded GlassWire.exe within the installer
2. Extract cleartext credentials
3. Document the App ID and Secret for verification

## Instructions

### Step 1: Extract Embedded Executable

**Context**: The setup file contains the main executable; use archive tools or hex editors to access GlassWire.exe.

If the setup is self-extracting, run it in a sandbox or use 7-Zip to unpack and locate GlassWire.exe.

> Identify the file path to GlassWire.exe.

### Step 2: Analyze Binary for Strings

**Context**: Search for hardcoded strings like '660471650708388' and '71a2d003a5ecfab4f4ad86dfb70b74e0'.

Use strings tool:

```bash
strings GlassWire.exe | grep -i facebook
```

> This reveals the App ID: 660471650708388 and Secret: 71a2d003a5ecfab4f4ad86dfb70b74e0 in cleartext.

**Expected Output**: List of strings including the credentials.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Credentials In Files]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[binary-analysis]]
- [[credential-extraction]]

