---
id: proc-190870-create-room
tags:
  - xss
  - propagation
  - nextcloud
  - spreed
  - call-room
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:47.159Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Create and Share Spreed Call Room

## Summary

This procedure uses the Spreed plugin to create a call room or public link after payload injection, embedding the stored XSS in the room context to expose it to victims via invitations or shared links.

## Description

Once the XSS payload is in the user name, attackers leverage Spreed's room creation features to invite users or share public rooms. The name renders in the room UI, setting up execution on victim interaction. This targets Nextcloud's web interface; requires prior injection and account access. Expected outcome: Victims receive invites with the tainted room data.

## Requirements

1. Injected XSS payload in user name from prior step.
2. Active Spreed plugin in Nextcloud.
3. List of victim emails or ability to generate shareable links.

## Defense

Defensive measures and detection strategies:

- Sanitize user data in room metadata and invitations.
- Rate-limit room creations and invitations to detect abuse.
- Log and alert on unusual room sharing patterns.

## Objectives

1. Create a room embedding the injected payload.
2. Distribute access to victims.
3. Maximize exposure for subsequent triggering.

## Instructions

### Step 1: Initiate Room Creation

**Context**: Start a new call room in Spreed to include the tainted name.

In the Spreed interface, select to create a single call room.

### Step 2: Invite Participants or Generate Link

**Context**: Add victims or make the room public to propagate the payload.

Invite specific users by email, or opt for a public room and copy the shareable link.

> Expected output: Invites sent or link generated, with the injected name visible in room details.

### Step 3: Distribute to Victims

**Context**: Ensure victims can access the room.

Send the invitation emails or share the public link via external channels.

> Success if victims confirm receipt and can join the room.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- room-creation
- invitation
