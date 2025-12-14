---
id: proc-login-verify-restrict-001
name: Login-and-Verify-Restricted-Access
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:59.742Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Valid Accounts]]'
tags:
  - shopify
  - login
  - restricted-access
platforms:
  - Web
tools: []
commands: []
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

# Login-and-Verify-Restricted-Access

## Summary

This procedure authenticates a zero-permission staff account to the Shopify admin UI and visually confirms restricted access, ensuring the account cannot interact with sensitive UI elements before proceeding to API exploitation.

## Description

After creating a no-permission staff account, logging in demonstrates that Shopify's frontend enforces access controls by hiding menus and content. This step validates the low-privilege state and sets up for intercepting API calls, where backend authorization may be weaker.

## Requirements

1. Staff account credentials (email/password from invitation)
2. Target store admin URL (e.g., https://store.myshopify.com/admin)
3. Web browser for login

## Defense

Defensive measures and detection strategies:

- Log all login attempts and correlate with permission levels
- Use session monitoring to detect anomalous access patterns from low-privilege accounts
- Implement UI-level access gates that redirect unauthorized users

## Objectives

1. Authenticate the staff account
2. Confirm UI restrictions (no menus, empty home)
3. Prepare browser session for proxy interception

## Instructions

### Step 1: Initiate Login

**Context**: Access the admin login page.

Navigate to https://store.myshopify.com/admin/login and enter staff email/password.

### Step 2: Observe Post-Login UI

**Context**: Verify restrictions after authentication.

Upon login, check for absence of navigation menus, home dashboard content, or any actionable sections.

**Expected Output**: Successful login with a blank or minimal interface indicating restricted access.

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
- [[login]]
- [[restricted-access]]
