---
tags:
  - sso
  - saml
  - entityid-manipulation
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Use Alternate Authentication Material]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: cfa268a0-c641-4def-befa-f89cc23f17ce
created_at: '2025-12-11T03:47:39.569Z'
updated_at: '2025-12-11T03:47:39.569Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1550]]'
---
# Register Malicious Grammarly Business Account with Spaced EntityId

## Summary

This procedure creates a new Grammarly business account with a modified entityId (appending a space) to exploit trimming inconsistencies in SSO handling.

## Description

By registering a duplicate entityId with a trailing space and a different keypair, this sets up conflicts for authentication and provisioning. The attack targets Grammarly's SSO integration, leading to potential DoS and takeovers. Expected outcome is a successfully created attacker organization without immediate detection.

## Requirements

1. Knowledge of the target entity's entityId.
2. Ability to create new Grammarly business accounts.
3. Different cryptographic keypair for the new account.

## Defense

Defensive measures and detection strategies:

- Enforce unique entityIds with normalization (e.g., trimming spaces).
- Audit new account creations for similar entityIds.

## Objectives

1. Create conflicting entityId.
2. Prepare for authentication conflicts.
3. Enable user provisioning to attacker org.

## Instructions

### Step 1: Obtain Original EntityId

**Context**: Copy the entityId from the legitimate setup.

Access the legitimate account's SSO config to note the entityId.

> No commands; web-based.

### Step 2: Register New Account

**Context**: Create the new account with modified entityId.

Sign up for a new Grammarly business account, input the entityId with a trailing space, and configure a new keypair.

> Expect successful registration.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Use Alternate Authentication Material]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- #sso
- #entityid-manipulation
