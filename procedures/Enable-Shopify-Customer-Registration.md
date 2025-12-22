---
id: proc-uuid-1
tags:
  - shopify
  - setup
  - registration
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - Cloud (Shopify)
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-13T23:55:38.222Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Enable-Shopify-Customer-Registration

## Summary

This procedure configures a Shopify store to allow customer registration, exposing the vulnerable /account/register endpoint for XSS testing.

## Description

In a Shopify environment, customer registration must be enabled via the admin panel to access the form. This step is prerequisite for submitting payloads to the POST endpoint at *.myshopify.com/account/register. Without it, the form may redirect or be unavailable. The procedure assumes admin access for setup; in wild exploitation, the feature is often enabled by default on public stores.

## Requirements

1. Admin access to Shopify store dashboard
2. Valid Shopify account with store ownership
3. No additional tools needed beyond web browser

## Defense

Defensive measures and detection strategies:

- Disable unnecessary customer registration if not required
- Monitor admin panel changes for unauthorized enabling of features
- Use Shopify's security settings to restrict account creation

## Objectives

1. Expose the registration endpoint for payload submission
2. Prepare the target for XSS testing
3. Validate endpoint accessibility

## Instructions

### Step 1: Access Shopify Admin

**Context**: Log in to the store's admin interface to modify customer account settings.

Navigate to https://admin.shopify.com/store/settings/customer_accounts in your browser.

### Step 2: Enable Registration

**Context**: Select the option to allow new customer accounts.

Choose "Accounts are optional" or "Accounts are created automatically, but customers can check out as a guest" and save changes.

**Expected Output**: Confirmation message in admin panel; test by visiting /account/register.

### Step 3: Verify Endpoint

**Context**: Confirm the form is now accessible.

Load https://*.myshopify.com/account/register in a browser; it should display the registration form fields.

**Expected Output**: Form loads with email, first name, last name, and password inputs.

**Success Indicators**:
- No redirect to login or error
- POST endpoint accepts submissions

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[shopify]]
- [[registration]]
- [[setup]]
