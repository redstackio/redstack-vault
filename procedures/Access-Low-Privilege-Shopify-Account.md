---
id: proc-shopify-low-priv-access-001
tags:
  - authorization-bypass
  - shopify
  - account-access
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
updated_at: '2025-12-14T17:28:44.990Z'
skill_level: basic
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Access-Low-Privilege-Shopify-Account

## Summary

This procedure establishes a session with a Shopify store using an account configured with 'No Access' permissions, setting the stage for exploiting authorization bypass vulnerabilities in the admin API.

## Description

In the context of Shopify's admin panel, accounts can be assigned minimal permissions like 'No Access' to specific stores. This procedure involves logging in with such an account to obtain a valid session cookie, which can then be used to interact with the GraphQL API. The target environment is a Shopify store (e.g., h1teststore2.myshopify.com), and the outcome is a authenticated session without elevated privileges, enabling subsequent unauthorized data access due to flawed permission checks.

## Requirements

1. Valid Shopify credentials for a 'No Access' account on the target store
2. Web browser or HTTP client for login
3. Network access to the Shopify admin login page

## Defense

Defensive measures and detection strategies:

- Enforce strict permission checks on all API endpoints
- Monitor login events for unusual account usage
- Implement rate limiting on admin API requests from low-privilege sessions

## Objectives

1. Obtain a valid session cookie for low-privilege API access
2. Verify 'No Access' status to confirm minimal privileges
3. Prepare for GraphQL queries without triggering alerts

## Instructions

### Step 1: Log In to Shopify Admin

**Context**: Authenticate using the low-privilege account to generate a session.

No specific command; use a web browser to navigate to https://[store].myshopify.com/admin/login and enter credentials for the 'No Access' account (e.g., attacker1).

> Upon success, inspect the browser's developer tools (Network tab) to extract the session cookie from the login response or subsequent requests.

### Step 2: Verify Permissions

**Context**: Confirm the account has 'No Access' to ensure the bypass scenario applies.

Navigate to the store settings in the admin panel and check user permissions.

> Expected: Permissions show 'No Access' for the target store, with no ability to view or edit data via UI.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- authorization-bypass
- shopify
- account-access
