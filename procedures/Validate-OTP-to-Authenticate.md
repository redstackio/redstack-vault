---
id: proc-uuid-mtn-step2-001
name: Validate-OTP-to-Authenticate
tags:
  - otp
  - authentication
  - web
type: procedure
tools: []
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
updated_at: '2025-12-14T17:30:27.224Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Validate-OTP-to-Authenticate

## Summary

This procedure completes the two-factor authentication process for the MTN offers dashboard by entering the received OTP, establishing a valid session tied to the phone number.

## Description

Following OTP delivery, this step involves submitting the code on the validation page to authenticate the user. The attack scenario uses this to create a legitimate session before exploiting IDOR. The target is the OTP validation endpoint, which checks the code against the session. Prerequisites: Received OTP SMS. Outcomes: Redirect to the dashboard with session cookies set, enabling further navigation.

## Requirements

1. Received 6-digit OTP via SMS
2. Active browser session from previous step
3. No additional tools needed

## Defense

Defensive measures and detection strategies:

- Enforce short OTP expiration (e.g., 5 minutes)
- Log failed OTP attempts and lock accounts after thresholds
- Bind sessions strictly to the originating phone number post-validation

## Objectives

1. Verify and activate the user session
2. Gain access to personalized dashboard
3. Prepare for parameter-based escalation

## Instructions

### Step 1: Receive and Enter OTP

**Context**: Input the OTP to confirm ownership of the phone number.

On the validation page (e.g., https://mtn.ng/offers/validate), enter the OTP code from SMS into the form field.

### Step 2: Submit for Validation

**Context**: Trigger backend verification to complete authentication.

Click the Validate button to submit the OTP.

> Successful submission sets session cookies and redirects to https://mtn.ng/offers/list?phone=<phone>, displaying authenticated content.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- otp
- validation
- session-establishment
