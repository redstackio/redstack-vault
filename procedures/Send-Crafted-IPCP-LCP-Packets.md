---
tags:
  - heap-overflow
  - data-leak
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - PS4
  - PS5
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: advanced
impact_level: high
detection_risk: medium
sub_techniques: []
id: a6b192be-f004-4d33-b1ca-d898dd3affe8
created_at: '2025-12-11T03:47:47.645Z'
updated_at: '2025-12-11T03:47:47.645Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1190]]'
---
# Send Crafted IPCP LCP Packets

## Summary

This procedure involves sending crafted IPCP or LCP CONF_REQ packets with invalid options to trigger heap buffer overwrite and overread in the PS4/PS5 kernel.

## Description

Exploits lack of validation in sppp_ipcp_RCR and sppp_lcp_RCR functions, where option length exceeds remaining buffer, causing bcopy overflow and data leak via CONF_REJ.

## Requirements

1. Established PPPoE connection
2. Packet crafting capability
3. Target running vulnerable PPP implementation

## Defense

Defensive measures and detection strategies:

- Patch kernel vulnerabilities (e.g., via system updates)
- Inspect PPP packets for invalid lengths

## Objectives

1. Trigger buffer overflow
2. Leak kernel data
3. Prepare for RCE

## Instructions

### Step 1: Craft Invalid Options

**Context**: Create CONF_REQ packets with p[1] > len.

Craft and send IPCP/LCP packets with oversized option lengths.

### Step 2: Send and Observe Response

**Context**: Send packets and capture leaked data in CONF_REJ.

Transmit the packets during negotiation and analyze responses for overread data.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- #heap-overflow
- #data-leak
