---
id: proc-insightly-shared-group-001
tags:
  - initial-access
  - account-setup
  - group-sharing
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
updated_at: '2025-12-13T23:55:20.898Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Create-Shared-Group-in-Insightly

## Summary

This procedure sets up two Insightly accounts and creates a shared group to enable collaborative notifications, prerequisite for propagating stored XSS payloads to multiple users.

## Description

In the context of exploiting Insightly's stored XSS, this step establishes legitimate access for an attacker-controlled account and a victim account within the same group. Shared groups allow notifications, including email subjects, to be visible to all members, facilitating the storage and execution of malicious content without direct victim interaction.

## Requirements

1. Access to email for account registration (e.g., two distinct email addresses)
2. Valid Insightly credentials for primary account
3. Web browser for navigation

## Defense

Defensive measures and detection strategies:

- Enforce group invitation approvals and audit logs for new members
- Limit shared access to trusted users only
- Monitor for anomalous account creations from the same IP

## Objectives

1. Gain shared access to notifications between accounts
2. Position attacker for payload injection visible to victims
3. Simulate legitimate user behavior to avoid detection

## Instructions

### Step 1: Register Primary Account

**Context**: Create the attacker's main account on Insightly.

Navigate to https://www.insightly.com and complete the registration form with valid details. Verify the account via email.

### Step 2: Register Secondary Account

**Context**: Create a victim-like account to receive shared notifications.

Repeat registration with a second email address.

### Step 3: Invite to Shared Group

**Context**: Link the accounts via a group to enable shared views.

Log in to the primary account, go to the Groups section, create a new group, and invite the secondary account's email. Accept the invitation from the secondary account.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[initial-access]]
- [[web]]

