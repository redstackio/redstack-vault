---
id: proc-edit-shopify-webhook-staff-001
tags:
  - shopify
  - webhook
  - tampering
  - access-control
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
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:29:36.300Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Edit-Order-Creation-Webhook-as-Staff

## Summary

This procedure exploits the lack of permission checks to allow low-privilege staff to modify the URL of an 'Order Creation' webhook, potentially redirecting notifications to malicious endpoints.

## Description

In Shopify's UI, clicking a webhook opens an edit modal where URL changes can be saved without verifying 'Orders' permission. This affects not just orders but potentially other types like Customer or Products.

## Requirements

1. Staff with 'Settings' permission
2. Visible 'Order Creation' webhook
3. Test URL for modification

## Defense

Defensive measures and detection strategies:

- Add server-side permission validation for all webhook actions
- Alert on webhook URL changes from low-priv accounts
- Use immutable webhooks or approval workflows

## Objectives

1. Alter webhook configuration unauthorizedly
2. Disrupt legitimate notifications
3. Demonstrate tampering impact

## Instructions

### Step 1: Log In as Staff and Navigate to Notifications

**Context**: Access the vulnerable interface.

Use staff credentials and go to Settings > Notifications.

**Expected Output**: Webhook list loads.

### Step 2: Select Webhook for Edit

**Context**: Open modification interface.

Click on the 'Order Creation' webhook.

**Expected Output**: Edit modal opens with current details.

### Step 3: Modify and Save

**Context**: Perform unauthorized change.

Update the URL field (e.g., to a test endpoint) and click 'Save Webhook'.

**Expected Output**: Success message; changes persisted.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- shopify
- tampering
