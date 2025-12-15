---
tags:
  - clickjacking
  - headers
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-check-headers]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:28:04.933Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 069ed985-8a40-4799-ae8f-732cc6e1e08b
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Identify-Missing-X-Frame-Options-Header

## Summary

This procedure checks for the absence of the X-Frame-Options HTTP header on a web application, which prevents clickjacking by disallowing iframe embedding. It is used in reconnaissance to identify sites vulnerable to UI redressing attacks.

## Description

Clickjacking exploits occur when a site lacks proper frame-busting headers like X-Frame-Options: DENY or SAMEORIGIN, allowing attackers to embed the site in an iframe and overlay invisible elements to trick users into unintended actions. This procedure targets public-facing web apps like https://factlink.com/, confirming vulnerability by inspecting response headers. Expected outcomes include header absence, enabling further exploitation steps. Prerequisites include basic command-line access and internet connectivity.

## Requirements

1. curl installed on the system
2. Network access to the target URL (e.g., https://factlink.com/)
3. Basic understanding of HTTP headers

## Defense

Defensive measures and detection strategies:

- Implement X-Frame-Options: DENY or SAMEORIGIN in server responses
- Use Content-Security-Policy (CSP) frame-ancestors directive
- Monitor for anomalous iframe embeddings via web application firewall (WAF) logs

## Objectives

1. Verify absence of frame protection headers
2. Assess clickjacking risk level
3. Document vulnerability for reporting

## Instructions

### Step 1: Fetch HTTP Headers

**Context**: Use curl to retrieve the HEAD response from the target site and inspect for X-Frame-Options.

**Command** ([[commands/curl-check-headers]]):
```bash
curl -I https://factlink.com/
```

> This command sends a HEAD request and outputs headers. Look for X-Frame-Options; its absence confirms the vulnerability. Expected output includes standard headers without the protection one.

### Step 2: Validate Header Absence

**Context**: Manually review the output or pipe to grep for confirmation.

**Command** ([[commands/curl-check-headers]]):
```bash
curl -I https://factlink.com/ | grep -i x-frame-options
```

> If no output, the header is missing. This step ensures accurate identification before proceeding to exploitation.

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

- [[clickjacking]]
- [[web-recon]]
