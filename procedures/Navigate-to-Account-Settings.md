---
tags:
  - navigation
  - shopify
  - admin-settings
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
updated_at: '2025-12-14T17:25:29.822Z'
skill_level: basic
impact_level: low
detection_risk: low
sub_techniques: []
id: 0fb26202-24d4-4662-bc86-9a33612a9a66
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Navigate-to-Account-Settings

## Summary

This procedure guides the attacker to the Shopify admin account settings page, where session management options are available for exploitation.

## Description

After authentication, the attacker must reach the specific admin page that triggers the vulnerable session expiration endpoint. This involves standard UI navigation within the authenticated session, positioning the attacker to interact with the IDOR-prone feature.

## Requirements

1. Active Shopify admin session
2. Web browser with the session cookies intact
3. Knowledge of the account settings URL structure (/admin/settings/account)

## Defense

Defensive measures and detection strategies:

- Rate-limit navigation to sensitive admin pages
- Log all accesses to account settings endpoints
- Implement role-based access control (RBAC) to restrict settings access

## Objectives

1. Load the account settings interface
2. Expose session expiration functionality
3. Set up for request interception

## Instructions

### Step 1: From Dashboard, Select Settings

**Context**: Use the admin menu to access account-related configurations.

No command; click 'Settings' in the left sidebar, then 'Account' under the General section.

> Expected output: Page loads at /admin/settings/account with form elements for account details.

### Step 2: Confirm Page Load

**Context**: Verify the presence of session management options.

Inspect the page for 'Expire all sessions' or similar buttons.

> Success shows interactive elements for session control.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[navigation]]
- [[shopify]]
- [[admin-settings]]
