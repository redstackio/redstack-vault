---
id: p-verify-cmd-execution
tags:
  - verification
  - rce-testing
  - windows
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
  - '[[tools/ysoserial]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/ysoserial-generate-commonscollections-fakefile]]'
verified: false
platforms:
  - Web
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Windows Command Shell]]'
updated_at: '2025-12-14T17:23:42.637Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Windows Command Shell]]'
---
# Verify Command Execution via Response Analysis

## Summary

This procedure verifies RCE success by sending payloads for existing vs. non-existent commands and analyzing response differences for Windows-specific error strings.

## Description

For a valid command like cmd.exe, successful execution yields no error; for fakefile.exe, a 'cannot find' error appears if deserialization triggers the command attempt. This distinguishes blind RCE confirmation without full shell.

## Requirements

1. Previous payload generation setup
2. Burp Suite for request/response handling
3. Understanding of Windows command behaviors

## Defense

Defensive measures and detection strategies:

- Log command execution attempts from web contexts
- Anomaly detection on response patterns indicating RCE probes
- Rate limiting on invoker endpoints

## Objectives

1. Confirm payload triggers command attempts
2. Differentiate success from failure
3. Validate RCE without outbound callbacks

## Instructions

### Step 1: Generate Test Payload

**Context**: Create payload for non-existent file to elicit error.

**Command** ([[commands/ysoserial-generate-commonscollections-fakefile]]):
```bash
java -jar ysoserial-0.0.4-all.jar CommonsCollections1 'fakefile.exe' > serialdata
```

> Expected: Binary file; send to endpoint and search response for 'The system cannot find the file specified'.

### Step 2: Compare with Valid Command

**Context**: Repeat with cmd.exe payload and note absence of error.

Send original payload; inspect response.

> Expected: Clean response or no error string, confirming execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Windows Command Shell]] Windows Command Shell

### Sub-Techniques


## Commands Used

- [[commands/ysoserial-generate-commonscollections-fakefile]]

## Tools Used

- [[tools/ysoserial]]
- [[tools/Burp-Suite]]

## Tags

- verification
- rce
