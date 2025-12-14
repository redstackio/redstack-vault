---
id: proc-uuid-1
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
  - Shopify
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:29:57.150Z'
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
# Access-Shopify-Admin-Menu-Creation

## Summary

This procedure outlines logging into the Shopify Admin and navigating to the menu creation or editing section, setting the stage for injecting payloads into vulnerable title fields.

## Description

In the context of exploiting stored XSS in Shopify's admin interface, this initial step requires authenticated access to reach the navigation menu management area. The target environment is the Shopify web platform, where menu titles are user-input fields. Prerequisites include valid admin credentials. Expected outcomes include access to input fields that lack proper escaping, enabling subsequent payload injection.

## Requirements

1. Valid Shopify Admin account credentials
2. Web browser (e.g., Chrome, Firefox) with session persistence
3. Direct network access to the Shopify instance

## Defense

Defensive measures and detection strategies:

- Implement multi-factor authentication (MFA) for admin logins
- Monitor admin login attempts and session anomalies via Shopify's audit logs

## Objectives

1. Establish authenticated session in Shopify Admin
2. Reach menu management interface
3. Prepare for payload injection without triggering alerts

## Instructions

### Step 1: Log In to Shopify Admin

**Context**: Authenticate to gain access to the admin dashboard, ensuring a persistent session.

Navigate to the Shopify Admin login page and enter credentials.

> Upon successful login, the dashboard loads, confirming access.

### Step 2: Navigate to Menu Section

**Context**: Locate the navigation or menu editing tools to access vulnerable fields.

From the dashboard, go to 'Online Store' > 'Navigation' or search for 'Menus' to open the creation/editing interface.

> The page displays 'Add menu' and 'Menu Item' options with title input fields.

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
