---
tags:
  - sso
  - provisioning
  - account-takeover
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Valid Accounts]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: b97d0a9f-4cc2-4f51-b411-3da9b93b8411
created_at: '2025-12-11T03:47:39.563Z'
updated_at: '2025-12-11T03:47:39.563Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1078]]'
---
# Provision Victim User to Attacker Organization

## Summary

This procedure reprovisions a victim user into the attacker's organization by exploiting entityId prioritization after user deletion.

## Description

Removing the user from the legitimate org and retrying login causes provisioning to the attacker's org due to trimming in validation but not in assignment. This enables potential access to user data. Targets Grammarly business accounts.

## Requirements

1. Administrative access to legitimate organization to delete user.
2. Malicious organization setup.
3. SSO login attempt post-deletion.

## Defense

Defensive measures and detection strategies:

- Detect anomalous user provisioning events.
- Ensure consistent entityId handling (trimming everywhere).

## Objectives

1. Reprovision user to attacker control.
2. Set stage for full takeover.
3. Confirm unauthorized access path.

## Instructions

### Step 1: Delete User

**Context**: Remove the user from the legitimate organization.

Access the org dashboard and delete the target user.

> Web interface action.

### Step 2: Retry Login

**Context**: Attempt login to trigger provisioning.

Retry SSO; observe provisioning to attacker's org.

> User added to attacker dashboard.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- #provisioning
- #account-takeover
