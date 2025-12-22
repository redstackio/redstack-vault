---
id: proc-assign-shopify-staff-perms-001
tags:
  - shopify
  - permissions
  - setup
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Manipulation]]'
updated_at: '2025-12-14T17:29:36.320Z'
skill_level: basic
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Account Manipulation]]'
---
# Assign-Limited-Settings-Permission-to-Staff

## Summary

This procedure sets up a low-privilege staff account in Shopify with only 'Settings' access, preparing for testing permission boundaries in webhook management.

## Description

In the Shopify admin panel, store owners can assign granular permissions to staff. This step limits access to 'Settings' to isolate the vulnerability where such users can still tamper with webhooks requiring 'Orders' permission. It simulates a real-world misconfiguration and is a prerequisite for exploitation.

## Requirements

1. Owner-level credentials for the Shopify store
2. Access to the admin panel staff management section
3. Existing staff account or ability to create one

## Defense

Defensive measures and detection strategies:

- Regularly audit staff permissions and webhook configurations
- Implement role-based access control (RBAC) with strict enforcement on all actions
- Monitor admin panel logs for unauthorized modifications to webhooks

## Objectives

1. Create a controlled low-privilege environment
2. Verify permission assignment limits access appropriately
3. Set stage for unauthorized access testing

## Instructions

### Step 1: Log In as Owner and Access Staff Management

**Context**: Gain administrative control to modify permissions.

Log in to the Shopify admin panel using owner credentials and navigate to Settings > Users and permissions > Staff.

**Expected Output**: Staff list displayed with edit options.

### Step 2: Select or Create Staff Account

**Context**: Target the account for permission adjustment.

Choose an existing staff member or add a new one, then click 'Edit permissions'.

**Expected Output**: Permission selection interface opens.

### Step 3: Assign Only 'Settings' Permission

**Context**: Restrict access to test vulnerability.

Uncheck all permissions except 'Settings', save changes, and confirm.

**Expected Output**: Updated permissions reflected, no 'Orders' access.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Account Manipulation]] Account Manipulation

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- shopify
- permissions
