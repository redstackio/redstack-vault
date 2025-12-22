---
tags:
  - intent-trigger
  - dialog
  - twitter
type: procedure
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:28:20.491Z'
sub_techniques: []
id: d95e3da3-4cb9-4180-8af2-ef65af4e601b
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-Twitter-Intent-Dialog

## Summary

This procedure handles the victim's click on the malicious URL, loading the Twitter intent favorite page and embedding the payload in a hidden input.

## Description

Clicking opens /intent/favorite, showing a dialog with 'Favorite' button. The payload in original_referer populates a hidden referer input, but processing is deferred until Referer is validated as twitter.com.

## Requirements

1. Victim's Twitter authentication
2. Malicious URL access
3. No ad blockers interfering with Twitter

## Defense

Defensive measures and detection strategies:

- Validate referer sources strictly
- Log intent accesses for anomalies
- Block non-standard parameters

## Objectives

1. Load intent page
2. Embed payload in DOM
3. Prepare for bypass

## Instructions

### Step 1: Victim Accesses URL

**Context**: Initiate page load.

URL directs to intent/favorite with parameters.

### Step 2: Dialog Displays

**Context**: Render hidden input with payload.

Observe <input type='hidden' name='referer' value='...[payload]...'>.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[intent-trigger]]
