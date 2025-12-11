---
tags:
  - recon
  - steam
type: procedure
tools:
  - '[[tools/Chrome-DevTools]]'
  - '[[tools/React-Developer-Tools]]'
  - '[[tools/Binary-Grep]]'
  - '[[tools/Vim]]'
  - '[[tools/Remote-Chrome-Console]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/steam-open-game]]'
  - '[[commands/steam-open-console]]'
  - '[[commands/window-top-postmessage]]'
  - '[[commands/open-steam-uri]]'
  - '[[commands/object-keys-window]]'
  - '[[commands/steam-openexternalforpid-jarfile]]'
  - '[[commands/steam-openexternalforpid-file]]'
  - '[[commands/custom-protocol-txt]]'
  - '[[commands/custom-protocol-calculator]]'
  - '[[commands/custom-protocol-jarfile-traversal]]'
  - '[[commands/custom-protocol-jarfile-path]]'
platforms:
  - Web
techniques:
  - '[[Active Scanning]]'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 14b18823-e8eb-4798-b523-0b8071f9ee19
created_at: '2025-12-11T06:10:22.149Z'
updated_at: '2025-12-11T06:10:22.149Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0007]]'
mitre_techniques:
  - '[[T1595]]'
---
# Reconnaissance on Steam Chat Application

## Summary

This procedure involves performing initial reconnaissance on the Steam Chat application to identify its structure, network behavior, and framework, confirming it's a React app using WebSocket for communication.

## Description

The attack targets the Steam Chat client, which mirrors the web version at https://steamcommunity.com/chat. By inspecting network traffic and code, attackers can identify potential entry points for further exploitation like XSS. This step is crucial for understanding how messages are handled via binary WebSocket frames and React rendering.

## Requirements

1. Access to Steam Chat via browser or client
2. Chrome browser with DevTools enabled
3. React Developer Tools extension installed

## Defense

Defensive measures and detection strategies:

- Monitor unusual network traffic to Steam endpoints
- Implement client-side logging for debugging attempts

## Objectives

1. Confirm React framework usage
2. Identify WebSocket protocol
3. Map out message handling flow

## Instructions

### Step 1: Inspect Network Traffic

**Context**: Monitor WebSocket usage and binary frames.

Use [[tools/Chrome-DevTools]] to open the Network tab and filter for WebSocket connections.

> Expected: Binary frames containing message data.

### Step 2: Search for Framework Indicators

**Context**: Confirm React app structure.

In [[tools/Chrome-DevTools]], search source code for 'OEMBED' and use [[tools/React-Developer-Tools]] to inspect components.

> Expected: React components and props visible.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/Chrome-DevTools]]
- [[tools/React-Developer-Tools]]

## Tags

- [[recon]]
- [[commands/steam-open-game]]
