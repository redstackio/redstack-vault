---
id: proc-csgo-kick-test-001
tags:
  - xss
  - kick
  - sourcemod
type: procedure
tools:
  - '[[tools/SourceMod]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/kickclient-function]]'
verified: false
platforms:
  - Windows
  - Game
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:24:14.858Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Test Kick Commands for Payload Delivery

## Summary

This procedure evaluates native and modded kick commands for delivering XSS payloads, culminating in a custom SourceMod plugin using KickClient() for unrestricted HTML/JS injection.

## Description

Native kickid fails locally, sm_kick has char limits, but KickClient() in a plugin allows full payloads like <a onmouseover='javascript:SteamOverlayAPI.OpenExternalBrowserURL(...)'> to trigger RCE via Steam API calls in the Panorama context.

## Requirements

1. Running SourceMod server
2. SourcePawn compiler for plugins
3. Connected client for testing

## Defense

Defensive measures and detection strategies:

- Limit kick message lengths server-side
- Sanitize all client messages
- Audit plugin usage

## Objectives

1. Identify delivery limitations
2. Implement unrestricted kicking
3. Validate JS execution

## Instructions

### Step 1: Test Native Kicks

**Context**: Check built-in commands for payload support.

In server console, try kickid #1 "payload" (local only, no popup) and sm_kick #1 "short payload" (limited chars).

> Expected output: Limitations confirmed.

### Step 2: Develop Custom Plugin

**Context**: Use SourcePawn to call KickClient(client, full_payload).

Write plugin code with OnPluginStart registering sm_testkick, then in handler: KickClient(client, args).

> Expected output: Payload sent without limits, popup triggers onmouseover.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/kickclient-function]]

## Tools Used

- [[tools/SourceMod]]

## Tags

- xss
- kick
- sourcemod
