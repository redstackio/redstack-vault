---
tags:
  - reconnaissance
  - ubiquiti
  - aircontrol
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Embedded Devices
  - Networking Hardware
submitted: true
created_at: '2024-01-01 12:00:00'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:31:43.158Z'
sub_techniques: []
id: 8387dfc3-6104-4d18-a0ac-0fcc9ba61803
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Confirm-airControl-Monitoring

## Summary

This procedure verifies if a target Ubiquiti device is being monitored by the airControl system, which is a critical prerequisite for exploiting the improper authentication vulnerability in the ticket-based WebUI access.

## Description

In the context of attacking Ubiquiti networking devices, confirming airControl monitoring involves accessing the airControl management interface to check the device's status. This step ensures the target meets the vulnerability conditions: it must be added to airControl, and the monitoring must be active. Without this, the ticket bypass cannot be triggered. The procedure assumes the attacker has network access to the airControl server or console.

## Requirements

1. Network access to the airControl management interface (typically web-based)
2. Knowledge of the target device's IP or hostname
3. No special credentials needed if airControl is already accessible

## Defense

Defensive measures and detection strategies:

- Restrict airControl access to trusted networks via firewalls
- Regularly audit monitored devices and remove unnecessary ones
- Enable logging of airControl interface access attempts

## Objectives

1. Identify if the device is vulnerable to airControl-specific exploits
2. Map the monitoring setup for further attack planning
3. Confirm prerequisites for authentication bypass

## Instructions

### Step 1: Access airControl Interface

**Context**: Log into the airControl dashboard to view managed devices.

No specific command; use the web interface to navigate to the device list.

> Manually check the devices section for the target. Expected output: Target device listed with active status.

### Step 2: Verify Monitoring Status

**Context**: Confirm the device is online and monitored.

Inspect the device's details page in airControl.

> Look for indicators like 'Connected' or 'Monitored' status. If not present, the device cannot be exploited via this vector.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Account Discovery]] Account Discovery

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Reconnaissance]]
- [[ubiquiti]]
- [[aircontrol]]
