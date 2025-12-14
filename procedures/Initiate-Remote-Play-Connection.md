---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567894
tags:
  - remote-play
  - connection
type: procedure
tools:
  - '[[tools/SteamLink]]'
tactics:
  - '[[Privilege Escalation]]'
commands: []
verified: false
platforms:
  - Windows
  - Android
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:29:36.117Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---
# Initiate-Remote-Play-Connection

## Summary

This procedure starts a Remote Play session from the SteamLink device to the host PC, setting the stage for the vulnerable driver installation triggered by SteamServices.

## Description

By initiating the connection over LAN, the procedure prompts the host Steam to prepare for streaming, which will lead to driver loading without integrity re-verification if files were previously replaced.

## Requirements

1. Steam running on host Windows PC
2. SteamLink logged in on Android device
3. Devices on same LAN

## Defense

Defensive measures and detection strategies:

- Log and alert on Remote Play connection attempts
- Disable Remote Play feature in Steam settings
- Use IDS to monitor Steam protocol traffic on LAN

## Objectives

1. Establish connection request from client
2. Prompt host for authorization
3. Trigger driver installation process

## Instructions

### Step 1: Scan for Host

**Context**: Use SteamLink to discover the target PC.

In the SteamLink app, tap to scan for computers running Steam.

> Expected output: Host PC appears in the list.

### Step 2: Select and Connect

**Context**: Initiate the streaming session.

Select the host PC and tap "Connect". Wait for the pairing code or direct LAN link.

> Expected output: Connection initiated, prompt sent to host.

### Step 3: Confirm Readiness

**Context**: Ensure no errors block the process.

Verify the app shows connection progress without failures.

> Expected output: Awaiting host authorization.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/SteamLink]]

## Tags

- [[remote-play]]
- [[connection]]
