---
tags:
  - buffer-overflow
  - bsp
  - deployment
type: procedure
tools:
  - '[[tools/WinDBG]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Malicious File]]'
updated_at: '2025-12-14T17:24:08.828Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: cdc52219-1c4d-4ab0-8b2c-d76a46b5e2b7
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Malicious File]]'
---
# Deploy Malformed BSP File to CS:GO Map Directory

## Summary

This procedure involves placing a pre-crafted malformed .BSP file into the CS:GO map directory, enabling the exploit vector for buffer overflow during map loading. It simulates the delivery phase where a victim is tricked into downloading the file from a malicious source.

## Description

The .BSP file format is used by the Source Engine for storing compiled map data in CS:GO. A malformed version exploits improper bounds checking in the zipFileHeader processing, leading to a buffer overflow. This step assumes the file (e.g., de_fuzz.bsp) has been crafted via fuzzing tools or hex editing to include oversized or invalid header data. Deployment mimics social engineering, such as sharing the file via Discord or a fake mod site, tricking the user into placing it in the maps folder. Prerequisites include CS:GO installed on Windows and knowledge of the file path.

## Requirements

1. Crafted malformed .BSP file (e.g., via fuzzing with tools like American Fuzzy Lop or manual editing)
2. Access to Windows file system and CS:GO installation directory
3. Steam account with CS:GO installed

## Defense

Defensive measures and detection strategies:

- Scan downloaded files with antivirus (e.g., detect anomalies in .BSP files)
- Restrict map loading to verified sources via game settings or mods
- Monitor file placements in game directories for unauthorized additions

## Objectives

1. Position the malicious file for loading without alerting the user
2. Enable seamless integration into the game's asset system
3. Set up for vulnerability trigger in subsequent steps

## Instructions

### Step 1: Locate CS:GO Map Directory

**Context**: Identify the standard installation path for CS:GO maps to ensure correct placement.

Navigate to the directory, typically `C:\Program Files (x86)\Steam\steamapps\common\Counter-Strike Global Offensive\csgo\maps\`.

> Verify the path exists and you have write permissions.

### Step 2: Copy Malformed BSP File

**Context**: Transfer the crafted de_fuzz.bsp file to the maps folder, making it loadable via console.

Use Windows Explorer or command prompt to copy:

```cmd
copy path\to\de_fuzz.bsp "C:\Program Files (x86)\Steam\steamapps\common\Counter-Strike Global Offensive\csgo\maps\de_fuzz.bsp"
```

> Expected output: File copied successfully, no errors. The file is now available for the game to parse.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Malicious File]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/WinDBG]]

## Tags

- buffer-overflow
- bsp
- deployment
