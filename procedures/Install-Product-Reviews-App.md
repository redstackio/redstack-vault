---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
tags:
  - shopify
  - app-install
type: procedure
tools:
  - '[[tools/Browser-Developer-Tools]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-13T23:52:25.315Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Install-Product-Reviews-App

## Summary

This procedure installs the Shopify 'Product Reviews' app on a target store, enabling the vulnerable review submission feature for subsequent exploitation.

## Description

In the context of exploiting self-XSS in Shopify, installing the app is the initial setup step. It requires access to the Shopify admin and adds the review functionality to the storefront. This exposes the email input field vulnerable to bypass and injection. Expected outcome is the app integration without errors, allowing access to product pages with review forms.

## Requirements

1. Valid Shopify merchant account with admin access
2. Internet connection to access the Shopify App Store
3. Browser for navigation (e.g., Chrome)

## Defense

Defensive measures and detection strategies:

- Monitor app installations in Shopify admin logs for unauthorized additions
- Use app review policies to vet third-party apps before installation

## Objectives

1. Enable Product Reviews feature on the store
2. Prepare storefront for review form access
3. Set up environment for XSS testing

## Instructions

### Step 1: Access Shopify Admin

**Context**: Log in to the merchant dashboard to reach the apps section.

Navigate to your Shopify admin panel at admin.shopify.com and sign in with merchant credentials.

### Step 2: Install the App

**Context**: Search and add the Product Reviews app to enable reviews.

In the Apps section, click 'Visit Shopify App Store', search for 'Product Reviews', select the official app, and click 'Add app'. Follow prompts to install and configure basic settings like enabling reviews on products.

> Upon success, the app will confirm installation, and review widgets will appear on product pages.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Browser-Developer-Tools]]

## Tags

- shopify
- app-install
