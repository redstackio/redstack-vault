---
tags:
  - wcf
  - path-injection
  - nordvpn
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands: []
verified: false
platforms:
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[T1068.001]]'
updated_at: '2025-12-14T17:29:28.615Z'
sub_techniques: []
id: c1f57ded-154c-47ce-85e6-1b6b923b84c3
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[T1068.001]]'
---
# Supply Arbitrary Path via ServerDomain Parameter

## Summary

This procedure allows a local attacker to inject an arbitrary file path into the NordVPN service's OpenVPN configuration loading process by manipulating the ServerDomain parameter in the VpnConnectionProxy WCF model, setting the stage for a TOCTOU exploit.

## Description

The NordVPN Windows service uses the VpnConnectionProxy WCF model to handle VPN connection requests. The ServerDomain parameter is concatenated with a base path using Path.Combine to form the full path to the OpenVPN configuration file. Due to insufficient validation, an attacker can supply paths like `..\..\C:\temp\bait.ovpn` to control the location. This enables placing a benign bait file for initial validation, which is later swapped. The attack requires local access to trigger WCF calls, typically via the NordVPN client or direct service interaction.

## Requirements

1. Local low-privileged user account on Windows with NordVPN installed
2. Ability to interact with the NordVPN service via WCF (e.g., through client API)
3. Knowledge of the service's base path for config files (usually in NordVPN installation directory)

## Defense

Defensive measures and detection strategies:

- Strictly validate and whitelist ServerDomain parameter to prevent path traversal (e.g., use fixed domains only)
- Implement path canonicalization and absolute path enforcement before file operations
- Monitor WCF calls for anomalous parameters using ETW logging or service auditing

## Objectives

1. Gain control over the OpenVPN config file path selection
2. Position a controllable file for subsequent race condition exploitation
3. Avoid immediate rejection by the service's input handling

## Instructions

### Step 1: Prepare the Bait File

**Context**: Create a benign OpenVPN config file at the target path to pass initial validation.

No specific command; manually create `C:\temp\bait.ovpn` with valid OpenVPN syntax (e.g., basic server config without 'engine' option).

> Ensure the file is syntactically valid to pass the service's check.

### Step 2: Inject Path via WCF

**Context**: Pass the arbitrary path through ServerDomain during a VPN connection attempt.

Use the NordVPN client to connect to a custom server or script a WCF call to set ServerDomain to your controlled path (e.g., via PowerShell reflection for service proxy).

> The service will use Path.Combine("base", ServerDomain) to build `C:\Program Files\NordVPN\OpenVPN\configs\..\..\temp\bait.ovpn`.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[T1068.001]] Exploitation for Privilege Escalation: Vulnerability in Software

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- wcf
- path-injection
- nordvpn
