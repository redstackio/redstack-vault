---
tags:
  - wordpress
  - invitation
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Valid Accounts]]'
skill_level: beginner
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 054ab29a-e2c8-4ded-b55f-85d9f5ab5b6c
created_at: '2025-12-13T09:01:26.551Z'
updated_at: '2025-12-13T09:01:26.551Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Invite Unverified Account

## Summary

This procedure uses a verified WordPress.com account to invite an unverified account to a site, initiating the verification bypass.

## Description

The invitation process allows the unverified account to accept and thereby verify the email without standard confirmation.

## Requirements

1. Verified WordPress.com account
2. Unverified account email
3. Access to a WordPress site

## Defense

Defensive measures and detection strategies:

- Audit invitations and user joins
- Detect anomalous invitation patterns

## Objectives

1. Send invitation to unverified account
2. Prepare for acceptance and verification
3. Ensure invitation is received

## Instructions

### Step 1: Access User Settings

**Context**: Navigate to invitation section.

From the verified account, go to settings > users.

> User management page opens.

### Step 2: Send Invitation

**Context**: Invite the target account.

Invite the second account (something@company.com).

> Invitation is sent successfully.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[wordpress]]
- [[invitation]]
