---
tags:
  - account-takeover
  - sso
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Modify Authentication Process]]'
skill_level: advanced
impact_level: critical
detection_risk: high
sub_techniques: []
id: c05f6b98-9568-4a48-9d77-5347acf0220c
created_at: '2025-12-13T09:01:26.856Z'
updated_at: '2025-12-13T09:01:26.856Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Modify Authentication Process]]'
---
# Modify EntityId for Account Takeover

## Summary

This procedure completes account takeover by changing the attacker's entityId and logging in with the attacker's keypair.

## Description

After provisioning, modifying the entityId allows the attacker to access the victim's account, potentially including personal documents. This exploits the takeover vector in Grammarly's SSO.

## Requirements

1. User provisioned to attacker organization
2. Control over attacker's entityId configuration
3. Attacker's keypair

## Defense

Defensive measures and detection strategies:

- Monitor entityId changes and login anomalies
- Implement multi-factor checks for provisioning

## Objectives

1. Achieve full account access
2. Access sensitive data
3. Demonstrate takeover impact

## Instructions

### Step 1: Change EntityId

**Context**: Update attacker's entityId.

Modify the entityId in the attacker's organization settings to a new value.

> This isolates the provisioned user.

### Step 2: Login with Attacker Keypair

**Context**: Access victim's account.

Log in to the victim's account using the attacker's keypair.

> Gain access to documents and data.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Modify Authentication Process]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[account-takeover]]
- [[sso]]
