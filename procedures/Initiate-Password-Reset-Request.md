---
id: proc-uuid-001
name: Initiate-Password-Reset-Request
tags:
  - password-reset
  - initial-access
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
updated_at: '2025-12-14T17:33:06.520Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Initiate-Password-Reset-Request

## Summary

This procedure initiates the password reset flow on a target web application by submitting a valid email address, triggering the delivery of a verification code via email. It sets the stage for subsequent brute-force exploitation in systems lacking rate limiting.

## Description

In the context of a U.S. Department of Defense web application, accessing the forgot password endpoint and providing a known valid email starts the reset process. The application sends a short verification code (e.g., 4-6 digits) to the email without enforcing limits on subsequent attempts, enabling efficient brute-forcing. Prerequisites include knowledge of the victim's email and direct access to the application's URL.

## Requirements

1. Valid email address associated with a target account
2. Network access to the web application's forgot password page (e.g., https://www.example.com/forgot-password)
3. Email access to receive the verification code

## Defense

Defensive measures and detection strategies:

- Implement rate limiting on reset requests and code submissions (e.g., max 5 attempts per IP/email per hour)
- Use longer, random codes (e.g., 8+ characters with letters/numbers) and short expiration times
- Monitor for unusual reset attempts from single IPs

## Objectives

1. Trigger email delivery of verification code
2. Gain access to the verification submission endpoint
3. Prepare for code brute-forcing

## Instructions

### Step 1: Access Forgot Password Page

**Context**: Navigate to the application's forgot password functionality to begin the reset process.

No specific command; use a web browser to visit the URL such as https://www.example.com/forgot-password and enter the target email.

> Submitting the email triggers an API call (likely POST /forgot-password) that sends the code.

### Step 2: Receive and Note Email

**Context**: Check the email inbox for the verification code, but do not use it yet.

**Expected Output**: Email with subject like "Password Reset Code" containing the code.

> This step confirms the reset is active; proceed to interception in the next procedure.

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

- [[password-reset]]
- [[initial-access]]
