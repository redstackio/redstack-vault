---
tags:
  - sso
  - saml
  - provisioning
  - dos
type: procedure
tools: []
tactics:
  - '[[Lateral Movement]]'
commands: []
verified: false
platforms:
  - Web
  - SAML SSO
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:33:34.315Z'
sub_techniques: []
id: d09b86ff-9428-4a5c-94e2-1e68bbfda757
validated: true
mitre_tactics:
  - '[[Lateral Movement]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Verify-DOS-and-Test-User-Provisioning-via-Re-Authentication

## Summary

This procedure confirms the ongoing DOS on the victim's SSO and exploits the provisioning flaw by deleting the user and re-authenticating, resulting in placement into the attacker's organization.

## Description

With the victim SSO blocked, deleting the user simulates a new provisioning scenario. Upon re-login, the SAML response's trimmed issuer authenticates the user, but the untrimmed entityId match routes them to the attacker's org, enabling unauthorized access.

## Requirements

1. Admin access to victim organization for user deletion
2. Persistent DOS from prior steps
3. Attacker's organization active with collision

## Defense

Defensive measures and detection strategies:

- Cross-validate trimmed and untrimmed entityIds during provisioning
- Require explicit organization confirmation post-auth
- Audit user deletions and re-provisionings for patterns

## Objectives

1. Validate persistent denial-of-service on victim login
2. Demonstrate unauthorized user migration to attacker org
3. Gain initial access to victim user within attacker control

## Instructions

### Step 1: Confirm Victim SSO DOS

**Context**: Attempt multiple logins to victim's account to verify inaccessibility.

No command; repeat SSO login attempts.

> Consistent errors confirm DOS; no access to victim resources.

### Step 2: Delete and Re-Authenticate User

**Context**: As victim admin, remove the user, then re-initiate SSO login.

No command; use admin panel to delete user, then login via SSO.

> User authenticates but is provisioned into attacker's org dashboard.

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement]] Lateral Movement

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[sso]]
- [[saml]]
- [[provisioning]]
- [[dos]]
