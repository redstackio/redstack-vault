---
tags:
  - idor
  - recon
type: procedure
tools:
  - '[[tools/Browser-Developer-Tools]]'
tactics:
  - '[[Discovery]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:28:59.137Z'
skill_level: intermediate
impact_level: low
sub_techniques: []
id: 5296c813-aea3-46b6-80bf-50e71602b167
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Extract-POS-User-ID-from-Users-Management

## Summary

This procedure involves inspecting the Stocky app's users management page to extract the user_id of a POS User, enabling targeted access to hidden endpoints.

## Description

As a Stocky App Administrator, access the users page and use browser developer tools to reveal the user_id from the delete button's URL or attributes. This ID is crucial for IDOR exploitation. The target environment is the web-based Stocky app on Shopify. Prerequisites include admin access and the existence of the POS User.

## Requirements

1. Stocky App Administrator permissions
2. Browser with developer tools enabled
3. Access to https://stocky.shopifyapps.com/preferences/users

## Defense

Defensive measures and detection strategies:

- Obfuscate user IDs in frontend HTML to prevent easy extraction
- Implement role-based visibility for user details
- Log inspections of user management pages

## Objectives

1. Obtain numeric user_id for POS User
2. Identify deletable user elements
3. Enable endpoint construction

## Instructions

### Step 1: Navigate to Users Page

**Context**: Load the management interface to view POS Users.

Open https://stocky.shopifyapps.com/preferences/users in the browser.

> Locate the POS User in the list.

### Step 2: Inspect Delete Button

**Context**: Use dev tools to extract ID from hidden attributes.

Right-click the delete button for the POS User, select Inspect Element, and examine the URL or data attributes for user_id.

> Expected: user_id like '12345' in href or onclick.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Browser-Developer-Tools]]

## Tags

- [[idor]]
- [[recon]]
