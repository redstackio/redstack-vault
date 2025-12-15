---
tags:
  - shopify
  - admin-access
type: procedure
tools:
  - '[[tools/Browser-Developer-Tools]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:28:44.294Z'
skill_level: intermediate
impact_level: low
sub_techniques: []
id: 7cc80517-eefa-4790-bc06-169b7fe6d57c
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Access-Shopify-Tax-Settings

## Summary

This procedure navigates to the Shopify admin panel's taxes settings page, providing the entry point for exploiting the tax override authorization bypass.

## Description

In the context of Shopify's web-based admin interface, authenticated users can access settings pages to configure taxes. This step assumes valid admin credentials and targets the URL https://SHOP.myshopify.com/admin/settings/taxes/, where SHOP is the shop subdomain. No special tools are required beyond a standard browser, but it sets up the environment for subsequent manipulation. Expected outcome is loading the page without restrictions, enabling further steps in the bypass chain.

## Requirements

1. Valid Shopify admin credentials for any shop
2. Web browser with internet access
3. HTTPS connectivity to myshopify.com

## Defense

Defensive measures and detection strategies:

- Implement role-based access controls (RBAC) to restrict settings page access
- Monitor admin panel logins for unusual patterns or IP anomalies

## Objectives

1. Gain access to the tax configuration interface
2. Prepare for tax override manipulation
3. Verify authenticated session validity

## Instructions

### Step 1: Log In to Admin Panel

**Context**: Authenticate to the Shopify admin to establish a session.

Enter credentials at the login page and proceed to the dashboard.

### Step 2: Navigate to Taxes Settings

**Context**: Directly access the taxes page to avoid menu navigation errors.

Open the URL https://SHOP.myshopify.com/admin/settings/taxes/ in the browser, replacing SHOP with the target shop subdomain.

> This loads the taxes settings interface, displaying current tax zones and overrides.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Browser-Developer-Tools]]

## Tags

- shopify
- admin-access
