---
id: d297e289-1a87-4c1e-9980-9732dc24303b
type: procedure
verified: false
submitted: true
created_at: '2025-12-11T06:10:15.736Z'
updated_at: '2025-12-11T06:10:15.736Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Valid Accounts]]'
sub_techniques: []
tags:
  - initial-access
  - account-takeover
commands:
  - '[[commands/aws-cognito-get-user]]'
  - '[[commands/aws-cognito-update-user-attributes]]'
  - '[[commands/aws-cognito-get-user-post-update]]'
  - '[[commands/aws-cognito-get-user-failure]]'
platforms:
  - Web
tools:
  - '[[tools/AWS-Command-Line-Interface]]'
skill_level: intermediate
impact_level: high
detection_risk: high
validated: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1078]]'
---

# Login with Manipulated Email

## Summary

This procedure performs login to Flickr using the case-sensitive manipulated email and attacker's password to achieve account takeover.

## Description

Exploiting the normalization collision, the attacker logs in with their credentials but the victim's email, gaining full access. This finalizes the takeover in the Flickr web environment. Expected outcome is access to the victim's account.

## Requirements

1. Manipulated email set and unverified.
2. Attacker's password.
3. Access to Flickr login endpoint.

## Defense

Defensive measures and detection strategies:

- Check email verification during login.
- Monitor for login anomalies like case variations.

## Objectives

1. Gain unauthorized access to victim's account.
2. Exploit email collision.
3. Achieve full takeover.

## Instructions

### Step 1: Perform Login

**Context**: Log in using the exact case-sensitive email and attacker's credentials.

Ensure the HTTP request preserves the exact capitalization of the email to exploit normalization collision.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- initial-access
- account-takeover
