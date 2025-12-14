---
tags:
  - clickjacking
  - iframe
  - single-url-test
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
updated_at: '2025-12-14T17:28:12.665Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 54d941fa-8665-47b1-ab1f-287d627e3523
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Reproduce-Clickjacking-Using-Iframe-for-Single-URL

## Summary

This alternative procedure uses a simple iframe in HTML to embed a single Semrush URL, verifying the site's susceptibility to clickjacking for targeted UI redressing.

## Description

For scenarios needing focus on one page, an iframe provides a straightforward way to frame content. Targeting https://semrush.com/ with dimensions 1247x800, this tests if the page loads without restrictions, enabling attacks where an invisible iframe overlays malicious content to capture clicks on sensitive elements like buttons or forms.

## Requirements

1. Text editor for HTML
2. Browser (Firefox v56 or Chrome)
3. Internet access

## Defense

Defensive measures and detection strategies:

- Set X-Frame-Options to block embedding
- CSP frame-ancestors 'none' to prevent iframes
- Scan for iframe usage in client-side code

## Objectives

1. Embed a single Semrush URL in an iframe
2. Confirm no cross-origin restrictions
3. Highlight simplicity of the attack vector

## Instructions

### Step 1: Create Iframe HTML

**Context**: Build a basic HTML page with an iframe sourcing the target URL.

Use this HTML:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Iframe Clickjacking Test</title>
</head>
<body>
    <iframe src="https://semrush.com/" width="1247" height="800"></iframe>
</body>
</html>
```

> Save as iframe.html. The iframe size mimics a full viewport for realistic testing.

### Step 2: Load and Observe

**Context**: Open the file to verify embedding.

Open iframe.html in the browser and check if the Semrush homepage loads inside the iframe.

> Expected: Page renders completely, allowing potential overlay for clickjacking.

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
- [[iframe]]
- [[web-exploit]]
