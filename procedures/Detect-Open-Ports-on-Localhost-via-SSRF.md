---
id: proc-exness-port-scan
tags:
  - ssrf
  - port-scanning
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/post-probe-localhost-port]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Vulnerability Scanning]]'
updated_at: '2025-12-14T03:46:14.642Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Vulnerability Scanning]]'
---
# Detect-Open-Ports-on-Localhost-via-SSRF

## Summary

This procedure uses SSRF to detect open ports on the backend localhost by sending requests to 127.0.0.1:PORT and distinguishing validation errors (closed) from verbose Python connection errors (open).

## Description

The vulnerability allows targeting localhost without validation, leaking details via Python Requests errors for open ports. Tested on port 80; extensible to others like 443. Targets web backends with SSRF, revealing internal service exposure in Kubernetes or similar environments.

## Requirements

1. Confirmed SSRF from prior procedure
2. curl for HTTP requests
3. Knowledge of common ports (80, 443)

## Defense

Defensive measures and detection strategies:

- Validate and block localhost/internal IP URLs at input
- Suppress verbose errors from libraries like requests
- Log and alert on SSRF attempts to internal addresses

## Objectives

1. Identify open internal ports
2. Confirm SSRF depth for localhost access
3. Map backend services

## Instructions

### Step 1: Target Specific Port

**Context**: Send SSRF payload to localhost port to observe response differences.

**Command** ([[commands/post-probe-localhost-port]]):

```bash
curl -X POST https://my.exnessaffiliates.com/api/partner_integrations/template/probe \
  -H "Content-Type: application/json" \
  -d '{"data":{"url":"https://127.0.0.1:80"}}'
```

> For closed ports: JSON validation error; for open: HTTPSConnectionPool error with connection details.

### Step 2: Iterate Ports

**Context**: Repeat for ports 443, 1068, etc., noting error patterns.

Modify URL in the command above, e.g., :443.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Vulnerability Scanning]] Scanning IP Blocks

### Sub-Techniques


## Commands Used

- [[commands/post-probe-localhost-port]]

## Tools Used


## Tags

- ssrf
- port-scanning
- localhost
