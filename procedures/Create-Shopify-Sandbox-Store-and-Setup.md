---
tags:
  - setup
  - shopify
  - sandbox
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:29:09.448Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 41abc1db-307a-485e-ac60-599fba543a53
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-Shopify-Sandbox-Store-and-Setup

## Summary

This procedure sets up a Shopify sandbox store, including admin login, product creation, and shipping configuration, to prepare a test environment for exploiting broken access control vulnerabilities in the admin panel.

## Description

In the context of testing Shopify's admin panel, this procedure involves creating a disposable sandbox store to simulate a real e-commerce environment. As an admin, you populate it with products and shipping details, which later serve as sensitive data exposed through unauthorized access. This setup is crucial for reproducing the vulnerability without affecting production stores. Expected outcomes include a fully configured store ready for staff account testing, with no risk of data leakage during setup.

## Requirements

1. Valid Shopify developer or partner account with permission to create sandbox stores.
2. Web browser with cookies enabled for session management.
3. Stable internet connection to myshopify.com.

## Defense

Defensive measures and detection strategies:

- Monitor admin account creations and logins for unusual patterns, such as rapid sandbox store setups.
- Implement rate limiting on store creation APIs to prevent abuse in testing environments.

## Objectives

1. Establish a controlled test store with admin access.
2. Add realistic data (products and shipping) to enable vulnerability impact demonstration.
3. Verify setup integrity before proceeding to exploitation.

## Instructions

### Step 1: Create and Access Sandbox Store

**Context**: Begin by creating a new sandbox store to isolate testing.

Navigate to the Shopify admin panel at https://admin.shopify.com and select the option to create a new sandbox store. Provide a store name (e.g., test-store-123) and complete the setup wizard.

> Once created, log in as the storefront admin to access the dashboard at https://<store>.myshopify.com/admin.

### Step 2: Add Products

**Context**: Populate the store with test products to include sensitive details in later previews.

From the admin dashboard, click on "Products" and then "Add product". Enter details such as title, description, price, and inventory for at least two items (e.g., "Test Widget" at $10.00).

> Save each product; confirm they appear in the products list.

### Step 3: Configure Shipping

**Context**: Set up shipping to add logistics data that can be exposed.

Go to "Settings" > "Shipping and delivery". Define shipping zones (e.g., US Domestic), rates (e.g., $5 flat rate), and handling instructions.

> Apply and save changes; test by simulating a checkout if possible.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[setup]]
- [[shopify]]
- [[sandbox]]
