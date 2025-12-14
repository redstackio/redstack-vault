---
id: proc-test-clickjacking-protections
name: Test API for Clickjacking Protections
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:12.706Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - clickjacking
  - headers
  - web-testing
commands:
  - '[[commands/check-http-headers-for-x-frame-options]]'
platforms:
  - Web
tools: []
skill_level: beginner
impact_level: low
detection_risk: low
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Test API for Clickjacking Protections

## Summary

This procedure tests a web API endpoint for clickjacking vulnerabilities by inspecting HTTP response headers for the presence of X-Frame-Options, a key defense against UI redressing attacks where malicious iframes overlay legitimate interfaces to trick user interactions.

## Description

Clickjacking occurs when an attacker uses iframes to overlay invisible elements on a legitimate page, capturing clicks intended for the victim site. The X-Frame-Options header prevents this by instructing browsers not to allow framing. This procedure targets public API endpoints like https://www.goodhire.com/api, assuming no authentication is needed for header checks. Expected outcome: Identification of missing protections, rated low severity as it requires social engineering for impact but exposes the endpoint to potential abuse.

## Requirements

1. Command-line access with curl installed (standard on most Unix-like systems).
2. Internet connectivity to reach the target URL.
3. Basic knowledge of HTTP headers.

## Defense

Defensive measures and detection strategies:

- Implement X-Frame-Options: DENY or SAMEORIGIN in server responses.
- Monitor for anomalous iframe embedding attempts via web application firewalls (WAF).
- Use Content-Security-Policy (CSP) frame-ancestors directive as an additional layer.

## Objectives

1. Retrieve and analyze HTTP headers from the target API.
2. Detect absence of anti-framing headers.
3. Validate potential for clickjacking exploitation.

## Instructions

### Step 1: Fetch HTTP Headers

**Context**: Use curl to send a HEAD request and inspect response headers for X-Frame-Options.

**Command** ([[commands/check-http-headers-for-x-frame-options]]):
```bash
curl -I https://www.goodhire.com/api
```

> This command performs a lightweight HEAD request, returning only headers. Look for lines like "X-Frame-Options: DENY". If missing, the endpoint is vulnerable to framing.

### Step 2: Analyze Output

**Context**: Review the headers output to confirm the absence of protective headers.

**Command** (Manual inspection):
No command needed; parse the curl output manually or with grep:
```bash
echo "$(curl -I https://www.goodhire.com/api)" | grep -i x-frame-options
```

> Expected: No output if header is missing, confirming vulnerability.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/check-http-headers-for-x-frame-options]]

## Tools Used


## Tags

- [[clickjacking]]
- [[web-vulnerability]]
