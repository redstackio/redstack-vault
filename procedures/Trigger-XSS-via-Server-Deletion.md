---
tags:
  - xss-trigger
  - dom-execution
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
updated_at: '2025-12-14T03:46:31.502Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: d3fd685c-58ee-4f11-8828-21fb7df7a9b4
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-via-Server-Deletion

## Summary

This procedure induces the new admin to delete the infected server, causing the VK.com interface to render the unsanitized name and execute the embedded JavaScript in their DOM.

## Description

The deletion process in VK group management fetches and displays the server name without output encoding, leading to DOM-based XSS. This executes arbitrary JS in the admin's authenticated session, potentially exfiltrating data or performing actions before the server is removed.

## Requirements

1. New admin with group access
2. Persistent server with payload
3. Means to prompt deletion (e.g., message)

## Defense

Defensive measures and detection strategies:

- Sanitize all reflected inputs in management UIs
- Use Content Security Policy (CSP) to block inline scripts
- Log and alert on JS errors in admin sessions

## Objectives

1. Cause payload reflection in victim browser
2. Execute JS in high-privilege context
3. Capture session data via triggered script

## Instructions

### Step 1: Prompt Deletion

**Context**: Convince the new admin to act on the server.

Contact the new admin externally, suggesting to clean up old servers by deleting the one with the odd name.

### Step 2: Perform Deletion

**Context**: The victim navigates and deletes, triggering XSS.

New admin goes to group servers, selects the infected server, and clicks delete. The name is parsed into the DOM, firing the onerror or onload event.

### Step 3: Observe Execution

**Context**: Monitor for successful trigger.

If payload includes exfil (e.g., to attacker's server), check logs for incoming requests with cookies.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss-trigger]]
