---
id: proc-csgo-disconnect-test-001
tags:
  - xss
  - testing
  - csgo
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/disconnect-with-image-payload]]'
verified: false
platforms:
  - Windows
  - Game
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:24:14.877Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Test Disconnect Message for XSS

## Summary

This procedure tests for XSS in the CS:GO disconnect popup by injecting an HTML payload via the console command, confirming if raw HTML like image tags renders without sanitization.

## Description

The disconnect command sends a message that populates the popup_generic.xml Label, which parses HTML if html='true'. A simple <img> tag loading an external resource verifies execution, bypassing cache by running twice. This proves the vector for more malicious JS payloads.

## Requirements

1. Running CS:GO client
2. Access to in-game console (~ key)
3. Internet connection for image load

## Defense

Defensive measures and detection strategies:

- Patch UI to escape messages
- Log anomalous disconnects
- Client updates to block external loads

## Objectives

1. Confirm XSS vulnerability
2. Validate popup rendering
3. Identify payload limitations

## Instructions

### Step 1: Open Console and Execute Payload

**Context**: Use the disconnect command to trigger the popup with embedded HTML.

**Command** ([[commands/disconnect-with-image-payload]]):

```bash
# In CS:GO console
disconnect "<img src='https://i.imgur.com/IbJKM0M.jpg'>"
```

> Explanation: This sends a disconnect message with an image tag. Run twice to bypass browser cache. Expected output: Cat image appears in the disconnect popup, confirming XSS.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/disconnect-with-image-payload]]

## Tools Used


## Tags

- xss
- testing
- csgo
