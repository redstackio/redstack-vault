---
id: proc-csgo-server-setup-001
tags:
  - setup
  - server
  - sourcemod
type: procedure
tools:
  - '[[tools/SourceMod]]'
  - '[[tools/Metamod]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Windows
  - Game
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[External Remote Services]]'
updated_at: '2025-12-14T17:24:14.863Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[External Remote Services]]'
---
# Setup CS:GO Dedicated Server with SourceMod

## Summary

This procedure sets up a dedicated CS:GO server and installs Metamod and SourceMod to enable custom plugin development for payload delivery via kick commands.

## Description

Valve provides documentation for dedicated servers. After setup, Metamod loads SourceMod, allowing plugins to hook events and execute server-side logic like custom kicks without message length limits, ideal for XSS payloads.

## Requirements

1. Windows machine for hosting
2. SteamCMD for server files
3. Administrative access

## Defense

Defensive measures and detection strategies:

- Monitor server plugin installations
- Restrict mod usage on official servers
- Validate plugin sources

## Objectives

1. Establish controlled server
2. Enable mod framework
3. Prepare for plugin deployment

## Instructions

### Step 1: Install Dedicated Server

**Context**: Download and configure base CS:GO server using SteamCMD.

Follow https://developer.valvesoftware.com/wiki/Counter-Strike:_Global_Offensive_Dedicated_Servers to install via SteamCMD.

> Expected output: Server executable ready in csgo directory.

### Step 2: Install Metamod and SourceMod

**Context**: Add mod support for plugins.

Download from https://www.sourcemm.net/ and https://wiki.alliedmods.net/Installing_sourcemod, extract to csgo/addons folder, configure metamod.vdf and sourcemod configs.

> Expected output: sm version command works in server console.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[External Remote Services]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/SourceMod]]
- [[tools/Metamod]]

## Tags

- setup
- server
- sourcemod
