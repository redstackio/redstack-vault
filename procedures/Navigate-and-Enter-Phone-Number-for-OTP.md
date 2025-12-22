---
id: proc-uuid-mtn-step1-001
name: Navigate-and-Enter-Phone-Number-for-OTP
tags:
  - authentication
  - otp
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
updated_at: '2025-12-14T17:30:27.226Z'
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
# Navigate-and-Enter-Phone-Number-for-OTP

## Summary

This procedure initiates access to the MTN offers dashboard by navigating to the entry page and submitting a valid Nigerian MTN phone number, triggering the delivery of a one-time password (OTP) via SMS for subsequent authentication.

## Description

In the context of exploiting broken access control in the MTN Nigeria web application, this step establishes the initial legitimate session. The target environment is the public-facing https://mtn.ng/offers/ endpoint, which accepts phone numbers without prior verification. Prerequisites include a valid MTN phone number capable of receiving SMS. Expected outcomes include redirection to an OTP input page and receipt of the SMS code, setting the stage for authentication and eventual IDOR exploitation.

## Requirements

1. Web browser with internet access
2. Valid Nigerian MTN phone number (e.g., 234xxxxxxxxx format)
3. SMS reception capability (physical or virtual SIM)

## Defense

Defensive measures and detection strategies:

- Implement rate limiting on phone number submissions to prevent enumeration
- Monitor for unusual OTP request patterns from single IPs
- Use CAPTCHA on initial forms to deter automated abuse

## Objectives

1. Trigger OTP delivery for a specific phone number
2. Gain entry to the authentication flow
3. Establish a baseline for session creation

## Instructions

### Step 1: Navigate to the Offers Page

**Context**: Access the public entry point for the offers service to begin the authentication process.

Visit the URL https://mtn.ng/offers/ in your web browser. The page should display a form for entering a phone number.

### Step 2: Submit Phone Number

**Context**: Provide a valid phone number to request OTP, simulating legitimate user behavior.

Enter a valid MTN phone number (e.g., 2348160817474) into the input field and click the Submit button.

> This action sends a POST request to the backend, which validates the number format and dispatches an SMS with a 6-digit OTP.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- authentication
- otp
- initial-access
