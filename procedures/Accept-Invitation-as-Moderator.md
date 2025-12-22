---
id: proc-streamlabs-accept-invite-001
tags:
  - shared-access
  - accept-invitation
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
updated_at: '2025-12-14T17:32:20.838Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Accept-Invitation-as-Moderator

## Summary

This procedure allows a secondary user to accept a moderator invitation from the parent Streamlabs account, joining with limited but exploitable permissions.

## Description

Using the invitation link, the moderator user logs in and accepts access, establishing a shared context. This targets the web invitation flow and assumes the inviter has already generated the link. Expected outcome: Moderator role assigned without additional verification.

## Requirements

1. Valid credentials for the moderator Streamlabs account (User B)
2. The invitation link from the parent account
3. Web browser access

## Defense

Defensive measures and detection strategies:

- Require explicit approval workflows for invitations
- Log and alert on invitation acceptances from unknown IPs
- Enforce multi-factor authentication for role acceptances

## Objectives

1. Join the parent account as moderator
2. Confirm shared access status
3. Enable dashboard visibility for the parent account

## Instructions

### Step 1: Log In to Moderator Account

**Context**: Prepare the moderator account by logging in separately.

Log out of any other session, then log in to User B's Streamlabs account at https://streamlabs.com.

**Expected Output**: User B's dashboard loads.

### Step 2: Accept the Invitation

**Context**: Use the provided link to join as moderator.

Paste and open the invitation link in the browser. Follow prompts to accept the moderator role.

**Expected Output**: Confirmation message; User B now appears in User A's shared access list as Moderator.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[shared-access]]
- [[accept-invitation]]
