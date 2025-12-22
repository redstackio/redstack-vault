---
tags:
  - persistence
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
  - '[[Impair Defenses]]'
updated_at: '2025-12-14T17:31:43.150Z'
sub_techniques:
  - '[[Disable or Modify Tools]]'
id: e7e49065-aec8-4b82-a35a-441846797d21
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Impair Defenses]]'
---
# Avoid-Device-Reboot

## Summary

This procedure ensures the Ubiquiti device does not reboot after invoking 'Open Web-UI' in airControl, preserving the vulnerable authentication state required for the ticket bypass exploit.

## Description

Rebooting the device resets the ticket system, closing the vulnerability window. This step involves monitoring and preventing reboots, which could be triggered manually, via updates, or automatically. The attacker must maintain the device's uptime to keep the empty ticket flaw active, allowing unauthenticated WebUI access.

## Requirements

1. Recent invocation of 'Open Web-UI' feature
2. Ability to monitor device status (via airControl or network pings)
3. Control over network to avoid update pushes

## Defense

Defensive measures and detection strategies:

- Schedule regular reboots for monitored devices
- Enable auto-reboot on idle or after management sessions
- Log all reboot events and correlate with airControl usage

## Objectives

1. Maintain the vulnerable post-'Open Web-UI' state
2. Extend the exploit window for access attempts
3. Avoid detection from reboot-related logs

## Instructions

### Step 1: Monitor Uptime

**Context**: Check device uptime to confirm no reboot.

Use airControl status or ping the device periodically.

> Expected output: Consistent uptime value since 'Open Web-UI' invocation.

### Step 2: Prevent Reboot Triggers

**Context**: Block potential reboot causes.

Avoid firmware updates or restarts; if admin access exists, disable auto-reboot features.

> Success if device remains operational without interruption.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Impair Defenses]] Impair Defenses

### Sub-Techniques

- [[Disable or Modify Tools]] Disable or Modify Tools

## Commands Used


## Tools Used


## Tags

- [[Persistence]]
- [[ubiquiti]]
- [[aircontrol]]
