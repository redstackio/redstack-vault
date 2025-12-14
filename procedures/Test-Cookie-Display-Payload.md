---
tags:
  - xss
  - cookie-access
  - payload-testing
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands:
  - '[[commands/alert-document-cookie]]'
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 7f320a3a-9087-4071-9b34-71c7098825e2
created_at: '2025-12-13T23:55:06.834Z'
updated_at: '2025-12-13T23:55:06.834Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Test-Cookie-Display-Payload

## Summary

This procedure tests the XSS vulnerability by injecting a payload to display document cookies, assessing what user data can be accessed despite HttpOnly protections.

## Description

Building on the basic injection, this targets document.cookie to reveal session or tracking data. The vuln allows reflected execution, but HttpOnly flags block direct access to main session cookies. Use case: Evaluate exposure for phishing or token theft. Target: Same Acronis endpoint. Outcomes: Visible cookies in alert, informing escalation potential.

## Requirements

1. Confirmed basic XSS from prior step
2. Browser with dev tools to inspect cookies
3. Valid login flow

## Defense

Defensive measures and detection strategies:

- Set HttpOnly and Secure flags on sensitive cookies
- Use CSP to restrict script sources
- Log and alert on suspicious parameter values in redirects

## Objectives

1. Display accessible cookies
2. Identify non-HttpOnly data for theft
3. Mitigate risks via awareness of limitations

## Instructions

### Step 1: Craft Cookie Payload

**Context**: Modify alert to target cookies.

**Command** ([[commands/alert-document-cookie]]):

```javascript
javascript:alert(document.cookie)
```

> Alerts all accessible cookies. Expected: Popup with non-HttpOnly values; main session hidden.

### Step 2: Execute via Redirect

**Context**: Inject and trigger on login.

**Command** ([[commands/alert-document-cookie]]):

Full URL:

```url
https://portal.acronis.com/portal/login-callback?redirectUrl=javascript:alert(document.cookie)
```

> Follow login process. Success: Cookie alert post-redirect.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/alert-document-cookie]]

## Tools Used


## Tags

- [[xss]]
- [[cookie-access]]
