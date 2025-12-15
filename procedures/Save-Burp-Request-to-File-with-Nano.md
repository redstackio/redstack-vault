---
tags:
  - file-export
  - request-saving
  - sqli-prep
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
  - '[[tools/nano]]'
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:30:35.246Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: c921d12f-68e3-47ea-9c53-e5bd103a9f4b
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Save-Burp-Request-to-File-with-Nano

## Summary

This procedure exports the captured HTTP request from Burp Suite to a text file using nano, creating input for SQLMap to exploit the SQL injection in Revive Adserver.

## Description

After interception, saving the request preserves the exact headers, method, and parameters (including the vulnerable 'keyword') for automated tool usage. This avoids re-authentication issues and ensures reproducibility. The target environment is a local Linux setup with Burp and nano available.

## Requirements

1. Captured request in Burp Suite
2. Nano text editor installed
3. Write permissions in the working directory

## Defense

Defensive measures and detection strategies:

- Log file creation events in web directories
- Scan for suspicious .txt files containing HTTP requests
- Use file integrity monitoring on server logs

## Objectives

1. Create a reusable request file for exploitation tools
2. Maintain request authenticity for successful injection
3. Enable offline analysis of the vulnerable payload point

## Instructions

### Step 1: Export from Burp

**Context**: Select and copy the request details from Burp's interface.

**Instructions**: In Burp's Proxy history or Repeater, right-click the request and choose 'Copy to file' or manually copy the raw request.

### Step 2: Open Nano and Paste

**Context**: Use nano to create and edit the file with the request content.

**Instructions**: Run `nano testsql.txt` and paste the HTTP request, ensuring it includes the full GET line, headers, and keyword parameter.

### Step 3: Save and Verify

**Context**: Confirm the file is correctly formatted for SQLMap.

**Instructions**: Save with Ctrl+O, exit with Ctrl+X, then cat the file to verify contents.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/nano]]

## Tags

- file-export
- request-saving
