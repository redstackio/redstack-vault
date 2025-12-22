---
tags:
  - ransomware
  - detection
  - simulation
type: procedure
tools:
  - '[[tools/ransomware-simulator]]'
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/run-ransomware-simulator]]'
verified: false
platforms:
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:28:51.601Z'
skill_level: intermediate
impact_level: medium
detection_risk: high
sub_techniques: []
id: c8e043bf-94f2-480d-a2eb-e984b09609e1
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---
# Prepare-and-Trigger-Ransomware-Simulation

## Summary

This procedure runs a ransomware simulator to trigger detection by Acronis Active Protection, placing the simulated malicious file in a state ready for quarantine without fully closing the alert.

## Description

The ransomware_sim.exe is executed against a user-writable directory like C:\Users\UNPRIVILIEGEDUSER\ to mimic file encryption, prompting Acronis to detect and block it. The user interacts with the dialog to block but not close, keeping the file eligible for API-triggered quarantine. This step relies on the service's detection of simulated ransomware behavior and sets up for the symlink abuse in the next phases.

## Requirements

1. ransomware_sim.exe placed in C:\ProgramData
2. Acronis Active Protection enabled and monitoring
3. Local execution privileges
4. User interaction for dialog handling

## Defense

Defensive measures and detection strategies:

- Enable behavioral monitoring for file encryption patterns
- Log all ransomware detection events and user interactions
- Block execution of unknown binaries in ProgramData

## Objectives

1. Simulate ransomware to trigger alert
2. Block without closing to prepare for API trigger
3. Confirm detection without full quarantine

## Instructions

### Step 1: Execute Ransomware Simulator

**Context**: Run the simulator to target a user directory and initiate encryption simulation.

**Command** ([[commands/run-ransomware-simulator]]):
```cmd
ransomware_sim.exe C:\Users\UNPRIVILIEGEDUSER\"
```

> This simulates encryption; Acronis should detect it immediately.

### Step 2: Handle Detection Dialog

**Context**: Interact with the Acronis popup to block the process.

No command; manually click 'block' in the dialog but avoid 'close'.

> Expected: File blocked, alert active for API interaction.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation

### Sub-Techniques


## Commands Used

- [[commands/run-ransomware-simulator]]

## Tools Used

- [[tools/ransomware-simulator]]

## Tags

- ransomware
- detection
- simulation
