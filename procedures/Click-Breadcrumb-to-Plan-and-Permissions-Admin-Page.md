---
tags:
  - privilege-escalation
  - shopify
  - full-admin
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
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:29:10.030Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 0e060e97-69b7-44d7-ae67-8490d0f2ec13
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---
# Click Breadcrumb to Plan and Permissions Admin Page

## Summary

This final procedure clicks the 'Plan and Permissions' breadcrumb on the loaded admin page, navigating to the core account settings at /admin/settings/account, completing the escalation to owner-level access.

## Description

The breadcrumb navigation in the admin interface allows unrestricted movement once the initial page is loaded via the exploit link. This grants access to sensitive features like staff addition, permission updates, and store ownership transfer (password-protected).

## Requirements

1. Plan & Permissions staff page loaded
2. Breadcrumb navigation visible at top
3. Persistent session from POS origin

## Defense

Defensive measures and detection strategies:

- Check session origin on breadcrumb clicks
- Require re-authentication for account settings
- Monitor access to /admin/settings/account

## Objectives

1. Reach full admin account settings
2. Enable owner actions like ownership transfer
3. Confirm complete privilege escalation

## Instructions

### Step 1: Locate Breadcrumb

**Context**: Identify navigation path.

At the top of the Plan & Permissions page, find the 'Plan and Permissions' breadcrumb link.

> Breadcrumb shows hierarchy including the link.

### Step 2: Navigate to Account Settings

**Context**: Complete the chain.

Click the 'Plan and Permissions' link to go to https://shop.myshopify.com/admin/settings/account.

> Full account settings load with owner privileges.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[privilege-escalation]]
- [[shopify]]
- [[full-admin]]
