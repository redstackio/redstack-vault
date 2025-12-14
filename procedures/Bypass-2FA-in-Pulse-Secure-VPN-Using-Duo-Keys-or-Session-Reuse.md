---
id: proc-uuid-3
tags:
  - 2fa-bypass
  - duo-impersonation
  - session-reuse
type: procedure
tools: []
tactics:
  - '[[Credential Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Credentials In Files]]'
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:31:53.003Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Credentials In Files]]'
  - '[[Valid Accounts]]'
---
# Bypass 2FA in Pulse Secure VPN Using Duo Keys or Session Reuse

## Summary

Bypass Duo 2FA in Pulse Secure VPN by impersonating the integration using extracted keys or reusing stolen sessions from unencrypted storage.

## Description

With Duo keys (integration_key, secret_key, api_hostname) from mtmp/system, generate valid 2FA responses. Alternatively, extract and reuse session tokens from randomVal/data.mdb since roaming is disabled, allowing hijacking without re-auth.

## Requirements

1. Extracted Duo keys or session data
2. VPN login endpoint access
3. Python for Duo API simulation if needed

## Defense

Defensive measures and detection strategies:

- Enable session roaming and encrypt storage
- Use hardware-based 2FA
- Monitor for duplicate session usage

## Objectives

1. Generate valid 2FA
2. Reuse active sessions
3. Gain full auth bypass

## Instructions

### Step 1: Impersonate Duo 2FA

**Context**: Use keys to craft 2FA response.

Simulate Duo API call (custom script):

```bash
# Pseudo-command: Use keys to sign request to Duo API
curl -H "Authorization: Basic $INTEGRATION_KEY:$SECRET_KEY" https://api-$HOSTNAME/d Duo/auth
```

> Returns valid auth token for VPN submission.

### Step 2: Reuse Session

**Context**: Inject stolen session from data.mdb.

Set cookie in browser or request:

```bash
curl -b "session_token=extracted_value" https://vpn.example.com/login
```

> Bypasses 2FA if session valid.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]]

### Techniques

- [[Credentials In Files]]
- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- 2fa-bypass
- duo-impersonation
- session-reuse
