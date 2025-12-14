---
tags:
  - exfiltration
  - cookie-theft
  - verification
type: procedure
tools:
  - '[[tools/000webhost]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/php-cookie-logger]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:30.678Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
id: 4e6e0d69-978a-4ee9-8201-ee5b3379fb22
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Verify-Cookie-Exfiltration-on-Attacker-Server

## Summary

This procedure checks the attacker's hosted server for received cookie data exfiltrated by the executed JavaScript payload, confirming successful XSS exploitation.

## Description

The JS payload sends `document.cookie` via an img src GET request to the attacker's endpoint (e.g., https://bl4de.000webhostapp.com/?c=...). A simple PHP script logs this to a file. The attacker accesses the server logs post-trigger to retrieve stolen data, enabling further attacks like session replay (mitigated by HttpOnly in PoC).

## Requirements

1. Hosted PHP receiver script from prior setup
2. Access to server file system (e.g., via FTP or panel)
3. Triggered XSS execution

## Defense

Defensive measures and detection strategies:

- Set HttpOnly and Secure flags on session cookies
- Implement referrer checks or CORS to block cross-origin exfiltration
- Monitor external requests from internal apps

## Objectives

1. Retrieve exfiltrated victim data
2. Validate attack success
3. Plan follow-on exploitation

## Instructions

### Step 1: Access Attacker Server

**Context**: Log into the hosting service.

Use [[tools/000webhost]] panel to view files.

**Expected Output**: Access to cookies.txt.

### Step 2: Check Log File

**Context**: Inspect for appended cookie strings.

Open cookies.txt; look for entries like `c=CMSSESSIONID=abc123;...`.

**Expected Output**: Victim's cookie data logged.

### Step 3: Analyze Data

**Context**: Use stolen cookies for potential attacks.

Review for session tokens; test in browser if non-HttpOnly.

**Expected Output**: Confirmation of data theft.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/php-cookie-logger]]

## Tools Used

- [[tools/000webhost]]

## Tags

- exfiltration
- cookie-theft
- verification
