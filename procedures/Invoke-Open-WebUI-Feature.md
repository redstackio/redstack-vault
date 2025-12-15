---
tags:
  - authentication-bypass
  - ubiquiti
  - aircontrol
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Embedded Devices
  - Networking Hardware
submitted: true
created_at: '2024-01-01 12:00:00'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:31:43.154Z'
sub_techniques: []
id: e204525a-838e-4327-9343-5652b167097a
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Invoke-Open-WebUI-Feature

## Summary

This procedure uses airControl's 'Open Web-UI' feature to access a monitored Ubiquiti device's WebUI, which inadvertently sets a vulnerable state in the ticket-based authentication system, enabling subsequent bypass.

## Description

The 'Open Web-UI' function in airControl proxies access to the device's management interface. When invoked, it generates a temporary ticket for legitimate access but leaves a flaw if not followed by a reboot: the authentication routine fails to validate empty tickets properly. This step is essential to prime the device for unauthenticated access and requires interaction with the airControl UI.

## Requirements

1. Confirmed airControl monitoring of the target device
2. Access to airControl interface (web console)
3. Target device online and responsive

## Defense

Defensive measures and detection strategies:

- Disable 'Open Web-UI' feature when not in use
- Implement strict session timeouts in airControl
- Monitor for unusual WebUI access patterns via device logs

## Objectives

1. Establish the post-'Open Web-UI' vulnerable condition
2. Gain temporary legitimate access to observe WebUI
3. Prepare for ticket bypass without reboot

## Instructions

### Step 1: Select Target Device

**Context**: Navigate to the device in airControl.

Use the airControl dashboard to locate and select the target.

> Expected output: Device details page loads.

### Step 2: Trigger Open Web-UI

**Context**: Invoke the feature to access WebUI.

Click the 'Open Web-UI' button in the device actions menu.

> The WebUI should open in a new tab or window via airControl proxy. Note the time to ensure no reboot follows.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[authentication-bypass]]
- [[ubiquiti]]
- [[aircontrol]]
