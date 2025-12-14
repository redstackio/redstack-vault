---
tags:
  - session-hijack
  - authentication
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Mobile
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:30:47.319Z'
sub_techniques: []
id: 65061ba9-5461-45a1-8c95-592bfac2588a
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Authenticate-and-Obtain-Session-with-Affirm-Client

## Summary

This procedure captures the session token from a successful OTP authentication response, using the Affirm-Client header as the session ID for subsequent authenticated requests.

## Description

Upon successful OTP brute-force, the API response includes an Affirm-Client header containing a base64-encoded session ID and a user_id. This header acts as the authentication mechanism for further API calls. No additional commands are needed beyond extracting from the prior response. Prerequisites: Successful brute-force. Outcome: Valid session for PII access.

## Requirements

1. Successful OTP submission response
2. Ability to inspect HTTP headers

## Defense

Defensive measures and detection strategies:

- Secure session tokens with short expiry and binding to device/IP
- Rotate sessions on login and monitor reuse
- Detect anomalous session usage post-auth

## Objectives

1. Extract session from auth response
2. Enable authenticated API access
3. Facilitate data exfiltration

## Instructions

### Step 1: Extract Session Details

**Context**: From the brute-force success response, note the Affirm-Client header and user_id.

No specific command; inspect response headers manually or via Burp.

> Expected: Affirm-Client value like ".eJyrVkrOzytJrSiJTyzKVLJSMjV2Cg80MDMJNwy39HCycFfSUSotTi1SsqpWyslPz8yLL04tLs7Mz8OlvLYWAD8TGa8.EOzRAg.KdnFWXFpkJrsLXazTxNyjxb5Jtk" and user_id "1479-5770-XGGL".

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- session-hijack
