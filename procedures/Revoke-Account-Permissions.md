---
tags:
  - permissions
  - revoke
  - deprivilege
type: procedure
tools: []
tactics:
  - '[[Lateral Movement]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:29:09.569Z'
skill_level: basic
impact_level: low
detection_risk: low
sub_techniques: []
id: 6fa0845c-9781-45bf-9a9e-a1d25aa89639
validated: true
mitre_tactics:
  - '[[Lateral Movement]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Revoke-Account-Permissions

## Summary

This procedure removes the 'Settings' permission from a Shopify admin account, downgrading it to unprivileged status to test API authorization bypass.

## Description

Shopify's admin panel allows permission management for staff accounts. By revoking 'Settings', the account loses UI access to device registration but the API endpoint fails to enforce this check. This step simulates an unauthorized user scenario, enabling the replay of captured requests without proper perms.

## Requirements

1. Access to Shopify admin web interface with permission to edit users
2. Target account identifier

## Defense

Defensive measures and detection strategies:

- Audit permission changes with alerts for sensitive revocations
- Implement role-based access control (RBAC) with granular logging

## Objectives

1. Downgrade account to unprivileged
2. Verify UI restrictions apply
3. Set up for unauthorized API access

## Instructions

### Step 1: Access User Management

**Context**: Locate the account settings.

Log in to the Shopify admin dashboard at `admin.shopify.com` and navigate to 'Settings' > 'Users and permissions'.

### Step 2: Edit and Revoke Permission

**Context**: Apply the downgrade.

Select the target account, edit its permissions, and uncheck 'Settings'. Save changes.

**Expected Output**: Permission list updated; attempting UI device registration now shows access denied.

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement]] Lateral Movement

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- shopify
- permissions
- admin
