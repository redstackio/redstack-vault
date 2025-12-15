---
tags:
  - sso
  - saml
  - propagation
  - dos
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
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:33:34.317Z'
sub_techniques: []
id: 2926ff11-61af-4485-943b-c38cd720b33e
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Wait-for-Propagation-and-Test-Victim-Login

## Summary

This procedure waits for the attacker's entityId change to propagate in Grammarly's backend systems and then tests login to the victim's account, triggering the DOS due to entityId prioritization.

## Description

Grammarly's system requires about 2 minutes for entityId updates to take effect. During this, the untrimmed colliding entityId overrides the victim's, causing authentication to fail as the organization lookup favors the attacker's setup while the trimmed SAML issuer still validates.

## Requirements

1. Malicious account configured with colliding entityId
2. Victim SSO credentials
3. Timer or wait mechanism for propagation

## Defense

Defensive measures and detection strategies:

- Implement immediate propagation locks or caching invalidation
- Monitor login failure rates post-SSO config changes
- Log entityId lookups for collision detection

## Objectives

1. Ensure backend synchronization of the colliding entityId
2. Induce and observe login failure on victim account
3. Confirm prioritization of attacker's organization

## Instructions

### Step 1: Initiate Propagation Wait

**Context**: After configuring the malicious account, pause to allow system-wide propagation.

No command; wait 2 minutes manually.

> Propagation completes; no visible indicators until testing.

### Step 2: Attempt Victim SSO Login

**Context**: Use legitimate victim credentials to authenticate via SSO.

No command; navigate to Grammarly login and select SSO option.

> Expect an error like 'Invalid organization' or 'SSO failure' due to mismatched entityId handling.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

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
- [[propagation]]
- [[dos]]
