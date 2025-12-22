---
tags:
  - web
  - credential-access
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
detection_risk: low
sub_techniques: []
id: 14c37dcc-609b-4c9d-9edd-572ef6c2040a
created_at: '2025-12-11T06:10:28.564Z'
updated_at: '2025-12-11T06:10:28.564Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0006]]'
mitre_techniques:
  - '[[T1550]]'
---
# Associate Attacker Phone Number

## Summary

This procedure silently associates the attacker's phone number with the victim's account after the fake postMessage is accepted.

## Description

Due to the bypassed validation, the target site processes the fake sign-in and links the phone number without user notification.

## Requirements

1. Successful postMessage injection
2. Attacker's phone number in the payload
3. Active victim session

## Defense

Defensive measures and detection strategies:

- Require user confirmation for phone associations
- Audit authentication events

## Objectives

1. Link attacker's phone to victim account
2. Enable password reset access
3. Achieve persistent credential access

## Instructions

### Step 1: Confirm Association

**Context**: The association happens automatically post-message.

No manual action; monitor for success via account checks.

> Expected: Backend updates the phone linkage.

### Step 2: Validate Linkage

**Context**: Test if the phone is associated.

Attempt a password reset to verify.

> If reset initiates to attacker's phone, success.

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
- credential-access
