---
tags:
  - email-change
  - auth-bypass
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Valid Accounts]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: f0026265-4d7b-44a2-bf4b-012b3042da3d
created_at: '2025-12-11T06:10:40.587Z'
updated_at: '2025-12-11T06:10:40.587Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1078]]'
---
# Change Email to Target and Trigger Confirmation

## Summary

This procedure changes the profile email to a target's address, triggering a flawed confirmation email process in Shopify.

## Description

The change exploits the root cause where the confirmation link is sent to the original email instead of the new one, enabling bypass.

## Requirements

1. Access to Shopify profile
2. Target email address

## Defense

Defensive measures and detection strategies:

- Ensure confirmations are sent to the new email
- Verify email changes with additional factors

## Objectives

1. Initiate confirmation for target email
2. Exploit misrouting bug

## Instructions

### Step 1: Update Email Field

**Context**: Edit and save the new email.

Update the email field to a target email like yaworsk@hackerone.com and click save.

> This triggers the email confirmation process.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- email-change
- auth-bypass
