---
tags:
  - xss
  - execution
  - javascript
type: procedure
tools:
  - '[[tools/Safari]]'
  - '[[tools/Chrome]]'
  - '[[tools/Firefox]]'
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:26:22.208Z'
skill_level: beginner
impact_level: high
detection_risk: medium
sub_techniques: []
id: b02aee26-d452-4ae3-a405-a9db78ece283
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger Reflected XSS via Browser

## Summary

This procedure loads the payload-injected URL in a web browser to trigger the reflected XSS, resulting in arbitrary JavaScript execution within the victim's session context on the Glassdoor site.

## Description

Upon loading the tampered URL, the server reflects the unsanitized path into the HTML, allowing the injected script to execute. The example payload triggers an alert, but in a real attack, it could exfiltrate cookies via `document.cookie` or redirect to a phishing site. This demonstrates the vulnerability's potential for session hijacking or data theft.

## Requirements

1. The modified URL from the injection procedure.
2. A modern web browser supporting JavaScript.
3. Optional: Developer tools to inspect execution.

## Defense

Defensive measures and detection strategies:

- Deploy browser-based protections like XSS filters.
- Use HTTP-only cookies to prevent theft.
- Scan for XSS patterns in client-side logs or error reports.

## Objectives

1. Execute the injected JavaScript payload.
2. Verify impact through alert or console output.
3. Simulate real-world effects like cookie access.

## Instructions

### Step 1: Load Tampered URL

**Context**: Enter the modified URL into the browser's address bar and navigate to it, triggering the reflection and execution.

Use any of the following browsers:

```url
https://www.glassdoor.co.in/FAQ/Mic%22%3e%3cimg%20onerro%3d%3e%3cimg%20src%3dx%20onerror%3dalert%601%60%3erosoft-Question-FAQ200086-E1651.htm?countryRedirect=true
```

> The page loads, and the onerror handler in the img tag executes the alert('1'). Check the browser console for any errors and confirm the alert dialog appears.

### Step 2: Verify Execution

**Context**: Inspect the page source or use developer tools to confirm the payload reflection.

Open browser dev tools (F12) and reload the page.

> Look for the injected `<img src=x onerror=alert`1`">` in the HTML source, confirming lack of sanitization.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Safari]]
- [[tools/Chrome]]
- [[tools/Firefox]]

## Tags

- [[xss]]
- [[Execution]]
- [[JavaScript]]
