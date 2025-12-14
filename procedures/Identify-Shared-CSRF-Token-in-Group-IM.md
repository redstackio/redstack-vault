---
id: proc-vk-csrf-identify
tags:
  - csrf
  - recon
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:27:42.736Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Identify Shared CSRF Token in Group IM

## Summary

This procedure involves analyzing VK.com's Group IM functionality to discover that the CSRF token (hash) is shared across all users accessing the same group, enabling subsequent impersonation attacks.

## Description

In VK.com's /al_im.php?gid=XXX endpoint, the 'hash' parameter used for actions like sending messages or deleting dialogs is generated based solely on the group_id, making it identical for all authorized users rather than unique per session or user. This shared token, valid for about 7 hours as a timehash or potentially static, allows CSRF exploitation. The procedure requires group access and browser inspection to confirm the vulnerability in a PHP-based web environment.

## Requirements

1. Valid VK.com account with access to the target group
2. Web browser with developer tools (e.g., Chrome DevTools)
3. Knowledge of the group_id (gid)

## Defense

Defensive measures and detection strategies:

- Implement user-specific CSRF tokens tied to session IDs
- Monitor for anomalous IM actions from group members
- Enable logging of hash usage and validate per-user uniqueness

## Objectives

1. Confirm shared nature of the CSRF hash
2. Determine token validity period for attack planning
3. Identify exploitable actions (e.g., message sending)

## Instructions

### Step 1: Access Group IM Interface

**Context**: Navigate to the target group's messaging to prepare for inspection.

Log in to VK.com and visit /al_im.php?gid=XXX to load the IM interface.

### Step 2: Inspect Network Requests

**Context**: Use developer tools to capture and analyze requests during IM actions.

Open browser developer tools (F12), go to the Network tab, and perform actions like sending a test message or deleting a dialog. Filter for requests to /al_im.php and examine the 'hash' parameter in POST data.

### Step 3: Verify Shared Token

**Context**: Test across sessions to confirm the hash is not user-specific.

Log out and log in with another account having group access, repeat an IM action, and compare the hash value. Note if it's identical and check expiration by testing after 7 hours.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[web]]
- [[recon]]
