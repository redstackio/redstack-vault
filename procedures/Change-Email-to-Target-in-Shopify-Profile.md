---
tags:
  - shopify
  - email-change
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: medium
detection_risk: medium
sub_techniques: []
id: f548e1f4-243d-4c31-bee1-6fb724104e60
created_at: '2025-12-13T09:01:26.844Z'
updated_at: '2025-12-13T09:01:26.844Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Change Email to Target in Shopify Profile

## Summary

This procedure updates the account email to a target address, triggering the vulnerable confirmation process.

## Description

Changing the email during the free trial causes the confirmation link to be sent to the original email, enabling bypass.

## Requirements

1. Access to Shopify profile
2. Target email address known

## Defense

Defensive measures and detection strategies:

- Send confirmations to the new email address
- Require re-authentication for email changes

## Objectives

1. Submit email change request
2. Trigger misdirected confirmation

## Instructions

### Step 1: Update Email Field

**Context**: Edit and save the new email.

Update the email field to the target like yaworsk@hackerone.com and submit the changes.

> This initiates the confirmation email to the wrong address.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- shopify
- email-change
