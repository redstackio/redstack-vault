---
id: proc-embed-iframe-001
tags:
  - clickjacking
  - iframe-embedding
  - web
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
updated_at: '2025-12-14T17:28:12.859Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Embed-Target-in-Malicious-Iframe

## Summary

This procedure creates an HTML page that embeds the target website (https://topechelon.com/) in an iframe, exploiting the absence of X-Frame-Options or CSP frame-ancestors to load the site without restrictions, setting the stage for clickjacking deception.

## Description

In a clickjacking attack, the first step is to embed the vulnerable site in an iframe on a malicious page. Since https://topechelon.com/ lacks anti-framing headers, the site loads fully, allowing attackers to overlay elements and trick users. This targets WordPress sites and leads to potential phishing or action hijacking for logged-in users.

## Requirements

1. Text editor (e.g., VS Code) to create HTML file
2. Local browser to test iframe loading
3. Internet access to the target URL

## Defense

Defensive measures and detection strategies:

- Implement X-Frame-Options: DENY or SAMEORIGIN header
- Use CSP with frame-ancestors 'self'
- Monitor for unusual iframe embeddings via WAF logs

## Objectives

1. Confirm the site can be framed externally
2. Prepare iframe for overlay deception
3. Validate no blocking occurs

## Instructions

### Step 1: Create Basic HTML with Iframe

**Context**: Build a simple page to embed the target, ensuring full load without errors.

No specific command; manually create the file.

```html
<!DOCTYPE html>
<html>
<head><title>Test Page</title></head>
<body>
<iframe src="https://topechelon.com/" frameborder="0" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
</body>
</html>
```

> Save as index.html and open in browser. The target site should load completely.

### Step 2: Verify Iframe Functionality

**Context**: Interact with the iframe to ensure clicks and navigation work as expected.

No command; manual testing.

> Click elements in the iframe; navigation should occur within the frame without escaping.

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
- [[web-exploitation]]
