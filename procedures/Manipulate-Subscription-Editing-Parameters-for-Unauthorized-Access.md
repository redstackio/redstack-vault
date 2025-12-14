---
id: proc-uuid-141120-param-manip
tags:
  - idor
  - authorization-bypass
  - parameter-manipulation
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-parameter-manipulation-test]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:28.540Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Manipulate-Subscription-Editing-Parameters-for-Unauthorized-Access

## Summary

This procedure exploits an improper authentication vulnerability in the teavana.com subscription editing endpoint by manipulating URL or POST parameters (e.g., subscription ID) to target and edit another user's shipping address without proper authorization checks.

## Description

In the teavana.com subscription management system, the editing functionality fails to validate that the requesting user owns the subscription being modified. An attacker with a valid session can alter parameters in the request to reference another user's subscription ID, obtained through enumeration or guessing, allowing unauthorized updates to sensitive data like shipping addresses. This leads to privacy breaches and potential service disruptions. The vulnerability was identified by testing parameter tampering in May 2016 and resolved by August 2016 after reporting to Starbucks.

## Requirements

1. Valid authenticated session on teavana.com (login credentials for any user account)
2. Knowledge of target subscription IDs (via enumeration, guessing sequential IDs, or prior recon)
3. Proxy tool like Burp Suite for request interception and modification
4. Network access to teavana.com over HTTPS

## Defense

Defensive measures and detection strategies:

- Implement server-side authorization checks to ensure users can only modify their own subscriptions
- Use session-based or JWT tokens bound to user IDs in requests
- Log and monitor anomalous parameter values or access patterns for unauthorized edits
- Rate-limit subscription editing endpoints to prevent brute-force ID guessing

## Objectives

1. Gain unauthorized access to another user's subscription data
2. Modify shipping address to disrupt deliveries or expose privacy
3. Demonstrate impact of improper authentication in web applications

## Instructions

### Step 1: Authenticate and Capture Legitimate Request

**Context**: Log in to teavana.com and navigate to the subscription editing page to capture a baseline request for your own subscription.

Use Burp Suite to intercept the request. No specific command needed here; configure your browser proxy to 127.0.0.1:8080.

**Expected Output**: HTTP POST or GET request to the editing endpoint, e.g., `/subscriptions/edit` with parameters like `subscription_id=123` and `shipping_address=...`.

### Step 2: Identify and Modify Target Parameters

**Context**: Change the `subscription_id` parameter to target another user's ID (e.g., increment from your own ID or guess based on patterns).

Intercept the request in Burp Suite, modify the parameter, and forward it.

**Command** ([[commands/curl-parameter-manipulation-test]]):
```bash
curl -X POST 'https://www.teavana.com/subscriptions/edit' \
  -H 'Cookie: session=your_session_token' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'subscription_id=456&shipping_address=123 Fake St, Anytown, USA&submit=Update'
```

> This curl command simulates the modified request, replacing `subscription_id=123` (your own) with `456` (target user's). Expected output: Server response with 200 OK and confirmation of update, without erroring on authorization.

### Step 3: Verify Unauthorized Modification

**Context**: Check the impact by attempting to view or confirm the change, or monitor for delivery issues.

If possible, use another session or tool to query the updated subscription details.

**Expected Output**: The target's shipping address is now altered, visible in order history or delivery logs if accessible.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-parameter-manipulation-test]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- idor
- authorization-bypass
- parameter-manipulation
