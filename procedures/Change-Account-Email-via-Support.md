---
id: d4e5f6g7-h8i9-0123-defg-456789012345
tags:
  - support-bypass
  - account-manipulation
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:32:58.371Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Change-Account-Email-via-Support

## Summary

This procedure coordinates with support agents to update the account's email address to a new one under attacker control, exploiting the lack of reset token invalidation during this process.

## Description

The attacker initiates a chat with NordVPN support (e.g., agents Claudia and Marcus) and requests an email change from main@main.com to main2@main2.com. Support processes this without checking or revoking active reset tokens, leaving the old link vulnerable. This social engineering element combined with the technical flaw enables the takeover.

## Requirements

1. Access to support chat interface
2. Valid account details for verification by support
3. Control over the new email address (main2@main2.com)

## Defense

Defensive measures and detection strategies:

- Automate email changes to always invalidate active sessions/tokens
- Require multi-factor verification for support-mediated changes
- Log and review support interactions for suspicious patterns

## Objectives

1. Migrate email to attacker-controlled address
2. Avoid triggering token invalidation
3. Maintain validity of the original reset link

## Instructions

### Step 1: Initiate Support Chat

**Context**: Contact support to begin the email change request.

Navigate to the support section and start a live chat session.

> Explain the need for email update, providing necessary account verification.

### Step 2: Request and Confirm Email Change

**Context**: Instruct support to update the email and verify completion.

Request change from main@main.com to main2@main2.com; wait for agents to process and confirm.

> Receive confirmation message that the update is complete.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[support-engineering]]
- [[email-change]]
