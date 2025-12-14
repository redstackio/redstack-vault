---
id: proc-dom-xss-url-craft-191416
tags:
  - xss
  - dom-based-xss
  - url-injection
  - script-execution
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:41.235Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Initial Access]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
---
# Craft-Malicious-URL-for-DOM-Based-XSS

## Summary

This procedure demonstrates exploiting a DOM-based Cross-Site Scripting (XSS) vulnerability by crafting a malicious URL that injects and executes arbitrary JavaScript in the victim's browser upon page load. It targets web applications with poor URL parameter sanitization, such as those on public-facing DoD websites, leading to potential disclosure of sensitive browser data like cookies or unauthorized content changes.

## Description

DOM-based XSS occurs when client-side scripts process URL data (e.g., query parameters, fragments) without proper validation, allowing attackers to inject executable code into the Document Object Model (DOM). In this scenario, a U.S. Department of Defense website reflected URL inputs directly into JavaScript contexts, enabling script execution. The attack requires no server interaction beyond loading the page; execution is purely client-side. Prerequisites include identifying a vulnerable parameter (e.g., via manual testing or tools like Burp Suite) and encoding payloads to evade filters. Expected outcomes: script execution confirming the vuln, with real-world impacts like session token theft via exfiltration to an attacker-controlled server.

## Requirements

1. Access to a web browser with developer tools for testing and encoding
2. Knowledge of the target URL structure (e.g., a search or redirect page on the DoD site)
3. Victim interaction: The target user must visit the crafted URL (e.g., via phishing)

## Defense

Defensive measures and detection strategies:

- Implement Content Security Policy (CSP) with strict script-src directives to block inline scripts
- Sanitize and validate all URL inputs on the client-side using libraries like DOMPurify before DOM insertion
- Monitor for anomalous JavaScript execution via browser security tools or Web Application Firewalls (WAFs) scanning for XSS payloads
- Educate users on phishing and URL verification

## Objectives

1. Inject and execute JavaScript in the victim's browser context
2. Access or exfiltrate browser-stored data like cookies
3. Demonstrate vulnerability for reporting and remediation

## Instructions

### Step 1: Identify Vulnerable Endpoint

**Context**: Locate a page where URL parameters or fragments are used in client-side JavaScript (e.g., document.write(location.hash) or innerHTML assignment from query params).

No command needed; use browser navigation to test the base URL (e.g., http://dod-website.example.com/search).

**Expected Output**: Page loads normally, but inspect source for unsanitized URL usage.

### Step 2: Craft and Encode Payload

**Context**: Create a JavaScript payload for execution, such as alerting cookies to prove control. Encode to bypass URL parsing issues.

Use browser dev tools or manual construction:

```javascript
// Payload: <script>alert(document.cookie)</script>
// URL-encoded: %3Cscript%3Ealert(document.cookie)%3C%2Fscript%3E
// Full example URL: http://dod-website.example.com/search?param=%3Cscript%3Ealert(document.cookie)%3C%2Fscript%3E
```

For DOM-based (often hash-based): http://dod-website.example.com/page#<script>alert(1)</script>

**Expected Output**: Encoded string ready for URL insertion.

### Step 3: Test Execution

**Context**: Deliver the URL to a victim or test environment to trigger script execution.

Navigate to the crafted URL in a browser.

```bash
# Manual browser test (no CLI; simulate with curl for fetch verification if needed)
# curl 'http://dod-website.example.com/search?param=%3Cscript%3Ealert(document.cookie)%3C%2Fscript%3E' --verbose
```

> Note: curl fetches but doesn't execute JS; use a real browser for validation. Success: Alert box appears with cookie data.

**Expected Output**: Malicious script runs, altering DOM or logging data.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Initial Access]]

### Techniques

- [[JavaScript]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[dom-based-xss]]
- [[web]]
- [[script-injection]]
