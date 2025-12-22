---
tags:
  - xss
  - recon
  - web
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-test-xss]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T03:15:30.971Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 42aba199-8b13-4d01-98de-5968a6216572
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Identify Vulnerable XSS Parameter

## Summary

This procedure involves scanning and testing web application parameters on sites like developer.gm.com to identify those vulnerable to cross-site scripting by checking for lack of input sanitization, allowing reflected script injection.

## Description

In the context of the developer.gm.com XSS vulnerability, attackers probe URL parameters (e.g., query strings in search or form inputs) to see if user input is reflected back into the HTML response without proper escaping. This enables JavaScript execution when a victim visits a crafted URL. Prerequisites include access to a web proxy tool and basic knowledge of HTML/JS. Expected outcomes: Confirmation of a reflectable parameter leading to alert() execution.

## Requirements

1. Web browser with developer tools
2. Proxy tool like Burp Suite for request interception
3. Direct network access to the target website

## Defense

Defensive measures and detection strategies:

- Implement content security policy (CSP) to block inline scripts
- Use input validation and output encoding (e.g., htmlspecialchars in PHP)
- Monitor for anomalous JavaScript in logs or WAF alerts

## Objectives

1. Discover unsanitized parameters
2. Verify script execution potential
3. Map vulnerable endpoints

## Instructions

### Step 1: Intercept and Test Parameter Reflection

**Context**: Use a proxy to capture requests and inject test payloads into parameters.

**Command** ([[commands/curl-test-xss]]):
```bash
curl -X GET "https://developer.gm.com/search?query=%3Cscript%3Ealert('XSS')%3C/script%3E" -v
```

> This command sends a URL-encoded XSS payload to a potential query parameter. Expected output: Response HTML containing the unescaped <script> tag, visible in the browser as an alert if loaded.

### Step 2: Verify Execution in Browser

**Context**: Load the crafted URL in a browser to confirm JavaScript runs.

**Instructions**: Paste the URL with payload into the browser address bar or use Burp's Repeater to simulate. Check for alert popup.

> No specific command; use browser dev tools (F12) to inspect response for reflection.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used

- [[commands/curl-test-xss]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- xss
- web-testing
