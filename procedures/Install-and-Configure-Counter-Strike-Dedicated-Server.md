---
tags:
  - server-setup
  - counter-strike
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
updated_at: '2025-12-14T17:23:28.446Z'
sub_techniques: []
id: f114195c-7d1a-472e-93b4-3c0f6ad2478e
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Install-and-Configure-Counter-Strike-Dedicated-Server

## Summary

This procedure sets up the Counter-Strike Dedicated Server environment on Windows, creating the foundation for hosting malicious maps that exploit the GoldSrc engine vulnerability.

## Description

The GoldSrc engine powers Counter-Strike servers, and this setup involves installing the Half-Life Dedicated Server (HLDS) with the cstrike mod. The server will later serve BSP files with oversized WAD names, causing a stack buffer overflow in the client's TEX_InitFromWad function via COM_FileBase without boundary checks. Prerequisites include a Windows machine and internet access for downloads.

## Requirements

1. Windows OS with administrative privileges
2. Steam account or access to Valve software archives for HLDS
3. Approximately 500MB disk space for installation

## Defense

Defensive measures and detection strategies:

- Monitor for unusual HLDS installations on network endpoints
- Use application whitelisting to restrict game server executables
- Network segmentation to isolate game traffic

## Objectives

1. Establish a functional dedicated server
2. Prepare directory structure for mods and maps
3. Ensure server is configurable for custom plugins

## Instructions

### Step 1: Download and Install HLDS

**Context**: Obtain the base server software from official sources.

Download the Half-Life Dedicated Server installer from SteamCMD or archives, then run it to install into SERVER_DIR (e.g., C:\SERVER_DIR). Select the cstrike mod during setup.

> No specific command; use graphical installer or SteamCMD: steamcmd +login anonymous +force_install_dir SERVER_DIR +app_update 90 validate +quit

### Step 2: Verify Installation

**Context**: Confirm the server binaries and mod directories are present.

Navigate to SERVER_DIR and ensure cstrike folder exists with addons, maps, and dlls subfolders.

> Expected: hlds.exe in root, liblist.gam in cstrike.

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

- [[server-setup]]
- [[counter-strike]]
