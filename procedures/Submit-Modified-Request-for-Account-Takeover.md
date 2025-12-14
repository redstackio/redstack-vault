---
id: proc-submit-modified-request-001
tags:
  - account-takeover
  - submit
  - authentication
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - iOS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:33:34.459Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Submit-Modified-Request-for-Account-Takeover

## Summary

This procedure forwards the token-modified Facebook login request to the Reverb server, resulting in successful authentication as the target user due to the absence of origin validation, achieving full account takeover.

## Description

After replacement, submitting the request to https://reverb.com/api/auth/facebook exploits the vulnerability, as the server accepts the external token without checking its app origin. This grants the attacker a valid session for the victim's account, allowing data access, modifications, and further actions. The attack targets the web backend serving the iOS app.

## Requirements

1. Modified request ready in Burp Suite Repeater from prior step
2. Network connectivity to reverb.com
3. Target user account to impersonate (via the login flow initiation)

## Defense

Defensive measures and detection strategies:

- Enforce strict token validation using Facebook's debug_token endpoint to verify app_id
- Implement multi-factor authentication (MFA) for account recovery post-takeover
- Audit logs for successful logins with mismatched token metadata and trigger alerts

## Objectives

1. Complete the authentication bypass
2. Gain persistent access to the target account
3. Confirm the vulnerability's impact through session validation

## Instructions

### Step 1: Forward the Request

**Context**: Send the altered request to the server for processing.

In Burp Repeater, click "Send" to forward the POST request to /api/auth/facebook.

### Step 2: Analyze Response

**Context**: Verify successful authentication and access.

Inspect the response for success indicators, such as 200 OK with session tokens or a redirect to the dashboard. Use the returned session to access account features, confirming takeover.

**Expected Output**: JSON response like {"success": true, "user_id": "target_user", "access_token": "session_token"}.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[account-takeover]]
- [[submit]]
