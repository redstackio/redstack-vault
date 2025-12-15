---
tags:
  - privilege-escalation
  - shopify
  - admin-bridge
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
updated_at: '2025-12-14T17:29:10.033Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 9d1b4eb0-f6b7-4160-8df8-cbbfbcf8c17e
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---
# Click Manage Shopify Admin Access from Roles Page

## Summary

This procedure scrolls to the bottom of the staff details in the roles page and clicks the 'Manage Shopify admin access' link, loading the full admin Plan & Permissions page.

## Description

This critical step exploits the unsecured link that bridges POS UI to the core Shopify admin without validating the originating session's permissions, assuming owner login context persists.

## Requirements

1. Staff details open in roles context
2. 'Manage Shopify admin access' link visible after scroll
3. No intervening permission gates

## Defense

Defensive measures and detection strategies:

- Remove or secure cross-app navigation links
- Validate user role on every page load
- Alert on transitions from POS to admin

## Objectives

1. Trigger load of admin staff page
2. Bypass POS permission boundaries
3. Gain access to Plan & Permissions

## Instructions

### Step 1: Scroll to Link

**Context**: Expose the hidden navigation.

In the staff details panel, scroll down to the bottom.

> Link 'Manage Shopify admin access' becomes visible.

### Step 2: Activate Link

**Context**: Initiate admin context shift.

Click the link to open the staff page from Plan and Permissions.

> Page loads as full admin interface.

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
- [[admin-bridge]]
