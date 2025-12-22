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
  - '[[Modify Authentication Process]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 8d1279bf-1b5e-4d59-b5f3-b05a8b2ce817
created_at: '2025-12-13T09:01:26.870Z'
updated_at: '2025-12-13T09:01:26.870Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Modify Authentication Process]]'
---
# Create Modified EntityId Account

## Summary

This procedure creates an attacker-controlled Grammarly Business account with a modified entityId that includes a trailing space to exploit improper handling.

## Description

By duplicating the legitimate entityId with a trailing space and using a different keypair, the attacker sets up a conflicting organization. This targets Grammarly's SSO integration, where trimming occurs during authentication but not provisioning. Expected outcome is acceptance of the modified entityId.

## Requirements

1. Access to Grammarly Business signup
2. Ability to specify custom entityId
3. Different keypair for the new organization

## Defense

Defensive measures and detection strategies:

- Enforce normalization of entityIds (e.g., trim spaces)
- Detect and alert on near-duplicate entityId creations

## Objectives

1. Create conflicting organization
2. Introduce spaced entityId
3. Prepare for DoS exploitation

## Instructions

### Step 1: Sign Up for New Account

**Context**: Create a new Grammarly Business account.

Navigate to Grammarly Business signup and enter details for a new organization.

> Use standard signup process.

### Step 2: Modify EntityId

**Context**: Set entityId with trailing space.

During SSO configuration, input the legitimate entityId followed by a space, and associate a unique keypair.

> This creates the duplicate that Grammarly accepts.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Modify Authentication Process]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[sso]]
- [[entityid-manipulation]]
