---
id: proc-access-shopify-settings
tags:
  - shopify
  - admin-access
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-13T23:52:43.984Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Access-Shopify-Admin-Settings

## Summary

This procedure outlines navigating to the Shopify admin settings general page to access editable store address fields, requiring only basic Settings permissions.

## Description

In a Shopify environment, the admin panel allows users with limited permissions to modify store details. This step targets the General settings to reach the vulnerable address field. It assumes valid credentials and focuses on legitimate navigation to avoid detection.

## Requirements

1. Valid Shopify account with Settings permissions
2. Web browser with internet access
3. No additional tools needed

## Defense

Defensive measures and detection strategies:

- Implement role-based access controls to limit settings modifications
- Monitor admin panel access logs for unusual navigation patterns

## Objectives

1. Reach the store address configuration page
2. Verify editable fields are accessible
3. Prepare for payload injection without triggering alerts

## Instructions

### Step 1: Log In to Shopify Admin

**Context**: Authenticate to gain access to the admin interface.

Log in using provided credentials at https://*.myshopify.com/admin.

> Expected: Dashboard loads successfully.

### Step 2: Navigate to General Settings

**Context**: Direct access to the page containing the vulnerable field.

Append `/settings/general` to the admin URL or click Settings > General.

> Expected: Page displays store information fields, including address inputs.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[shopify]]
- [[admin-access]]
