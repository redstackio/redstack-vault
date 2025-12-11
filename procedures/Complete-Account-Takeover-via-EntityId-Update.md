---
tags:
  - sso
  - account-takeover
  - entityid-update
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
impact_level: high
detection_risk: high
sub_techniques: []
id: bffda68e-aa8c-49cc-9df4-34b1fbd0bf48
created_at: '2025-12-11T03:47:39.560Z'
updated_at: '2025-12-11T03:47:39.560Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1550]]'
---
# Complete Account Takeover via EntityId Update

## Summary

This procedure finalizes account takeover by updating the attacker's entityId and authenticating with their keypair to access the victim's provisioned account.

## Description

After provisioning, changing to a unique entityId allows the attacker to log in and access documents, completing the takeover. This exploits the initial conflict and provisioning flaw in Grammarly's SSO.

## Requirements

1. Victim user provisioned to attacker org.
2. Access to update entityId in attacker account.
3. Attacker's keypair.

## Defense

Defensive measures and detection strategies:

- Track entityId changes and correlate with logins.
- Implement re-verification on entityId updates.

## Objectives

1. Gain full access to victim account.
2. Access personal documents.
3. Demonstrate complete takeover.

## Instructions

### Step 1: Update EntityId

**Context**: Change the attacker's entityId to a new unique value.

Access the attacker account config and update the entityId.

> Ensure it's unique to avoid further conflicts.

### Step 2: Authenticate as Victim

**Context**: Log in using attacker's keypair.

Attempt SSO login; access the victim's account and data.

> Confirm access to documents.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Use Alternate Authentication Material]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- #account-takeover
- #entityid-update
