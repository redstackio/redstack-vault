---
tags:
  - shopify
  - admin-access
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
id: 19892918-0bb4-4fe2-bb20-52a18d01896a
created_at: '2025-12-14T00:11:16.170Z'
updated_at: '2025-12-14T00:11:16.170Z'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-Return-Magic-Admin-Page

## Summary

This procedure navigates to the administrative dashboard of the Return Magic app within Shopify, enabling access to configuration tabs like Settings.

## Description

After installation, the app's admin page provides entry to vulnerable features such as portal content editing. The URL follows Shopify's app proxy pattern, loading the app in an iframe or dedicated view. This step assumes the app is installed and user has admin privileges.

## Requirements

1. Return Magic app installed in the Shopify store
2. Shopify admin session active
3. Web browser with JavaScript enabled

## Defense

Defensive measures and detection strategies:

- Enforce multi-factor authentication for Shopify admin
- Log and alert on unusual app access patterns
- Restrict app permissions to minimal scopes

## Objectives

1. Load the Return Magic dashboard
2. Prepare for settings navigation
3. Confirm admin interface accessibility

## Instructions

### Step 1: Open Shopify Apps List

**Context**: Locate the installed app.

In Shopify admin, go to Apps and click on Return Magic.

### Step 2: Load Admin Interface

**Context**: Access the app's internal dashboard.

Use the direct URL `https://<shop>.myshopify.com/admin/apps/returnmagic` or click through from the apps list to load the page.

### Step 3: Verify Dashboard

**Context**: Ensure full functionality.

Check for top menu with Settings tab and left sidebar options.

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
- [[admin-access]]
