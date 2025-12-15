---
id: proc-check-headers-clickjacking
name: Check-Security-Headers-for-Clickjacking
tags:
  - clickjacking
  - headers
  - recon
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
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T17:28:12.787Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Check-Security-Headers-for-Clickjacking

## Summary

This procedure inspects the HTTP security headers of a target web application to identify clickjacking vulnerabilities, specifically checking for improper or deprecated X-Frame-Options configurations that allow unauthorized framing.

## Description

Clickjacking vulnerabilities arise when sites fail to prevent embedding in iframes from external domains, enabling attackers to overlay invisible elements and trick users into clicking on sensitive UI components. This procedure uses curl to fetch response headers from exchangemarketplace.com, focusing on X-Frame-Options. The site's use of ALLOW-FROM https://exchangemarketplace.com is deprecated in modern browsers (e.g., Chrome 77+, Firefox 65+), rendering it ineffective and allowing arbitrary framing. Prerequisites include command-line access and internet connectivity; expected outcomes include confirmation of framable status, paving the way for PoC development.

## Requirements

1. curl installed on the system
2. Network access to the target URL (https://exchangemarketplace.com)
3. Basic knowledge of HTTP headers

## Defense

Defensive measures and detection strategies:

- Implement strict X-Frame-Options: DENY or SAMEORIGIN
- Use Content-Security-Policy (CSP) frame-ancestors directive to restrict framing
- Monitor for anomalous iframe embeddings in web traffic logs

## Objectives

1. Verify X-Frame-Options header value
2. Confirm vulnerability to clickjacking
3. Gather evidence for exploitation planning

## Instructions

### Step 1: Fetch HTTP Headers

**Context**: Retrieve the response headers to inspect frame protection settings.

**Command** ([[commands/curl-check-headers]]):
```bash
curl -I https://exchangemarketplace.com
```

> This command sends a HEAD request and outputs headers. Look for `X-Frame-Options: ALLOW-FROM https://exchangemarketplace.com`, indicating the vulnerability. Expected output includes full header list; success if no DENY/SAMEORIGIN is present.

### Step 2: Analyze Results

**Context**: Manually review the output for deprecated configurations.

No command needed; parse the curl output to confirm the header value is ineffective.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Gather Victim Host Information]]

### Sub-Techniques



## Commands Used

- [[commands/curl-check-headers]]

## Tools Used



## Tags

- [[clickjacking]]
- [[web-recon]]
