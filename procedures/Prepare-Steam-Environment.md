---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567891
tags:
  - steam
  - setup
type: procedure
tools:
  - '[[tools/Steam]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Windows
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:29:36.148Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Prepare-Steam-Environment

## Summary

This procedure sets up the Steam client on a Windows 10 x64 target to prepare for exploiting the Remote Play driver installation vulnerability, ensuring no drivers are pre-installed.

## Description

The attack begins by installing Steam on a fresh Windows 10 x64 system and logging in, which performs initial integrity checks but does not install Remote Play drivers until the first session. This creates a window for later file replacement. The procedure verifies the absence of audio devices in Device Manager to confirm the setup is ready for escalation.

## Requirements

1. Windows 10 x64 machine with administrative access for installation
2. Valid Steam account credentials
3. Internet access for downloading Steam

## Defense

Defensive measures and detection strategies:

- Monitor Steam installations and driver directories for unauthorized changes
- Use file integrity monitoring tools like Sysmon to detect modifications in `C:\Program Files (x86)\Steam\`
- Restrict write access to Steam directories via group policies

## Objectives

1. Establish a running Steam instance without Remote Play drivers
2. Verify environment readiness for driver tampering
3. Prepare for subsequent privilege escalation steps

## Instructions

### Step 1: Install Steam

**Context**: Download and install the latest Steam client to create the baseline environment.

Go to the official Steam website, download the installer, and run it as a standard user. Follow the setup wizard to complete installation.

> Expected output: Steam installed in `C:\Program Files (x86)\Steam\`.

### Step 2: Launch and Log In

**Context**: Start Steam and authenticate to trigger initial integrity checks without installing drivers.

Launch Steam.exe and log in with account credentials. Allow it to update if prompted.

> Expected output: Steam running and logged in.

### Step 3: Verify No Drivers Installed

**Context**: Confirm Remote Play drivers are not present to ensure the exploitation window is open.

Open Device Manager (devmgmt.msc), navigate to Sound, video and game controllers. Check for absence of Steam Streaming Microphone and Speakers.

> Expected output: No Steam audio devices listed.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Steam]]

## Tags

- [[tools/Steam]]
- [[setup]]
