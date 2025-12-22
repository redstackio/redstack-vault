---
id: proc-vk-window-enum-001
tags:
  - browser-console
  - global-enum
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/enumerate-window-globals]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Process Discovery]]'
updated_at: '2025-12-13T23:52:33.999Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Process Discovery]]'
---
# Enumerate-Global-Window-Functions-for-Callback-Abuse

## Summary

This procedure uses the browser console to iterate over window properties, identifying global functions like requestAnimationFrame that accept callbacks for abusing the restricted callback parameter.

## Description

In the victim or test browser, enumerate window globals to find functions matching the callback regex and accepting function arguments, such as requestAnimationFrame, mozRequestAnimationFrame, webkitRequestAnimationFrame, and msRequestAnimationFrame.

## Requirements

1. Open browser console on VK.com page
2. JavaScript execution access
3. Knowledge of callback-accepting APIs

## Defense

Defensive measures and detection strategies:

- Restrict global function exposure
- Monitor console access in production

## Objectives

1. List window properties
2. Identify callback functions
3. Select abuse target like requestAnimationFrame

## Instructions

### Step 1: Execute Enumeration

**Context**: Iterate over window to log globals.

Execute [[commands/enumerate-window-globals]] in console:

```javascript
for (let prop in window) { console.log(prop); }
```

> Expected output: Console logs including requestAnimationFrame and prefixes.

### Step 2: Verify Callback Acceptance

**Context**: Test selected function.

Check typeof window.requestAnimationFrame === 'function' and that it accepts a callback.

> Expected output: Confirmation it can be set as callback for eval abuse.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Process Discovery]]

### Sub-Techniques


## Commands Used

- [[commands/enumerate-window-globals]]

## Tools Used


## Tags

- browser-console
- global-enum
