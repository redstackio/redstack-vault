---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567892
tags:
  - auth-bypass
  - email
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:31:11.082Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Access-Email-Verification-Link

## Summary

This procedure uses the verification link from the registration email to authenticate and activate the account, demonstrating the URL-based auth mechanism without password.

## Description

Clicking the link sends a GET request with 'fbcid' parameter, which the app uses to verify and log in the user. This exposes the vulnerability as the link persists beyond activation.

## Requirements

1. Received verification email
2. Web browser
3. Network access to the app

## Defense

Defensive measures and detection strategies:

- Use one-time-use tokens in links
- Log and alert on repeated link access
- Enforce HTTPS and token validation

## Objectives

1. Activate the account via link
2. Establish initial authenticated session
3. Capture the full URL for reuse

## Instructions

### Step 1: Open Email

**Context**: Locate the verification email in the inbox.

Open the email from the app (e.g., Zomato).

> Email body contains the clickable 'Verify Email Address' link.

### Step 2: Click and Access Link

**Context**: Trigger the GET request to authenticate.

Click the link; observe redirection to logged-in state.

> Browser performs GET to endpoint like /verify?fbcid=encoded_value, setting session.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[auth-bypass]]
- [[email]]
