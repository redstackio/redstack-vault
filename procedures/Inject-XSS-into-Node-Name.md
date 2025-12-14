---
tags:
  - xss
  - injection
  - payload
type: procedure
tools:
  - '[[tools/Firefox]]'
  - '[[tools/Chromium]]'
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
updated_at: '2025-12-14T03:16:20.441Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 2cb8d50e-5bcd-4a0f-8693-a82639b7eb3f
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-XSS-into-Node-Name

## Summary

This procedure demonstrates injecting a script payload into a Node-RED node's name field, triggering immediate XSS execution due to unsanitized HTML rendering.

## Description

In the Node-RED UI, node names are editable fields that use jQuery's .html() for rendering, allowing script tags to execute when the node is selected or viewed. The payload <script>alert('xss')</script> executes in the current browser session. This is a stored XSS as it persists in the flow configuration. Target environment is the local web UI; no network access beyond localhost needed.

## Requirements

1. Node-RED server running on port 1880
2. Access to the web UI in a browser
3. Basic knowledge of HTML/JavaScript payloads

## Defense

Defensive measures and detection strategies:

- Sanitize inputs using .text() instead of .html() in frontend code
- Implement Content Security Policy (CSP) to block inline scripts
- Monitor browser console for unexpected alerts or script executions

## Objectives

1. Exploit lack of input sanitization in node names
2. Achieve JavaScript execution in the attacker's browser
3. Validate vulnerability presence

## Instructions

### Step 1: Add and Edit Node

**Context**: Introduce a node to the workspace and modify its name to include the XSS payload.

**Instructions**: Drag an 'inject' node from the left palette to the workspace. Double-click the node to open the info tab, enter `<script>alert('xss')</script>` in the 'Name' field, and click 'Done'.

> The payload injects immediately; an alert box should appear with 'xss', confirming execution via unsanitized rendering.

### Step 2: Observe Execution

**Context**: Verify the script runs without deployment.

**Instructions**: Select the node in the workspace; the name renders as HTML, re-triggering if interactive.

> Expected output: Repeated alert on interaction, demonstrating client-side execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Firefox]]
- [[tools/Chromium]]

## Tags

- xss
- injection
- payload
