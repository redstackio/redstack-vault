---
tags:
  - web
  - email
  - invitation
type: procedure
tools: []
tactics: []
commands: []
verified: false
platforms:
  - Web
submitted: true
techniques: []
sub_techniques: []
id: 7a037475-8c17-4ca3-8c88-c23d4dabb70e
created_at: '2025-12-14T03:46:38.265Z'
updated_at: '2025-12-14T03:46:38.265Z'
validated: true
---
# Enter Victim Email and Send Invitation

## Summary

Provides the victim's email and submits the invitation, storing the injected XSS payload.

## Description

After injecting the payload into the name field, this completes the form by entering the target victim's email and sending the invitation. The payload is stored server-side and included in the invitation email or team view.

## Requirements

1. Completed name field with payload
2. Victim's valid email address
3. Form still open

## Defense

Defensive measures and detection strategies:

- Scan invitation payloads for malicious patterns before sending
- Require approval workflows for team invitations
- Monitor email send logs

## Objectives

1. Deliver the malicious invitation
2. Store the payload for later retrieval

## Instructions

### Step 1: Fill Email and Submit

**Context**: Finalize and dispatch the tainted invitation.

Action:

Enter the victim's email in the email field, then click submit to send the invitation.

> Submission should succeed, sending an email to the victim with a join link. The stored name payload travels with the invitation data.

## MITRE ATT&CK Mapping

### Tactics


### Techniques


### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- web
- email
- invitation
