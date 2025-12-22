---
tags:
  - provisioning
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
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 52cfc5b4-9027-49ca-8a2d-5a4f65846223
created_at: '2025-12-13T09:01:26.859Z'
updated_at: '2025-12-13T09:01:26.859Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Modify Authentication Process]]'
---
# Provision User to Attacker Organization

## Summary

This procedure provisions a user from the victim organization into the attacker's by exploiting entityId prioritization after user deletion.

## Description

Deleting the user from the victim organization allows authentication against the original but provisioning to the attacker's due to the spaced entityId. This targets user management in Grammarly's SSO.

## Requirements

1. DoS condition already induced
2. Administrative access to victim organization for user deletion
3. Legitimate credentials

## Defense

Defensive measures and detection strategies:

- Audit user provisioning events
- Prevent entityId conflicts in database

## Objectives

1. Redirect user provisioning
2. Gain control over user account
3. Set up for takeover

## Instructions

### Step 1: Delete User

**Context**: Remove user from legitimate organization.

Access the organization dashboard and delete the target user.

> This clears the user for reprovisioning.

### Step 2: Attempt Login

**Context**: Trigger provisioning to attacker org.

Log in again; observe provisioning to the attacker's organization.

> User now under attacker control.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Modify Authentication Process]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[provisioning]]
- [[sso]]
