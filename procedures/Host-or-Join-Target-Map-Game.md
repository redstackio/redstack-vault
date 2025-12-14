---
id: proc-goldsrc-host-join-map
tags:
  - rce
  - map-loading
  - game-hosting
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Windows
  - Game (GoldSrc Engine)
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:23:41.600Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Host-or-Join-Target-Map-Game

## Summary

This procedure involves hosting a listen server or joining a dedicated server on a specific map (e.g., cs_assault) to trigger the loading and parsing of the malicious detail texture file, initiating the stack overflow.

## Description

Once the malicious file is placed and the feature enabled, loading the target map causes the GoldSrc engine to seek and parse the corresponding _detail.txt file in hw.dll. This step simulates or executes the vulnerability trigger in a game context, applicable to both local and remote scenarios.

## Requirements

1. Counter-Strike client or server software
2. Network connectivity for joining servers
3. Target map (cs_assault) and malicious file in place

## Defense

Defensive measures and detection strategies:

- Restrict map rotations to verified files only
- Monitor server logs for unusual map loads or crashes
- Use client-side file integrity checks

## Objectives

1. Force engine to load the vulnerable map
2. Initiate parsing of _detail.txt
3. Observe initial overflow effects

## Instructions

### Step 1: Host Listen Server

**Context**: For local testing, create a game instance on the target map.

No command; from main menu, select New Game > cs_assault.

> Expected output: Map loads, detail file parsed if enabled.

### Step 2: Join Dedicated Server

**Context**: Connect to a remote server running the map for exploitation.

No command; use console connect <server_ip> or server browser.

> Expected output: Client joins, downloads assets, parses file leading to overflow.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- rce
- map-loading
- game-hosting
