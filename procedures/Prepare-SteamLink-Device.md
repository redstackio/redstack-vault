---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567892
tags:
  - steamlink
  - setup
type: procedure
tools:
  - '[[tools/SteamLink]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Android
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:29:36.143Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Prepare-SteamLink-Device

## Summary

This procedure configures a secondary Android device with SteamLink to enable initiation of a Remote Play session, which will trigger the vulnerable driver installation on the host.

## Description

SteamLink serves as the client to connect to the host PC via Remote Play over LAN. Installing and logging into the app prepares it to send a connection request, exploiting the lack of driver integrity checks during installation.

## Requirements

1. Android device on the same LAN as the target Windows PC
2. Valid Steam account credentials (same as host)
3. Google Play Store access

## Defense

Defensive measures and detection strategies:

- Block unauthorized SteamLink connections via firewall rules on LAN
- Monitor for unexpected Remote Play initiations in Steam logs
- Use network segmentation to isolate gaming devices

## Objectives

1. Install and authenticate SteamLink on a mobile device
2. Ensure LAN connectivity to the host
3. Prepare for connection initiation

## Instructions

### Step 1: Install SteamLink App

**Context**: Download the official SteamLink app to enable Remote Play client functionality.

Open Google Play Store, search for "Steam Link", and install the app by Valve Corporation.

> Expected output: App installed on Android device.

### Step 2: Log In to SteamLink

**Context**: Authenticate with the same account as the host to pair devices.

Launch the app and log in using Steam credentials. Grant necessary permissions for network access.

> Expected output: Logged in and ready to scan for hosts.

### Step 3: Verify Network Detection

**Context**: Confirm the app can detect the host PC on the LAN.

In the app, initiate a device scan. Ensure the Windows PC running Steam appears in the list.

> Expected output: Host PC listed for connection.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/SteamLink]]

## Tags

- [[tools/SteamLink]]
- [[setup]]
