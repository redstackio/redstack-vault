---
id: proc-csgo-craft-payload
tags:
  - rop-chain
  - fake-object
  - payload-injection
type: procedure
tools:
  - '[[tools/Python-3-Script-for-CSGO-Exploit]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Process Hollowing]]'
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-14T17:24:08.941Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Process Hollowing]]'
  - '[[Exploitation for Client Execution]]'
---
# Craft-and-Send-Payload-as-Map-Name

## Summary

This procedure crafts a ROP chain and fake IClientNetworkable object into a map name payload, sending it multiple times to the connecting CS:GO client to stage the exploit in memory, bypassing null character limitations in string handling.

## Description

Using the known global address for the map name, the payload includes ROP gadgets from client_panorama.dll and tier0.dll, plus a vtable for the fake object to hijack virtual calls. The Python script implements Protocol Buffer serialization for server messages. Target is Windows CS:GO client; prerequisites: base address and variable offset. Expected outcome: Payload reliably loaded without corruption.

## Requirements

1. Python 3 with Protocol Buffers library installed.
2. Malicious CS:GO server running (e.g., via srcds).
3. Victim client connected or connecting.

## Defense

Defensive measures and detection strategies:

- Limit map name length and validate characters server-side.
- Detect repeated identical map name sends as anomalous.
- Use memory integrity checks for global strings.

## Objectives

1. Primary objective: Stage ROP and fake object in client memory.
2. Secondary objective: Handle string null termination.
3. Expected outcome: Payload ready for EntityMsg trigger.

## Instructions

### Step 1: Generate ROP Chain

**Context**: Build gadgets for flow control to LaunchProcess.

Use ROPgadget or manual search in client_panorama.dll.

> Find pop/ret, etc., chaining to IProcessUtils::LaunchProcess("calc.exe"). Expected output: Byte array of chain.

### Step 2: Construct Fake Object

**Context**: Create vtable pointing to ROP entry.

Define fake IClientNetworkable with vptr to payload.

> Pad structure to align with entity size. Expected output: Fake object bytes.

### Step 3: Embed and Send via Script

**Context**: Inject into map name and send repeatedly.

Configure Python script with CLIENT_BASE and payload.

> Run script to send as CSVCMsg_ServerInfo map field multiple times. Expected output: Client copies payload to global.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Process Hollowing]] Process Hollowing
- [[Exploitation for Client Execution]] Exploitation for Client Execution

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Python-3-Script-for-CSGO-Exploit]]

## Tags

- [[rop-chain]]
- [[fake-object]]
- [[payload-injection]]
