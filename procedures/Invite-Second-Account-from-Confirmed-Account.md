---
tags:
  - invitation
  - wordpress-com
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:31:42.761Z'
sub_techniques: []
id: ebd1cb6e-96b1-438c-9259-84685d1a00c3
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Invite-Second-Account-from-Confirmed-Account

## Summary

This procedure sends an invitation from the attacker's confirmed WordPress.com account to the unconfirmed victim's account, initiating the verification bypass.

## Description

WordPress.com's invitation system allows verified accounts to invite others via notifications, without checking ownership. This flaw lets the attacker queue a verification action for the victim's email. The invite appears in the target account's notifications, ready for acceptance.

## Requirements

1. Confirmed personal WordPress.com account (from prior procedure)
2. Unconfirmed account with victim's email
3. Web browser

## Defense

Defensive measures and detection strategies:

- Restrict invitations to verified contacts only
- Notify invitees via email immediately
- Audit invitation logs for anomalies

## Objectives

1. Send invite to victim's account
2. Trigger notification-based verification path
3. Bypass direct email confirmation

## Instructions

### Step 1: Access Invitation Interface

**Context**: Log into the confirmed account and find user settings.

Login to personal WordPress.com account, go to Settings > Users.

> Invitation form appears.

### Step 2: Send Invitation

**Context**: Target the unconfirmed account.

Enter victim@company.com in the invite email field and submit.

> Invitation sent; check for confirmation in notifications.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- invitation
- wordpress-com
