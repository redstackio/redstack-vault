---
id: proc-connect-ios-rogue-wifi-001
tags:
  - ios
  - wifi
  - initial-access
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - iOS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Adversary-in-the-Middle]]'
updated_at: '2025-12-14T17:24:44.832Z'
skill_level: low
impact_level: medium
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Adversary-in-the-Middle]]'
---
# Connect-iOS-Device-to-Rogue-WiFi

## Summary

This procedure involves joining the target iOS device to the rogue WiFi access point, positioning its traffic for interception via the transparent proxy setup.

## Description

On a stock iPhone (iOS 9.3.3/9.3.5, no jailbreak), select and connect to the rogue SSID. The open network allows easy access, routing all outbound traffic (including Twitter app HTTPS) through the attacker's Linux machine. Outcomes: Device online but compromised network path.

## Requirements

1. Rogue AP broadcasting
2. Physical proximity to iOS device
3. No app modifications

## Defense

Defensive measures and detection strategies:

- Avoid open WiFi; use cellular or verified networks
- iOS prompts for captive portals; verify legitimacy
- Monitor connected networks in Settings

## Objectives

1. Gain network control over device
2. Enable traffic routing to proxy
3. No authentication barriers

## Instructions

### Step 1: Select and Join Network

**Context**: From iOS Settings, connect to rogue SSID.

No command; manual:
- Go to Settings > Wi-Fi
- Select "RogueTwitterNet" (or configured SSID)
- Join without password

> Expected: Connected status, IP assigned via DHCP.

### Step 2: Verify Connectivity

**Context**: Test basic internet to confirm routing.

Open Safari and browse a site; traffic should proxy.

> Successful if pages load (routed through attacker).

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Adversary-in-the-Middle]] Adversary-in-the-Middle

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- ios
- wifi
