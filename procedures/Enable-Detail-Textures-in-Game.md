---
id: proc-goldsrc-enable-detail-textures
tags:
  - rce
  - feature-enable
  - console-command
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/r-detailtextures-1]]'
verified: false
platforms:
  - Windows
  - Game (GoldSrc Engine)
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[User Execution]]'
updated_at: '2025-12-14T17:23:41.606Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[User Execution]]'
---
# Enable-Detail-Textures-in-Game

## Summary

This procedure activates the detail textures feature in GoldSrc games via console command, forcing the engine to load and parse vulnerable _detail.txt files during map initialization, setting up the stack overflow exploit.

## Description

In Counter-Strike, the r_detailtextures cvar controls whether the game loads additional texture detail files for maps. Enabling it (value 1) triggers hw.dll to parse these files without bounds checks, allowing malformed input to overflow the stack. This step is manual on clients but can be forced remotely via server plugins.

## Requirements

1. Running instance of Counter-Strike
2. Console access (enabled via ~ key)
3. Malicious _detail.txt already placed

## Defense

Defensive measures and detection strategies:

- Set r_detailtextures 0 in autoexec.cfg or server cvars
- Log console command executions on servers
- Patch hw.dll or use updated GoldSrc builds

## Objectives

1. Activate parsing of detail texture files
2. Ensure vulnerability trigger on next map load
3. Prepare for overflow during client execution

## Instructions

### Step 1: Launch Game and Open Console

**Context**: Start Counter-Strike and access the developer console to issue commands.

No command; launch the game executable and press ~ to open console.

> Expected output: Console prompt appears.

### Step 2: Enable Detail Textures

**Context**: Set the cvar to load detail files, priming the exploit.

**Command** ([[commands/r-detailtextures-1]]):
```bash
r_detailtextures 1
```

> This enables the feature; game will parse _detail.txt on map load. Expected output: No error, feature activated.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[User Execution]]

### Sub-Techniques


## Commands Used

- [[commands/r-detailtextures-1]]

## Tools Used


## Tags

- rce
- feature-enable
- console-command
