---
id: proc-craft-first-app-variable-2024
tags:
  - xss
  - javascript-uri
  - payload-split
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/set-variable-b-roomtitle]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:55:06.519Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Craft First Malicious App Name for Variable Setup

## Summary

This procedure creates a dummy app with a crafted name using the '|' character to forge a javascript: URI that sets a variable for referencing the room title element in a Chaturbate stored XSS attack.

## Description

Exploiting the lack of '|' filtering in the app_info_json parameter of the start_defchat JS function, the app name is split to create a malicious link. This first app sets `b` to '#roomtitle', preparing for the second payload part. Requires app creation privileges in the broadcast room.

## Requirements

1. Broadcaster account with app/bot creation ability
2. Knowledge of the 32-character app name limit
3. Browser for link inspection

## Defense

Defensive measures and detection strategies:

- Filter '|' and other URI-forging characters in app names
- Escape app names in HTML <a> tag construction
- Log and review app names for suspicious patterns like 'javascript:'

## Objectives

1. Forge first javascript: URI in app link
2. Set global variable for DOM element reference
3. Bypass length limits via payload splitting

## Instructions

### Step 1: Prepare App Creation

**Context**: Navigate to the app/bot creation interface in the broadcast room.

**Instructions**: Ensure the room title payload is already set from prior steps.

### Step 2: Set Malicious App Name

**Context**: Craft the name to include the '|' separator for URI forgery.

**Command** ([[commands/set-variable-b-roomtitle]]):

Use app name: `1|javascript:b='#roomtitle';0`

> This creates a link like <a href="javascript:b='#roomtitle';0">. The '0' pads syntax. Expected output: App runs, link appears in chat header; clicking sets `b` variable. Verify in console.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/set-variable-b-roomtitle]]

## Tools Used


## Tags

- [[xss]]
- [[javascript-uri]]
