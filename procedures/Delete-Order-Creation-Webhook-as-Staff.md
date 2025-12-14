---
id: proc-delete-shopify-webhook-staff-001
tags:
  - shopify
  - webhook
  - deletion
  - access-control
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
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:29:36.290Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Delete-Order-Creation-Webhook-as-Staff

## Summary

This procedure shows how staff with 'Settings' permission can delete critical webhooks, disabling notifications for order events and causing business disruptions.

## Description

Deletion in the Shopify admin UI lacks permission enforcement, allowing removal of webhooks for Orders, Customers, Products, etc., without 'Orders' access.

## Requirements

1. Staff with 'Settings' permission
2. Existing 'Order Creation' webhook
3. Admin panel access

## Defense

Defensive measures and detection strategies:

- Require elevated permissions for deletions
- Log and review all webhook removals
- Implement soft deletes or backups for webhooks

## Objectives

1. Remove webhook unauthorizedly
2. Interrupt order processing notifications
3. Highlight denial-of-service potential

## Instructions

### Step 1: Log In as Staff

**Context**: Use low-priv account.

Access admin with staff credentials.

**Expected Output**: Restricted dashboard.

### Step 2: Navigate to Notifications

**Context**: Locate target webhook.

Go to Settings > Notifications.

**Expected Output**: List including target webhook.

### Step 3: Perform Deletion

**Context**: Execute removal action.

Select the 'Order Creation' webhook and click delete, confirm if prompted.

**Expected Output**: Webhook removed from list.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion]] Defense Evasion

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- shopify
- deletion
