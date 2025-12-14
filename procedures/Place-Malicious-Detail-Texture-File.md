---
id: proc-goldsrc-place-detail-file
tags:
  - rce
  - stack-overflow
  - file-placement
type: procedure
tools:
  - '[[tools/WinDbg]]'
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
updated_at: '2025-12-14T17:23:41.611Z'
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
# Place-Malicious-Detail-Texture-File

## Summary

This procedure involves crafting a malformed detail texture file (_detail.txt) and placing it in the game's maps directory to set up exploitation of the stack overflow vulnerability in hw.dll for GoldSrc games like Counter-Strike.

## Description

The attack targets the parsing logic in hw.dll, which lacks bounds checking when loading map-specific detail texture files (e.g., cs_assault_detail.txt). By creating a file with excessive or invalid data, an attacker prepares the environment for overflow during game map loading. This is typically done on a listen server client or dedicated server, requiring file system access to the game's installation directory.

## Requirements

1. Access to the Counter-Strike installation directory (cstrike/maps)
2. Crafted malicious _detail.txt file (e.g., oversized binary data to trigger overflow)
3. Windows environment with GoldSrc game installed

## Defense

Defensive measures and detection strategies:

- Disable detail textures via r_detailtextures 0 in server configs
- Validate and scan downloaded map files for anomalies using antivirus
- Monitor file placements in game directories for unauthorized modifications

## Objectives

1. Position the malicious file for automatic loading during map initialization
2. Ensure compatibility with target map (e.g., cs_assault)
3. Prepare for feature enablement to trigger parsing

## Instructions

### Step 1: Craft the Malicious File

**Context**: Generate a malformed cs_assault_detail.txt with data exceeding buffer limits to cause stack overflow in hw.dll parsing.

No command; manually create/edit the file using a text editor or hex editor, appending excessive texture definitions or binary junk.

> Use tools like a hex editor to insert overflow payloads. Expected output: File saved with size large enough to overflow (e.g., > buffer limit in hw.dll).

### Step 2: Place File in Directory

**Context**: Copy the file to the appropriate maps folder for loading.

No command; use file explorer or copy command:

```bash
copy cs_assault_detail.txt c:\Program Files\Counter-Strike\cstrike\maps\
```

> Places the file where the game expects it. Expected output: File confirmed in cstrike/maps.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/WinDbg]]

## Tags

- rce
- stack-overflow
- file-placement
