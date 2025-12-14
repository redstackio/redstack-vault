---
id: proc-shopify-create-dev-store
tags:
  - shopify
  - development-store
  - setup
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:29:56.872Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-New-Shopify-Development-Store

## Summary

This procedure outlines creating a new Shopify development store via the Partner Dashboard to serve as a source for generating preview tokens, enabling subsequent authentication bypass attacks on other stores.

## Description

In the context of exploiting Shopify's unscoped preview tokens post-August 17, 2020, this initial setup step creates a fresh development store with automatic password protection. The store acts as a token generator without needing custom configurations. Prerequisites include a valid Shopify Partner account. Expected outcome is a new store ready for theme preview access.

## Requirements

1. Active Shopify Partner account with permissions to create stores
2. Web browser access to partners.shopify.com
3. Compliance with Shopify's development store policies (e.g., no production use)

## Defense

Defensive measures and detection strategies:

- Monitor Partner Dashboard for unusual store creation patterns
- Implement rate limiting on development store provisioning
- Audit logs for token generation tied to specific stores

## Objectives

1. Establish a controlled source store for token extraction
2. Ensure the store meets post-2020 password standards
3. Prepare for preview URL generation without errors

## Instructions

### Step 1: Log In to Partner Dashboard

**Context**: Access the Shopify Partner interface to initiate store creation.

Navigate to https://partners.shopify.com and log in with partner credentials.

> Expected output: Dashboard loaded with store management options.

### Step 2: Create Development Store

**Context**: Provision a new store designated for development.

Click 'Stores' > 'Create store' and select 'Development store'. Provide a name and ensure it enables password protection by default.

> Expected output: Confirmation email and admin URL for the new store.

### Step 3: Verify Store Access

**Context**: Confirm the store is active and protected.

Log in to the new store's admin at <store-name>.myshopify.com/admin and check settings for password protection.

> Expected output: Admin dashboard accessible; storefront prompts for password when visited.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[shopify]]
- [[development-store]]
- [[setup]]
