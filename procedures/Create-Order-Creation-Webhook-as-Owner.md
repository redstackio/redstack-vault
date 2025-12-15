---
id: proc-create-shopify-webhook-001
tags:
  - shopify
  - webhook
  - setup
type: procedure
tools: []
tactics:
  - '[[Persistence]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Manipulation]]'
updated_at: '2025-12-14T17:29:36.318Z'
skill_level: basic
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Account Manipulation]]'
---
# Create-Order-Creation-Webhook-as-Owner

## Summary

This procedure establishes a test 'Order Creation' webhook in Shopify's Notifications settings, which is intended to trigger on order events but can later be tampered with by low-privilege users.

## Description

Shopify webhooks notify external services of events like order creation. Owners can create these via the admin UI under Settings > Notifications. This step confirms creation works with proper permissions, contrasting with the lack of checks on edits/deletes.

## Requirements

1. Owner credentials with full permissions
2. Valid webhook endpoint URL (e.g., a test server)
3. Access to Settings > Notifications

## Defense

Defensive measures and detection strategies:

- Limit webhook creation to high-privilege roles only
- Log all webhook creations and monitor for anomalies
- Use webhook verification signatures to prevent tampering

## Objectives

1. Set up a critical notification endpoint
2. Verify webhook functionality for orders/create event
3. Prepare for permission bypass testing

## Instructions

### Step 1: Log In as Owner

**Context**: Ensure elevated access for creation.

Access the Shopify admin dashboard with owner account.

**Expected Output**: Dashboard loads successfully.

### Step 2: Navigate to Notifications

**Context**: Locate webhook management.

Go to Settings > Notifications in the left sidebar.

**Expected Output**: Webhooks section visible.

### Step 3: Create Webhook

**Context**: Configure for order creation events.

Click 'Create webhook', select 'Order Creation', enter URL, and save.

**Expected Output**: Webhook added to list with active status.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]] Persistence

### Techniques

- [[Account Manipulation]] Account Manipulation

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- shopify
- webhook
