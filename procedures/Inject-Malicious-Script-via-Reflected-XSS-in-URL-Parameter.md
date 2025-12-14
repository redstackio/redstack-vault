---
tags:
  - xss
  - reflected-xss
  - script-injection
  - web-exploit
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands:
  - '[[commands/curl-fetch-xss-payload]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:25.276Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
id: dfc61611-07c9-4d00-851d-3f7a5fae4cf3
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Malicious-Script-via-Reflected-XSS-in-URL-Parameter

## Summary

This procedure exploits a reflected cross-site scripting (XSS) vulnerability by crafting a URL with a malicious JavaScript payload in a user-controlled parameter, causing the script to execute in the victim's browser upon page load. It is commonly used against web applications lacking proper input sanitization, such as search fields on public websites, to steal cookies or manipulate content.

## Description

In a reflected XSS attack, user input from a URL parameter is directly embedded into the HTML response without escaping, allowing attackers to inject and execute scripts. This procedure targets a U.S. Navy website where a parameter (e.g., 'q' in a search URL) reflects input. The attack requires no authentication and can be delivered via phishing links. Expected outcomes include JavaScript execution, enabling actions like cookie theft (e.g., `document.cookie`) or page defacement. Prerequisites include identifying the vulnerable endpoint through manual testing or fuzzing.

## Requirements

1. Public access to the target website (e.g., U.S. Navy site)
2. Knowledge of the vulnerable URL parameter (e.g., via exploring forms or URLs)
3. A web browser or tool like curl for testing payloads
4. Basic understanding of URL encoding for special characters in payloads

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and output encoding (e.g., HTML-escape user input)
- Deploy Content Security Policy (CSP) headers to restrict script execution
- Use Web Application Firewalls (WAFs) to detect and block common XSS payloads
- Monitor server logs for suspicious URL parameters containing script tags

## Objectives

1. Inject and reflect a malicious script to execute JavaScript in the browser
2. Demonstrate potential for data exfiltration, such as stealing session cookies
3. Highlight the vulnerability for reporting and remediation

## Instructions

### Step 1: Identify Vulnerable Parameter

**Context**: Navigate to the target website and test input fields or URL parameters to find one that reflects user input directly in the HTML response without sanitization.

**Instructions**: Enter test strings like "test<123>" in forms and check the page source for unescaped output.

### Step 2: Craft and Test Malicious Payload

**Context**: Create a simple JavaScript payload to verify execution, such as an alert box displaying cookies, and encode it for URL safety.

**Command** ([[commands/curl-fetch-xss-payload]]):
```bash
curl -G "https://navy-site.example.com/search" --data-urlencode "q=<script>alert(document.cookie)</script>"
```

> This command fetches the page with the injected payload. In a browser, the response will render and execute the script, showing an alert with cookie data. Expected output in curl is the HTML response containing the unescaped `<script>` tag; in browser, visual execution confirms success.

### Step 3: Validate Execution and Impact

**Context**: Load the crafted URL in a browser to confirm script execution and assess potential impacts like cookie access.

**Instructions**: Open `https://navy-site.example.com/search?q=%3Cscript%3Ealert(document.cookie)%3C/script%3E` and inspect for execution. Use developer tools to verify if the script runs in the context of the site.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/curl-fetch-xss-payload]]

## Tools Used


## Tags

- [[xss]]
- [[reflected-xss]]
- [[web]]
- [[injection]]
