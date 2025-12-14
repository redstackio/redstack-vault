---
tags:
  - rce
  - verification
type: procedure
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - macOS
  - Windows
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-14T17:23:41.638Z'
skill_level: beginner
impact_level: high
detection_risk: high
sub_techniques: []
id: 750ccef2-b7d7-4f14-9c52-5a0ba9ffaf20
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
---
# Verify-Arbitrary-Command-Execution

## Summary

This procedure validates the success of the RCE by observing the host OS launch the targeted application or file via the openExternal call, confirming arbitrary command execution.

## Description

After the payload triggers openExternal, the Electron app opens the specified URL on the host (e.g., file:///System/Applications/Calculator.app on macOS). This demonstrates full RCE as the attacker can chain to any executable, file, or network resource. Verification involves interacting with the launched app to ensure control.

## Requirements

1. Payload execution completed
2. Access to the host OS desktop
3. Knowledge of target app (e.g., Calculator for testing)

## Defense

Defensive measures and detection strategies:

- Prompt user confirmation for all external opens
- Restrict file:// protocols in Electron's protocol handler
- Monitor process launches correlating with app usage

## Objectives

1. Observe launched application on host
2. Perform test action to confirm execution
3. Assess potential for further exploitation

## Instructions

### Step 1: Monitor Host Response

**Context**: Watch for the application to launch post-payload trigger.

On macOS, expect Calculator.app to open; on Windows, calc.exe.

> App window appears; no errors in Electron console.

### Step 2: Validate Functionality

**Context**: Interact with the app to prove RCE (e.g., compute 7*191 = 1337).

Enter calculation in Calculator and verify result.

> Correct output confirms host-level execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploitation for Client Execution]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[command-injection]]
- [[os-rce]]
