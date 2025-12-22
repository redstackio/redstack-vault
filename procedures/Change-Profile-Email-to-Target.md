---
id: proc-uuid-3
tags:
  - email-change
  - bypass
  - shopify
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Account Manipulation]]'
updated_at: '2025-12-14T17:30:58.668Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Account Manipulation]]'
---
# Change-Profile-Email-to-Target

## Summary

This procedure updates the Shopify profile email to a target address, triggering the vulnerable confirmation process.

## Description

The core flaw occurs here: changing the email quickly after signup causes the confirmation to be sent to the original email. This step exploits the timing and logic error in pending confirmation handling.

## Requirements

1. Access to profile page
2. Known target email address

## Defense

Defensive measures and detection strategies:

- Delay email changes post-signup
- Send confirmations only to the new email
- Validate changes against signup email

## Objectives

1. Set profile email to target
2. Queue misdirected confirmation

## Instructions

### Step 1: Edit Email Field

**Context**: Modify the account email.

In the profile form, locate the email input and enter the target email (e.g., yaworsk@hackerone.com).

> Field accepts the input without immediate validation.

### Step 2: Save Changes

**Context**: Submit the update to trigger confirmation.

Click 'Save' to apply the change.

> System saves and queues confirmation; no error if done promptly after signup.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Account Manipulation]] Account Manipulation

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[email-change]]
- [[bypass]]
- [[shopify]]
