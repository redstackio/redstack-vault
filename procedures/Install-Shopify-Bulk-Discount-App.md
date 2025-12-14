---
id: procedure-install-bulk-discount-app
tags:
  - shopify
  - app-installation
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
techniques: []
updated_at: '2025-12-14T03:15:35.245Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
---
# Install-Shopify-Bulk-Discount-App

## Summary

This procedure installs the vulnerable Bulk Discount App on a Shopify store, enabling the reflection of unsanitized data from products or collections.

## Description

The Bulk Discount App integrates with Shopify stores to manage discounts but fails to sanitize reflected inputs. Installation requires a paid plan and grants the app access to store data. This step is prerequisite for accessing the vulnerable interface at bulkdiscounts.shopifyapps.com.

## Requirements

1. Shopify store on a paid basic plan or higher.
2. Admin access to the store.
3. Web browser for app store navigation.

## Defense

Defensive measures and detection strategies:

- Review app permissions before installation and limit to necessary scopes.
- Audit installed apps regularly for known vulnerabilities via Shopify's app review process.
- Use enterprise plans with enhanced app vetting.

## Objectives

1. Deploy the app to access its interface.
2. Ensure integration with store data for payload reflection.
3. Confirm app functionality without errors.

## Instructions

### Step 1: Navigate to Apps Section

**Context**: Locate the app in the Shopify ecosystem.

In the Shopify admin dashboard, click "Apps" in the sidebar, then search for "Bulk Discount" or browse the app store.

> This displays available apps with installation options.

### Step 2: Install and Onboard

**Context**: Authorize and complete setup.

Select the Bulk Discount App, review permissions, and click "Install app". Follow any setup wizards to activate.

> Installation redirects to bulkdiscounts.shopifyapps.com for authentication.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques


### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[shopify]]
- [[app-installation]]
