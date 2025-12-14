---
tags:
  - u2f
  - 2fa
  - skip-setup
type: procedure
tools: []
tactics: []
commands: []
platforms:
  - Web
techniques: []
skill_level: low
impact_level: low
detection_risk: low
sub_techniques: []
id: 972fc0b7-a370-4ac4-8b25-0fc5dddb5bdd
created_at: '2025-12-14T17:24:45.458Z'
updated_at: '2025-12-14T17:24:45.458Z'
verified: false
validated: true
submitted: true
---
# Skip-U2F-Security-Key-Registration

## Summary

This procedure ensures no FIDO U2F security key is registered during 2FA setup on Legal Robot, isolating the authenticator app method.

## Description

U2F is an optional hardware-based 2FA method. By skipping it, the account relies solely on the app, highlighting the notification logic flaw later. No hardware is needed; simply avoid the registration prompt. Outcome: Clean 2FA config with only app enabled.

## Requirements

1. Active 2FA session in settings
2. No U2F-compatible hardware

## Defense

Defensive measures and detection strategies:

- Clearly label optional 2FA methods in UI
- Track incomplete setups for user nudges
- Audit 2FA method combinations

## Objectives

1. Maintain single-method 2FA for testing
2. Prevent unintended key registration
3. Verify isolated app dependency

## Instructions

### Step 1: Review 2FA Options

**Context**: Identify and ignore U2F prompt.

In 2FA settings, note the U2F section but do not select or configure it.

### Step 2: Confirm Setup

**Context**: Save without U2F.

Proceed to save 2FA config, ensuring only authenticator app is active.

## MITRE ATT&CK Mapping

### Tactics


### Techniques


### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[u2f]]
- [[2fa]]
- [[skip-setup]]
