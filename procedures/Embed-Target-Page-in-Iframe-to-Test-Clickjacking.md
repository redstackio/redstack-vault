---
tags:
  - clickjacking
  - web
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
updated_at: '2025-12-14T17:28:12.961Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: b96131c3-5f2a-4332-a6d7-bc4a24c4baff
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Embed-Target-Page-in-Iframe-to-Test-Clickjacking

## Summary

This procedure tests for clickjacking vulnerabilities by attempting to embed the target page in an iframe from an external site, confirming if frame protections like Content-Security-Policy (CSP) frame-ancestors or X-Frame-Options are absent.

## Description

Clickjacking involves tricking users into clicking on hidden or overlaid elements by embedding the target in an iframe. In this case, the WordPress Foundation donation page at https://wordpressfoundation.org/donate/ lacks protections, allowing full embedding. The procedure creates a basic HTML test page and loads it to verify the vulnerability, setting the stage for exploitation like donation redirection.

## Requirements

1. Web browser (e.g., Chrome, Firefox)
2. Text editor to create HTML file
3. Local file access or simple web server to host the test page

## Defense

Defensive measures and detection strategies:

- Implement X-Frame-Options: DENY or SAMEORIGIN header
- Use CSP with frame-ancestors 'self' directive
- Monitor for unusual iframe embeddings via web application firewall (WAF)

## Objectives

1. Confirm the target page can be iframed without restrictions
2. Identify absence of frame-busting headers
3. Validate setup for further exploitation

## Instructions

### Step 1: Create Test HTML File

**Context**: Build a simple HTML page that embeds the target donation page in a full-sized iframe to check for loading success.

Create a file named `test-iframe.html` with the following content:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Clickjacking Test</title>
</head>
<body>
    <iframe src="https://wordpressfoundation.org/donate/" height="1200px" width="1920px" frameborder="0px"></iframe>
</body>
</html>
```

> This embeds the donation page at full viewport size. Save and open `test-iframe.html` in a browser.

### Step 2: Verify Embedding

**Context**: Load the test page and inspect for successful rendering, checking browser console for any blocking errors.

Open the file in a browser and observe if the donation page loads completely.

> Expected: Full page renders without CSP violations or frame denials. Check developer tools (F12) for errors like "Refused to display in a frame" – absence confirms vulnerability.

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
- [[web]]
- [[iframe]]
