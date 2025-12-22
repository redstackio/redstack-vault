---
id: proc-invite-trigger-xss
tags:
  - xss-trigger
  - admin-invite
  - account-takeover
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
  - '[[JavaScript]]'
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:31:18.944Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Valid Accounts]]'
---
---

# Invite-Admin-and-Trigger-XSS

## Summary

This procedure invites an admin to the malicious channel and simulates admin interaction to trigger the stored XSS, executing JavaScript in the admin's context for potential session theft.

## Description

After creation, invite the admin via UI. As admin, editing the invalid room name calls saveRoomSettings, which invokes getValidRoomName and reflects the payload in an unescaped toastr error via handleError in app/utils/client/lib/handleError.js. This leads to XSS execution upon save.

## Requirements

1. Malicious channel created with payload
2. Admin account credentials
3. Web access to the instance

## Defense

Defensive measures and detection strategies:

- Sanitize room names on save and escape toastr inputs
- Require multi-factor authentication for admins
- Audit room edits for anomalous payloads

## Objectives

1. Induce admin to interact with the channel
2. Execute XSS for privilege escalation
3. Confirm payload reflection

## Instructions

### Step 1: Invite Admin

**Context**: Add admin to the channel as attacker.

**Instructions**: In the channel settings, use the invite feature to add the admin user.

**Expected Output**: Admin receives invitation and joins.

### Step 2: Switch to Admin Session

**Context**: Log in as admin to simulate victim.

**Instructions**: Log out of attacker, log in with admin credentials.

### Step 3: Edit Channel Name

**Context**: Modify the name to trigger validation error.

**Instructions**: Go to channel settings, change name (e.g., 'me' to 'you'), and click save.

**Expected Output**: Error dialog with XSS execution (alert(origin)).

### Step 4: Validate Execution

**Context**: Observe payload impact.

**Instructions**: Note the alert; in real attacks, replace with session-stealing code.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[JavaScript]]
- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss-trigger
- admin-invite
- account-takeover

