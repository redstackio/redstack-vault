---
tags:
  - brute-force
  - 2fa-setup
  - email-verification
type: procedure
tools:
  - '[[tools/burp-suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Brute Force]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 5236c5c3-5b80-4b8e-9cfe-bb1c266fb804
created_at: '2025-12-14T17:24:47.712Z'
updated_at: '2025-12-14T17:24:47.712Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Brute Force]]'
---
# Request Email Confirmation Code During 2FA Setup

## Summary

This procedure initiates the 2FA setup process in Evernote by requesting a 6-digit verification code to the target's email, setting the stage for brute-force exploitation due to the lack of rate limiting.

## Description

During Evernote account creation or 2FA enablement, the system sends a time-sensitive 6-digit code to the provided email for ownership verification. This step involves navigating the web interface to trigger the email, intercepting the subsequent verification request with a proxy tool like Burp Suite. No authentication is required beforehand, making it accessible to external attackers using the victim's email address. The expected outcome is receipt of the code (by the victim or if intercepted) and a capturable HTTP request containing the confirmationCode parameter.

## Requirements

1. Access to the victim's email address (to initiate signup)
2. Burp Suite or similar proxy for request interception
3. Direct web access to Evernote's signup/2FA endpoint

## Defense

Defensive measures and detection strategies:

- Implement rate limiting on verification code requests (e.g., max 5 attempts per IP/email per hour)
- Monitor for anomalous signup attempts from unknown IPs using the same email
- Use CAPTCHA on verification pages to deter automation

## Objectives

1. Trigger delivery of the 6-digit verification code to the victim's email
2. Intercept the verification submission request for modification
3. Prepare for brute-force testing without alerting the system

## Instructions

### Step 1: Initiate Account Creation

**Context**: Start the process by attempting to create an account with the victim's email to reach the 2FA setup.

Intercept the request using Burp Suite proxy configured on your browser.

> Navigate to Evernote signup, enter victim's email (e.g., victim@gmail.com), and proceed until the verification code request is sent. The system emails the code.

### Step 2: Intercept Verification Request

**Context**: Capture the POST request that submits the code to the endpoint.

Enter an arbitrary code (e.g., 000000) to generate the request for interception.

> In Burp Suite Proxy, view the intercepted request to the email verification endpoint (likely /api/account/verify or similar), noting the confirmationCode parameter.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Brute Force]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/burp-suite]]

## Tags

- [[brute-force]]
- [[2fa-setup]]
