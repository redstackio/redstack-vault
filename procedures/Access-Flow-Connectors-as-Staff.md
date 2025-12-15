---
id: uuid-placeholder-3
tags:
  - shopify
  - flow-connectors
  - staff-access
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - Shopify
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:30:07.360Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Access-Flow-Connectors-as-Staff

## Summary

This procedure logs in as a staff member to access the Flow app's connectors page, verifying permission-based access to third-party integration settings.

## Description

Using the staff account with 'Apps' permission, navigate to the connectors section in Flow. This step confirms the account can interact with sensitive URLs before revocation, highlighting the lack of per-session validation.

## Requirements

1. Staff credentials with 'Apps' permission.
2. Installed Flow app.
3. Shopify store URL.

## Defense

Defensive measures and detection strategies:

- Enforce session-based permission checks in apps.
- Log access to app connectors and alert on anomalous staff activity.

## Objectives

1. Gain access to connector settings.
2. Prepare for signed URL generation.
3. Test permission enforcement.

## Instructions

### Step 1: Staff Login

**Context**: Authenticate as staff.

Log in to https://[shop].myshopify.com/admin with staff credentials.

### Step 2: Navigate to Flow

**Context**: Enter the app.

Go to Apps > Flow.

### Step 3: Access Connectors

**Context**: Reach the settings page.

Click on Connectors or navigate to https://[shop].myshopify.com/admin/apps/flow/connectors.

> Expected output: Page loads with Google Sheets, Trello, Asana options.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[shopify]]
- [[staff-access]]
