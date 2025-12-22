---
id: proc-uuid-1
tags:
  - sqli
  - recon
  - web
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/endpoint-baseline-test]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:14.969Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Identify Vulnerable Endpoint

## Summary

This procedure establishes a baseline for the target web endpoint by sending a normal request and observing response behavior, preparing for SQL injection testing on the /elist/viewem6.php rememail parameter.

## Description

In a DoD subdomain context, the endpoint processes email listing requests via POST. Lack of input validation allows injection. This step confirms accessibility and normal latency, essential for detecting delays in subsequent injection tests. Target: HTTPS on port 443, no auth required.

## Requirements

1. Burp Suite installed and proxy configured
2. Network access to the target subdomain
3. Valid session cookies if session-based

## Defense

Defensive measures and detection strategies:

- Implement web application firewall (WAF) to block anomalous requests
- Log and monitor POST parameters for unusual patterns
- Use parameterized queries to prevent injection

## Objectives

1. Verify endpoint functionality
2. Establish baseline response time
3. Identify injection parameter (rememail)

## Instructions

### Step 1: Send Baseline Request

**Context**: Intercept and replay a standard POST to observe normal behavior.

**Command** ([[commands/endpoint-baseline-test]]):
```bash
# In Burp Suite Repeater: POST https://████████/elist/viewem6.php
# Headers: User-Agent, Cookie (v1st=A9532F64A9E711AF; PHPSESSID=1796d85a30d3addf5934c1f0fafec529)
# Body: rememail=test@att.net
```

> This sends a legitimate email parameter, expecting a quick response without errors or delays.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/endpoint-baseline-test]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- sqli
- recon
