---
id: dll-payload-prep
tags:
  - payload-creation
  - dll-placement
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/whoami-validate-privileges]]'
verified: false
platforms:
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[DLL Search Order Hijacking]]'
updated_at: '2025-12-14T17:29:36.854Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[DLL Search Order Hijacking]]'
---
# Prepare-Malicious-DLL-and-Payload

## Summary

This procedure involves placing a malicious snapapi.dll in a writable PATH directory and creating a batch file payload to execute arbitrary commands upon DLL loading, enabling code execution in the context of systeminfo.exe's elevated privileges.

## Description

Exploiting the observed DLL search order, a custom malicious DLL (e.g., one that loads and runs a batch file) is copied to a user-modifiable PATH folder like C:\Python27. A supporting batch file in C:\attacker\mmg.bat includes commands to validate escalation, such as dumping privilege information. This preparation requires local write access but no initial elevation, making it suitable for low-privilege attackers on Windows systems with the Acronis agent.

## Requirements

1. Local write access to a PATH directory (e.g., C:\Python27)
2. Pre-built malicious snapapi.dll (e.g., from attachment or custom build)
3. Text editor for batch file creation

## Defense

Defensive measures and detection strategies:

- Remove unnecessary writable directories from PATH
- Use application whitelisting to block unsigned DLLs
- Audit file placements in system PATH via integrity monitoring

## Objectives

1. Position malicious DLL for hijacking
2. Set up payload for elevated execution
3. Ensure payload validates success (e.g., via file output)

## Instructions

### Step 1: Place Malicious DLL

**Context**: Copy the DLL to a hijackable PATH location.

Use File Explorer or command line to copy:

```cmd
copy malicious_snapapi.dll C:\Python27\
```

> Ensure C:\Python27 is in PATH (verify with echo %PATH%). The DLL should mimic the legitimate snapapi.dll to load successfully.

### Step 2: Create Payload Directory and Batch File

**Context**: Set up a directory for the batch file and embed validation commands.

Create the directory:

```cmd
mkdir C:\attacker
```

Then create mmg.bat with content including [[commands/whoami-validate-privileges]]:

```cmd
@echo off
whoami /all >> C:\attacker\who.txt
```

> Save as C:\attacker\mmg.bat. The malicious DLL is configured to execute this batch upon loading (e.g., via DllMain).

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[DLL Search Order Hijacking]]

### Sub-Techniques


## Commands Used

- [[commands/whoami-validate-privileges]]

## Tools Used


## Tags

- payload-creation
- dll-placement
