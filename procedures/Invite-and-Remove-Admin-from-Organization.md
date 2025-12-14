---
id: proc-invite-remove-admin
tags:
  - admin-invite
  - access-revocation
  - fabric-io
type: procedure
tools: []
tactics:
  - '[[Persistence]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:28:58.775Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Invite-and-Remove-Admin-from-Organization

## Summary

Invite a test admin to the organization, promote their role, capture IDs, and remove them to test if access rights are properly revoked in Fabric.io.

## Description

This step simulates the vulnerability trigger by granting and then revoking admin privileges. Log in as Victimadmin to invite Hackeradmin, promote to admin, and record IDs. Then remove Hackeradmin, which should revoke all permissions but fails due to the bug. Target environment is the Fabric.io web app; outcomes include retained session-based access for exploitation.

## Requirements

1. Existing VictimOrg with Victimadmin access
2. Hackeradmin account credentials
3. Browser network inspection tools

## Defense

Defensive measures and detection strategies:

- Implement immediate token revocation on user removal
- Log all role changes and audit post-removal actions

## Objectives

1. Establish ex-admin scenario
2. Capture IDs for request modification
3. Confirm UI removal without backend cleanup

## Instructions

### Step 1: Invite and Promote Admin

**Context**: Add Hackeradmin as admin to VictimOrg and note identifiers.

Log in as Victimadmin, go to VictimOrg settings > Team, invite Hackeradmin by email, accept invite, promote to admin role. Inspect network requests to get VictimOrg id (54af7e07b8568e8c6a0001e) and Victimmember id (552787195127ae16b8000987).

**Expected Output**: Hackeradmin appears as admin in team list.

### Step 2: Remove Admin

**Context**: Revoke Hackeradmin's membership to trigger improper revocation.

From team settings, click remove on Hackeradmin.

**Expected Output**: Hackeradmin disappears from UI team list; no error messages.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]] Persistence

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[admin-invite]]
- [[access-revocation]]
