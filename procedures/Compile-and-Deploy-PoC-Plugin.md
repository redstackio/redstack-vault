---
id: uuid-step2
tags:
  - plugin-compile
  - poc
  - amxx
type: procedure
tools:
  - '[[tools/AMXX-Compiler]]'
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
updated_at: '2025-12-14T17:24:14.445Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
---
# Compile-and-Deploy-PoC-Plugin

## Summary

Compiles the proof-of-concept AMXX plugin (poc_calc_pop.sma) that intercepts HUD messages and sends crafted WeaponList data to trigger client memory corruption.

## Description

The plugin exploits the lack of bounds checking in CHudAmmo::MsgFunc_WeaponList by using a negative iId value to underflow the rgWeapons array, overwriting gEngfuncs. It chains ROP gadgets from HUD_DirectorMessage and SendCmd to execute calc.exe. This procedure requires the AMXX compiler and source script. Outcome: Deployed plugin ready to execute on server start.

## Requirements

1. AMXX compiler installed
2. poc_calc_pop.sma source file
3. Access to server plugins folder

## Defense

Defensive measures and detection strategies:

- Scan plugins for malicious code before loading
- Client-side input validation updates
- Server logging for unusual message sends

## Objectives

1. Build the exploit plugin
2. Integrate into server configuration
3. Verify plugin activation

## Instructions

### Step 1: Compile the Script

**Context**: Generate the binary plugin file.

Run the AMXX compiler on poc_calc_pop.sma to produce poc_calc_pop.amxx.

### Step 2: Deploy to Server

**Context**: Place and enable the plugin.

Copy poc_calc_pop.amxx to cstrike\addons\amxmodx\plugins, then add 'poc_calc_pop' to plugins.ini in the same directory.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/AMXX-Compiler]]

## Tags

- plugin-compile
- poc
- amxx
