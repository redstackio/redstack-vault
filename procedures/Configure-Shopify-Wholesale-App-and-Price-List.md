---
tags:
  - csrf
  - shopify
  - setup
  - wholesale
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
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:27:50.040Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 86c12e7d-e6fa-4b40-94c7-eba4f52cea1b
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Configure Shopify Wholesale App and Price List

## Summary

This procedure sets up the Shopify Wholesale application, including installation and creation of a price list, to prepare the environment for exploiting the CSRF vulnerability in customer invitation functionality.

## Description

In the context of the CSRF attack on Shopify's Wholesale app, this initial setup configures the app within a Shopify store admin panel. It involves logging in, installing the app, and creating a price list associated with 'wholesale' tagged customers. This enables the vulnerable invitation endpoint. Prerequisites include access to a Shopify store with admin privileges. Expected outcomes: App ready for customer tagging and invitation testing, with no immediate impact but foundational for the attack chain.

## Requirements

1. Active Shopify store account with admin access
2. Internet connection for app installation from Shopify app store
3. Basic familiarity with Shopify admin interface

## Defense

Defensive measures and detection strategies:

- Restrict Wholesale app installation to trusted admins via role-based access controls (RBAC)
- Monitor app installations and configurations in Shopify audit logs for anomalous activity

## Objectives

1. Install and enable Wholesale app to expose invitation endpoints
2. Create price list to link with tagged customers
3. Verify setup without triggering alerts

## Instructions

### Step 1: Log In and Install App

**Context**: Access the Shopify admin to install the Wholesale application, which introduces the vulnerable CSRF-exposed functionality.

Navigate to the Shopify admin dashboard and search for the 'Wholesale' app in the app store. Click 'Add app' and follow the installation prompts to enable it.

> Expected: App icon appears in the admin sidebar; no errors during install.

### Step 2: Create Price List

**Context**: Configure a price list to associate with wholesale customers, setting up the backend for invitations.

In the Wholesale app dashboard, select 'Price Lists' and click 'Create price list'. Define rules to apply to customers tagged 'wholesale', such as custom pricing tiers.

> Expected: New price list saved and visible in the app's configuration section.

### Step 3: Verify Configuration

**Context**: Ensure the app and price list are operational before proceeding to customer tagging.

Return to the Wholesale dashboard and confirm the price list is active. Test by navigating to the customers section (empty at this stage).

> Expected: No configuration errors; dashboard loads fully.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[shopify]]
- [[wholesale]]
