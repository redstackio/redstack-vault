---
tags:
  - map-load
  - console-command
  - trigger
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Malicious File]]'
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-14T17:24:08.816Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: fceebba0-d87d-4c76-a391-e86b9537b964
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Malicious File]]'
  - '[[Exploitation for Client Execution]]'
---
# Load Malicious Map via CS:GO In-Game Console

## Summary

This procedure triggers the buffer overflow by loading the malformed .BSP file using CS:GO's in-game console, simulating user execution of the malicious map.

## Description

CS:GO's console allows direct commands for map loading, which invokes the engine's .BSP parser. Entering 'map de_fuzz' processes the file's zipFileHeader, encountering the malformed data and causing an access violation due to buffer overflow. This step demonstrates the user-executed vector for RCE, where an attacker could host the map on a malicious server. Prerequisites: Game running, file in place, console enabled.

## Requirements

1. CS:GO launched and in a state where console is accessible
2. Malformed .BSP file deployed in maps directory
3. Console enabled (via launch options -console if needed)

## Defense

Defensive measures and detection strategies:

- Validate map files before loading (e.g., checksums in custom mods)
- Disable console access or restrict map commands in multiplayer settings
- Log console inputs for anomalous map loads

## Objectives

1. Initiate parsing of the malicious .BSP to trigger overflow
2. Reproduce the access violation reliably
3. Highlight the ease of exploitation via user action

## Instructions

### Step 1: Open In-Game Console

**Context**: Access the console interface to enter commands.

Press the ~ (tilde) key while in-game.

> Expected output: Console panel opens at the top of the screen.

### Step 2: Execute Map Load Command

**Context**: Issue the command to load the specific malformed map, starting the vulnerable parsing routine.

Enter the following in the console:

```
map de_fuzz
```

> Expected output: Game attempts to load the map, leading to a crash or freeze as the buffer overflow occurs in zipFileHeader processing.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Malicious File]]
- [[Exploitation for Client Execution]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- map-load
- console-command
- trigger
