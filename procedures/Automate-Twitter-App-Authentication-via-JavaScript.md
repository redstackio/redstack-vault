---
tags:
  - javascript
  - automation
  - twitter-oauth
type: procedure
tools: []
tactics:
  - '[[Persistence]]'
commands: []
verified: false
platforms:
  - Web
  - Twitter
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:28:12.896Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 0524b439-c97b-4162-a266-5a6d458cb8a7
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Automate-Twitter-App-Authentication-via-JavaScript

## Summary

This procedure uses JavaScript on the OAuth page to automatically click the authenticate button if the victim is logged into Twitter, granting the malicious app permissions to send DMs without further interaction.

## Description

At api.twitter.com/oauth/authenticate, embedded JS detects logged-in state and simulates a click on the 'Authorize app' button, installing the app and enabling viral DM propagation to all contacts.

## Requirements

1. Victim logged into Twitter
2. Malicious app with DM send permissions
3. JS-enabled browser on OAuth page

## Defense

Defensive measures and detection strategies:

- Disable JS for suspicious sites or use NoScript
- Review app permissions before auth
- Detect automated OAuth consents via logs

## Objectives

1. Automate app installation
2. Grant DM sending access
3. Enable silent propagation

## Instructions

### Step 1: Load OAuth Screen

**Context**: Redirect lands on Twitter auth page for malicious app.

Browser displays authenticate interface.

> Expected: 'Authorize' button visible.

### Step 2: Execute JS Automation

**Context**: Script runs to auto-click if session active.

Embed JS like document.querySelector('button').click();

> Expected: App authorized without user input.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[JavaScript]]
- [[automation]]
- [[twitter-oauth]]
