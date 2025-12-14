---
tags:
  - verification-bypass
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
updated_at: '2025-12-14T17:31:42.758Z'
sub_techniques: []
id: d0c87793-6435-4271-8a27-efac721cdcce
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Accept-Invitation-on-Second-Account-to-Verify-Email

## Summary

This procedure accepts the invitation on the unconfirmed account, verifying the victim's email without actual ownership or link clicks.

## Description

The core flaw: Accepting an invite via notifications verifies the email, as WordPress.com trusts the invitation process over direct confirmation. This grants full account status to the attacker-controlled credentials, enabling SSO matching on the target site.

## Requirements

1. Invitation sent to the unconfirmed account
2. Login access to the victim's email account
3. Web browser

## Defense

Defensive measures and detection strategies:

- Require email confirmation for all verifications, including invites
- Validate invite acceptances against email ownership
- Monitor for rapid verification after invitations

## Objectives

1. Accept invite to trigger verification
2. Gain confirmed status on victim's email
3. Enable SSO impersonation

## Instructions

### Step 1: Login to Unconfirmed Account

**Context**: Access notifications.

Log into the WordPress.com account with victim's email credentials.

> Dashboard shows pending notifications.

### Step 2: Accept Invitation

**Context**: Complete the verification.

Click the invitation notification and accept.

> Email status updates to verified in profile settings.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- verification-bypass
- wordpress-com
