---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567891
tags:
  - multiplayer-setup
  - initial-access
  - portal-2
type: procedure
tools:
  - '[[tools/Custom-Portal2-Voice-Exploit-DLL]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Windows
  - Game (Portal 2)
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:08.853Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Establish-Multiplayer-Session-in-Portal-2

## Summary

This procedure sets up a trusted multiplayer session in Portal 2, enabling the exchange of voice data packets between the attacker and victim, which is a prerequisite for exploiting the voice processing vulnerability.

## Description

In the context of the Portal 2 buffer overflow exploit, the attacker must gain initial access to the victim's client through a multiplayer invitation. This involves using Steam's networking to join a session where voice chat is enabled. The procedure assumes both parties have valid Steam accounts and the game installed. Once in the session, voice packets can be sent via the game's protocol, setting the stage for the overflow attack. Expected outcomes include a stable connection allowing real-time data exchange without suspicion.

## Requirements

1. Valid Steam accounts for attacker and victim
2. Portal 2 installed on Windows machines for both
3. Internet connection for Steam matchmaking
4. Victim must initiate the friend invite or lobby join

## Defense

Defensive measures and detection strategies:

- Restrict multiplayer invites to trusted contacts only
- Monitor unusual voice traffic spikes in game logs
- Use Steam's privacy settings to limit friend requests

## Objectives

1. Gain access to victim's game client via multiplayer
2. Enable voice data exchange channel
3. Position for subsequent exploit delivery

## Instructions

### Step 1: Initiate Invitation

**Context**: The victim must invite the attacker to establish trust and enable session setup.

No specific command; use Steam interface:

- Open Steam, navigate to Portal 2 library.
- From friends list, send invite to attacker or create public lobby.

> Victim confirms attacker joins the lobby.

### Step 2: Confirm Session Readiness

**Context**: Verify multiplayer connectivity before proceeding.

- Start a co-op or versus match.
- Test basic in-game communication to ensure voice is active.

> Successful join shows both players in the same session.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Custom-Portal2-Voice-Exploit-DLL]]

## Tags

- [[multiplayer-setup]]
- [[initial-access]]
