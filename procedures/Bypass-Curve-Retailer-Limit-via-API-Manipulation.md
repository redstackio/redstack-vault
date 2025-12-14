---
tags:
  - business-logic
  - api-manipulation
  - android
  - privilege-escalation
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/retrieve-curve-merchants-list]]'
verified: false
platforms:
  - Android
  - Web API
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:28:28.379Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 24cbc3ad-3106-4266-b201-bab65ce94854
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---
# Bypass-Curve-Retailer-Limit-via-API-Manipulation

## Summary

This procedure exploits a business logic flaw in the Curve Android app by intercepting and modifying the API response for the merchants list, allowing non-premium users to reset and reselect retailers repeatedly, bypassing the 3-retailer limit and gaining cashback on all available options.

## Description

The Curve app enforces a 3-retailer limit for non-premium users client-side, but fails to validate this on the server. By using a proxy like Burp Suite to empty the merchants array in the GET response from `/v1/rewards/users/programs/[id]/merchants`, the app resets the selection state, enabling unlimited additions. This leads to unauthorized premium feature access and potential financial impact. Target environment: Android app communicating with REST API over HTTPS; requires proxy setup on the device/emulator.

## Requirements

1. Valid non-premium Curve account credentials
2. Android device or emulator (e.g., Genymotion) with proxy routing enabled (e.g., via Burp Suite CA certificate installation)
3. Burp Suite configured to intercept mobile traffic
4. Network access to api.imaginecurve.com

## Defense

Defensive measures and detection strategies:

- Implement server-side validation of retailer counts and user tiers before applying changes
- Use request signing or integrity checks on API responses to prevent tampering
- Monitor for anomalous retailer additions or proxy-like traffic patterns (e.g., repeated GETs with modified responses)
- Enforce rate limiting on rewards API endpoints

## Objectives

1. Reset the client-side retailer selection state via API manipulation
2. Add multiple sets of retailers to exceed non-premium limits
3. Achieve cashback rewards on all retailers, simulating premium access

## Instructions

### Step 1: Setup Proxy and Login

**Context**: Prepare the environment and authenticate to establish a session.

Install and configure [[tools/Burp-Suite]] as a proxy. On the Android device/emulator, set proxy to Burp's listener (e.g., 127.0.0.1:8080) and install Burp's CA certificate. Launch Curve app and login as non-premium user.

### Step 2: Initial Selection and Confirmation

**Context**: Trigger the initial API population to set up for interception.

Navigate to 'Earn Curve Cash', select 3 retailers, and click 'Confirm'. This adds them server-side.

### Step 3: Intercept and Execute Merchants List Retrieval

**Context**: Capture the response containing the current merchants to modify it.

Return to 'Earn Curve Cash' to trigger a refresh. Intercept the GET request using [[commands/retrieve-curve-merchants-list]] equivalent in Burp or curl for testing:

**Command** ([[commands/retrieve-curve-merchants-list]]):
```bash
curl -X GET "https://api.imaginecurve.com/v1/rewards/users/programs/e329e463-7f5d-4358-9109-4f97c9f86abd/merchants" \
  -H "Accept: application/json" \
  -H "Curve-UserAgent: Android;Genymotion;Custom Phone" \
  -H "Curve-AppAndVersion: Curve Android 2.9.0" \
  -H "crv-user-agent: Android 2.9.0/20900" \
  -H "Authorization: APE7kg446BXw2iFEI6Ca079RaGrJ3bcelA9DKDoUFUA" \
  -H "crv-idempotency-key: a161ccfc-077c-4099-a180-ebbbacb50da6" \
  -H "crv-request-id: 88fb2296-46f4-49e4-858f-8aff312a9587" \
  -H "crv-correlation-id: android-98600fe2-6b09-48d8-94b1-cecf73094c43" \
  -H "Host: api.imaginecurve.com" \
  --connect-timeout 10
```

> This command retrieves the JSON response with the merchants array. In Burp, view and modify the response body to `{"success":true,"data":{"merchants":[]}}` before forwarding.

### Step 4: Select and Confirm New Retailers

**Context**: Exploit the reset state to add more retailers.

Disable interception, select 3 new retailers, and confirm. Repeat interception/modification cycle to accumulate all retailers.

### Step 5: Verify Bypass

**Context**: Confirm the exploit success.

Check account rewards section; more than 3 retailers should be active for cashback.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation

### Sub-Techniques


## Commands Used

- [[commands/retrieve-curve-merchants-list]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- business-logic
- api-manipulation
- android
- privilege-escalation
