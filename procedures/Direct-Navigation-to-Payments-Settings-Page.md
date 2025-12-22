---
id: d4e5f6g7-h8i9-0123-defg-456789012345
tags:
  - ui-bypass
  - broken-access-control
  - shopify
  - settings-page
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T12:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:28:51.826Z'
skill_level: basic
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Direct-Navigation-to-Payments-Settings-Page

## Summary

This procedure bypasses Shopify's UI permission restrictions by directly navigating to the payments settings page, allowing viewing of payment gateways with a non-privileged admin session.

## Description

The `/admin/settings/payments` page in Shopify's admin UI does not re-enforce permission checks on direct access, relying solely on menu visibility for restriction. This enables unprivileged admins to load and view sensitive financial details, including gateway lists and partial credentials, in a rendered HTML format.

## Requirements

1. Active admin session without 'Settings' permission
2. Web browser with the session active
3. Target store's admin URL base

## Defense

Defensive measures and detection strategies:

- Implement client-side and server-side permission validation on all admin pages
- Log direct URL accesses to restricted paths and alert on anomalies
- Use JavaScript to redirect unauthorized users on page load

## Objectives

1. Load restricted UI page without menu access
2. View payment configurations visually
3. Confirm disclosure of sensitive data elements

## Instructions

### Step 1: Ensure Active Session

**Context**: Verify the limited-privilege session is still valid from prior login.

**Command** (Browser Check):

Navigate to `/admin` and confirm dashboard loads with restricted menu.

> Expected output: Dashboard visible, no Settings option in sidebar.

### Step 2: Direct URL Access

**Context**: Manually enter the restricted page URL to bypass UI navigation.

**Command** (Browser Navigation):

In the address bar, enter `https://shop.myshopify.com/admin/settings/payments` and press Enter.

> Expected output: Page loads showing payment gateways table with details like provider names and credential inputs (partial).

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- ui-bypass
- broken-access-control
- shopify
- settings-page
