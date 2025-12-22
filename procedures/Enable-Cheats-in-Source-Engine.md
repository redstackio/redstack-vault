---
id: proc-enable-cheats-source
tags:
  - cheats-enable
  - privilege-escalation
  - game-config
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/sv-cheats-1]]'
verified: false
platforms:
  - Windows
  - Source Engine
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Abuse Elevation Control Mechanism]]'
updated_at: '2025-12-14T17:26:27.091Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Abuse Elevation Control Mechanism]]'
---
# Enable-Cheats-in-Source-Engine

## Summary

This procedure enables cheat mode in the Source Engine via console command, unlocking restricted commands like mat_crosshair_edit necessary for the exploitation chain.

## Description

The sv_cheats cvar must be set to 1 to allow developer commands. In single-player or controlled server environments, this bypasses restrictions, enabling the vulnerable material editor. Without this, mat_crosshair_edit is blocked, preventing RCE.

## Requirements

1. Game loaded with console access
2. Local server or single-player mode
3. No server-side cheat restrictions

## Defense

Defensive measures and detection strategies:

- Enforce sv_cheats 0 on all servers
- Monitor console logs for cheat enables
- Use anti-cheat software to block cvar changes

## Objectives

1. Unlock cheat commands
2. Prepare for vulnerable command invocation
3. Maintain game stability post-enable

## Instructions

### Step 1: Open Console and Enable Cheats

**Context**: Set the server variable to permit cheats.

**Command** ([[commands/sv-cheats-1]]):
```bash
sv_cheats 1
```

> Console outputs confirmation; cheats are now active. Test with a simple command if needed.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Abuse Elevation Control Mechanism]] Abuse Elevation Control Mechanism

### Sub-Techniques


## Commands Used

- [[commands/sv-cheats-1]]

## Tools Used


## Tags

- cheats-enable
- privilege-escalation
