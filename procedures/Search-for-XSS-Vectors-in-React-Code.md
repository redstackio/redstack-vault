---
tags:
  - xss
  - react
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
  - '[[JavaScript]]'
skill_level: advanced
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 834e5168-f5df-489f-9581-506737221d47
created_at: '2025-12-11T06:10:22.146Z'
updated_at: '2025-12-11T06:10:22.146Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0007]]'
mitre_techniques:
  - '[[T1059.007]]'
---
# Search for XSS Vectors in React Code

## Summary

This procedure searches for potential XSS vulnerabilities in React code by identifying unsafe functions and tracing user input handling.

## Description

React apps can be vulnerable to XSS if user input is rendered via dangerous methods like innerHTML without sanitization. This involves setting breakpoints and analyzing call stacks to find where chat messages are processed and sent via WebSocket.

## Requirements

1. Access to Steam Chat in Chrome
2. Knowledge of JavaScript debugging

## Defense

Defensive measures and detection strategies:

- Use strict Content Security Policy without unsafe-inline
- Sanitize all user input in BBCode parsing

## Objectives

1. Locate unsafe rendering functions
2. Trace input sanitization paths
3. Identify potential injection points

## Instructions

### Step 1: Code Search

**Context**: Search for vulnerable patterns.

In [[tools/Chrome-DevTools]], use the search pane to find 'dangerously' or 'innerHTML'.

> Expected: Hits on React rendering functions.

### Step 2: Set Breakpoints and Trace

**Context**: Debug execution flow.

Set breakpoints on found functions, send test messages, and inspect call stacks.

> Expected: Revelation of unsanitized user input paths.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[JavaScript]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/Chrome-DevTools]]

## Tags

- [[xss]]
- [[tools/React-Developer-Tools]]
