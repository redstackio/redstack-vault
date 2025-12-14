---
id: proc-uuid-4
tags:
  - vpn-login
  - credential-use
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:31:52.998Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Login to SSL VPN Using Bypassed Credentials

## Summary

Authenticate to the Pulse Secure SSL VPN using extracted plaintext credentials combined with bypassed 2FA.

## Description

Submit username/password from analysis and 2FA token or session to the login endpoint, gaining a valid VPN session for internal access.

## Requirements

1. Plaintext credentials
2. Bypassed 2FA token/session
3. VPN portal URL

## Defense

Defensive measures and detection strategies:

- Enforce strong password policies
- Rate-limit login attempts
- Log failed/successful logins

## Objectives

1. Establish VPN session
2. Access internal resources
3. Prepare for proxy use

## Instructions

### Step 1: Submit Login Form

**Context**: Use browser or curl to login.

```bash
curl -d "username=extracted_user&password=plaintext_pass&duo_token=generated" https://vpn.example.com/dana-na/auth/login.htm
```

> Redirects to dashboard on success.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- vpn-login
- credential-use
