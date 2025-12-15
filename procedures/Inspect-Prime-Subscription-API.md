---
id: proc-inspect-streamlabs-api-1070510
tags:
  - api-inspection
  - business-logic
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:36.358Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Inspect-Prime-Subscription-API

## Summary

This procedure inspects the Streamlabs Prime subscription API endpoint to confirm that non-subscribers receive false values for subscription flags, setting the stage for response manipulation in a business logic bypass attack.

## Description

In the Streamlabs web application, client-side JavaScript checks the user's Prime status via the API at https://streamlabs.com/api/v5/user/prime/subscription. For non-Prime users, this returns a JSON object with flags like "has_prime": false. Intercepting this with a proxy tool like Burp Suite reveals the vulnerability, as the response can be tampered with to simulate a subscribed state. This is part of an attack scenario targeting unauthorized access to premium features in a web-based streaming dashboard.

## Requirements

1. Valid non-Prime Streamlabs account and login
2. Browser configured to proxy traffic through Burp Suite (e.g., FoxyProxy extension)
3. Network access to https://streamlabs.com

## Defense

Defensive measures and detection strategies:

- Implement server-side validation for all Prime feature accesses, rejecting client-side assertions
- Monitor for anomalous API response patterns or proxy-like traffic anomalies using WAF rules
- Rate-limit reward redemptions and require CAPTCHA for high-value actions

## Objectives

1. Confirm API returns false for non-Prime users
2. Identify exact JSON fields for later tampering
3. Establish baseline for exploitation

## Instructions

### Step 1: Configure Proxy and Login

**Context**: Set up Burp Suite to intercept HTTPS traffic and access the Streamlabs dashboard to trigger the API call.

In Burp Suite, ensure the proxy is running on localhost:8080. Configure your browser to use this proxy and install the Burp CA certificate for HTTPS interception. Log into your Streamlabs account at https://streamlabs.com/dashboard.

### Step 2: Trigger and Intercept API Call

**Context**: Navigate to a page that checks Prime status, such as the rewards or settings page, to force the API request.

Browse to https://streamlabs.com/dashboard and interact with Prime-gated features (e.g., attempt to view rewards). In Burp's Proxy > HTTP history, filter for the API endpoint and forward the request.

**Expected Output**: Intercepted response JSON like {"has_prime": false, "blocked": true}.

### Step 3: Analyze Response

**Context**: Examine the JSON structure to note tamperable fields.

View the response body in Burp's Inspector tab, confirming all subscription-related booleans are false.

**Expected Output**: Detailed view of false flags, ready for Match and Replace rules.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[api-inspection]]
- [[business-logic]]
