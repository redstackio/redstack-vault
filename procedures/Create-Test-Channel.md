---
tags:
  - channel-creation
  - setup
  - rocket-chat
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Valid Accounts]]'
skill_level: basic
impact_level: low
detection_risk: low
sub_techniques: []
id: 04f443d4-e990-49c9-8399-d69fb71ccb30
created_at: '2025-12-14T03:47:13.126Z'
updated_at: '2025-12-14T03:47:13.126Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Create-Test-Channel

## Summary

This procedure creates a new channel in Rocket.Chat for testing and payload delivery, using the web interface or API to establish a controlled environment.

## Description

Rocket.Chat channels serve as message containers. Creating a dedicated channel like '#cookies' isolates the attack and facilitates targeting specific users. This step assumes authenticated access and targets public or private channels. Expected outcome: A new channel ready for invitations and posts.

## Requirements

1. Authenticated session or API token in Rocket.Chat
2. Permissions to create channels (default for users)
3. Web interface or API access

## Defense

Defensive measures and detection strategies:

- Log channel creation events and review for suspicious names (e.g., '#cookies')
- Restrict channel creation to trusted users or admins
- Monitor for rapid channel setups followed by invites to high-privilege users

## Objectives

1. Isolate attack operations in a single channel
2. Prepare venue for admin luring and payload viewing
3. Ensure payload persistence for multiple viewers

## Instructions

### Step 1: Use Web Interface

**Context**: Create the channel directly in the UI for simplicity.

1. Log in to Rocket.Chat.
2. Click the '+' icon next to Channels.
3. Select 'Create Channel', name it '#cookies', set as public or private.
4. Save to create.

> Channel appears in the sidebar upon success.

### Step 2: API Alternative

**Context**: If preferring API, use chat.createChannel endpoint.

```bash
curl -H "X-Auth-Token: <Token>" -H "X-User-Id: <user Id>" -H "Content-type:application/json" https://<server>/api/v1/channels.create -d '{"name": "cookies"}'
```

> Expected output: {"channel": {...}} with channel details.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[channel-creation]]
- [[setup]]
- [[rocket-chat]]
