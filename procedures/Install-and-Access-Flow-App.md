---
id: p-install-flow-app
name: Install-and-Access-Flow-App
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:18.721Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - shopify
  - flow-app
  - installation
commands: []
platforms:
  - Web
tools: []
skill_level: intermediate
impact_level: low
detection_risk: low
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Install-and-Access-Flow-App

## Summary

This procedure installs the Shopify Flow app on the target store and authenticates as the staff user to access its interface, setting the stage for GraphQL token exposure during navigation.

## Description

The adversary, using owner access, installs the Flow app from the Shopify App Store. Then, switching to the staff account, they log in to the admin and navigate within the app. This triggers internal API calls, including the vulnerable GraphQL query. The target environment is a Shopify store with the app ecosystem enabled. Outcomes include app installation and staff access to the Connectors tab, where the vulnerability manifests.

## Requirements

1. Installed staff account with 'Apps' permission
2. Owner or staff credentials
3. Access to https://apps.shopify.com

## Defense

Defensive measures and detection strategies:

- Review and approve app installations manually
- Monitor app usage logs for unusual staff interactions
- Limit app permissions to least privilege

## Objectives

1. Integrate the vulnerable Flow app into the store
2. Authenticate staff access to trigger internal queries
3. Position for token interception

## Instructions

### Step 1: Install Flow App as Owner

**Context**: Add the Flow app to enable its functionality.

Log in as owner, navigate to https://apps.shopify.com/flow, and click 'Add app' to install on the store.

> Expected output: App installation confirmation and appearance in the admin apps list.

### Step 2: Log In as Staff User

**Context**: Switch to staff credentials to simulate limited access.

Log out of owner account, then log in with staff credentials at https://[store].myshopify.com/admin.

> Success: Staff dashboard loads, with access to installed apps including Flow.

### Step 3: Access Flow App Interface

**Context**: Navigate to prepare for monitoring.

From the staff admin, click on the Flow app to open it.

> Expected output: Flow app dashboard visible to staff user.

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
- [[flow-app]]
- [[installation]]
