---
tags:
  - android
  - drozer
  - connection
type: procedure
tools:
  - '[[tools/Drozer]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/drozer-console-connect]]'
verified: false
platforms:
  - Android
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:24:39.876Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 677415f2-30ad-4c87-8d6a-d154606b9ed5
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Connect-to-Drozer-Console

## Summary

This procedure establishes a console connection from the host to the Drozer agent on the Android device, enabling execution of security assessment commands like activity invocation.

## Description

After installing the agent and starting the embedded server, connecting the Drozer console allows interactive sessions for exploring app components. In this attack, it provides the bridge to send intents that exploit exported activities, bypassing app locks without needing root or physical access beyond the emulator.

## Requirements

1. Drozer framework installed on host
2. Drozer Agent running with embedded server on device
3. Network connectivity between host and device (localhost for emulator)

## Defense

Defensive measures and detection strategies:

- Block connections to Drozer ports (default 31415) via firewall
- Detect agent APKs through signature-based mobile security scans
- Log unusual network activity from apps

## Objectives

1. Securely connect host console to device agent
2. Verify communication for subsequent commands
3. Enable intent-based app interactions

## Instructions

### Step 1: Launch Drozer Console Connection

**Context**: Initiate the connection to the running agent server.

**Command** ([[commands/drozer-console-connect]]):
```bash
drozer console connect
```

> This command opens a CMD/console and connects to the agent, establishing the interactive session. Expected output: 'Connected to Drozer agent' confirmation.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used

- [[commands/drozer-console-connect]]

## Tools Used

- [[tools/Drozer]]

## Tags

- android
- drozer
- connection
