---
id: proc-inject-xss-message
name: Inject-XSS-into-Rocket-Chat-Message
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:37.364Z'
tactics:
  - '[[Execution]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
tags:
  - xss
  - injection
commands: []
platforms:
  - Web
tools: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---

# Inject-XSS-into-Rocket-Chat-Message

## Summary

This procedure injects the crafted XSS payload into a Rocket.Chat message using the chat interface, storing it persistently for execution when viewed by users.

## Description

Rocket.Chat allows any user to send messages with markdown, and due to flawed sanitization, nested tags preserve script injection. The attack targets message inputs during testing or normal use. Expected outcomes: Payload stored in database, rendered maliciously on view, affecting all viewers including admins.

## Requirements

1. Valid Rocket.Chat user account with messaging permissions.
2. Access to a channel or direct message.
3. Crafted payload from prior procedure.

## Defense

Defensive measures and detection strategies:

- Input validation on message submission to strip dangerous tags.
- Rate limiting on message sends to prevent spam injections.
- Audit logs for messages containing script-like patterns.

## Objectives

1. Persist the XSS payload in a message.
2. Ensure it renders without immediate detection.
3. Target high-visibility channels for broad impact.

## Instructions

### Step 1: Access Message Input

**Context**: Log in and select a target channel to send the payload.

Navigate to Rocket.Chat, join/create a channel, and click the message compose box.

> No command; UI interaction. Expected: Input field active.

### Step 2: Submit Payload

**Context**: Paste and send the nested markdown payload.

Enter: `**<script>alert('Injected');</script>**` and press Enter.

> Message submits and appears in history. Expected: No errors, payload stored.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[injection]]
