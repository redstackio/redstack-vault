---
id: proc-mozilla-hubs-spectator-bypass-001
tags:
  - client-side-bypass
  - spectator-exploit
  - javascript-modification
type: procedure
tools:
  - '[[tools/Chrome-DevTools]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/hubs-add-model]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:30:46.928Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Bypass-Room-Entry-as-Spectator

## Summary

This procedure bypasses Mozilla Hubs' room entry requirement by modifying client-side JavaScript, allowing spectators to execute /add commands and spawn objects without joining, expanding the attack surface to external observers.

## Description

Hubs performs room entry checks client-side in message-dispatch.js (this.scene.is('entered')), which can be tampered with using browser DevTools. This enables unauthorized object placement from spectator mode, targeting webpack-bundled JS in Hubs client. Useful for stealthy disruptions without triggering join logs.

## Requirements

1. Room URL accessible as spectator
2. Chrome browser with DevTools
3. Basic JavaScript knowledge for modifications

## Defense

Defensive measures and detection strategies:

- Move entry checks to server-side with session validation
- Obfuscate or minify client JS to hinder tampering
- Monitor WebSocket traffic for anomalous commands from non-entered sessions

## Objectives

1. Gain command execution without formal room entry
2. Enable external attacks on room integrity
3. Demonstrate client-side enforcement flaws

## Instructions

### Step 1: Load as Spectator

**Context**: Access room without entering to maintain external position.

No command; navigate to room URL but do not click 'Join Meeting'.

> Spectator view loads; chat may be partially available.

### Step 2: Modify Client-Side Check

**Context**: Alter JS to fake entry status.

**Tool**: Use [[tools/Chrome-DevTools]] to enable debugging, open Sources tab, locate webpack://hubs/src/message-dispatch.js, set breakpoint, and modify 'this.scene.is('entered')' to return true.

> JS modification applied; entered flag bypassed.

### Step 3: Execute Spawn Command

**Context**: Run chat command post-modification.

**Command** ([[commands/hubs-add-model]]):
```bash
/add https://quikke.assets.dev.myhubs.net/hubs/assets/models/DuckyMesh-b80f0ece1f58a683839a..glb
```

> Object spawns in room from spectator mode.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/hubs-add-model]]

## Tools Used

- [[tools/Chrome-DevTools]]

## Tags

- [[client-side-bypass]]
- [[spectator-exploit]]
- [[javascript-modification]]
