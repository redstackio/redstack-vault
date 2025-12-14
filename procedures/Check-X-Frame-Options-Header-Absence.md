---
id: proc-check-xframe-absence
tags:
  - clickjacking
  - header-check
  - web-recon
type: procedure
tools:
  - '[[tools/Browser-Unspecified]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:04.839Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Check-X-Frame-Options-Header-Absence

## Summary

This procedure inspects the HTTP response headers of a target website, such as yelp.com, to determine if the X-Frame-Options header is missing, which would allow the site to be embedded in iframes from external domains, enabling clickjacking attacks.

## Description

In a typical web security assessment, the absence of X-Frame-Options exposes sites to UI redressing attacks where malicious pages overlay invisible iframes to capture user interactions. This procedure targets public-facing web applications and uses browser developer tools to examine headers without requiring specialized software. Prerequisites include internet access and a modern browser. Expected outcomes confirm framing permissiveness, highlighting risks like unauthorized clicks on hidden elements.

## Requirements

1. Web browser with developer tools (e.g., Chrome DevTools)
2. Public access to the target URL (e.g., http://yelp.com)
3. Basic knowledge of HTTP headers

## Defense

Defensive measures and detection strategies:

- Implement X-Frame-Options: DENY or SAMEORIGIN in server responses
- Monitor for anomalous iframe embeddings via web application firewalls (WAF)
- Use Content-Security-Policy (CSP) frame-ancestors directive as an alternative

## Objectives

1. Verify absence of frame protection headers
2. Assess initial vulnerability to clickjacking
3. Gather evidence for reporting

## Instructions

### Step 1: Navigate to Target

**Context**: Access the target site to trigger header inspection.

Open a web browser and navigate to http://yelp.com.

> The site loads normally; no special commands needed.

### Step 2: Inspect Headers

**Context**: Use developer tools to view network responses.

Right-click on the page, select "Inspect", go to the Network tab, reload the page, and select the main document request to view response headers.

> Look for X-Frame-Options; if absent, the site is frameable. Expected output: Headers list without X-Frame-Options.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Browser-Unspecified]]

## Tags

- [[clickjacking]]
- [[web-recon]]
