---
tags:
  - sso
  - saml
  - entityid
  - collision
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - SAML SSO
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:33:34.318Z'
sub_techniques: []
id: a48a7f19-d7e9-4243-b458-1ff00c1235e4
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-Malicious-Business-Account-with-Trailing-Space-EntityId

## Summary

This procedure involves registering a new Grammarly Business account under attacker control and configuring its SAML SSO with an entityId that exactly matches the victim's but includes a trailing space, exploiting the lack of trimming during organization matching.

## Description

By appending a trailing space to the entityId (e.g., 'myentity '), the attacker's organization becomes a higher-priority match in the untrimmed lookup, while the SAML response issuer is trimmed during validation, allowing authentication to pass but routing to the wrong org. This sets up the collision without immediate detection.

## Requirements

1. Knowledge of victim's entityId from prior setup
2. Access to a separate IdP for the malicious account
3. Ability to register new Grammarly Business accounts

## Defense

Defensive measures and detection strategies:

- Normalize (trim) entityIds consistently across authentication and provisioning
- Validate uniqueness of entityIds with canonicalization
- Alert on SSO configurations with whitespace variations

## Objectives

1. Create attacker-controlled organization with colliding identifier
2. Configure distinct keypair to avoid immediate conflicts
3. Prepare for propagation and prioritization exploit

## Instructions

### Step 1: Register New Business Account

**Context**: Sign up for a new Grammarly Business account to serve as the malicious entity.

No command; use the registration form on grammarly.com/business.

> Complete signup with attacker details; access the new admin dashboard.

### Step 2: Configure SSO with Modified EntityId

**Context**: In the new account's SSO settings, input the victim's entityId plus trailing space and a new keypair.

No command; upload IdP metadata with the altered entityId (e.g., 'myentity ') and generate/use a unique signing keypair.

> Configuration saves; test basic SSO if needed, but avoid victim interaction yet.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[sso]]
- [[saml]]
- [[entityid]]
- [[collision]]
