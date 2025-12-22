---
tags:
  - xss
  - payload
  - filename-injection
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Linux
  - macOS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:49.807Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 17c0f1fb-b290-4ff5-b3c1-3aae2486a73c
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Create-Malicious-Filenames

## Summary

This procedure creates files in the target directory with filenames embedding XSS payloads, such as onmouseover events, to exploit the lack of sanitization in the http_server module's directory listing rendering.

## Description

In the attack scenario, filenames like '" onmouseover=alert(1) "' or '<img src=x onmouseover=alert(1)>image' are crafted to inject HTML attributes or tags that execute JavaScript when rendered in the browser. The target environment is a local directory (e.g., ~/Desktop/) on a Unix-like system. Expected outcomes include files ready for serving, leading to script execution on client-side interaction. No special tools are needed beyond basic file creation commands.

## Requirements

1. Write access to the target directory
2. Shell environment supporting special characters in filenames
3. Basic knowledge of XSS payload construction

## Defense

Defensive measures and detection strategies:

- Sanitize and encode filenames in directory listings (e.g., use HTML entities)
- Implement file naming policies to block special characters
- Monitor directory changes for suspicious filename patterns

## Objectives

1. Store malicious payloads in filenames
2. Prepare directory for vulnerable serving
3. Ensure payloads survive rendering without escaping

## Instructions

### Step 1: Create Payload Files

**Context**: Use touch to create empty files with malicious names containing JavaScript events.

**Command**:
```bash
touch "\" onmouseover=alert(1) \""
touch '<img src=x onmouseover=alert(1)>image'
```

> These commands create files where the names inject onmouseover handlers or img tags. Expected output is silent success; verify with ls -la to see the files.

### Step 2: Verify Creation

**Context**: List directory contents to confirm malicious names are present.

**Command**:
```bash
ls -la
```

> Displays filenames, confirming payloads like the quoted onmouseover string.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- payload-creation
- xss-injection
