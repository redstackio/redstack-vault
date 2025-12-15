---
id: proc-shopify-revoke-permissions
tags:
  - shopify
  - permissions
  - revocation
type: procedure
tools: []
tactics:
  - '[[Defense Evasion]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Access Removal]]'
updated_at: '2025-12-14T17:30:35.775Z'
skill_level: low
impact_level: low
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Account Access Removal]]'
---
# Revoke-Development-Store-Permissions

## Summary

This procedure revokes specific development store permissions from a staff member after process initiation, testing the enforcement of access controls in ongoing workflows.

## Description

Using the organization owner account, edit the staff permissions to remove development store access while retaining managed store permissions. This step exploits the vulnerability by showing that revocation does not interrupt the creation process. Targeted at the Shopify web dashboard, it requires owner access and results in a de-elevated staff role that should block new actions but not complete existing ones.

## Requirements

1. Organization owner login
2. Ongoing staff session from initiation step
3. Dashboard access

## Defense

Defensive measures and detection strategies:

- Audit permission changes in real-time with notifications
- Re-validate user permissions on every API/UI interaction
- Implement time-bound permissions with automatic revocation

## Objectives

1. Downgrade staff to managed stores only
2. Ensure revocation does not halt active processes
3. Highlight improper access control gaps

## Instructions

### Step 1: Access Permissions Management

**Context**: Log in as owner and navigate to staff settings.

**Command** (Browser):
```bash
# UI: https://partners.shopify.com/settings/users
# Select staff (Doe)
```

> Owner dashboard loaded. Expected output: Staff list visible.

### Step 2: Revoke Specific Permissions

**Context**: Remove development store access.

**Command** (UI Edit):
```bash
# 1. Edit Doe’s role
# 2. Uncheck 'Development stores'
# 3. Keep 'Add/remove managed stores'
# 4. Save
```

> Permissions updated. Expected output: Confirmation; staff loses direct dev access.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion]] Defense Evasion

### Techniques

- [[Account Access Removal]] Account Access Removal (inverse for testing)

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[shopify]]
- [[permissions]]
- [[revocation]]
