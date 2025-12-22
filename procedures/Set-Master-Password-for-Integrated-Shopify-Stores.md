---
tags:
  - shopify
  - password-reset
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands: []
platforms:
  - Web
  - Cloud
techniques:
  - '[[Valid Accounts]]'
skill_level: beginner
impact_level: high
detection_risk: high
sub_techniques: []
id: c3f89060-b92d-4497-bc95-e4e165279f7b
created_at: '2025-12-13T09:01:26.830Z'
updated_at: '2025-12-13T09:01:26.830Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Set Master Password for Integrated Shopify Stores

## Summary

This procedure sets a new master password for all integrated stores, completing the takeover.

## Description

With SSO integration, the attacker can reset passwords and gain full control over the target's shops.

## Requirements

1. Integrated accounts via SSO
2. Access to profile settings

## Defense

Defensive measures and detection strategies:

- Enforce password reset notifications to original owners
- Detect and alert on bulk password changes

## Objectives

1. Reset passwords
2. Achieve full account control

## Instructions

### Step 1: Change Password

**Context**: Follow prompts to set new password.

Follow the on-screen instructions to change the password, gaining control over all stores under the email.

> Password update confirmation.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- shopify
- password-reset
