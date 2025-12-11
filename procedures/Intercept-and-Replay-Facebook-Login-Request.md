---
tags:
  - authentication-bypass
  - traffic-interception
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/reverb-facebook-login-post]]'
platforms:
  - iOS
  - Web
techniques:
  - '[[Valid Accounts]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 7dcf7c9f-1a1c-4baa-bb78-8edaeba1641c
created_at: '2025-12-11T06:10:15.372Z'
updated_at: '2025-12-11T06:10:15.372Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1078]]'
---
# Intercept and Replay Facebook Login Request

## Summary

This procedure involves using Burp Suite to intercept and replay the Facebook login request in the Reverb iOS app, identifying the lack of server-side validation for access tokens.

## Description

The procedure targets the /api/auth/facebook endpoint, capturing the POST request with the fb_token. By replaying it, attackers confirm the vulnerability, setting the stage for token substitution. This is applicable in scenarios where OAuth tokens are not app-specific validated, leading to authentication bypass. Expected outcome is successful request capture and replay without errors.

## Requirements

1. Burp Suite installed and configured as a proxy for iOS traffic
2. Access to the Reverb iOS app and a valid Facebook login flow
3. Network interception capability (e.g., via WiFi proxy)

## Defense

Defensive measures and detection strategies:

- Implement server-side validation to ensure tokens are issued for the specific app ID
- Monitor for anomalous login patterns, such as tokens from unexpected app sources
- Use rate limiting and anomaly detection on authentication endpoints

## Objectives

1. Capture the vulnerable login request
2. Verify replayability to confirm endpoint behavior
3. Prepare for token manipulation in subsequent steps

## Instructions

### Step 1: Set Up Interception

**Context**: Configure Burp Suite to intercept HTTP traffic from the Reverb iOS app during Facebook login.

Launch Burp Suite and set it as the proxy for the iOS device. Initiate the Facebook login in the app to capture the request.

> This step ensures all traffic to reverb.com is proxied through Burp.

### Step 2: Capture and Replay Request

**Context**: Intercept the POST request and replay it to test the endpoint.

**Command** ([[commands/reverb-facebook-login-post]]):
```bash
POST /api/auth/facebook HTTP/1.1
Host: reverb.com
{"fb_token":"EAAJ8Of8D..."}
```

> Execute this in Burp's Repeater to replay the request. Expected output is a successful authentication response.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques



## Commands Used

- [[commands/reverb-facebook-login-post]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[authentication-bypass]]
- [[traffic-interception]]
