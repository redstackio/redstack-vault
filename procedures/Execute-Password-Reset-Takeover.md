---
tags:
  - web
  - account-takeover
type: procedure
tools: []
tactics:
  - '[[Credential Access]]'
commands:
  - '[[commands/postmessage-send-fake-signin]]'
platforms:
  - Web
techniques:
  - '[[Use Alternate Authentication Material]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 7c4b1231-5e75-4b8b-bf0a-404e53a91154
created_at: '2025-12-11T06:10:28.560Z'
updated_at: '2025-12-11T06:10:28.560Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0006]]'
mitre_techniques:
  - '[[T1550]]'
---
# Execute Password Reset Takeover

## Summary

This procedure uses the associated phone number to reset the password and gain full control of the victim's account.

## Description

With the phone linked, the attacker can request a password reset via Digits, receiving the code and completing the takeover.

## Requirements

1. Phone number associated
2. Access to attacker's phone for reset code
3. Target site's reset functionality

## Defense

Defensive measures and detection strategies:

- Multi-factor authentication beyond phone
- Rate limit reset requests

## Objectives

1. Reset victim password
2. Log in as victim
3. Achieve account takeover

## Instructions

### Step 1: Initiate Password Reset

**Context**: Use the site's reset feature with the associated phone.

Navigate to reset page and request code to attacker's phone.

> Code is sent to attacker.

### Step 2: Complete Reset and Login

**Context**: Enter the code and set new password.

Submit the form and log in with new credentials.

> Expected: Full access to victim's account.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]]

### Techniques

- [[Use Alternate Authentication Material]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- web
- account-takeover
