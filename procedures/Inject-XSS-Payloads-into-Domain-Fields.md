---
tags:
  - xss
  - payload-injection
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/javascript-alert-document-domain]]'
  - '[[commands/javascript-alert-document-domain-semicolon]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:29:20.268Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: a17690de-ff72-47c7-8b6d-b685aeddf138
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-XSS-Payloads-into-Domain-Fields

## Summary

This procedure involves entering JavaScript payloads into the Custom Domain and Demo Domain fields of the Federalist site settings to store malicious code that executes later, exploiting lack of sanitization for javascript: pseudoprotocols.

## Description

The Federalist admin panel fails to sanitize inputs in domain fields, allowing storage of XSS payloads. An attacker injects 'javascript:alert(document.domain)' into Custom Domain and a variant with semicolon into Demo Domain to evade checks. This stores the script server-side, triggering in other admins' browsers during interactions like viewing sites, potentially leading to session theft or CSRF bypass in the same-origin context.

## Requirements

1. Admin access to site settings page (/sites/<siteid>/settings)
2. Browser for form input
3. Knowledge of target site ID

## Defense

Defensive measures and detection strategies:

- Sanitize all inputs with allowlists for domain fields (e.g., validate against valid TLDs)
- Implement Content Security Policy (CSP) to block inline JavaScript execution
- Log and review unusual inputs in admin fields for javascript: patterns

## Objectives

1. Store XSS payload in Custom Domain field
2. Store variant payload in Demo Domain to bypass checks
3. Ensure payloads persist without immediate execution

## Instructions

### Step 1: Enter Payload in Custom Domain

**Context**: Inject basic javascript: payload into the Custom Domain field.

**Command** ([[commands/javascript-alert-document-domain]]):

Enter the following in the Custom Domain field:

```javascript
javascript:alert(document.domain)
```

> This payload uses the pseudoprotocol to execute an alert showing the domain upon trigger. Expected output: Field accepts input without error.

### Step 2: Enter Variant Payload in Demo Domain

**Context**: Use a semicolon to differentiate and bypass any duplication validation.

**Command** ([[commands/javascript-alert-document-domain-semicolon]]):

Enter the following in the Demo Domain field:

```javascript
javascript:alert(document.domain);
```

> The semicolon evades basic checks, storing the payload for later demo site trigger. Expected output: Field populated successfully.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/javascript-alert-document-domain]]
- [[commands/javascript-alert-document-domain-semicolon]]

## Tools Used


## Tags

- xss
- payload-injection
