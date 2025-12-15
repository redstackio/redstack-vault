---
tags:
  - ssrf
  - port-scan
type: procedure
tools:
  - '[[tools/nodejs]]'
  - '[[tools/request-npm]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/node-portscanner-jsreport]]'
platforms:
  - Web
  - Node.js
techniques:
  - '[[Network Service Scanning]]'
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: a12c9d9e-e96d-4705-83b4-74a912ff3d03
created_at: '2025-12-14T17:23:25.001Z'
updated_at: '2025-12-14T17:23:25.001Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Network Service Scanning]]'
  - '[[Exploit Public-Facing Application]]'
---
# Discover Script-Manager Port via SSRF

## Summary

This procedure exploits SSRF in jsreport's Puppeteer module to perform internal port scanning and identify the random port of the script-manager server.

## Description

Puppeteer renders HTML templates server-side, allowing arbitrary URLs in elements like <img> to trigger SSRF. A custom Node.js script automates divide-and-conquer scanning over ports 1024-65535 by sending templated POSTs and analyzing debug error logs for connection refusals.

## Requirements

1. Running jsreport instance with template 'test1' and its shortid
2. Node.js 10.16.0+ with 'request' module installed (npm install request)
3. Access to jsreport API

## Defense

Defensive measures and detection strategies:

- Disable debug logging in Puppeteer
- Validate and restrict URLs in HTML templates
- Monitor for unusual internal connection attempts from the application server

## Objectives

1. Scan port ranges using SSRF
2. Narrow down to the exact script-manager port
3. Log the discovered port for exploitation

## Instructions

### Step 1: Prepare portScanner.js Script

**Context**: Write the Node.js script to automate SSRF requests.

**Command** (File Creation):
No CLI; create portScanner.js with code using request.post to /api/report/{template} with form data including HTML that loops img src over 1000-port chunks, detecting via 'ECONNREFUSED' or 500 errors.

> Script uses Promises for async scanning.

### Step 2: Execute Scanning

**Context**: Run the script with template name and ID to discover the port.

**Command** ([[commands/node-portscanner-jsreport]]):
```bash
node portScanner.js test1 BJe2Pi2AgB
```

> Scans in chunks, outputs the open port, e.g., 12354, based on successful connections.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Network Service Scanning]] Network Service Scanning
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/node-portscanner-jsreport]]

## Tools Used

- [[tools/nodejs]]
- [[tools/request-npm]]

## Tags

- ssrf
- port-scan
