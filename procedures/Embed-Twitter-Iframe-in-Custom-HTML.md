---
id: proc-uuid-3
tags:
  - iframe
  - sandbox
  - clickjacking
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
updated_at: '2025-12-14T17:28:13.005Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Embed-Twitter-Iframe-in-Custom-HTML

## Summary

Embed an iframe sourcing a Twitter page into the custom HTML file, using sandbox attributes to disable JavaScript frame-busters and enable clickjacking overlays.

## Description

This core exploitation step inserts a framed Twitter page into the Player Card HTML, overlaying bait content to trick clicks. It evades X-Frame-Options via nested framing and disables JS busting with sandbox. CSP frame-ancestors is bypassed in Safari/IE. Prerequisites: Hosted custom HTML and Twitter URL; outcomes: Functional clickjacking setup for wormable actions like auto-tweeting.

## Requirements

1. Hosted custom HTML on whitelisted domain
2. Knowledge of Twitter page URLs to frame
3. HTML editing skills

## Defense

Defensive measures and detection strategies:

- Implement robust frame-ancestors CSP
- Detect sandboxed iframes in embeds
- Monitor for anomalous tweet interactions

## Objectives

1. Frame Twitter content in Player Card
2. Disable protections with sandbox
3. Overlay bait for UI redressing

## Instructions

### Step 1: Insert Iframe Element

**Context**: Add the iframe to the HTML body to load Twitter content.

In the custom.html, insert: <iframe src="//twitter.com/target-page" sandbox="allow-scripts allow-same-origin"></iframe>. Position it to cover the card area.

> The sandbox disables frame-busters while allowing scripts.

### Step 2: Add Overlay Bait

**Context**: Layer transparent or subtle elements over the iframe to hijack clicks.

Add divs with z-index higher than the iframe, containing bait like "Click to play" buttons aligned over Twitter actions (e.g., tweet button).

> Expected: Clicks on bait trigger framed Twitter interactions.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[iframe]]
- [[clickjacking]]
