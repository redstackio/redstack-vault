---
tags:
  - plugin-dev
  - rce
  - csgo
type: procedure
tools:
  - '[[tools/sourcemod]]'
  - '[[tools/testkick-smx]]'
tactics:
  - '[[Execution]]'
  - '[[Persistence]]'
commands:
  - '[[commands/kickclient-with-unlimited-payload]]'
platforms:
  - Windows
  - 'CS:GO'
techniques:
  - '[[JavaScript]]'
  - '[[Exploitation for Client Execution]]'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques: []
id: e3b2404d-c103-4d13-8efa-0d41fad43ba2
created_at: '2025-12-14T00:11:25.219Z'
updated_at: '2025-12-14T00:11:25.219Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Persistence]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Exploitation for Client Execution]]'
---
# Develop SourceMod Plugin for RCE Testing

## Summary

This procedure creates a SourceMod plugin (testkick.smx) to bypass character limits and test RCE payloads via onmouseover events.

## Description

The plugin uses KickClient() to deliver large JS payloads that execute on mouseover, opening file URLs like calc.exe through SteamOverlayAPI.

## Requirements

1. SourceMod scripting knowledge
2. Dedicated server with SourceMod
3. Plugin compilation tools

## Defense

Defensive measures and detection strategies:

- Block SteamOverlayAPI file access
- Scan plugins for malicious hooks

## Objectives

1. Deliver unlimited payloads
2. Achieve interactive RCE
3. Validate JS execution

## Instructions

### Step 1: Create and Install Plugin

**Context**: Develop testkick.smx for custom kicks.

Place in addons\sourcemod\plugins after compilation with [[tools/sourcemod]].

> Registers sm_testkick command.

### Step 2: Trigger Exploit

**Context**: Kick and mouse over payload.

Use [[commands/kickclient-with-unlimited-payload]]:

```bash
KickClient(client, full)
```

> Mouse over to execute JS.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Persistence]]

### Techniques

- [[JavaScript]]
- [[Exploitation for Client Execution]]

### Sub-Techniques



## Commands Used

- [[commands/kickclient-with-unlimited-payload]]

## Tools Used

- [[tools/sourcemod]]
- [[tools/testkick-smx]]

## Tags

- [[plugin-dev]]
- [[rce]]
- [[csgo]]
