---
tags:
  - pppoe
  - initial-access
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - PS4
  - PS5
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: advanced
impact_level: medium
detection_risk: low
sub_techniques: []
id: 5e6877f9-0d10-4340-8e30-6193505d0fcd
created_at: '2025-12-11T03:47:47.653Z'
updated_at: '2025-12-11T03:47:47.653Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1190]]'
---
# Setup Malicious PPPoE Server

## Summary

This procedure sets up a malicious PPPoE server to establish a connection with PS4/PS5 consoles, enabling the injection of crafted PPP packets to exploit kernel vulnerabilities.

## Description

By acting as a PPPoE server, an attacker can interact with the target's sppp kernel module during protocol negotiation. This is the initial step for exploiting heap vulnerabilities in PPP handling, leading to potential RCE. The target must be configured to use PPPoE for internet access.

## Requirements

1. Network access to the target's PPPoE interface
2. Software to emulate a PPPoE server (e.g., custom script or tool like rp-pppoe)
3. Knowledge of PPP protocol for packet crafting

## Defense

Defensive measures and detection strategies:

- Restrict PPPoE to trusted servers or use VPNs
- Monitor for anomalous PPPoE connections and packet anomalies

## Objectives

1. Establish PPPoE session with target
2. Prepare for packet injection
3. Enable further exploitation steps

## Instructions

### Step 1: Configure PPPoE Server

**Context**: Set up the server to respond to PPPoE discovery from the PS4/PS5.

Configure and run a PPPoE server on your machine to accept connections from the target console.

### Step 2: Establish Connection

**Context**: Wait for the target to initiate PPPoE and respond accordingly.

Monitor for PADI packets and respond with PADO, then proceed to session establishment.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- #pppoe
- [[Initial Access]]
