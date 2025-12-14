---
id: proc-verify-network
tags:
  - network-config
  - ipv6
type: procedure
tools: []
tactics:
  - '[[Defense Evasion]]'
commands:
  - '[[commands/display-network-interfaces]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[System Network Configuration Discovery]]'
updated_at: '2025-12-14T17:31:52.783Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[System Network Configuration Discovery]]'
---
# Verify-Network-Configuration

## Summary

This procedure checks the VPS network interfaces to confirm multiple IPv6 addresses are assigned and ready for IP rotation in attacks.

## Description

On the Hetzner VPS, use ifconfig to inspect venet0 interface, verifying addresses like 2a04:XXXX:0:32::1001/64 to ::1010/64, ensuring at least 500 addresses for rotation without reuse within 4 seconds.

## Requirements

1. SSH access to VPS
2. ifconfig or equivalent installed (standard on Linux)

## Defense

Defensive measures and detection strategies:

- Log interface changes on servers
- Monitor for unusual IPv6 traffic patterns
- Restrict IPv6 usage if not needed

## Objectives

1. Confirm IPv6 subnet assignment
2. List available addresses for rotation
3. Validate interface readiness

## Instructions

### Step 1: Display Interfaces

**Context**: Run command to view all network configurations.

Execute [[commands/display-network-interfaces]]:

```bash
ifconfig
```

> Expected output: Shows lo and venet0 with multiple IPv6 addresses (e.g., 2a04:XXXX:0:32::1001/64, ::1010/64, etc.).

### Step 2: Validate Addresses

**Context**: Manually check for sufficient IPv6 count.

No command; grep output if needed:

```bash
grep -o '2a04:XXXX:0:32::[0-9]*/64' <(ifconfig)
```

> Expected: List of 500+ unique IPv6 addresses.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion]] Defense Evasion

### Techniques

- [[System Network Configuration Discovery]] System Network Configuration Discovery

### Sub-Techniques


## Commands Used

- [[commands/display-network-interfaces]]

## Tools Used


## Tags

- [[network-config]]
- [[ipv6]]
