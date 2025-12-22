---
tags:
  - xss
  - configuration
  - web-embed
type: procedure
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
updated_at: '2025-12-13T23:08:55.604Z'
skill_level: basic
impact_level: low
sub_techniques: []
id: 3f4816a9-40f7-41dc-9a93-3dd6d7729219
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Enable-IRCCloud-Embed-Settings

## Summary

This procedure configures the IRCCloud web client to enable social media link embeds, specifically for Mastodon, allowing subsequent steps to process and load malicious iframes.

## Description

In the attack scenario, the victim's IRCCloud settings must support embedding social media content. By default, 'Embed social media links' is enabled under 'Chat & embeds', but this step verifies and ensures it, targeting web-based IRC clients where embeds query external APIs like Mastodon's for preview data. Prerequisites include access to the victim's session or assuming default settings; outcomes enable iframe creation from untrusted sources, leading to XSS.

## Requirements

1. Access to IRCCloud web client (victim's browser session)
2. No special tools; manual settings navigation
3. Default or enabled embed feature

## Defense

Defensive measures and detection strategies:

- Disable social media embeds in IRCCloud settings to prevent API queries and iframe loads
- Monitor for unusual settings changes or embed-related network requests in browser dev tools

## Objectives

1. Prepare IRCCloud client for Mastodon link processing
2. Ensure no embed restrictions block the attack
3. Validate configuration for embed vulnerability

## Instructions

### Step 1: Access IRCCloud Settings

**Context**: Log into the web client and navigate to configuration to check embed options.

Open IRCCloud in a browser, click the settings icon, go to 'Chat & embeds' section, and locate 'Embed social media links'. Toggle it on if disabled.

> This step assumes victim control or defaults; in real attacks, rely on defaults being on.

### Step 2: Confirm Embed Functionality

**Context**: Test the setting by sending a benign Mastodon link to verify embedding works.

Send a safe Mastodon toot link in a test channel and observe if an embed preview appears without errors.

> Expected: Preview iframe loads; no console errors about embeds.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[web-embed]]
