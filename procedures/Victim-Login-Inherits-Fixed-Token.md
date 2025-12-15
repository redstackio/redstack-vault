---
tags:
  - csrf
  - session-sharing
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
updated_at: '2025-12-14T17:33:06.077Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 7d009477-9b1e-42a3-8be2-d2313b5f5e86
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Victim-Login-Inherits-Fixed-Token

## Summary

This procedure involves the victim logging into Khan Academy on a shared browser, where they inherit the attacker's fixed fkey CSRF token.

## Description

In shared computer scenarios, the static fkey from a prior session is reused by the victim's login, binding their authenticated actions to the attacker's known token. This enables forging without direct access, amplified by social engineering to get the victim to log in post-attacker logout.

## Requirements

1. Shared browser environment with lingering fkey
2. Victim's Khan Academy credentials
3. Attacker knowledge of the setup (e.g., via phishing lure)

## Defense

Defensive measures and detection strategies:

- Enforce token regeneration on every login
- Use device binding or multi-factor for session validation
- Log session token mismatches or shared device usage

## Objectives

1. Establish victim's session with compromised fkey
2. Confirm inheritance via inspection
3. Set stage for forged requests

## Instructions

### Step 1: Induce Victim Login

**Context**: Trick the victim into logging in on the prepared browser.

Use social engineering (e.g., email lure) to direct victim to https://www.khanacademy.org and have them authenticate.

> Victim enters credentials; session starts with the pre-existing fkey.

### Step 2: Validate Inherited Token

**Context**: Attacker (remotely or later) verifies the fkey matches.

If possible, inspect victim's browser or infer via subsequent exploit success.

> DevTools on victim's side shows the same fkey value as attacker's extracted one.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[shared-session]]
