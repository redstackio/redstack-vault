---
tags:
  - email-change
  - shopify
type: procedure
tools:
  - '[[tools/HTTP-Proxy-(e.g.,-Burp-Suite)]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 8e2b6ef7-7312-4e60-bdc0-8a9563cd7b67
created_at: '2025-12-11T03:47:56.691Z'
updated_at: '2025-12-11T03:47:56.691Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1190]]'
---
# Change Partner Email and Capture Confirmation Link

## Summary

This procedure changes the partner email to an attacker-owned address and captures the confirmation link for later use in the race condition exploit.

## Description

By changing the email to one controlled by the attacker and grabbing the confirmation link without visiting it, this sets up the timing attack for bypassing verification on a victim's email.

## Requirements

1. Access to Partners Dashboard
2. Attacker-owned email address

## Defense

Defensive measures and detection strategies:

- Implement transaction locking on email changes
- Monitor rapid email change attempts

## Objectives

1. Obtain confirmation link for owned email
2. Prepare for race condition

## Instructions

### Step 1: Change Email

**Context**: Navigate to settings and update email to attacker-owned address.

Go to https://partners.shopify.com/[ID]/settings and update the email.

### Step 2: Capture Link

**Context**: Check email and grab the confirmation link.

Retrieve the link from the confirmation email but do not visit it.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- #email-change
- #shopify
