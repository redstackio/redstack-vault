---
tags:
  - slack
  - post-submission
  - malicious-content
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands: []
verified: false
platforms:
  - Web
  - Desktop
  - Mobile
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:26:56.260Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: 275abbf7-16e3-4d39-b973-1498681a53e2
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Submit-Malicious-Post-in-Slack

## Summary

This procedure covers forwarding the modified request and sharing the post containing the DOM clobbering payload in a Slack channel or DM.

## Description

After interception, this submits the post to make the malicious hyperlink live. The payload remains dormant until rendered. Targets Slack's sharing mechanism; outcomes include the post appearing normal but primed for DoS on view.

## Requirements

1. Successfully modified POST request from prior interception
2. Target channel or DM with sharing permissions

## Defense

Defensive measures and detection strategies:

- Scan posted content for HTML injection patterns pre-render
- Rate-limit post submissions to detect bulk malicious activity
- User reporting mechanisms for suspicious posts

## Objectives

1. Complete post creation without errors
2. Share to a viewable location
3. Ensure payload is preserved in the post

## Instructions

### Step 1: Complete Submission

**Context**: Allow the request to proceed post-modification.

Forward in proxy tool and confirm in Slack UI.

> Post is drafted.

### Step 2: Share Post

**Context**: Publish to channel or DM.

Click send/share in the editor.

> Post is now live.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[submission]]
- [[sharing]]
