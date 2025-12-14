---
id: proc-configure-shopify-email
tags:
  - shopify
  - app-setup
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
updated_at: '2025-12-13T23:52:49.963Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Configure-Shopify-Email-App

## Summary

This procedure sets up the Shopify Email app on a target store, providing access to the vulnerable template branding features for subsequent XSS injection.

## Description

In the context of exploiting stored XSS in Shopify, configuring the Email app is the initial step to enable access to the store name field. This involves installing the app from the Shopify App Store and navigating to its settings. The procedure assumes admin access to the store and targets web-based Shopify environments. Expected outcomes include readiness for payload injection without triggering alerts.

## Requirements

1. Valid Shopify admin credentials for the target store
2. Internet access to the Shopify App Store
3. Web browser for navigation

## Defense

Defensive measures and detection strategies:

- Monitor app installations in Shopify admin logs for unauthorized access
- Implement role-based access controls to limit app configuration to trusted users

## Objectives

1. Install and activate the Shopify Email app
2. Gain access to template branding page
3. Prepare environment for XSS exploitation

## Instructions

### Step 1: Install the App

**Context**: Locate and install the Shopify Email app to integrate it with the store.

No command required; use the UI:

- Log in to Shopify admin at your-store.myshopify.com/admin
- Navigate to Apps > Shopify App Store
- Search for "Shopify Email" and click Install

> Successful installation redirects to the app dashboard.

### Step 2: Access Template Branding

**Context**: Enter the app settings to reach the vulnerable configuration area.

No command required; use the UI:

- From the app dashboard, select Settings or Branding
- Proceed to Template Branding section

> The page loads with editable fields including store name.

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
- [[app-installation]]
