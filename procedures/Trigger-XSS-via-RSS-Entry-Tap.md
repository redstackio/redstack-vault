---
id: uuid-placeholder-003
tags:
  - xss
  - dom-xss
  - javascript
  - ios
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - iOS
  - Mobile
submitted: true
created_at: '[TIMESTAMP]'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:20.851Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-via-RSS-Entry-Tap

## Summary

This procedure details how to trigger the DOM-based XSS payload in the Brave iOS app by interacting with the malicious RSS entry, resulting in JavaScript execution on the privileged localhost domain.

## Description

After adding the malicious RSS feed, the app renders entries in Brave Today. Tapping an entry with a javascript: URL in the <link> href executes the payload directly in the app's webview context on http://localhost:65XX. This compromises internal app features without server-side involvement, relying on user interaction for delivery. The attack succeeds due to lack of scheme validation in the RSS parser.

## Requirements

1. Malicious RSS feed already added and enabled in Brave Today
2. New browser tab open in Brave iOS
3. User interaction capability on the device

## Defense

Defensive measures and detection strategies:

- Strip or rewrite non-http/https URLs in RSS links during parsing
- Use sandboxed webviews for feed rendering to limit localhost access
- Log and alert on JS alerts or domain accesses from feeds

## Objectives

1. Load Brave Today to display malicious entry
2. Execute javascript: payload via tap
3. Confirm compromise of localhost domain

## Instructions

### Step 1: Close Settings and Open New Tab

**Context**: Transition from configuration to browsing mode.

Exit settings menu and create a new tab in the browser.

> Prepares the interface for Brave Today sidebar.

### Step 2: Enable Brave Today Sidebar

**Context**: Activate the feed view to show entries.

Tap to enable the Brave Today sidebar; the PoC feed entries load.

> Malicious "XSS" entry appears in the list.

### Step 3: Tap the XSS Article Entry

**Context**: Trigger the payload execution.

Locate and tap the "XSS" entry from the PoC feed.

> The app parses the javascript:alert(document.domain) in the <link> href, executing it on localhost:65XX, popping an alert with the domain.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[xss]]
- [[dom-xss]]
- [[JavaScript]]
- [[ios]]
