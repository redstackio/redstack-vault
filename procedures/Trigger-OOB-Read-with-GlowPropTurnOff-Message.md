---
id: proc-source-glowprop-trigger
tags:
  - oob-read
  - trigger
  - rce
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
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-14T17:24:08.899Z'
skill_level: advanced
impact_level: critical
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
---
# Trigger-OOB-Read-with-GlowPropTurnOff-Message

## Summary

This procedure sends a crafted GlowPropTurnOff usermessage with a large entity index to trigger an out-of-bounds read, accessing the fake object in memory and hijacking control flow via vtable to execute the ROP chain for RCE.

## Description

Immediately after sending the payload, the plugin transmits GlowPropTurnOff with entidx set to a large value like 0xfe43167, which overflows after shl eax,4 to point to the controlled memory. This leads to a call to GetBaseEntity() through the fake vtable, executing ROP gadgets and ultimately running arbitrary code like calc.exe on the client.

## Requirements

1. Payload already sent via ShowMenu
2. SourceMod plugin loaded
3. Vulnerable client connected

## Defense

Defensive measures and detection strategies:

- Add upper bound checks (ent_idx < 2048) in handlers
- Crash on invalid entity access instead of silent read
- Network monitoring for suspicious usermessage patterns

## Objectives

1. Trigger OOB read to access fake handle
2. Hijack vtable for ROP execution
3. Achieve RCE on client

## Instructions

### Step 1: Prepare Trigger Message

**Context**: Set up the overflowing entity index.

In plugin, calculate entidx to overflow to payload address (e.g., 0xfe43167 based on shift).

> Ensure timing: Send right after ShowMenu.

### Step 2: Send GlowPropTurnOff

**Context**: Transmit to exploit the handler.

```pawn
Handle msg = StartMessageOne("GlowPropTurnOff", client);
PbSetInt(msg, "entidx", 0xfe43167);
EndMessage();
```

> Triggers entitylist[overflow] -> fake vtable -> ROP.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/SourceMod]]

## Tags

- exploit-trigger
- vtable-hijack
- rop-execution
