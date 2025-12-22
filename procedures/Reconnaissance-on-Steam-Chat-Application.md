---
tags:
  - recon
  - steam
  - react
type: procedure
tools:
  - '[[tools/Chrome-DevTools]]'
  - '[[tools/React-Chrome-Extension]]'
tactics:
  - '[[Discovery]]'
commands: []
platforms:
  - Web
  - Windows
techniques:
  - '[[Gather Victim Network Information]]'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 556f98cf-ee5c-4416-9d39-61fec0201819
created_at: '2025-12-14T00:11:25.301Z'
updated_at: '2025-12-14T00:11:25.301Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Gather Victim Network Information]]'
---
# Reconnaissance on Steam Chat Application

## Summary

This procedure involves initial reconnaissance on the Steam chat application to identify its codebase, frameworks, and potential entry points for exploitation.

## Description

The Steam desktop chat uses the same codebase as the web version at https://steamcommunity.com/chat. By using debugging tools, attackers can observe WebSocket communications, confirm React usage, and search for embedding systems like OEMBED.

## Requirements

1. Access to Steam chat web or desktop client
2. Chrome browser with DevTools enabled
3. React Developer Tools extension installed

## Defense

Defensive measures and detection strategies:

- Monitor for unusual debugging activity in client-side applications
- Implement client-side security headers to restrict debugging

## Objectives

1. Confirm technology stack (React, WebSocket)
2. Identify potential unsafe patterns
3. Map out chat message handling

## Instructions

### Step 1: Inspect Application Codebase

**Context**: Use DevTools to analyze the chat interface.

Open Chrome DevTools and navigate to the Sources tab to search for React components and WebSocket frames.

> Expected: Confirmation of React and binary WebSocket protocol.

### Step 2: Search for Embedding Systems

**Context**: Look for OEMBED and unsafe HTML handling.

Use the React extension to inspect props and jump to code showing dangerouslySetInnerHTML usage.

> Expected: Identification of potential XSS vectors in message parsing.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Gather Victim Network Information]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/Chrome-DevTools]]
- [[tools/React-Chrome-Extension]]

## Tags

- recon
- steam
- react
