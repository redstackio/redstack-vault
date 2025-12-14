---
id: proc-steam-broadcast-start-001
tags:
  - steam
  - broadcast
  - initial-access
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
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:27:35.518Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Start-Steam-Broadcast

## Summary

This procedure initiates a live broadcast session on Steam Community, generating a unique URL that exposes the Steam ID necessary for subsequent CSRF targeting in the broadcast chat feature.

## Description

In the context of a CSRF attack on Steam's broadcast chat, starting a broadcast provides the foundational URL structure. The vulnerability lies in the chat moderation endpoint, but this step sets up the target environment by creating an active session with a parseable ID. Expected outcomes include a live broadcast ready for ID extraction and potential exploitation.

## Requirements

1. Active Steam account with broadcasting enabled
2. Web browser access to steamcommunity.com
3. Stable internet connection for live streaming

## Defense

Defensive measures and detection strategies:

- Monitor for unusual broadcast initiations from moderator accounts
- Implement rate limiting on broadcast starts
- Educate users on verifying broadcast URLs before sharing

## Objectives

1. Create an active broadcast session
2. Generate a target URL for ID extraction
3. Establish prerequisites for CSRF payload crafting

## Instructions

### Step 1: Log In and Access Broadcasting

**Context**: Authenticate and navigate to the broadcasting interface to begin the session.

Log into your Steam account at steamcommunity.com and select the "Broadcast" option from the community features.

### Step 2: Initiate Live Broadcast

**Context**: Start the live stream to generate the unique broadcast URL.

Click "Go Live" or equivalent to begin broadcasting, which creates a URL like `https://steamcommunity.com/broadcast/watch/{STEAM ID}/`.

> This URL is shareable and contains the embedded Steam ID; copy it for the next step.

**Expected Output**: Confirmation of live status and the broadcast URL displayed.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[steam]]
- [[broadcast]]
- [[initial-access]]
