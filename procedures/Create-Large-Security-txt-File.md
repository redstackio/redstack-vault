---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
tags:
  - dos
  - resource-exhaustion
  - file-generation
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands: []
verified: false
platforms:
  - Linux
  - macOS
  - Windows
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:26:48.885Z'
skill_level: novice
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Create-Large-Security-txt-File

## Summary

This procedure generates a 1-2 GB security.txt file filled with dummy content to exploit resource limits in applications that fetch and process such files without size checks, simulating a malicious oversized response.

## Description

In the context of testing a Chrome extension's getSecuritytxt function, create an oversized security.txt file on a local host. Security.txt files are meant to provide security contact info but can be bloated to cause denial of service when processed via AJAX without timeouts. The file is hosted locally to trigger the vulnerability upon extension activation, leading to high CPU and memory usage.

## Requirements

1. Access to a terminal or command prompt on Linux/macOS/Windows
2. Sufficient disk space (at least 2 GB free)
3. Basic scripting knowledge to generate repetitive content if needed

## Defense

Defensive measures and detection strategies:

- Implement file size limits (e.g., max 1 MB) in fetch functions
- Add timeouts (e.g., 10 seconds) to AJAX/XHR requests
- Monitor for anomalous large file downloads in browser extensions

## Objectives

1. Produce a file large enough to exhaust resources during full processing
2. Ensure the file mimics a valid security.txt to bypass basic validation
3. Prepare for hosting without alerting security tools

## Instructions

### Step 1: Generate Base File Structure

**Context**: Start with a valid security.txt header to ensure it's recognized as such.

**Command** (using echo and redirection):
```bash
echo "Contact: https://example.com/security\nPreferred-Languages: en" > large-security.txt
```

> This creates the initial file with standard directives. Expected output: A small text file with two lines.

### Step 2: Inflate File Size

**Context**: Append junk data or repeat content to reach 1-2 GB, simulating bloat from untrusted sources.

**Command** (using dd for binary padding or a loop for text):
```bash
# Option 1: Binary padding (faster)
dd if=/dev/zero bs=1M count=2048 >> large-security.txt
# Option 2: Text repetition (more realistic for security.txt)
for i in {1..100000}; do echo "Dummy entry $i: https://example.com" >> large-security.txt; done
```

> Adjust count for size; verify with `ls -lh large-security.txt`. Expected output: File grows to 1-2 GB without errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Endpoint Denial of Service]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[dos]]
- [[resource-exhaustion]]
