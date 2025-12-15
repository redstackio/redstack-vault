---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567893
tags:
  - dll-injection
  - packet-crafting
  - buffer-overflow
  - portal-2
type: procedure
tools:
  - '[[tools/Custom-Portal2-Voice-Exploit-DLL]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Windows
  - Game (Portal 2)
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Dynamic-link Library Injection]]'
updated_at: '2025-12-14T17:24:08.850Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Dynamic-link Library Injection]]'
---
# Inject-Malicious-DLL-to-Send-Crafted-Voice-Packets

## Summary

This procedure involves injecting a custom DLL into the attacker's Portal 2 process to generate and transmit oversized voice packets, exploiting the lack of length validation in the victim's buffer.

## Description

The DLL (ID: F630586) hooks into the game's networking code to create CLC_VoiceData messages with m_nLength exceeding the 4096-byte voiceDataBuffer size. The root cause is the unvalidated ReadBits call in CGameClient::ProcessVoiceData and the SV_BroadcastVoiceData function's inadequate Bits2Bytes conversion. Source code for the DLL is available (ID: F630587). This leads to stack overflow and shellcode execution on the victim.

## Requirements

1. Running Portal 2 process on attacker's Windows machine
2. DLL injection tool (e.g., standard Windows injector)
3. Knowledge of game process ID (portal2.exe)
4. Active multiplayer session

## Defense

Defensive measures and detection strategies:

- Enable Data Execution Prevention (DEP) and ASLR in Windows
- Scan for unauthorized DLLs in game processes using tools like Process Explorer
- Valve anti-cheat detection for injected modules

## Objectives

1. Load exploit payload into attacker's client
2. Craft malicious voice packets
3. Transmit to victim to trigger overflow

## Instructions

### Step 1: Identify Process

**Context**: Locate the Portal 2 executable for injection.

- Use Task Manager or Process Explorer to find portal2.exe PID.

> Note the process ID, e.g., 1234.

### Step 2: Inject DLL

**Context**: Load the malicious DLL into the process.

- Use an injector: e.g., via LoadLibrary call on DLL path.
- Target PID from Step 1, inject F630586.dll.

> DLL loads; hooks activate to monitor voice send functions.

### Step 3: Trigger Packet Send

**Context**: Simulate voice input to send crafted data.

- In-game, activate voice chat; DLL intercepts and modifies packets to oversized length.

> Network capture shows large CLC_VoiceData messages sent.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Dynamic-link Library Injection]] Dynamic-link Library Injection

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Custom-Portal2-Voice-Exploit-DLL]]

## Tags

- [[dll-injection]]
- [[packet-crafting]]
