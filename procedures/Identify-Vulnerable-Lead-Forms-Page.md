---
tags:
  - recon
  - web
  - clickjacking
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:28:12.546Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: a22efe1f-0a1b-4d63-a833-0218167c4c63
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Identify Vulnerable Lead Forms Page

## Summary

This procedure involves locating and verifying web endpoints vulnerable to clickjacking, specifically targeting VK.com's /lead_forms_app.php which handles user application forms including phone and email submissions without frame-busting protections.

## Description

In a clickjacking attack, the first step is reconnaissance to identify pages that can be embedded in iframes from external domains. For VK.com, the 'Form for collecting applications' feature at /lead_forms_app.php lacks X-Frame-Options headers or JavaScript frame-busters, allowing attackers to frame the page. This procedure confirms the endpoint's vulnerability by testing iframe embedding, setting the stage for UI manipulation to steal user data. Prerequisites include basic web knowledge and access to a browser for testing; no special credentials are needed as the vulnerability affects any embeddable page.

## Requirements

1. Web browser for manual testing
2. Local web server or HTML file editor to create test iframes
3. Internet access to VK.com

## Defense

Defensive measures and detection strategies:

- Implement X-Frame-Options: DENY or SAMEORIGIN headers on all pages
- Use Content-Security-Policy (CSP) with frame-ancestors directive to restrict framing
- Monitor for unusual iframe embedding attempts via web application firewall (WAF) logs

## Objectives

1. Discover unprotected endpoints handling sensitive form submissions
2. Verify iframe embeddability to assess clickjacking risk
3. Document technical details for exploitation planning

## Instructions

### Step 1: Locate the Endpoint

**Context**: Search for form-handling pages in the target application, focusing on features like lead generation that collect personal info.

For VK.com, navigate to the 'Form for collecting applications' and identify /lead_forms_app.php as the handler.

**Expected Output**: Endpoint URL confirmed, e.g., https://vk.com/lead_forms_app.php.

### Step 2: Test Iframe Embedding

**Context**: Create a simple HTML test to check if the page can be framed externally.

Create an HTML file with the following iframe:

```html
<!DOCTYPE html>
<html>
<head><title>Test</title></head>
<body>
<iframe src="https://vk.com/lead_forms_app.php" width="800" height="600"></iframe>
</body>
</html>
```

Open the file in a browser and observe if the VK page loads without errors or blanking.

**Expected Output**: The form page renders fully inside the iframe, showing input fields for phone and email.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[recon]]
- [[web]]
- [[clickjacking]]
