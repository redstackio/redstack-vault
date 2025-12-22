---
tags:
  - privilege-escalation
  - shopify
  - pos-login
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:29:10.046Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 95a2bbef-e9d7-41e5-8fb9-93fb417c3a75
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---
# Login to POS with Admin then Switch to Limited User

## Summary

This procedure authenticates into the Shopify POS app using owner credentials and switches to a limited user's session via PIN, establishing the constrained context for escalation.

## Description

The POS app allows session inheritance from owner login, but permission checks are role-based. This step leverages that to enter a limited state, requiring physical device access. It sets up the environment where UI flaws can be exploited without alerting on credential use.

## Requirements

1. POS terminal device (e.g., iPad, browser emulation)
2. Store owner admin credentials
3. PIN for the limited POS user from prior setup

## Defense

Defensive measures and detection strategies:

- Require unique device authentication for POS
- Log session switches and PIN entries
- Implement session timeout on role changes

## Objectives

1. Enter POS under owner context initially
2. Switch to limited role without logout
3. Confirm restricted UI loads

## Instructions

### Step 1: Launch and Admin Login

**Context**: Initiate POS with high privileges.

Open the Shopify POS application on the terminal. Enter store owner admin email and password to log in.

> POS dashboard loads with full options visible.

### Step 2: Switch Sessions

**Context**: Downgrade to limited user.

From the POS interface, enter the PIN of the limited user (from Step 2 of chain). Confirm the switch.

> Interface updates to show only permitted features, like staff management.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[privilege-escalation]]
- [[shopify]]
- [[pos-login]]
