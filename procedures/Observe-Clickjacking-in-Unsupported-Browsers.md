---
id: proc-uuid-5
tags:
  - safari
  - ie
  - exploitation
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
updated_at: '2025-12-14T17:28:12.995Z'
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
# Observe-Clickjacking-in-Unsupported-Browsers

## Summary

Expand the malicious tweet in browsers like Safari or IE that lack CSP frame-ancestors support to observe and demonstrate the clickjacking, confirming action hijacking.

## Description

In unsupported browsers, the iframe frames Twitter without restrictions, allowing overlays to trick users into actions like following or tweeting. This validates the wormable nature, especially on timelines. Prerequisites: Posted tweet and target browser; outcomes: Proof-of-concept of severe impact via subtle clicks.

## Requirements

1. Safari or Internet Explorer browser
2. Access to the posted tweet
3. Victim simulation setup

## Defense

Defensive measures and detection strategies:

- Polyfill CSP for legacy browsers
- Browser-specific framing policies
- Anomaly detection in user actions

## Objectives

1. Load tweet in unsupported browser
2. Expand and interact with card
3. Verify unintended actions

## Instructions

### Step 1: Load Tweet in Target Browser

**Context**: Open the tweet in Safari or IE to bypass CSP limitations.

Navigate to the tweet URL in the browser and ensure it's not blocked.

> X-Frame-Options evaded via nesting.

### Step 2: Expand and Test Clickjacking

**Context**: Interact with the expanded card to trigger hijacked actions.

Click the bait overlay; observe if it causes Twitter actions like retweeting without direct intent.

> Expected: Wormable spread if auto-tweet configured.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[clickjacking]]
- [[safari]]
