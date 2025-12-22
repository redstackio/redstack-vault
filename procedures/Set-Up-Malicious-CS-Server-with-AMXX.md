---
id: uuid-step1
tags:
  - server-setup
  - amxx
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
updated_at: '2025-12-14T17:24:14.451Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Set-Up-Malicious-CS-Server-with-AMXX

## Summary

This procedure sets up a Counter-Strike 1.6 dedicated server integrated with AMX Mod X to support malicious plugins for exploiting client vulnerabilities.

## Description

The setup involves downloading and configuring the CS 1.6 server binaries on a Windows machine, then installing AMX Mod X as a mod to enable plugin execution. This environment allows sending crafted network messages to connected clients, targeting the WeaponList parser in client.dll. Prerequisites include a Windows system with administrative privileges and internet access for downloads. Expected outcome is a running server ready for plugin deployment.

## Requirements

1. Windows OS with admin access
2. Download CS 1.6 dedicated server from Valve/Steam
3. AMX Mod X installer package
4. Basic networking knowledge to configure ports

## Defense

Defensive measures and detection strategies:

- Monitor for unusual game server traffic or plugin loads
- Use client-side patches or updated game versions to prevent connection to untrusted servers
- Network firewalls to block outbound connections to suspicious IPs

## Objectives

1. Establish exploit hosting environment
2. Enable plugin-based message crafting
3. Prepare for client targeting

## Instructions

### Step 1: Install CS Dedicated Server

**Context**: Download and extract the base server files.

Download the Half-Life dedicated server (HLDS) with CS 1.6 mod from official sources, extract to a directory like C:\hldssrc, and run hlds.exe -game cstrike to verify basic functionality.

### Step 2: Integrate AMX Mod X

**Context**: Add mod support for plugins.

Extract AMX Mod X to the cstrike\addons folder, copy modules to cstrike\dlls, and edit liblist.gam to include addons\amxmodx\dlls\amxmodx_mm_i386.dll. Restart the server to load the mod.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/AMX-Mod-X]]

## Tags

- server-setup
- amxx
- counter-strike
