---
id: proc-php-trigger-crash-001
tags:
  - php
  - dos
  - crash
type: procedure
tools:
  - '[[tools/fsockopen]]'
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/php-execute-poc]]'
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T05:32:09.952Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Trigger-PHP-Crash-with-PoC

## Summary

This procedure executes the PoC script to send the malformed request, triggering a null pointer dereference in PHP's php_session_rfc1867_callback and causing a remote crash of the PHP process for denial-of-service.

## Description

The crafted request leads to uninitialized progress->data being dereferenced during array separation in the session callback, resulting in a segmentation fault. No custom server code is needed; it affects built-in or FPM handlers. Exploitation requires the server to process the request, confirming the crash via logs or process termination.

## Requirements

1. poc.php script prepared
2. Vulnerable PHP server running on localhost:8000
3. PHP CLI access

## Defense

Defensive measures and detection strategies:

- Patch to PHP 7.1+ or enable cleanup
- Use process supervisors like systemd to restart crashed PHP-FPM
- Intrusion detection on unusual POST patterns to /index.php

## Objectives

1. Send request causing uninitialized data access
2. Observe remote process crash
3. Validate DoS impact

## Instructions

### Step 1: Execute PoC Script

**Context**: Run the script to connect and transmit the request via socket.

**Command** ([[commands/php-execute-poc]]):
```bash
php poc.php
```

> Executes the fsockopen-based request. Expected output: Dump of partial HTTP response, e.g., 'HTTP/1.1 200 OK' followed by crash indication.

### Step 2: Verify Crash

**Context**: Check server logs or process status for segmentation fault.

**Command** ([[commands/ps-check-php-process]]):
```bash
ps aux | grep php
```

> Monitors for PHP process termination. Expected output: No running PHP server process post-execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[Endpoint Denial of Service]]

### Sub-Techniques


## Commands Used

- [[commands/php-execute-poc]]
- [[commands/ps-check-php-process]]

## Tools Used

- [[tools/fsockopen]]

## Tags

- php
- dos
- crash
