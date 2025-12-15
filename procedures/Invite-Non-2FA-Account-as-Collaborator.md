---
tags:
  - auth-bypass
  - invitation-bypass
  - hackerone
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
impact_level: high
detection_risk: medium
sub_techniques: []
id: 37230d3c-f71a-4463-9157-f7b32c0b3fd8
created_at: '2025-12-14T17:24:45.529Z'
updated_at: '2025-12-14T17:24:45.529Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Invite-Non-2FA-Account-as-Collaborator

## Summary

This procedure registers a new HackerOne account without 2FA and invites it as a collaborator to a report in a 2FA-required program, exploiting the lack of validation in the invitation process.

## Description

The attack scenario targets the collaborator invitation feature in HackerOne reports. By creating a secondary account that skips 2FA setup and inviting it from a report in a 2FA-enforced program, the platform fails to enforce multi-factor checks during invitation. This allows potential unauthorized access. Prerequisites include an existing 2FA-enabled program with a report, and the procedure assumes web-based interactions via the HackerOne UI.

## Requirements

1. Access to the original HackerOne account with report ownership.
2. Ability to register new accounts on HackerOne.
3. Email access for the new account to receive invitations.

## Defense

Defensive measures and detection strategies:

- Validate 2FA status of all invitees before allowing acceptance.
- Log and alert on invitations to non-2FA accounts in secure programs.
- Implement invitation approval workflows for sensitive reports.

## Objectives

1. Create a non-2FA account to simulate an unauthorized user.
2. Send an invitation without triggering 2FA enforcement.
3. Confirm the invitation is receivable by the non-2FA account.

## Instructions

### Step 1: Register New Account Without 2FA

**Context**: Create a secondary account that does not enable multi-factor authentication.

Visit hackerone.com/signup, provide email and password, complete registration, but skip the 2FA setup prompt during onboarding.

> Expected output: Account dashboard accessible without 2FA prompts.

### Step 2: Send Collaborator Invitation

**Context**: From the original report, invite the new account as a collaborator.

Log back into the original account, navigate to the submitted report, click the "Invite Collaborator" option, enter the new account's username or email, and send the invitation.

> Expected output: Invitation sent successfully, with no 2FA validation error; notification or email delivered to the new account.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[auth-bypass]]
- [[hackerone]]
