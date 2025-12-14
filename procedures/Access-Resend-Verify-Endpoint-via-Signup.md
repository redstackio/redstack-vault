---
id: uuid-1
tags:
  - initial-access
  - wordpress
type: procedure
tools:
  - '[[tools/Intercepting-Proxy]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:33:12.528Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-Resend-Verify-Endpoint-via-Signup

## Summary

This procedure involves registering a test account on the target WordPress site to gain access to the resend-verify functionality, which is unprotected and exposes a username enumeration vulnerability.

## Description

In the context of the en.instagram-brand.com site, signing up creates a session that enables the resend email feature. This endpoint (/wp-json/brc/v1/resend-verify) lacks protections, allowing subsequent exploitation. The procedure requires no special privileges and sets up for request interception.

## Requirements

1. Public access to the target site's registration page (e.g., https://en.instagram-brand.com/register/signup)
2. A disposable email for test signup
3. Browser with proxy support for next steps

## Defense

Defensive measures and detection strategies:

- Implement CAPTCHA on signup and resend endpoints
- Rate limit registration attempts
- Monitor for anomalous signup patterns

## Objectives

1. Establish access to the vulnerable resend-verify endpoint
2. Trigger initial session for request capture
3. Prepare for enumeration without alerting defenses

## Instructions

### Step 1: Navigate and Register

**Context**: Visit the signup page and complete registration to unlock the resend feature.

No specific command; use browser to register at https://en.instagram-brand.com/register/signup with any email. After confirmation, the resend button appears.

> Successful registration shows a dashboard or confirmation page with resend option.

### Step 2: Confirm Endpoint Access

**Context**: Verify the resend functionality is available post-signup.

Click the resend button to ensure it triggers a request to /wp-json/brc/v1/resend-verify.

> Endpoint access confirmed if request is generated.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Intercepting-Proxy]]

## Tags

- initial-access
- wordpress
