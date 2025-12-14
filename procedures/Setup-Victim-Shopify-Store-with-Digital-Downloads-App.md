---
id: proc-setup-victim-store
tags:
  - shopify
  - setup
  - app-installation
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
  - Shopify
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:29:44.435Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Setup Victim Shopify Store with Digital Downloads App

## Summary

This procedure sets up a Shopify test store, creates sample products, installs the Digital Downloads app, and configures a product with an attachment. It simulates a vulnerable environment where app and product details can be disclosed via IDOR.

## Description

In the context of testing Shopify's access controls, this procedure establishes the victim store as the target. Using a primary account, create a store, add products like 'Tt' and 'PP', install the app from the Shopify App Store, and attach an image or file to 'Tt' via the app dashboard. This makes the product visible in the app interface, exposing its ID and title for later disclosure testing. Prerequisites include a valid Shopify developer or trial account. Expected outcomes: App integrated, product attachment confirmed, endpoint URL obtainable.

## Requirements

1. Valid Shopify account with permissions to create stores and install apps
2. Access to Shopify App Store
3. Web browser for admin navigation

## Defense

Defensive measures and detection strategies:

- Implement strict permission checks on app endpoints to validate store ownership
- Monitor unusual cross-store access patterns in app logs
- Use Shopify's staff permission granular controls to limit dashboard visibility

## Objectives

1. Prepare a store with the Digital Downloads app installed and partially configured
2. Create traceable products to test disclosure
3. Establish baseline for unauthorized access simulation

## Instructions

### Step 1: Create Test Store

**Context**: Log in and set up the victim store to serve as the disclosure target.

Navigate to Shopify admin, create a new store named test.myshopify.com using manual UI steps.

> No command; use browser to complete account creation and store setup.

### Step 2: Add Products

**Context**: Introduce products that will be targeted for attachment and disclosure.

In the admin panel, go to Products > Add product, create 'Tt' and 'PP' via /admin/products or UI.

> Manual UI entry; note product IDs post-creation.

### Step 3: Install and Configure App

**Context**: Integrate the vulnerable app and attach content to a product.

Search for 'Digital Downloads' in the App Store, install it, then in the app dashboard, add 'Tt' and upload an image attachment.

> App installation via one-click from store; configuration through app-specific UI.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[shopify]]
- [[app-installation]]
