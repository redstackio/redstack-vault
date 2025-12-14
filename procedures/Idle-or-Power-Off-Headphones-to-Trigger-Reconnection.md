---
id: proc-uuid-003
name: Idle-or-Power-Off-Headphones-to-Trigger-Reconnection
tags:
  - bluetooth
  - reconnection
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - IoT
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:31:52.354Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Idle-or-Power-Off-Headphones-to-Trigger-Reconnection

## Summary

This procedure simulates a disconnection by idling or powering off the Sony WH-1000XM5 headphones, triggering the vulnerable reconnection process that seeks previously paired devices.

## Description

The headphones' firmware enters reconnection mode after idle or power cycle, scanning for paired devices without re-authentication. This step prepares for the spoofed connection. No tools required; physical access to headphones needed. Outcome: Headphones ready to auto-connect.

## Requirements

1. Physical access to WH-1000XM5 headphones
2. Previously paired device context

## Defense

Defensive measures and detection strategies:

- Implement timeout-based re-pairing prompts
- Monitor for frequent power cycles in logs
- Educate users on secure power-off procedures

## Objectives

1. Induce reconnection scan
2. Avoid entering pairing mode

## Instructions

### Step 1: Idle or Power Off

**Context**: Leave headphones idle for ~1 minute or power off to disconnect from any active session.

**Instructions**: Wait or press power button to shut down. Expected output: No active Bluetooth connection.

### Step 2: Confirm Disconnection

**Context**: Verify no connection via LED indicators or app.

**Instructions**: Check headphone status lights. Expected output: Disconnected state.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[bluetooth]]
- [[reconnection]]
