---
id: uuid-placeholder-5
tags:
  - shopify
  - permission-revocation
  - staff-removal
type: procedure
tools: []
tactics:
  - '[[Persistence]]'
commands: []
verified: false
platforms:
  - Web
  - Shopify
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:30:07.357Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Revoke-Staff-Permissions

## Summary

This procedure removes or deactivates a staff account's permissions in Shopify, simulating a security hygiene step that fails to invalidate existing signed URLs.

## Description

As the owner, revoke access to test if prior actions (like URL generation) persist. This highlights the vulnerability where path_hmac-based URLs remain valid without session ties.

## Requirements

1. Owner credentials.
2. Existing staff account to revoke.
3. Access to admin panel.

## Defense

Defensive measures and detection strategies:

- Automate permission revocation to invalidate associated tokens/URLs.
- Audit logs for post-revocation access attempts.

## Objectives

1. Simulate departed staff.
2. Test URL persistence.
3. Highlight authorization gap.

## Instructions

### Step 1: Owner Login

**Context**: Regain control.

Log in as owner to admin panel.

### Step 2: Manage Staff

**Context**: Revoke access.

Go to Settings > Users and permissions, select the staff account, and click 'Remove' or deactivate.

> Expected output: Account removed from list.

### Step 3: Confirm Revocation

**Context**: Verify no access.

Attempt staff login; it should fail.

> Expected output: Access denied.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]] Persistence

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[permission-revocation]]
