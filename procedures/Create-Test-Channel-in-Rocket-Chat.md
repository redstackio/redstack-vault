---
id: proc-rocket-chat-create-channel
tags:
  - setup
  - electron
type: procedure
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Electron
  - macOS
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:23:28.589Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-Test-Channel-in-Rocket-Chat

## Summary

This procedure sets up a new channel in the Rocket.Chat Desktop application to safely test malicious payloads without affecting other users or production environments.

## Description

In the context of exploiting Rocket.Chat Desktop, creating a dedicated test channel provides an isolated space to send crafted messages. The Rocket.Chat Desktop app, built on Electron, renders chat messages using a Markdown parser vulnerable to attribute injection. This step assumes the attacker has access to send messages in the app, either as a legitimate user or via social engineering to get the victim to interact.

## Requirements

1. Installed and running Rocket.Chat Desktop application.
2. Authentication to the Rocket.Chat server (username/password or token).
3. Network connectivity to the chat server.

## Defense

Defensive measures and detection strategies:

- Monitor for unusual channel creation patterns in audit logs.
- Enforce channel creation policies requiring admin approval.
- Use endpoint detection to flag rapid channel setups in Electron apps.

## Objectives

1. Establish a controlled testing environment.
2. Prepare for payload delivery.
3. Minimize detection risk during initial setup.

## Instructions

### Step 1: Launch Application and Authenticate

**Context**: Open the Rocket.Chat Desktop app and log in to ensure access to channel management features.

No specific command; use the app's UI to log in with valid credentials.

> Expected: Dashboard loads with existing channels visible.

### Step 2: Create New Channel

**Context**: Use the channel creation interface to make a new private or public channel.

No specific command; click the "+" icon next to channels, select "Create Channel", name it (e.g., "test-xss"), and confirm.

> Expected: New channel appears in the list, ready for messages.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[setup]]
- [[electron]]
