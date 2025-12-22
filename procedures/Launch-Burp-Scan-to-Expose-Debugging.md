---
id: proc-launch-burp-scan
tags:
  - burp-suite
  - scan
  - chrome-debugging
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - macOS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-14T17:28:12.945Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
---
# Launch-Burp-Scan-to-Expose-Debugging

## Summary

This procedure launches a Burp Suite scan to trigger the embedded headless Chrome browser, exposing its remote debugging interface via an insecure websocket on a randomized port.

## Description

Burp Suite's scanner and crawler use an embedded headless Chrome instance for site analysis. When a scan is initiated, Chrome launches with the --remote-debugging-port flag, creating a websocket endpoint (e.g., ws://127.0.0.1:9225) instead of a secure named pipe. This exposure allows local JavaScript to scan and connect to it. The procedure targets the exploit server URL to ensure the scan interacts with the attacker's hosted content. Prerequisites include Burp Suite Professional edition installed on macOS.

## Requirements

1. Burp Suite Professional installed and licensed
2. Target URL (exploit server) reachable
3. macOS environment with Java runtime

## Defense

Defensive measures and detection strategies:

- Disable remote debugging in Burp configurations or use pipe transport (--remote-debugging-pipe)
- Monitor for headless Chrome processes with debugging flags (ps aux | grep chrome)
- Use tools like Puppeteer for secure alternatives

## Objectives

1. Activate Burp's embedded Chrome with debugging exposed
2. Ensure websocket is accessible locally
3. Simulate normal scanning behavior to avoid suspicion

## Instructions

### Step 1: Initiate Burp Scan

**Context**: Open Burp Suite and start a scan on the exploit server to launch headless Chrome.

**Command** (No CLI; GUI action):
No direct command; use Burp UI: Dashboard > New scan > Target: http://127.0.0.1:8000 > Start scan.

> Burp launches Chrome with randomized port. Expected output: Scan progress in Burp interface; verify debugging with `lsof -i :9222-9300` or browser dev tools. Success if websocket connects without auth.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- burp-suite
- scan
- chrome-debugging
