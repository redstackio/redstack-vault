---
id: proc-gitlab-intercept-2fa
tags:
  - intercept
  - 2fa
  - http-request
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
updated_at: '2025-12-14T17:31:30.876Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Intercept 2FA Submission Request

## Summary

This procedure captures the HTTP POST request sent when submitting the 2FA token in GitLab, allowing inspection of the multipart form-data containing the OTP attempt for later modification.

## Description

During the 2FA step, the request to /users/sign_in includes user[otp_attempt] but lacks user[login], relying on the session for user context. Using a proxy like Burp Suite, the attacker intercepts this to prepare for parameter injection. This targets Ruby on Rails sessions and assumes prior login completion.

## Requirements

1. Active session from attacker login
2. Burp Suite configured as proxy
3. Target at 2FA prompt

## Defense

Defensive measures and detection strategies:

- Implement request signing or CSRF tokens to prevent tampering
- Log and alert on proxied or modified authentication requests
- Use HTTPS with HSTS to hinder interception

## Objectives

1. Capture 2FA submission POST
2. Analyze form fields for modification points
3. Pause request for editing

## Instructions

### Step 1: Configure Proxy

**Context**: Set up Burp Suite to intercept browser traffic to the GitLab instance.

In Burp, enable Intercept in Proxy tab and configure browser proxy settings.

> Ensures all requests to target are captured.

### Step 2: Submit 2FA Token

**Context**: Trigger the request by entering and submitting the attacker's OTP on the 2FA page.

Enter OTP (e.g., 212421) and submit; request halts at Burp.

> Intercepted: POST /users/sign_in with Content-Type: multipart/form-data; fields include user[otp_attempt].

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

- [[intercept]]
- [[2fa]]
- [[http-request]]
