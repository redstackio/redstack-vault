---
tags:
  - shopify
  - app-install
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 7a0406b2-dbc8-411b-8b78-7b213341eac0
created_at: '2025-12-14T00:11:16.181Z'
updated_at: '2025-12-14T00:11:16.181Z'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Install-Return-Magic-App

## Summary

This procedure installs the Return Magic app from the Shopify app store, providing access to its portal management features where the stored XSS vulnerability can be exploited.

## Description

The Return Magic app is a Shopify plugin for handling returns and portal content. Installation grants administrative access to settings, including the unsanitized content editor. This step is prerequisite for navigating to vulnerable sections and requires Shopify store ownership.

## Requirements

1. Valid Shopify admin credentials for a store
2. Internet access to the Shopify app store
3. No additional tools beyond a web browser

## Defense

Defensive measures and detection strategies:

- Monitor app installations in Shopify audit logs for unauthorized additions
- Implement app review policies before installation
- Use Shopify's app permissions to limit scope

## Objectives

1. Add the Return Magic app to the target Shopify store
2. Enable access to app-specific settings
3. Prepare for subsequent navigation and exploitation steps

## Instructions

### Step 1: Log In to Shopify Admin

**Context**: Authenticate to the store dashboard to access the app store.

Log in at `https://admin.shopify.com` using store owner credentials and select the target store.

### Step 2: Search and Install App

**Context**: Locate and add the Return Magic app.

Navigate to Apps > Shopify App Store, search for "Return Magic", click on the app listing, and select Install App. Review and accept permissions.

### Step 3: Confirm Installation

**Context**: Verify the app is active.

Return to Apps section; the Return Magic app should appear in the list.

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
- [[app-install]]
