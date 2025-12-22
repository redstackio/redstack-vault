---
tags:
  - xss
  - websocket
  - payload-insertion
type: procedure
tools:
  - '[[tools/Google-Chrome]]'
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 58ed1e22-2938-48f8-8be7-7543f2e18f27
created_at: '2025-12-13T23:55:38.190Z'
updated_at: '2025-12-13T23:55:38.190Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Modify-WebSocket-Request-to-Insert-Malicious-URI

## Summary

This procedure bypasses direct editor restrictions by intercepting and modifying WebSocket requests during undo operations to embed javascript: URIs in Slack posts.

## Description

Slack uses WebSocket for real-time edits. By capturing requests during undo (Ctrl+Z) after link deletion, the 'links' JSON array can be altered to include malicious URIs like 'javascript:alert("XSS")'. This stores the payload persistently for execution on click.

## Requirements

1. Browser with dev tools (e.g., Chrome) for WebSocket inspection
2. Slack post editing access
3. Proxy or dev tools to modify requests

## Defense

Defensive measures and detection strategies:

- Validate all incoming WebSocket payloads server-side
- Log and alert on URI scheme anomalies
- Rate-limit edit operations

## Objectives

1. Insert payload without UI blocking
2. Ensure persistence in post
3. Trigger execution in domain context

## Instructions

### Step 1: Trigger WebSocket Request

**Context**: Delete a link in the editor and perform undo to generate a modifiable request.

Use Ctrl+Z in the Markdown editor after deletion.

> Expected: WebSocket frame with 'links' array captured in Network tab.

### Step 2: Modify and Replay

**Context**: Alter the JSON to inject the payload.

Edit the request body: Change 'links' to include {"url": "javascript:alert(\"XSS\")"}.

> Expected: Modified request sent; payload appears in editor on refresh.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Google-Chrome]]

## Tags

- [[xss]]
- [[websocket]]
