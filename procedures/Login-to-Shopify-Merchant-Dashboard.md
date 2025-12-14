---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567891
tags:
  - shopify
  - login
  - auth
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
updated_at: '2025-12-14T17:32:20.602Z'
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
# Login-to-Shopify-Merchant-Dashboard

## Summary

This procedure authenticates a user to the Shopify merchant dashboard, establishing a session necessary for subsequent API setup in a CSRF attack scenario.

## Description

Logging into the Shopify admin dashboard is the initial step to access app development features. In the context of exploiting CSRF via Basic Auth, this sets up the environment where the victim has an active session, making it easier to store API credentials in the browser. The procedure targets web-based admin interfaces and assumes valid merchant credentials.

## Requirements

1. Valid Shopify merchant account credentials (email and password)
2. Web browser with no existing session cookies for the target shop
3. Internet access to https://[shop].myshopify.com/admin

## Defense

Defensive measures and detection strategies:

- Enable multi-factor authentication (MFA) on Shopify accounts to prevent unauthorized logins
- Monitor login attempts from unusual IP addresses via Shopify's audit logs
- Use browser extensions to block or warn on suspicious login pages

## Objectives

1. Establish authenticated session in the admin dashboard
2. Prepare for private app creation
3. Ensure browser state is ready for credential storage

## Instructions

### Step 1: Navigate and Authenticate

**Context**: Access the admin login page and submit credentials to initiate the session.

Open a web browser and navigate to https://[shop].myshopify.com/admin. Enter the merchant email and password in the login form, then submit.

> Upon success, the dashboard loads with navigation to products, orders, and apps sections. If MFA is enabled, complete the additional verification.

### Step 2: Verify Session

**Context**: Confirm the login by accessing a protected resource.

After login, navigate to any admin section like Products. The page should load without re-prompting for credentials.

> Expected: Full access to admin features; session cookie set in browser storage.

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
- [[login]]
- [[auth]]
