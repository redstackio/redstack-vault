---
tags:
  - otp-interception
  - sms
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
  - '[[Modify Authentication Process]]'
updated_at: '2025-12-14T17:28:44.231Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: d6e765b8-b8a0-4f68-a5bd-8b003a7f78f4
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Modify Authentication Process]]'
---
---

# Receive-OTP-via-SMS

## Summary

This procedure involves passively receiving the OTP via SMS on the attacker's mobile device after initiating a manipulated request, exploiting the delivery to an arbitrary phone.

## Description

Following the OTP initiation, Zomato's SMS service delivers the 6-digit code to the specified phone number without further checks. The attacker, having provided their own number, receives the OTP intended for the target restaurant owner. This step is passive and relies on standard SMS delivery, typically within seconds to minutes, with a 5-minute validity window.

## Requirements

1. Mobile device capable of receiving SMS
2. Phone number used in the initiation step must be active
3. Completion of prior OTP request step

## Defense

Defensive measures and detection strategies:

- Bind OTP delivery to verified user sessions or pre-authenticated phones
- Use app-based push notifications instead of SMS for OTP
- Monitor SMS gateway logs for unusual delivery patterns
- Implement OTP expiration and one-time-use enforcement

## Objectives

1. Capture the 6-digit OTP code from SMS
2. Ensure OTP is received before expiration
3. Prepare for immediate verification to complete takeover

## Instructions

### Step 1: Monitor SMS Inbox

**Context**: Wait for and extract the OTP from the incoming SMS message from Zomato's SMS provider.

No command required; manually check phone messages.

> Expected SMS: "Zomato: Your verification code is 123456. Do not share. Valid for 5 minutes." Extract the code 123456 for use in verification.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Modify Authentication Process]] Modify Authentication Process

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- otp-interception
- sms-delivery

---
