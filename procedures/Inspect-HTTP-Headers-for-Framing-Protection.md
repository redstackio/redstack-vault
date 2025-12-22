---
id: proc-inspect-headers-clickjacking
name: Inspect HTTP Headers for Framing Protection
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:04.946Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Active Scanning]]'
sub_techniques: []
tags:
  - reconnaissance
  - headers
  - x-frame-options
  - web
commands:
  - '[[commands/curl-check-headers]]'
platforms:
  - Web
tools: []
skill_level: intermediate
impact_level: low
detection_risk: low
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Active Scanning]]'
---

# Inspect HTTP Headers for Framing Protection

## Summary

This procedure involves checking HTTP response headers of a target website to detect the absence of framing protection headers like X-Frame-Options, which enables clickjacking vulnerabilities. It is primarily used in web reconnaissance to identify sites susceptible to UI redressing attacks.

## Description

In a clickjacking attack scenario, attackers exploit sites without proper anti-framing headers to embed content in iframes on malicious pages. This procedure targets web applications like the Localize website, where the server fails to send X-Frame-Options, allowing external framing. Prerequisites include public access to the target URL. Expected outcomes: Confirmation of vulnerability, enabling further exploitation steps.

## Requirements

1. Network access to the target website (e.g., https://localizejs.com)
2. Command-line tools like curl or a web browser with developer tools
3. Basic knowledge of HTTP headers

## Defense

Defensive measures and detection strategies:

- Implement X-Frame-Options: DENY or SAMEORIGIN in server responses
- Monitor for anomalous iframe embeddings via WAF rules
- Use Content-Security-Policy (CSP) frame-ancestors directive

## Objectives

1. Identify missing security headers to confirm clickjacking risk
2. Map vulnerable pages across the site
3. Gather evidence for vulnerability reporting

## Instructions

### Step 1: Check Headers Using Curl

**Context**: Use curl to fetch and inspect response headers from the target URL, focusing on X-Frame-Options.

**Command** ([[commands/curl-check-headers]]):
```bash
curl -I https://localizejs.com/
```

> This command sends a HEAD request and displays headers. Look for X-Frame-Options; if absent, the site is vulnerable. Repeat for multiple pages (e.g., /dashboard, /tasks) to confirm widespread issue.

### Step 2: Verify with Browser DevTools

**Context**: Use browser tools for interactive inspection if curl is unavailable.

**Instructions**: Open the target page in Chrome, press F12, go to Network tab, reload, and select the request to view headers.

**Expected Output**: Headers list without X-Frame-Options.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used

- [[commands/curl-check-headers]]

## Tools Used


## Tags

- [[Reconnaissance]]
- [[web]]
