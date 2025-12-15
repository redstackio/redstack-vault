---
tags:
  - payload-hosting
  - http-server
type: procedure
tools:
  - '[[tools/Custom-Python-HTTP-Server]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/start-python-http-server]]'
platforms:
  - Linux
techniques:
  - '[[Remote File Copy]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: ec8e6742-d093-4240-9add-c26cd7fad563
created_at: '2025-12-14T17:23:28.020Z'
updated_at: '2025-12-14T17:23:28.020Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Remote File Copy]]'
---
# Set-Up-Malicious-HTTP-Server

## Summary

This procedure deploys a custom Python HTTP server on a remote VPS to host a malicious PHP webshell and provide delaying endpoints, enabling the exploitation of Concrete CMS's timeout mechanism during remote file imports.

## Description

The server serves a PHP webshell (e.g., containing phpinfo() for PoC) at /byc.php and responds to /stuck with a 10-second delay to overload the CMS import process, forcing a timeout before temporary files are cleaned up. This setup is crucial for persisting the uploaded payload in the target's temp directory.

## Requirements

1. Remote VPS with Python 3 installed
2. Firewall allowing inbound traffic on port 8877
3. Custom server.py script prepared

## Defense

Defensive measures and detection strategies:

- Block unexpected outbound connections from CMS to unknown IPs
- Monitor for high-volume delayed HTTP requests
- Restrict file manager to trusted domains only

## Objectives

1. Host the PHP payload for remote download
2. Induce delays to bypass cleanup
3. Log requests for monitoring import progress

## Instructions

### Step 1: Prepare Server Script

**Context**: Ensure the custom server.py is configured to serve the webshell and delay.

No command; edit server.py to include EXPLOIT='<?php phpinfo(); ?>' for /byc.php and time.sleep(10) for /stuck.

> Script ready for execution.

### Step 2: Start the Server

**Context**: Launch the HTTP server on the specified port.

**Command** ([[commands/start-python-http-server]]):
```bash
python3 server.py --port 8877
```

> Starts the server, logging requests with timestamps. Expected output: "Server listening on port 8877".

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Remote File Copy]]

### Sub-Techniques


## Commands Used

- [[commands/start-python-http-server]]

## Tools Used

- [[tools/Custom-Python-HTTP-Server]]

## Tags

- [[payload-hosting]]
- [[rce]]
