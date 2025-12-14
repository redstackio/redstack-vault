---
id: install-acronis-trigger
tags:
  - installation-trigger
  - service-startup
type: procedure
tools:
  - '[[tools/Acronis-True-Image-2021-Installer]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/run-acronis-installer]]'
verified: false
platforms:
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Malicious File]]'
updated_at: '2025-12-14T17:28:52.223Z'
skill_level: beginner
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Malicious File]]'
---
# Install-Acronis-True-Image-to-Trigger-Service

## Summary

This procedure downloads and runs the Acronis True Image 2021 installer, which starts the Scheduler2 Service and triggers the attempt to execute the hijacked 'C:\program.exe'.

## Description

The installation process initializes the service, causing schedul2.exe to run as SYSTEM and probe for the vulnerable path. Use silent mode for automation. This step assumes the malicious EXE is already placed. Expected outcome: Service starts, hijack executes if file present.

## Requirements

1. Downloaded installer from official source
2. Admin privileges for installation
3. Procmon running for observation

## Defense

Defensive measures and detection strategies:

- Verify installer integrity with hashes
- Monitor service installations with AppLocker
- Disable auto-start for third-party services

## Objectives

1. Initiate service startup
2. Trigger the vulnerable execution path
3. Observe escalation in monitoring tool

## Instructions

### Step 1: Download Installer

**Context**: Obtain the EXE from Acronis site if not present.

Manual download: https://download.acronis.com/AcronisTrueImage2021.exe

No command; browser or wget.

### Step 2: Run Installation

**Context**: Execute the installer to start services.

Use [[commands/run-acronis-installer]] for silent install:

```bash
AcronisTrueImage2021.exe /SILENT
```

> Runs without UI; completes in ~5 minutes.

### Step 3: Verify Service Start

**Context**: Check if Scheduler2 Service is running.

Use services.msc or sc query.

```bash
sc query schedul2
```

> Shows STATE: 4 RUNNING if successful.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Malicious File]] User Execution: Malicious File

### Sub-Techniques


## Commands Used

- [[commands/run-acronis-installer]]

## Tools Used

- [[tools/Acronis-True-Image-2021-Installer]]

## Tags

- [[acronis]]
- [[service-trigger]]
