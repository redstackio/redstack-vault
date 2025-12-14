---
id: proc-trigger-recursive-popups-brave
tags:
  - dos
  - javascript
  - popup
  - execution
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
  - Linux
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:26:30.438Z'
skill_level: beginner
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-Recursive-Popups-in-Brave

## Summary

This procedure executes JavaScript within the loaded HTML to create endless recursive popups using location.reload(), causing uncontrolled resource consumption in Brave browser and leading to a freeze.

## Description

Once the malicious HTML is loaded, the embedded JavaScript runs automatically, implementing a loop with location.reload() that spawns popup dialogs repeatedly. Brave's lack of limits on popups and poor handling of reloads in this context results in the browser becoming unresponsive. This targets Chromium-based Brave version 0.11.6, but may affect similar versions. Prerequisites include the HTML being open; no further user input is needed.

## Requirements

1. Malicious HTML loaded in Brave browser
2. JavaScript execution enabled (default in browsers)
3. Target platform: Linux or Windows with Brave installed

## Defense

Defensive measures and detection strategies:

- Enable strict popup blocking in browser settings
- Use sandboxed browsing or isolated environments
- Monitor for high CPU/memory usage from browser processes

## Objectives

1. Overwhelm browser resources with recursive popups
2. Cause interface freeze and prevent normal operations
3. Demonstrate DoS without external tools

## Instructions

### Step 1: Load the HTML to Initiate Script

**Context**: Opening the file triggers the JavaScript loop automatically.

No command; the script is inline in HTML, e.g., <script>while(true){location.reload();}</script> or similar recursive function.

> Expected output: Popups begin appearing in a loop, each reloading and spawning more.

### Step 2: Allow Recursion to Build

**Context**: Let the loop run to consume resources; no intervention needed.

Observe via browser console if open.

> Expected output: Increasing number of dialogs, browser lag.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- dos
- javascript
- popup
