---
tags:
  - server-launch
  - map-deploy
type: procedure
tools:
  - '[[tools/AMX-Mod-X]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:23:28.424Z'
sub_techniques: []
id: da7614bd-3a93-4672-b255-d70511b5f11b
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Start-Server-and-Deploy-Secondary-Map

## Summary

Launches the Counter-Strike server on the initial malicious map and deploys the secondary BSP file after load to complete the exploit chain.

## Description

Starting with +map cs_pwn ensures the client loads the first overflow-triggering file. The secondary map (F558347) is added post-load to potentially chain further execution or handle map changes, exploiting the same buffer overflow vulnerability.

## Requirements

1. Prepared server with maps and plugins
2. Crafted secondary BSP F558347
3. Firewall configured for port 27015

## Defense

Defensive measures and detection strategies:

- Monitor server logs for map load errors
- Restrict map changes to admin-only
- IDS rules for anomalous game traffic

## Objectives

1. Boot server with exploit map
2. Add secondary map dynamically
3. Confirm server stability

## Instructions

### Step 1: Launch Server

**Context**: Start HLDS with cstrike mod and initial map.

Run hlds.exe -console -game cstrike +map cs_pwn +maxplayers 32 -port 27015.

> Console output shows map loading.

### Step 2: Deploy Secondary Map

**Context**: Add F558347 after full load.

Once server console indicates cs_pwn loaded, extract F558347 to SERVER_DIR/cstrike/maps/ (e.g., as cs_pwn2.bsp).

> No restart needed; changelevel command optional.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/AMX-Mod-X]]

## Tags

- [[server-launch]]
- [[map-deploy]]
