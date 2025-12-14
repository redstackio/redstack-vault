---
tags:
  - propagation
  - cross-user
  - xss
  - web
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
sub_techniques: []
id: 2848a785-feaa-4503-a9a6-d0eae414e867
created_at: '2025-12-14T17:32:01.944Z'
updated_at: '2025-12-14T17:32:01.944Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Share-Wallet-for-Cross-User-Impact

## Summary

This procedure shares the tainted wallet to affect other users, propagating the stored XSS when they view settings.

## Description

If sharing is enabled, victims viewing the settings execute the payload. A server-side filter partially mitigates JS at report time, but HTML injection persists in the web app.

## Requirements

1. Wallet with stored payload
2. Sharing feature available
3. Access to other user accounts for testing

## Defense

Defensive measures and detection strategies:

- Disable or restrict wallet sharing
- Filter shared content for XSS

## Objectives

1. Extend impact beyond originator
2. Trigger XSS in multiple contexts
3. Highlight persistence risks

## Instructions

### Step 1: Initiate Share

**Context**: Use sharing functionality.

**Action**: Select the wallet and choose share option, providing access to another user.

> Share link or permissions granted.

### Step 2: Victim Access

**Context**: Simulate other user viewing.

**Action**: Log in as another user and access the shared wallet settings.

> Settings load for the victim.

### Step 3: Confirm Impact

**Context**: Check execution.

**Action**: Observe if payload triggers in victim's browser.

> XSS executes; note any server-side filtering effects.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[propagation]]
- [[cross-user]]
- [[xss]]
- [[web]]
