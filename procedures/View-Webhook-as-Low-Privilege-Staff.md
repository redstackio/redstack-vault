---
id: proc-view-shopify-webhook-staff-001
tags:
  - shopify
  - webhook
  - access-control
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:29:36.305Z'
skill_level: basic
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# View-Webhook-as-Low-Privilege-Staff

## Summary

This procedure tests if staff with 'Settings' permission can view webhooks created by owners, revealing insufficient visibility controls in Shopify's admin panel.

## Description

Despite lacking 'Orders' permission, staff can access the Notifications page and see all webhooks, including those for order events. This is the first indicator of improper access control.

## Requirements

1. Staff credentials with 'Settings' only
2. Pre-existing webhook from owner
3. Admin panel access

## Defense

Defensive measures and detection strategies:

- Enforce permission-based filtering on UI views
- Audit access logs for low-priv users viewing high-priv resources
- Implement least-privilege principles strictly

## Objectives

1. Confirm unauthorized visibility
2. Identify scope of accessible webhooks
3. Validate setup for further tampering

## Instructions

### Step 1: Log In as Staff

**Context**: Use limited account to test access.

Enter staff credentials in Shopify admin login.

**Expected Output**: Dashboard loads with restricted menu.

### Step 2: Navigate to Settings > Notifications

**Context**: Attempt to access webhook list.

Click Settings > Notifications in the sidebar.

**Expected Output**: Page loads without errors.

### Step 3: View Webhook List

**Context**: Check for owner-created items.

Scan the webhooks table for 'Order Creation' entry.

**Expected Output**: Webhook visible in list.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- shopify
- access-control
