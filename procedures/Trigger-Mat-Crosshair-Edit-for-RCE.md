---
id: proc-trigger-mat-crosshair-rce
tags:
  - rce-trigger
  - path-truncation
  - command-execution
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/mat-crosshair-edit]]'
verified: false
platforms:
  - Windows
  - Source Engine
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Client Execution]]'
  - '[[Windows Command Shell]]'
updated_at: '2025-12-14T17:26:27.078Z'
sub_techniques:
  - '[[Windows Command Shell]]'
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
  - '[[Windows Command Shell]]'
---
# Trigger-Mat-Crosshair-Edit-for-RCE

## Summary

This procedure executes the vulnerable mat_crosshair_edit command in the Source Engine, exploiting buffer truncation to alter a material path and execute a malicious .js file, resulting in remote code execution on the Windows client.

## Description

The command handler uses a 256-byte buffer for paths, but Windows paths can be up to 260 bytes (MAX_PATH). A crafted long path truncates, changing .vmt to .js, which Windows associates with Script Host (cscript/wscript). The PoC .js runs calc.exe as proof. Server filters may require brute-force for random markers in multiplayer.

## Requirements

1. Cheats enabled
2. Malicious map loaded
3. Vulnerable Source Engine version

## Defense

Defensive measures and detection strategies:

- Increase buffer sizes and add path validation in engine updates
- Block external file associations for game materials
- Monitor for unexpected process launches (e.g., calc.exe) during gameplay

## Objectives

1. Invoke the truncation vulnerability
2. Execute arbitrary code via .js payload
3. Validate RCE with observable output like calc.exe

## Instructions

### Step 1: Execute Vulnerable Command

**Context**: Trigger the material editor to process the long path.

**Command** ([[commands/mat-crosshair-edit]]):
```bash
mat_crosshair_edit
```

> Command runs; due to truncation, .js executes via Script Host, launching calc.exe. Success if external app starts without game disruption.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution
- [[Windows Command Shell]] Windows Command Shell

### Sub-Techniques

- [[Windows Command Shell]] Windows Command Shell

## Commands Used

- [[commands/mat-crosshair-edit]]

## Tools Used


## Tags

- rce-trigger
- path-truncation
