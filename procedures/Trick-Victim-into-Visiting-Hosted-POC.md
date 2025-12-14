---
tags:
  - social-engineering
  - phishing
  - execution
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:30:07.436Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 53f7a548-530b-4c29-a168-743d0f4b4546
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
  - '[[Exploit Public-Facing Application]]'
---
# Trick-Victim-into-Visiting-Hosted-POC

## Summary

This procedure delivers the hosted CSRF PoC link to the victim, tricking them into loading it while logged into Tucows to execute unauthorized note modification.

## Description

The victim is induced to visit the URL (e.g., via phishing email), where the page auto-submits the forged POST using their session cookies, bypassing CSRF protections. This leads to data loss, phishing injection, or privacy breaches if notes hold sensitive info. Requires victim to be authenticated.

## Requirements

1. Hosted PoC URL
2. Communication channel to victim (email, chat)
3. Knowledge of victim's login habits

## Defense

Defensive measures and detection strategies:

- Train on link verification and CSRF awareness
- Monitor for unexpected note changes and alert users

## Objectives

1. Induce page load in authenticated session
2. Trigger forged request
3. Achieve unauthorized data alteration

## Instructions

### Step 1: Craft Delivery Message

**Context**: Disguise the link.

Create a phishing pretext, e.g., "Check this update on your order: [URL]".

> Embed URL in email or message.

### Step 2: Monitor Execution

**Context**: Confirm impact.

Send link; if possible, check notes for changes post-visit.

> Expected: Auto-submit sends POST; notes modified/deleted.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- social-engineering
- phishing
