---
id: p4q5r6s7-t8u9-0123-efgh-ij4567890123
tags:
  - ui-toggle
  - bounty
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:53.509Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Enable-Bounty-Only-Invitations

## Summary

This procedure activates the 'Bounty programs only' option in HackerOne preferences, revealing the minimum bounty slider that enforces the client-side limit to be bypassed.

## Description

Enabling this UI toggle filters invitations to bounty-awarding programs and triggers the GraphQL mutation for preferences. It's a prerequisite for the vulnerability exploitation in the web UI.

## Requirements

1. Preferences page loaded
2. Authenticated session

## Defense

Defensive measures and detection strategies:

- Server-side validation of toggles
- Audit UI changes

## Objectives

1. Activate bounty filter
2. Display min bounty slider

## Instructions

### Step 1: Toggle Option

**Context**: Enable the invitation filter.

Locate and toggle 'Only invite me for programs that award a Bounty' to on.

> Slider appears for min bounty adjustment.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- toggle
- filter
