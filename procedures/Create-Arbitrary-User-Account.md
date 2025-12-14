---
id: proc-005
tags:
  - account-creation
  - dos
type: procedure
tools:
  - '[[tools/token-dev]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/submit-jwt-via-browser-console]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Create Account]]'
updated_at: '2025-12-14T17:31:42.863Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques:
  - '[[Local Account]]'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Create Account]]'
---
# Create-Arbitrary-User-Account

## Summary

This alternative procedure uses the same endpoint to register new users with arbitrary details, bypassing validation and enabling DoS or malicious profile injection.

## Description

By submitting unsigned JWTs with custom payloads, attackers can create unlimited 'Customer' role accounts, injecting untrusted data visible to admins and potentially overwhelming the user database.

## Requirements

1. Generated unsigned JWT with new details
2. Target endpoint access

## Defense

Defensive measures and detection strategies:

- Cap user registrations per IP/time
- Validate all user inputs server-side
- Review new accounts for anomalies

## Objectives

1. Establish persistence via new account
2. Inject malicious data
3. Perform DoS through mass creation

## Instructions

### Step 1: Generate New JWT

**Context**: Create token with arbitrary email and role.

**Command** (Tool Usage):

Use [[tools/token-dev]] with payload {"email": "fake@example.com", "role": "Customer"}.

> Expected output: New unsigned token.

### Step 2: Submit for Registration

**Context**: POST to endpoint as in hijack.

**Command** ([[commands/submit-jwt-via-browser-console]]):
```javascript
// Same as hijack but with new token
fetch(url, { /* ... */ body: newToken });
```

> Expected output: Success response; new account created.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Create Account]] Create Account

### Sub-Techniques

- [[Local Account]] Local Account

## Commands Used

- [[commands/submit-jwt-via-browser-console]]

## Tools Used

- [[tools/token-dev]]

## Tags

- account-creation
- dos
