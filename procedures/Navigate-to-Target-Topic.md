---
id: proc-uuid-2
tags:
  - navigation
  - web
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
updated_at: '2025-12-14T17:26:55.801Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Navigate-to-Target-Topic

## Summary

This procedure positions the attacker within the forum to target a specific topic for reply submission, setting up the vulnerable endpoint interaction.

## Description

For the DoS attack, navigation to a default topic like discobot's welcome message exposes the reply POST endpoint. The scenario involves an authenticated web session on Discourse. Outcomes: Access to composer for interception. Prerequisites: Active session.

## Requirements

1. Authenticated session from prior login
2. Browser access to forum topics
3. Knowledge of target topic ID (e.g., welcome topic)

## Defense

Defensive measures and detection strategies:

- Log user navigation patterns for unusual topic access
- Rate-limit topic views or interactions

## Objectives

1. Load the target topic page
2. Expose the reply interface
3. Prepare for request interception

## Instructions

### Step 1: Browse to Welcome Topic

**Context**: Select a low-traffic topic to minimize detection during testing.

No command; in browser, go to https://try.discourse.org/t/welcome-to-discourse/1 or similar discobot post.

> Page loads with topic content and reply button. Expected: Composer opens on click.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise (adapted for navigation)

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- navigation
- web
