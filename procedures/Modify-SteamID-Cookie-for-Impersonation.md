---
tags:
  - cookie
  - modification
  - idor
  - impersonation
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-modify-cookie]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:48.356Z'
skill_level: intermediate
impact_level: medium
sub_techniques: []
id: 608f7d06-9303-422b-8c48-cbf3d80c8a26
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Modify-SteamID-Cookie-for-Impersonation

## Summary

This procedure alters the steamid cookie in a captured 2FA request to a victim's SteamID, exploiting lack of validation for unauthorized account targeting.

## Description

In Steam-integrated apps like CS Money, the server trusts the steamid cookie without cross-verifying against sessions or tokens. Modifying it enables IDOR-style impersonation, allowing attacks on /login/confirm and /2fa/delete endpoints.

## Requirements

1. Captured request from prior step
2. Victim's SteamID (e.g., 7656119xxxxxxxxx format)
3. Proxy or scripting tool for editing HTTP requests

## Defense

Defensive measures and detection strategies:

- Validate cookies against server-side sessions or JWTs
- Implement CSRF tokens tied to authenticated users
- Audit cookie changes in access logs

## Objectives

1. Substitute steamid for target account
2. Maintain request validity for forwarding
3. Enable impersonation without credentials

## Instructions

### Step 1: Edit Cookie in Proxy

**Context**: Change the steamid value in the captured request.

In Burp Repeater, update Cookie: steamid= to victim's ID.

Or use [[commands/curl-modify-cookie]]:

```bash
curl -X POST https://target.com/login/confirm -H "Cookie: steamid=victim_steamid" -d '{"token":"session_token","code":"123456"}'
```

> Request now targets victim's account.

### Step 2: Verify Modification

**Context**: Forward once with valid code to test impersonation.

Submit and check server response for account-specific errors.

> Success if response indicates victim's session context.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-modify-cookie]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[cookie]]
- [[modification]]
- [[idor]]
- [[impersonation]]
