---
tags:
  - woocommerce
  - wordpress
  - role-assignment
  - privilege-escalation
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
updated_at: '2025-12-14T17:29:44.831Z'
sub_techniques: []
id: ace0f80f-648d-4202-b0c8-22c553097777
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Account Manipulation]]'
---
# Assign-Editor-Role-to-Low-Privilege-User

## Summary

This procedure exploits WooCommerce's insufficient blacklist in the map_meta_cap filter to assign an Editor role to an arbitrary low-privilege user, enabling further escalation via capabilities like unfiltered_html.

## Description

WooCommerce's wc_modify_map_meta_cap function restricts Shop Managers from editing or promoting Admins but permits other roles like Editor. By editing a user (e.g., customer) and selecting Editor, the change persists due to the lack of a whitelist. This targets the WordPress user meta table, altering capabilities without code execution. Prerequisites: Active Shop Manager session and existence of a target user.

## Requirements

1. Active Shop Manager admin session
2. Target low-privilege user account (e.g., Subscriber or Customer)
3. Access to WordPress Users admin panel

## Defense

Defensive measures and detection strategies:

- Implement role whitelisting in custom plugins to restrict Shop Manager actions
- Audit user role changes via WordPress hooks (e.g., user_register, set_user_role)
- Use capability checks beyond blacklists, such as promote_users meta cap

## Objectives

1. Elevate user role to Editor
2. Bypass WooCommerce-specific restrictions
3. Enable dangerous capabilities for the target user

## Instructions

### Step 1: Access User List

**Context**: Locate the target user for role modification.

In the admin dashboard, go to Users > All Users and select a low-privilege user to edit.

> This opens the user edit form with current role displayed.

### Step 2: Modify Role

**Context**: Assign the Editor role, exploiting the blacklist gap.

In the 'Role' dropdown, select 'Editor' and click 'Update User'.

> The update succeeds as Editor is not blacklisted, changing the user's wp_capabilities meta.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Account Manipulation]] Account Manipulation

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- woocommerce
- wordpress
- role-assignment
