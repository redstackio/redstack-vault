---
tags:
  - shopify
  - authentication
  - staff-login
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
updated_at: '2025-12-14T17:29:29.006Z'
sub_techniques: []
id: 188f5201-447b-4b29-ba9a-ae4bbd944d7e
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Authenticate as Staff with Settings Permission

## Summary

This procedure authenticates a user to the Shopify admin panel using a staff account limited to 'Settings' permission, establishing a session for testing low-privilege API access in vulnerability assessments.

## Description

In the context of Shopify security testing, low-privilege staff accounts are used to identify authorization flaws. This step involves standard web authentication to the admin panel, ensuring the session token is available for GraphQL API calls. The target environment is the Shopify admin interface, and success is confirmed by restricted access to features like orders.

## Requirements

1. Valid staff credentials with only 'Settings' permission assigned in Shopify admin
2. Web browser or HTTP client capable of handling session cookies
3. Access to the Shopify store's admin URL (e.g., https://yoursubdomain.myshopify.com/admin)

## Defense

Defensive measures and detection strategies:

- Implement role-based access control (RBAC) audits to ensure permissions align with API scopes
- Monitor login events for anomalous staff authentications from unusual IPs
- Use multi-factor authentication (MFA) for all staff accounts

## Objectives

1. Establish a valid session with minimal permissions
2. Verify permission restrictions before API testing
3. Prepare for unauthorized action attempts

## Instructions

### Step 1: Access Admin Login

**Context**: Navigate to the Shopify admin login page to begin authentication.

No specific command; use a web browser to visit https://yoursubdomain.myshopify.com/admin/login and enter staff credentials.

> Upon successful login, the dashboard should load with limited navigation options, confirming 'Settings' only access.

### Step 2: Extract Session Token

**Context**: Obtain the session token for API requests from browser developer tools or cookies.

Inspect network requests or cookies for 'X-Shopify-Access-Token' or equivalent session identifier.

> Expected output: A valid token string for use in subsequent API calls.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- shopify
- authentication
- staff-login
