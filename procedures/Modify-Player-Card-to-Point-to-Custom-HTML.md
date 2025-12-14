---
id: proc-uuid-2
tags:
  - twitter
  - player-card
  - modification
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
updated_at: '2025-12-14T17:28:13.008Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Modify-Player-Card-to-Point-to-Custom-HTML

## Summary

Modify the Twitter Player Card configuration to redirect the _twitter:player_ property to a custom HTML file hosted on a whitelisted domain, setting the stage for iframe-based clickjacking.

## Description

Twitter's Player Card renders custom HTML from whitelisted domains in tweets. This procedure updates the card's metadata to point to attacker-controlled HTML, bypassing basic framing checks. It exploits evadable protections like X-Frame-Options: SAMEORIGIN via nested origins. Prerequisites: Whitelisted domain and text editor; outcomes include a configured card ready for embedding Twitter iframes, enabling UI redressing.

## Requirements

1. Whitelisted domain for hosting HTML
2. Text editor (e.g., VS Code)
3. Cloned starter bundle from prior step

## Defense

Defensive measures and detection strategies:

- Strict whitelisting review for domains
- Audit metadata changes in card configs
- Enforce CSP frame-ancestors universally

## Objectives

1. Redirect Player Card to custom content
2. Ensure whitelisting compatibility
3. Prepare for iframe insertion

## Instructions

### Step 1: Edit Metadata Property

**Context**: Locate the _twitter:player_ property in the card config file from the starter bundle.

Open the config file and change the value to your custom HTML URL, e.g., _twitter:player: https://whitelisted-domain.com/custom.html.

> Validate the URL is accessible and whitelisted.

### Step 2: Host and Test Config

**Context**: Upload the modified config to your whitelisted domain and verify rendering.

Host the file and use Twitter's card validator tool to check if the property resolves correctly.

> Expected: Card preview shows custom HTML intent.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[twitter]]
- [[player-card]]
