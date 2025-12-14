---
id: proc-uuid-4
tags:
  - xss
  - javascript
  - jquery
  - dom-xss
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
updated_at: '2025-12-13T23:52:44.223Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-JavaScript-Execution-via-jQuery-Parsing

## Summary

This procedure exploits the jQuery HTML parsing sink in TweetDeck to execute the injected XSS payload, achieving arbitrary JavaScript in the victim's browser context.

## Description

When the source is passed to `$()` in TweetDeck's JS bundle (bundle.6f91b4e832.js), jQuery interprets the payload as HTML, creating elements like SVG that trigger onload events. This leads to JS execution on the TweetDeck domain, enabling session hijacking or data theft. Target: TweetDeck web app. Note: May require IE for CSP bypass in some cases.

## Requirements

1. Victim interaction from previous step
2. TweetDeck loaded in browser
3. Payload in source field

## Defense

Defensive measures and detection strategies:

- Escape HTML in jQuery inputs
- Use text() instead of html() for source rendering
- Implement strict CSP without unsafe-inline
- Monitor for anomalous JS execution in browser

## Objectives

1. Parse payload via jQuery sink
2. Execute onload script
3. Achieve domain-context JS control

## Instructions

### Step 1: jQuery Processes Source

**Context**: Sink activation from link click.

The function `$(n.getMainTweet().source).attr('href')` parses the source string containing the payload.

### Step 2: HTML Element Creation

**Context**: Payload interpreted as DOM nodes.

jQuery creates an SVG element from `<svg onload=alert(document.domain)>`, attaching it to the DOM implicitly.

### Step 3: Onload Execution

**Context**: Trigger script in victim context.

The onload fires, executing alert or custom JS on tweetdeck.twitter.com domain.

**Expected Output**: Alert dialog or console execution confirming domain access.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- javascript
