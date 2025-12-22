---
tags:
  - mitigation
  - testing
type: procedure
tools:
  - '[[tools/poc.py]]'
  - '[[tools/rce0923234.html]]'
  - '[[tools/unifi-video.Win7_x64.v3.10.7-beta.2_ee88ac.190725.1817.exe]]'
  - '[[tools/2019-04-21_17-47-17.mp4]]'
  - '[[tools/ubiq_rce.mp4]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/launchprocess-websocket]]'
platforms:
  - Windows
techniques:
  - '[[Network Sniffing]]'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: ca2bf341-d350-4e89-8114-63cedd34574f
created_at: '2025-12-11T06:10:22.815Z'
updated_at: '2025-12-11T06:10:22.815Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0007]]'
mitre_techniques:
  - '[[T1040]]'
---
# Test Mitigation in Beta Software

## Summary

This procedure tests the beta version of UniFi Video to confirm the addition of client certificate authentication mitigates the vulnerability.

## Description

Installing the beta software adds authentication to the API, preventing unauthenticated command execution. Tests confirm previous exploits fail.

## Requirements

1. Access to beta installer
2. Windows test environment
3. Previous exploit tools for validation

## Defense

Defensive measures and detection strategies:

- Deploy authenticated services
- Regularly update software

## Objectives

1. Install beta version
2. Attempt exploits and confirm failure
3. Verify security improvements

## Instructions

### Step 1: Install Beta Software

**Context**: Run the installer to update UniFi Video.

Execute [[tools/unifi-video.Win7_x64.v3.10.7-beta.2_ee88ac.190725.1817.exe]].

> Follow installation prompts.

### Step 2: Test Exploits

**Context**: Retry local and remote exploits.

Attempt WebSocket connections without certificates.

> Expect authentication errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Network Sniffing]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/unifi-video.Win7_x64.v3.10.7-beta.2_ee88ac.190725.1817.exe]]

## Tags

- mitigation
- testing
