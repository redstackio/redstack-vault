---
id: proc-analyze-rate-limit
tags:
  - reconnaissance
  - rate-limiting
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:31:52.793Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Analyze-Login-Rate-Limiting-Mechanism

## Summary

This procedure tests the rate limiting on a web login endpoint to identify thresholds and potential bypass methods, such as IP-based limits that can be evaded with rotation.

## Description

In the attack on HackerOne's /sessions endpoint, analysis revealed a 4-second delay per IP, allowing 15 guesses per minute. This was tested by sending POST requests and monitoring block responses, enabling calculation of hourly/daily limits (900/hour, 21,600/day). This reconnaissance step is crucial for planning brute-force attacks where IP rotation can scale attempts.

## Requirements

1. Access to the target login endpoint (e.g., https://hackerone.com/sessions)
2. Tool for sending HTTP POST requests (e.g., curl or Python requests)
3. Basic scripting knowledge to automate timing tests

## Defense

Defensive measures and detection strategies:

- Implement account-level rate limiting or CAPTCHA after failed attempts
- Monitor for anomalous request patterns from single IPs
- Use behavioral analysis to detect scripted login attempts

## Objectives

1. Identify rate limit thresholds per IP
2. Calculate effective guess rates (e.g., 15/min per IP)
3. Assess bypass feasibility (e.g., via multiple IPs)

## Instructions

### Step 1: Test Request Timing

**Context**: Send POST requests to the login endpoint with invalid credentials and measure response times/delays.

No specific command; use tools like curl:

```bash
curl -X POST https://hackerone.com/sessions -d 'login=invalid&password=invalid' -v
```

> Send requests at varying intervals (e.g., <4s, >4s) and observe if blocked (e.g., 429 response). Expected: Blocks for requests faster than 4 seconds.

### Step 2: Calculate Limits

**Context**: Based on delay, compute scalable rates.

No command; manual calculation: 60s / 4s = 15/min per IP.

> Expected: Documentation of limits like 900/hour, highlighting bypass via IP changes.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Reconnaissance]]
- [[rate-limiting]]
