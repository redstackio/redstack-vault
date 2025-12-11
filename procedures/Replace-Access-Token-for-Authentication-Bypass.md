---
tags:
  - authentication-bypass
  - token-manipulation
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/reverb-facebook-login-post]]'
platforms:
  - iOS
  - Web
techniques:
  - '[[Valid Accounts]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: e295a88f-08c9-45a6-951b-1d7317396a0d
created_at: '2025-12-11T06:10:15.369Z'
updated_at: '2025-12-11T06:10:15.369Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1078]]'
---
# Replace Access Token for Authentication Bypass

## Summary

This procedure replaces the fb_token in the intercepted request with one from another Facebook app to achieve authentication bypass and account takeover on Reverb.com.

## Description

Building on intercepted traffic, modify the fb_token to use a token from apps like Lyst or Letgo. This exploits the lack of app-specific validation, allowing login as the associated user. Applicable in OAuth misconfiguration scenarios, with outcomes including full access to victim accounts.

## Requirements

1. Intercepted request from prior step
2. Valid Facebook access token from another app linked to the target user
3. Burp Suite for request modification and sending

## Defense

Defensive measures and detection strategies:

- Validate token's app ID matches the expected value on server-side
- Implement token introspection with Facebook API to verify issuance
- Log and alert on logins with mismatched token metadata

## Objectives

1. Substitute fb_token with external one
2. Send modified request to bypass auth
3. Achieve account takeover

## Instructions

### Step 1: Obtain External Token

**Context**: Acquire a Facebook access token from another integrated app associated with the victim.

Obtain the token via compromise of another app (e.g., Lyst or Letgo).

> Ensure the token is valid and linked to the target user's Facebook account.

### Step 2: Modify and Send Request

**Context**: Replace the token in the request and send it to authenticate.

**Command** ([[commands/reverb-facebook-login-post]]):
```bash
POST /api/auth/facebook HTTP/1.1
Host: reverb.com
{"fb_token":"[EXTERNAL_FB_TOKEN]"}
```

> Use Burp Repeater to modify and send. Expected output is successful login as the victim.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques



## Commands Used

- [[commands/reverb-facebook-login-post]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[authentication-bypass]]
- [[token-manipulation]]
