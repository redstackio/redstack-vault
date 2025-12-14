---
id: modify-payload-quarantine
tags:
  - payload-modify
  - av-bypass
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/echo-modify-to-calc]]'
verified: false
platforms:
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Windows Command Shell]]'
  - '[[Disable or Modify Tools]]'
updated_at: '2025-12-14T17:29:44.751Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Windows Command Shell]]'
  - '[[Disable or Modify Tools]]'
---
# Modify-Payload-Before-Quarantine

## Summary

This procedure overwrites the detected threat file with attacker-controlled content during the AV detection window, allowing the quarantined version to contain malicious payload instead of the benign test string.

## Description

Exploiting the delay in Acronis AV's quarantine process when 'Block and notify' is active, modify the file contents post-detection but pre-quarantine. This injects commands like 'calc' for testing or more malicious code, enabling execution upon restoration to a redirected location. Requires quick execution after AV alert but before quarantine completes.

## Requirements

1. AV detection already triggered
2. User interaction rights for file writes
3. Timing: Act within seconds of detection prompt

## Defense

Defensive measures and detection strategies:

- Configure AV to immediately quarantine without user prompt delay
- Monitor file write events on recently detected threats
- Use behavior-based detection for rapid modifications

## Objectives

1. Replace EICAR with executable payload
2. Ensure quarantine captures modified content
3. Set up for privilege escalation on restore

## Instructions

### Step 1: Overwrite File Contents

**Context**: Rapidly replace the file to embed the desired command.

**Command** ([[commands/echo-modify-to-calc]]):
```cmd
echo calc > %userprofile%\Desktop\eicar\eicar.bat
```

> This echoes 'calc' and overwrites the batch file, which will run Calculator when executed. Do this immediately after AV detection. Expected output: File contents updated to 'calc'.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Windows Command Shell]] Windows Command Shell
- [[Disable or Modify Tools]] Disable or Modify Tools

### Sub-Techniques

-

## Commands Used

- [[commands/echo-modify-to-calc]]

## Tools Used

-

## Tags

- payload-modify
- av-bypass
