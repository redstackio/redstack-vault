---
tags:
  - clickjacking
  - web-testing
  - iframe
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:28:04.593Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: 9e3fcb1f-57a0-4b8e-bbb9-6beb01ad6c01
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Test-for-ClickJacking-Susceptibility-on-Webpage

## Summary

This procedure tests whether a target webpage can be embedded in an iframe from an external domain, revealing potential ClickJacking vulnerabilities due to missing protections like X-Frame-Options headers. It is primarily used in web security assessments to identify sites susceptible to UI redressing attacks.

## Description

ClickJacking, or UI Redressing, involves tricking users into clicking on hidden elements by overlaying invisible iframes of legitimate sites on malicious pages. This procedure simulates basic framing to check for restrictions. In the Yelp case, the homepage at https://www.yelp.com/ loads without issues, allowing attackers to hijack user interactions for actions like form submissions or data entry. Prerequisites include a web browser and basic HTML knowledge; no special tools are needed.

## Requirements

1. Web browser with developer tools (e.g., Chrome DevTools to inspect headers)
2. Internet access to the target URL
3. Local file system access to create test HTML files

## Defense

Defensive measures and detection strategies:

- Implement X-Frame-Options: DENY or SAMEORIGIN headers to block framing
- Use Content-Security-Policy (CSP) frame-ancestors directive to restrict embedding domains
- Monitor for anomalous iframe embeddings via web application firewalls (WAFs)

## Objectives

1. Verify if the target site can be iframed externally
2. Identify missing security headers
3. Assess potential for UI redressing attacks

## Instructions

### Step 1: Create Basic Iframe Test File

**Context**: Build a simple HTML file to attempt embedding the target URL in an iframe and observe if it loads.

Create a file named test-iframe.html with the following content:

```html
<!DOCTYPE html>
<html>
<head><title>ClickJacking Test</title></head>
<body>
<iframe src="https://www.yelp.com/" width="500" height="500"></iframe>
</body>
</html>
```

> This embeds the Yelp homepage. Open the file in a browser; successful load indicates vulnerability.

### Step 2: Inspect for Blocking Headers

**Context**: Use browser tools to check response headers for frame protections.

Load the target URL directly, open DevTools (F12), go to Network tab, reload, and select the request. Look for X-Frame-Options or CSP headers.

> Absence of restrictive headers confirms susceptibility. For Yelp, no such headers are present.

### Step 3: Test Cross-Origin Framing

**Context**: Ensure the iframe works from a different origin (local file vs. remote site).

Host the test HTML on a local server (e.g., Python's http.server) and access via http://localhost:8000/test-iframe.html.

> If the iframe loads, the site is vulnerable to external framing.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[clickjacking]]
- [[web-vulnerability]]
