---
id: proc-uuid-2
name: Force CAPTCHA to Extract State Token
tags:
  - access-control
  - captcha-bypass
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:33:34.296Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Force CAPTCHA to Extract State Token

## Summary

This procedure manipulates the CAPTCHA in Remitly's MFA endpoint to trigger a token-leaking flow, extracting the victim's state_token and JWT reliably.

## Description

The /orchestrator/v1/mfa/start endpoint has improper access control, allowing CAPTCHA token manipulation to force an alternative response path that leaks state_token without adequate validation or rate limiting. This is crucial for obtaining complete victim session data. Use a proxy to modify requests post-CAPTCHA trigger.

## Requirements

1. Proxy interception active
2. Victim's email
3. Ability to solve CAPTCHAs manually

## Defense

Defensive measures and detection strategies:

- Validate CAPTCHA tokens server-side before processing any MFA flows
- Implement rate limiting on MFA starts and CAPTCHA submissions
- Monitor for incomplete or malformed CAPTCHA tokens in logs

## Objectives

1. Trigger CAPTCHA display via token manipulation
2. Solve and resubmit to leak state_token
3. Combine with prior JWT for full session hijack

## Instructions

### Step 1: Submit Initial MFA Request

**Context**: Start MFA for victim to reach CAPTCHA.

POST to /orchestrator/v1/mfa/start with victim's email via proxy.

> Response may include CAPTCHA challenge.

### Step 2: Modify CAPTCHA Token

**Context**: Force alternative flow by altering token.

In the resubmit request, remove most of the CAPTCHA token value (e.g., keep only prefix).

> This forces CAPTCHA redisplay; solve it manually in browser.

### Step 3: Resubmit Solved CAPTCHA

**Context**: Obtain leaked tokens post-solve.

Forward the request with solved CAPTCHA and full payload.

> Expected: Response with state_token and JWT.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[access-control]]
- [[captcha-bypass]]
