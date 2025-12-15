---
tags:
  - dos
  - rendering
  - crash
  - phishing
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
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:26:56.254Z'
skill_level: beginner
impact_level: high
detection_risk: high
sub_techniques: []
id: 082b5d09-5927-498c-87d5-833d71d64ad8
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Trigger-DOS-by-Viewing-Post

## Summary

This procedure activates the DOM clobbering by rendering the malicious post, causing JavaScript errors and application crashes, with optional phishing on mobile.

## Description

Viewing the post parses the injected HTML, creating named elements that override document.write, createElement, etc., leading to JS failures and DoS. On mobile, <iframe> injection enables phishing. Targets post rendering engine; outcomes: Immediate crash on affected clients.

## Requirements

1. Live malicious post in a channel or DM
2. Victim access to view the post (self or shared)

## Defense

Defensive measures and detection strategies:

- Sanitize rendered HTML to strip name attributes and dangerous tags
- Isolate rendering in sandboxed iframes
- Monitor JS error logs for clobbering patterns

## Objectives

1. Cause application denial of service via errors
2. Demonstrate cross-platform impact
3. Enable phishing if iframes are injected

## Instructions

### Step 1: Navigate to Post

**Context**: Access the containing channel or DM.

Open Slack and go to the location.

> Post loads.

### Step 2: Render and Interact

**Context**: View the post to trigger clobbering; on mobile, click for phishing.

Scroll to or click the post.

> JS errors occur, app crashes; iframe may load phishing site.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Endpoint Denial of Service]] Endpoint Denial of Service

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[trigger]]
- [[crash]]
