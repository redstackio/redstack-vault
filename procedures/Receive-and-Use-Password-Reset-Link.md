---
tags:
  - account-takeover
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
  - '[[tools/Content-Type-Converter]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: high
detection_risk: high
sub_techniques: []
id: c476493d-7c55-4537-be62-b5ffb17fa1b1
created_at: '2025-12-11T06:10:31.048Z'
updated_at: '2025-12-11T06:10:31.048Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1190]]'
---
# Receive and Use Password Reset Link

## Summary

This procedure involves checking the attacker's email for the reset link, using it to change the password, and logging into the victim's GitLab account.

## Description

Upon receiving the email, click the reset link, set a new password, and access the account. This finalizes the account takeover without victim interaction. Applicable to exploited GitLab instances.

## Requirements

1. Attacker's email access
2. Received reset link
3. Web browser

## Defense

Defensive measures and detection strategies:

- Require user confirmation for resets
- Alert on suspicious logins

## Objectives

1. Access reset link
2. Change password
3. Achieve account takeover

## Instructions

### Step 1: Check Email and Reset

**Context**: Open the email and click the link.

Set a new password and log in as the victim.

> Confirm access to account features.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- account-takeover
