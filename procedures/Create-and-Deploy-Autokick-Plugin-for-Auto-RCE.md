---
id: proc-csgo-autokick-deploy-001
tags:
  - rce
  - auto-exploit
  - sourcemod
type: procedure
tools:
  - '[[tools/SourceMod]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/kickclient-with-ban-payload]]'
verified: false
platforms:
  - Windows
  - Game
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-14T17:24:14.840Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Exploitation for Client Execution]]'
---
# Create and Deploy Autokick Plugin for Auto-RCE

## Summary

This procedure develops and deploys an automated SourceMod plugin that kicks players with an RCE payload immediately after spawn, eliminating the need for manual interaction.

## Description

The autokick.smx hooks the player_spawn event, sets a 0.1s timer, and calls KickClient with an escaped ban-style payload. The mouse centers on kick, ensuring hover triggers the onmouseover JS to open local files via SteamOverlayAPI, enabling no-interaction RCE for potential botnet recruitment.

## Requirements

1. SourcePawn development environment
2. Server access for deployment
3. Testing clients

## Defense

Defensive measures and detection strategies:

- Event hooking restrictions
- Auto-kick detection in logs
- UI sandboxing from system APIs

## Objectives

1. Automate payload delivery
2. Achieve interaction-free RCE
3. Scale to multiple victims

## Instructions

### Step 1: Develop Plugin Code

**Context**: Hook spawn and delay kick.

In SourcePawn: public void OnPluginStart() { HookEvent("player_spawn", Event_PlayerSpawned); } Then in event: CreateTimer(0.1, Timer_Kick, client); In timer: [[commands/kickclient-with-ban-payload]].

> Expected output: Payload prepared with escapes for ban popup.

### Step 2: Compile and Deploy

**Context**: Place on server for auto-execution.

Compile to autokick.smx, copy to plugins folder, restart server.

> Expected output: Plugin loads, kicks on spawn.

### Step 3: Test Auto-Trigger

**Context**: Connect and spawn to verify.

Join server; on spawn, auto-kick with payload.

> Expected output: RCE triggers on default mouse position.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]
- [[Exploitation for Client Execution]]

### Sub-Techniques


## Commands Used

- [[commands/kickclient-with-ban-payload]]

## Tools Used

- [[tools/SourceMod]]

## Tags

- rce
- auto-exploit
- sourcemod
