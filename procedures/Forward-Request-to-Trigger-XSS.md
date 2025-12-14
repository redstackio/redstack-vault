---
tags:
  - xss-execution
  - cookie-theft
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands:
  - '[[commands/inject-xss-payload-img-onerror]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:19.861Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: a8342c57-00cb-4b9b-875f-c8233e2dbe04
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Forward-Request-to-Trigger-XSS

## Summary

This procedure releases the modified request in Burp Suite to send it to the server, resulting in the reflection and execution of the XSS payload, demonstrating cookie theft via alert.

## Description

Upon forwarding, the server reflects the payload in the response HTML, triggering onerror in the img tag to execute alert(document.cookie). Since cookies lack HttpOnly, session data is exposed. This confirms the vulnerability and highlights impacts like theft, redirects, and phishing in the DoD environment.

## Requirements

1. Modified request ready in Burp
2. Browser session active
3. Monitoring for popups

## Defense

Defensive measures and detection strategies:

- Output encoding for all user inputs
- Browser-based detection of unexpected alerts
- Session monitoring for anomalous activity

## Objectives

1. Execute JS in victim's context
2. Capture and display stolen cookies
3. Validate vulnerability for reporting

## Instructions

### Step 1: Review and Forward

**Context**: Ensure payload integrity before sending.

**Command** (Burp Action):

Click 'Forward' in Burp Proxy.

> Request transmits. Expected output: Server response loads in browser.

### Step 2: Observe Execution

**Context**: Watch for payload trigger using [[commands/inject-xss-payload-img-onerror]].

**Command** (Expected JS):
```javascript
<img src=x onerror=alert(document.cookie)>
```

> Alert pops up. Expected output: Dialog shows cookie string, e.g., sessionid=abc123.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/inject-xss-payload-img-onerror]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- xss-execution
- cookie-theft
