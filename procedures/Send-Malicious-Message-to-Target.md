---
tags:
  - xss
  - stored-xss
  - private-messages
type: procedure
tools:
  - '[[tools/Chrome]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:30.686Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 99f98123-6fde-4366-a7b4-6beff1932713
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Send-Malicious-Message-to-Target

## Summary

This procedure sends the crafted private message containing the stored XSS payload to the target user, storing the malicious content in the CMS database for later triggering.

## Description

After composing the message, the attacker submits the form via the Concrete CMS interface. The payload is stored server-side and displayed sanitized in the inbox view, preventing immediate execution. This step relies on the target's interaction (replying) to activate the XSS. The attack targets users like admins who may reply to messages, leading to JS execution in their browser.

## Requirements

1. Authenticated session from previous procedure
2. Composed message with payload ready
3. Target user must have messaging enabled

## Defense

Defensive measures and detection strategies:

- Sanitize all stored message content at storage and display levels
- Rate-limit message sending to prevent spam-like attacks
- Log and alert on messages containing script-like patterns

## Objectives

1. Deliver payload to target's inbox
2. Ensure payload survives storage without defusing
3. Await victim interaction for exploitation

## Instructions

### Step 1: Submit the Message Form

**Context**: Send the private message to the target.

Click submit on the composition form at `index.php/account/messages/write/{user_id}`.

**Expected Output**: Success message; entry in sender's sent items.

### Step 2: Verify Storage

**Context**: Optionally check sender's outbox to confirm payload storage.

Navigate to inbox/sent and view the message; payload should appear but not execute.

**Expected Output**: Sanitized view of message content.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Chrome]]

## Tags

- xss
- stored-xss
- private-messages
