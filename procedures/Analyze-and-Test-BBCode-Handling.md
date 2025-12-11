---
tags:
  - bbcode
  - xss
type: procedure
tools:
  - '[[tools/Chrome-DevTools]]'
  - '[[tools/React-Developer-Tools]]'
  - '[[tools/Binary-Grep]]'
  - '[[tools/Vim]]'
  - '[[tools/Remote-Chrome-Console]]'
tactics:
  - '[[Lateral Movement]]'
commands:
  - '[[commands/steam-open-game]]'
  - '[[commands/steam-open-console]]'
  - '[[commands/window-top-postmessage]]'
  - '[[commands/open-steam-uri]]'
  - '[[commands/object-keys-window]]'
  - '[[commands/steam-openexternalforpid-jarfile]]'
  - '[[commands/steam-openexternalforpid-file]]'
  - '[[commands/custom-protocol-txt]]'
  - '[[commands/custom-protocol-calculator]]'
  - '[[commands/custom-protocol-jarfile-traversal]]'
  - '[[commands/custom-protocol-jarfile-path]]'
platforms:
  - Web
techniques:
  - '[[User Execution]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 178887e0-4622-4635-9dab-cf32d24bc33e
created_at: '2025-12-11T06:10:22.144Z'
updated_at: '2025-12-11T06:10:22.144Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0008]]'
mitre_techniques:
  - '[[T1204]]'
---
# Analyze and Test BBCode Handling

## Summary

This procedure analyzes BBCode parsing in Steam Chat and tests tags for exploitation potential, focusing on [url] allowing arbitrary URIs.

## Description

Messages are rendered twice (client-side and server-side), and unsanitized [url] tags permit javascript: URIs, leading to stored XSS.

## Requirements

1. Steam chat access to a test account
2. Ability to send and receive messages

## Defense

Defensive measures and detection strategies:

- Server-side sanitization of BBCode tags
- Block javascript: and steam:// URIs in chat

## Objectives

1. Observe rendering behavior
2. Identify exploitable tags
3. Confirm arbitrary URL allowance

## Instructions

### Step 1: Test BBCode Tags

**Context**: Send various tags and observe rendering.

Send [url=xxx], [code], [image] in chat and monitor in [[tools/Chrome-DevTools]].

> Expected: [url] renders as <a href> with user-controlled href.

### Step 2: Test Arbitrary URIs

**Context**: Attempt javascript: injection.

Send [url=javascript:alert(1)] and click.

> Expected: Alert execution confirming XSS.

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement]]

### Techniques

- [[User Execution]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/Chrome-DevTools]]

## Tags

- [[bbcode]]
- [[xss]]
