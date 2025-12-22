---
id: proc-uuid-2
tags:
  - scheme-bypass
  - ui-redressing
  - bookmarking
  - drag-and-drop
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
  - Microsoft Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Client Execution]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:23:31.272Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
  - '[[JavaScript]]'
---
# Bypass-chrome-Scheme-via-Bookmarking-or-Drag-and-Drop

## Summary

This procedure exploits inadequate restrictions in Brave browser by using UI redressing in a local PoC to bookmark or drag-and-drop a 'chrome://brave' URL, bypassing scheme protections and loading the restricted internal page.

## Description

Brave's prior fixes failed to block chrome:// URLs from user interactions like CTRL+click on bookmarks or drag into windows. The PoC popup provides the anchor; dragging to bookmarks or main window (e.g., on brave.com) navigates without validation. Targets Windows Brave versions with exposed APIs. Requires user interaction post-PoC opening.

## Requirements

1. Target has opened PoC HTML locally in Brave
2. Browser bookmarks bar visible or enabled
3. User performs drag-and-drop or click actions

## Defense

Defensive measures and detection strategies:

- Patch Brave to version post-2018 fix for scheme bypass
- Disable bookmarking from untrusted sources
- Monitor for anomalous chrome:// navigations in browser logs

## Objectives

1. Load restricted chrome://brave page
2. Expose internal APIs for further exploitation
3. Avoid direct URL entry blocks

## Instructions

### Step 1: Trigger PoC Popup

**Context**: User clicks in PoC to open popup with anchor.

**Instructions**: Instruct: "Click anywhere to see instructions."

> Expected: Popup with <a href="chrome://brave">Brave Settings</a> appears.

### Step 2: Bookmark or Drag Anchor

**Context**: Use UI to place URL in bookmark bar or window.

**Instructions**: Drag anchor to bookmark bar; if empty, right-click > Bookmark Link. Alt: Drag to main window.

> Expected: Bookmark created or direct navigation attempt.

### Step 3: Open Bookmarked URL

**Context**: Navigate using bypass method.

**Instructions**: CTRL+click bookmark or middle-click to open in new tab.

> Expected: chrome://brave loads successfully.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution
- [[JavaScript]] Command and Scripting Interpreter: JavaScript

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[scheme-bypass]]
- [[ui-redressing]]
