---
tags:
  - server-hosting
  - malicious-server
  - csgo
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
  - '[[Standard Application Layer Protocol]]'
updated_at: '2025-12-14T17:23:50.075Z'
sub_techniques:
  - '[[Web Protocols]]'
id: c62df62d-787f-43b0-ba45-592f6f7945f3
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Standard Application Layer Protocol]]'
---
# Host-Malicious-Game-Server

## Summary

This procedure sets up and hosts a local CS:GO game server using the malicious 'aim_pwn' map, simulating the environment where victims connect and download the exploit resources.

## Description

Hosting the server loads the map, preparing the malicious texture for delivery. In a real attack, this would be a public server tricking players into joining, leading to automatic resource download and overflow on the client side.

## Requirements

1. CS:GO installed with the malicious map in place.
2. Local network or port forwarding for remote access.
3. Game launched with hosting privileges.

## Defense

Defensive measures and detection strategies:

- Scan hosted maps for anomalies like long filenames.
- Client-side verification of downloaded resources.
- Network monitoring for suspicious server connections.

## Objectives

1. Deploy the malicious map via server.
2. Enable victim connections.
3. Trigger resource download.

## Instructions

### Step 1: Launch CS:GO with Hosting

**Context**: Start the game in a mode that allows server creation.

Run csgo.exe and navigate to the 'Create a Game' menu.

> Game launches to the main menu.

### Step 2: Select and Host Map

**Context**: Choose the malicious map to host.

In the game creation menu, select 'aim_pwn' as the map and start the local server.

> Server hosts successfully, map loads in background.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Standard Application Layer Protocol]]

### Sub-Techniques

- [[Web Protocols]]

## Commands Used


## Tools Used


## Tags

- server-hosting
- malicious-server
- csgo
