---
tags:
  - email-confirmation
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
id: 7bb4b588-7cf0-4859-9c03-141ee98931e0
created_at: '2025-12-11T06:10:40.585Z'
updated_at: '2025-12-11T06:10:40.585Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1078]]'
---
# Receive and Use Misrouted Confirmation Email

## Summary

This procedure involves receiving the confirmation email sent to the original attacker email, containing the link for the target.

## Description

Due to the bug, the email from mailer@shopify.com arrives at the signup email, allowing the attacker to proceed with verification.

## Requirements

1. Access to original email inbox
2. Triggered confirmation from previous step

## Defense

Defensive measures and detection strategies:

- Fix routing to send to new email
- Monitor for anomalous confirmation patterns

## Objectives

1. Obtain verification link
2. Prepare for confirmation

## Instructions

### Step 1: Check Email Inbox

**Context**: Wait and retrieve the email.

The confirmation email from mailer@shopify.com is sent to the original signup email (attacker@gmail.com).

> Extract the verification link from the email.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- email-confirmation
- auth-bypass
