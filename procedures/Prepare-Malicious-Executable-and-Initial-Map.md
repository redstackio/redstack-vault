---
tags:
  - payload-prep
  - bsp-map
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
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-14T17:23:28.435Z'
sub_techniques: []
id: c155bca8-6e0a-438b-992d-b76ba1d13a92
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
---
# Prepare-Malicious-Executable-and-Initial-Map

## Summary

Prepares the malicious payload executable and deploys the first crafted BSP map file to the server's maps directory, setting up the initial overflow trigger.

## Description

The executable (pwn.ed) is placed for download post-exploit, while F558346 is a BSP file with long WAD names that overflow the stack buffer in COM_FileBase when processed by TEX_InitFromWad on the client. This map is named cs_pwn.bsp for server loading.

## Requirements

1. Crafted BSP file F558346
2. Malicious .exe file (e.g., trojan)
3. SERVER_DIR with cstrike structure

## Defense

Defensive measures and detection strategies:

- Validate BSP files for oversized lumps (WAD list)
- Block unsigned executables in game directories
- Use file integrity monitoring on maps folder

## Objectives

1. Position payload for post-exploit download
2. Place initial malicious map
3. Ensure files are accessible via server

## Instructions

### Step 1: Copy Executable

**Context**: Place pwn.ed in the cstrike root for client-side download.

Copy the .exe to SERVER_DIR/cstrike/pwn.ed.

> Ensure it's executable and not quarantined.

### Step 2: Extract Initial Map

**Context**: Deploy F558346 as cs_pwn.bsp.

Extract or copy F558346 to SERVER_DIR/cstrike/maps/cs_pwn.bsp.

> Verify file size and BSP header integrity.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploitation for Client Execution]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[payload-prep]]
- [[bsp-map]]
