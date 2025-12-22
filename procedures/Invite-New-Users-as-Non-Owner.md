---
tags:
  - privilege-escalation
  - invite
  - yelp
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:30:35.262Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 8abbbe6b-5653-4b0d-9379-0cac9b267f9c
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---
# Invite-New-Users-as-Non-Owner

## Summary

This procedure exploits improper access controls in Yelp's business account to allow a non-owner user to invite additional users, bypassing required permissions and adding unauthorized members to the account.

## Description

Yelp's invite functionality is vulnerable to privilege escalation because it lacks proper authorization checks for non-owner roles. A standard business user can navigate to the invite feature, submit emails for new users, and successfully add them, despite documentation and UI suggesting this should be owner-only. This occurs in the web interface, leading to unauthorized expansions of account access. Prerequisites include an active non-owner session from the login procedure.

## Requirements

1. Active session as a non-owner business user
2. List of target email addresses for invitations
3. Web browser with the ability to inspect network requests if needed for verification

## Defense

Defensive measures and detection strategies:

- Enforce strict RBAC on invite endpoints with server-side permission validation
- Log all invite actions with user role details for anomaly detection
- Implement rate limiting on user addition features to prevent abuse

## Objectives

1. Access and utilize the invite feature without owner permissions
2. Successfully add new users to the business account
3. Confirm invitations are processed despite access restrictions

## Instructions

### Step 1: Navigate to Invite Section

**Context**: Locate the invite functionality within the business account settings, which is unexpectedly accessible to non-owners.

No command required; from the dashboard, click on 'Settings' or 'Team' menu, then select 'Invite Users' or equivalent option.

> The form should load without permission errors, allowing input of email addresses.

### Step 2: Submit Invitations

**Context**: Enter and send invites for new users, exploiting the lack of checks.

No command required; fill in email fields (e.g., test@example.com), optionally add roles, and click 'Send Invite'. Watch for a success message.

> Expected output: Confirmation toast or page update stating 'Invitations sent', with new users now associated with the account in the inviter's view.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[invite]]
- [[escalation]]
- [[access-bypass]]
