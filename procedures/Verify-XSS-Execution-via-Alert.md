---
id: proc-uuid-3
tags:
  - xss
  - verification
  - javascript
type: procedure
tools:
  - '[[tools/marked]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/observe-xss-trigger]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:07.852Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
---

# Verify-XSS-Execution-via-Alert

## Summary

This procedure confirms the XSS vulnerability by triggering the injected JavaScript payload, observing execution through a browser alert, validating the sanitization bypass in react-marked-markdown.

## Description

After rendering, the malicious link's href executes on user interaction or parsing. This step tests for alert popup, proving arbitrary code execution. In real scenarios, this could lead to session hijacking or phishing via stolen cookies/data.

## Requirements

1. Rendered component from previous procedure
2. Open browser tab with the app loaded
3. No additional tools; uses built-in browser features
4. Console access for error checking

## Defense

Defensive measures and detection strategies:

- Enable strict CSP headers to forbid javascript: URLs
- Audit rendered DOM for suspicious hrefs using tools like OWASP ZAP
- Log and alert on unexpected JavaScript executions in web apps

## Objectives

1. Trigger the payload to execute JavaScript
2. Validate vulnerability impact
3. Document success for reporting

## Instructions

### Step 1: Interact with Rendered Link

**Context**: Click the link to invoke the href handler.

**Command** ([[commands/observe-xss-trigger]]):
```javascript
// No explicit command; simulate click or auto-parse
document.querySelector('a[href^="javascript:"]').click();
```

> Run in browser console if needed. Expected output: Alert box with "1" appears.

### Step 2: Inspect and Confirm

**Context**: Verify the execution via dev tools.

**Command** (Console inspection):
```javascript
console.log(document.querySelector('a').getAttribute('href'));
```

> Expected output: Logs "javascript: alert`1`", confirming unsanitized href.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/observe-xss-trigger]]

## Tools Used

- [[tools/marked]]

## Tags

- xss
- verification
- javascript

