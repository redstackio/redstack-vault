---
tags:
  - removal
  - staff
  - revoke
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - Shopify
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:29:44.798Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: b60a5985-06c0-4476-8dd4-129558647eb3
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Remove-Staff-Account

## Summary

This procedure removes the staff account from Shopify to simulate an ex-employee scenario, allowing testing of whether prior signed URLs remain valid despite revoked permissions.

## Description

Switch to shop owner credentials and access the users management section in the Shopify admin. Locate the staff account created earlier and delete it. This action revokes all permissions but does not invalidate existing signed URLs or tokens in the Flow app, enabling the authorization bypass. Confirm removal by attempting staff login, which should fail.

## Requirements

1. Shopify shop owner credentials
2. Access to Settings > Users and permissions
3. Prior staff account existence

## Defense

Defensive measures and detection strategies:

- Automatically invalidate all active sessions and tokens on staff removal
- Audit logs for post-removal access attempts to apps
- Enforce permission checks on every API/URL access

## Objectives

1. Revoke staff permissions to test persistence
2. Simulate real-world offboarding
3. Verify login failure post-removal

## Instructions

### Step 1: Access Users Management

**Context**: Log in as owner to manage staff.

No specific command; manual UI navigation:

Log in at https://admin.shopify.com > Settings > Users and permissions.

> List of staff accounts displays.

### Step 2: Remove Account

**Context**: Delete the target staff member.

No specific command; manual UI action:

Select staff account > Click 'Remove' or 'Delete' > Confirm.

> Account is removed; permissions revoked.

### Step 3: Verify Removal

**Context**: Test that staff can no longer access admin.

No specific command; manual test:

Attempt login with staff credentials > Should redirect or deny access.

> Confirms revocation successful.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[removal]]
- [[staff]]
- [[revoke]]
