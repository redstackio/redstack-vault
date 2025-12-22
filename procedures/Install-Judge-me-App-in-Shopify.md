---
tags:
  - shopify
  - app-install
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
  - Shopify
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 9f64240a-58e3-4608-a536-7c2e26fda2af
created_at: '2025-12-13T23:52:25.698Z'
updated_at: '2025-12-13T23:52:25.698Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Install Judge.me App in Shopify

## Summary

This procedure outlines logging into a Shopify development store and installing the Judge.me app to access its product management features, setting the stage for vulnerability exploitation.

## Description

In a Shopify environment, admins can install third-party apps like Judge.me from the App Store. This step requires admin credentials and provides access to the app's interface at /admin/apps/judgeme, where product filters are used. No technical exploits occur here; it's preparatory access.

## Requirements

1. Valid Shopify admin credentials for a development or target store
2. Internet access to the Shopify admin panel
3. Web browser for navigation

## Defense

Defensive measures and detection strategies:

- Monitor app installations via Shopify audit logs for unauthorized additions
- Enforce app review policies before installation
- Use Shopify's app permissions to limit scope

## Objectives

1. Establish access to Judge.me product filters
2. Prepare environment for payload injection and triggering
3. Verify app integration without errors

## Instructions

### Step 1: Log In to Shopify Admin

**Context**: Access the Shopify control panel to begin app management.

Navigate to your Shopify store's admin URL (e.g., https://xxx.myshopify.com/admin) and log in with admin credentials.

### Step 2: Install Judge.me App

**Context**: Add the Judge.me app to enable product review and filtering features.

In the admin panel, go to Apps > Shopify App Store, search for "Judge.me", select the app, and click Install. Follow any permission prompts to authorize access to products.

**Expected Output**: Confirmation message and app icon added to the Apps section.

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
