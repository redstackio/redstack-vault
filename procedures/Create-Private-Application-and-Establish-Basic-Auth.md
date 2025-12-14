---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567892
tags:
  - shopify
  - api
  - basic-auth
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
  - '[[Domain Accounts]]'
updated_at: '2025-12-14T17:32:20.596Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Domain Accounts]]'
---
# Create-Private-Application-and-Establish-Basic-Auth

## Summary

This procedure creates a private app in Shopify to generate API credentials and stores HTTP Basic Auth in the browser, enabling automatic authentication for CSRF exploitation.

## Description

Private apps in Shopify allow custom API access. By creating one and accessing an example auth URL, the browser prompts for and stores the API key/password as Basic Auth credentials. This exploits the lack of CSRF tokens in API endpoints, as the browser includes the Authorization header in subsequent requests without user interaction. Prerequisites include an active admin session.

## Requirements

1. Active Shopify admin session from prior login
2. Permissions to create apps (store owner or collaborator role)
3. Web browser supporting Basic Auth storage (e.g., Chrome)

## Defense

Defensive measures and detection strategies:

- Disable or restrict private app creation in store settings
- Use API tokens with limited scopes instead of Basic Auth
- Clear browser credentials regularly and monitor for unauthorized API key generation

## Objectives

1. Generate API key and password for the private app
2. Store Basic Auth credentials in browser for auto-inclusion
3. Set up for CSRF form submission

## Instructions

### Step 1: Create Private App

**Context**: Navigate to app development and generate credentials.

In the admin dashboard, go to Apps > Develop apps for your store > Create an app. Name it (e.g., "Test App"), configure API scopes (e.g., read/write products), and reveal the API key and password.

> Note the credentials; they will be used in the next step. The app is now listed under developed apps.

### Step 2: Establish Basic Auth in Browser

**Context**: Use the example URL to prompt and store credentials.

Copy the example auth URL provided (e.g., https://[shop].myshopify.com/admin/api/2023-10/products.json) and open it in a new browser tab. When prompted, enter the API key as username and password as password. Accept to store.

> Success: The JSON response loads without further prompts; check Network tab in dev tools for Authorization: Basic [base64] header.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Domain Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[shopify]]
- [[api]]
- [[basic-auth]]
