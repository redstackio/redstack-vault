---
tags:
  - csrf
  - social-engineering
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:57.372Z'
sub_techniques: []
id: e514ffc9-2d86-4541-8f12-84b57d0b82c5
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Deliver-CSRF-Attack-to-Victim

## Summary

This procedure tricks an authenticated Lichess user into visiting the hosted page and clicking the link, triggering the CSRF to update their network routing settings without consent.

## Description

Social engineering is key here, as the victim must be logged in for the session cookies to be sent with the forged request. The impact is a forced switch to direct routing, potentially causing slower connections by avoiding CDN optimization.

## Requirements

1. Hosted URL from previous procedure
2. Communication channel to victim (email, Discord, etc.)
3. Victim authenticated in Lichess

## Defense

Defensive measures and detection strategies:

- User training on suspicious links
- Browser extensions for CSRF warnings
- Server-side logging of setting changes tied to referrers

## Objectives

1. Induce victim interaction with the payload
2. Confirm execution via settings change
3. Minimize detection during delivery

## Instructions

### Step 1: Craft Delivery Message

**Context**: Create a pretext to get the victim to click the URL.

Example message: "Hey, check out this cool chess opening strategy: https://attacker-site.com/csrf.html"

Send via preferred channel.

### Step 2: Monitor Execution

**Context**: Verify the attack succeeds without direct access.

If possible, ask the victim about their connection or check public indicators. In a test, log into Lichess, click the link, and navigate to /account/network to see usingAltSocket=false applied.

**Expected Output**: Settings updated; no confirmation dialog appears.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[social-engineering]]
