---
id: proc-intercept-modify-signup
tags:
  - saml
  - bypass
  - http-modify
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/hackerone-signup-bypass]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:30:58.363Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Intercept and Modify Signup Request

## Summary

This procedure uses an intercepting proxy to modify the HackerOne signup request by appending trailing control characters (%0d%0a) to the email parameter, bypassing SAML domain enforcement and creating an unauthorized account with a restricted domain.

## Description

The attack targets the POST /users endpoint where domain checks fail to normalize trailing characters, preventing the SSO redirect. This is executed in a web environment with SAML/SSO. Prerequisites: Burp Suite configured as proxy, prior observation of standard signup redirect. Outcomes include account creation without SSO enforcement.

## Requirements

1. Intercepting proxy like Burp Suite
2. Knowledge of the signup request format
3. Target endpoint access (hackerone.com/users)

## Defense

Defensive measures and detection strategies:

- Normalize and strip control characters (e.g., %0d%0a) from input parameters before validation
- Log and alert on anomalous request parameters in auth flows
- Use strict email validation regex that ignores trailing whitespace/control chars

## Objectives

1. Bypass SAML redirect for restricted domains
2. Create account with prohibited email
3. Enable subsequent verification and access

## Instructions

### Step 1: Intercept Request

**Context**: Configure Burp Suite to intercept traffic from the browser during signup submission.

**Command** (No direct command; use Burp UI):

Intercept the POST /users request in Burp Suite Proxy > Intercept tab.

> Observe the raw request with user[email]=test@hackerone.com.

### Step 2: Modify and Forward

**Context**: Append %0d%0a to the email parameter to evade normalization.

**Command** ([[commands/hackerone-signup-bypass]]):

```bash
curl -X POST https://hackerone.com/users \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'user[name]=Test User&user[username]=testuser&user[email]=test@hackerone.com%0d%0a&user[password]=password123&user[password_confirmation]=password123'
```

> Forward the modified request. Expected output: {"redirect_path":"/users/sign_in","errors":{}}, confirming bypass.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used

- [[commands/hackerone-signup-bypass]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- saml
- bypass
- http-modify
