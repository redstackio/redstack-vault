---
tags:
  - authentication-bypass
  - ubiquiti
  - webui
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
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:31:43.148Z'
sub_techniques: []
id: 610b1d0c-6139-4991-8792-ee984023fa1d
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Access-WebUI-Without-Ticket

## Summary

This procedure exploits the improper authentication in airControl-monitored Ubiquiti devices by accessing the WebUI with an empty ticket, allowing login as any user without credentials.

## Description

After 'Open Web-UI' usage and no reboot, the ticket validation routine fails, permitting empty ticket submissions to authenticate as administrative users. This grants full access to device configuration, controls, and settings, posing a critical risk. Discovered in 2017, it affects devices until firmware/software updates are applied.

## Requirements

1. Device monitored by vulnerable airControl version
2. 'Open Web-UI' invoked since last reboot
3. Direct network access to device WebUI (e.g., http://device-ip)

## Defense

Defensive measures and detection strategies:

- Apply firmware updates post-March 2017
- Reboot devices after airControl sessions
- Monitor WebUI access logs for empty ticket attempts

## Objectives

1. Gain unauthorized full access to device WebUI
2. Impersonate any user for configuration changes
3. Exfiltrate or modify device settings

## Instructions

### Step 1: Navigate to WebUI

**Context**: Direct browser access to the device.

Open http://<device-ip> in a browser.

> Expected output: Login form loads.

### Step 2: Submit Empty Ticket

**Context**: Attempt login without valid credentials.

Leave the ticket field empty and submit the form (no username/password needed).

> Due to the flaw, access is granted as any user. Expected output: Full WebUI dashboard accessible.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[authentication-bypass]]
- [[ubiquiti]]
- [[webui]]
