---
tags:
  - idor
  - web
  - request-capture
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
  - '[[tools/Mozilla-Firefox]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: c44b6183-8e87-414f-adc1-978d400b0566
created_at: '2025-12-14T17:25:47.561Z'
updated_at: '2025-12-14T17:25:47.561Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Capture-Attacker-Profile-Update-Request

## Summary

This procedure intercepts the HTTP POST request to the /app/updateUser endpoint from the attacker's session using Burp Suite, revealing the JSON payload structure for IDOR exploitation.

## Description

While authenticated as the attacker, navigating to the user profile page triggers a POST request to update profile details. Burp Suite proxies the traffic to capture this request, which includes predictable 'id' and 'email' fields without authorization checks. This step is crucial for understanding the payload and preparing modifications, with outcomes including detailed request logs for analysis.

## Requirements

1. Authenticated attacker session in [[tools/Mozilla-Firefox]]
2. [[tools/Burp-Suite]] configured as proxy (e.g., Community Edition v2022.8.4)
3. Intercept enabled in Burp

## Defense

Defensive measures and detection strategies:

- Log all profile update requests with user IP and session IDs
- Implement WAF rules to detect proxy-like traffic patterns
- Enforce HTTPS and monitor for unusual request interception attempts

## Objectives

1. Capture the exact JSON payload for profile updates
2. Identify vulnerable fields like 'id' and 'email'
3. Prepare data for cross-account exploitation

## Instructions

### Step 1: Configure Proxy and Navigate to Profile

**Context**: Set up Burp to intercept traffic and access the profile page.

No specific command; configure in Burp UI.

> In [[tools/Burp-Suite]], enable Intercept. In Firefox (proxied through Burp at 127.0.0.1:8080), navigate to https://mtnmobad.mtnbusiness.com.ng/#/userProfile. Expected output: Profile page loads, triggering POST /app/updateUser.

### Step 2: Intercept and Inspect Request

**Context**: Capture the request and examine the payload.

No specific command; use Burp UI.

> When the POST request is intercepted, view the JSON body containing fields like 'id', 'email', username, etc. Expected output: Full request details visible in Burp Repeater or Inspector.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]
- [[tools/Mozilla-Firefox]]

## Tags

- [[idor]]
- [[web]]
- [[request-capture]]
