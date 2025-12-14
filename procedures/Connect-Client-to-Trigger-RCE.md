---
id: uuid-step5
tags:
  - client-exploit
  - rce
  - rop-chain
type: procedure
tools:
  - Counter-Strike 1.6 client
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Client Execution]]'
  - '[[Process Injection]]'
updated_at: '2025-12-14T17:24:14.435Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
  - '[[Process Injection]]'
---
# Connect-Client-to-Trigger-RCE

## Summary

Connects a vulnerable Counter-Strike 1.6 client to the malicious server, triggering the WeaponList underflow and ROP chain for code execution.

## Description

Upon connection, the plugin sends a crafted InitHUD message followed by WeaponList with negative iId, causing underflow in rgWeapons[-x] to overwrite gEngfuncs. This redirects control flow to ROP gadgets in HUD_DirectorMessage and SendCmd, executing system() with calc.exe. Targets unpatched clients. Outcome: Arbitrary code runs on client without privileges.

## Requirements

1. Vulnerable CS 1.6 client (pre-patch)
2. Network access to server IP
3. No anti-cheat interference

## Defense

Defensive measures and detection strategies:

- Patch client.dll for bounds checking
- Avoid connecting to unknown servers
- Monitor for unexpected process launches like calc.exe

## Objectives

1. Establish client-server connection
2. Deliver exploit payload
3. Achieve RCE confirmation

## Instructions

### Step 1: Launch Client

**Context**: Start the game.

Execute hl.exe -game cstrike.

### Step 2: Connect to Server

**Context**: Trigger exploitation.

In console, enter 'connect <server_ip>:27015' to join and receive messages.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution
- [[Process Injection]] Process Injection

### Sub-Techniques


## Commands Used


## Tools Used

- Counter-Strike 1.6 client

## Tags

- client-exploit
- rce
- rop-chain
