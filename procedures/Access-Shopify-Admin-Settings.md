---
tags:
  - shopify
  - admin-access
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Valid Accounts]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: e056ed7a-805f-414d-9ffb-cceb5c0a0acb
created_at: '2025-12-14T17:30:18.198Z'
updated_at: '2025-12-14T17:30:18.198Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Access-Shopify-Admin-Settings

## Summary

This procedure outlines how to log in and navigate to the Shopify admin settings page to access the store address configuration, serving as the entry point for injecting payloads in subsequent steps.

## Description

In a Shopify environment, admin access is required to modify store settings. This step involves using valid credentials to reach the general settings where the vulnerable address field is located. It assumes the attacker has obtained admin privileges, either legitimately or via prior compromise. The procedure targets https://*.myshopify.com/admin/settings/general and sets up for stored XSS exploitation.

## Requirements

1. Valid Shopify admin credentials for the target store.
2. Web browser with internet access.
3. No additional tools needed.

## Defense

Defensive measures and detection strategies:

- Implement multi-factor authentication (MFA) for admin logins.
- Monitor admin login attempts from unusual IPs.

## Objectives

1. Gain access to the admin dashboard.
2. Navigate to store settings.
3. Prepare for payload injection.

## Instructions

### Step 1: Log In to Admin Dashboard

**Context**: Use credentials to authenticate and access the admin interface.

**Command** (Manual Browser Action):

Open https://*.myshopify.com/admin and enter username/password.

> Successful login redirects to the dashboard. Expected output: Admin homepage loads.

### Step 2: Navigate to General Settings

**Context**: Access the specific page for store address configuration.

**Command** (Manual Browser Action):

Click Settings > General or directly visit https://*.myshopify.com/admin/settings/general.

> Expected output: Page loads with store details form, including address fields.

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
