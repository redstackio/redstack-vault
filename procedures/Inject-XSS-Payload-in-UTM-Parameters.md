---
tags:
  - xss
  - reflected-xss
  - payload-injection
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
updated_at: '2025-12-14T00:11:09.425Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 3df8f4ff-85aa-4b93-95a4-5e7e341f7610
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-XSS-Payload-in-UTM-Parameters

## Summary

This procedure exploits insufficient input validation in URL-based UTM tracking parameters to inject and reflect malicious JavaScript payloads, resulting in arbitrary code execution in the victim's browser, such as displaying alerts to confirm the vulnerability.

## Description

In scenarios like marketing tracking on e-commerce sites, UTM parameters (utm_source, utm_medium, utm_campaign) are appended to URLs and reflected back into the HTML without proper sanitization. An attacker can URL-encode XSS payloads and trick users into visiting the malicious link, leading to script execution. This is particularly effective on main domains where session cookies are accessible. Prerequisites include a vulnerable endpoint and a web browser for testing; no authentication is needed as it's reflected.

## Requirements

1. Access to a web browser (e.g., Firefox or Internet Explorer) for payload testing
2. Knowledge of the target URL structure, such as https://www.instacart.com/green-zebra-grocery
3. Basic URL encoding skills to obfuscate payloads

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and output encoding for all URL parameters using libraries like OWASP ESAPI
- Deploy Content Security Policy (CSP) to restrict inline scripts and iframes
- Monitor for anomalous JavaScript execution in web logs or use WAF rules to block common XSS patterns

## Objectives

1. Confirm reflected XSS by executing a simple alert script
2. Demonstrate potential for more severe payloads like keyloggers
3. Validate vulnerability across browsers for impact assessment

## Instructions

### Step 1: Construct Malicious URL

**Context**: Build a URL with URL-encoded XSS payloads targeting the UTM parameters to break out of any HTML context and inject a script tag.

No specific command; manually construct the URL:

```url
https://www.instacart.com/green-zebra-grocery?utm_source=%3E%22%27%3E<script>alert(/Hussain/)</script>&utm_medium=%22%27%3E<script>alert(/XSS/)</script>&utm_campaign=%22%27%3E<script>alert(/injection/)</script>
```

> This URL encodes payloads like ">'><script>alert(/Hussain/)</script> to close HTML tags and inject the script. The %3E represents '>', ensuring reflection triggers execution.

### Step 2: Test Payload Execution

**Context**: Visit the constructed URL in a browser to observe reflection and execution.

Open the URL in Firefox or Internet Explorer.

> Expected behavior: Three alerts pop up displaying 'Hussain', 'XSS', and 'injection'. Inspect the page source to confirm unsanitized reflection in the HTML.

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
