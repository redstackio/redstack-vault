---
tags:
  - password-reset
  - shopify
type: procedure
tools: []
tactics:
  - '[[Persistence]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Modify Authentication Process]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 93bfe0c9-7dbe-47f6-b177-f4ec50c0c2a8
created_at: '2025-12-13T09:01:26.799Z'
updated_at: '2025-12-13T09:01:26.799Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Modify Authentication Process]]'
---
# Set New Password for Victim Account

## Summary

This procedure sets a new password for the victim's Shopify account during the merging process, without enabling 2FA.

## Description

On the new-password page, input a chosen password and submit, opting out of 2FA. This changes the victim's credentials, enabling takeover. Outcome is control over the account password.

## Requirements

1. Access to new-password page via bypass
2. Chosen new password

## Defense

Defensive measures and detection strategies:

- Enforce 2FA during password changes
- Alert on unauthorized password resets

## Objectives

1. Change victim account password
2. Avoid 2FA setup

## Instructions

### Step 1: Enter and Submit Password

**Context**: Set the new password.

Enter new password, decline 2FA, and submit.

> Confirms password change.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]]

### Techniques

- [[Modify Authentication Process]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[password-reset]]
- [[shopify]]
