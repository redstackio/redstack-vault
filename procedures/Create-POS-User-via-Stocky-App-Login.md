---
tags:
  - shopify
  - user-creation
type: procedure
tools:
  - '[[tools/Browser-Developer-Tools]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
  - Mobile
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[External Remote Services]]'
updated_at: '2025-12-14T17:28:59.140Z'
skill_level: beginner
impact_level: low
sub_techniques: []
id: 32de6782-a673-4cc4-9f63-a34ebc2d66f5
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[External Remote Services]]'
---
# Create-POS-User-via-Stocky-App-Login

## Summary

This procedure creates a Point of Sale (POS) User account in the Stocky Shopify app backend by logging in through the POS mobile application, establishing a target for privilege escalation.

## Description

In the Stocky app environment, logging into the app from the POS mobile app automatically provisions a POS User in the backend without explicit admin intervention. This user type has limited permissions but can be targeted for elevation due to lax controls. The procedure requires access to the POS app and assumes the attacker has initial admin credentials in Stocky. Expected outcome is a new user entry visible in the admin users management page.

## Requirements

1. Valid credentials for the POS mobile application
2. Network access to Shopify and Stocky services
3. Stocky App Administrator role for verification

## Defense

Defensive measures and detection strategies:

- Monitor automatic user creations tied to POS logins for anomalies
- Implement approval workflows for POS-linked user provisioning
- Log all backend user creations with source IP and device details

## Objectives

1. Provision a base POS User for manipulation
2. Ensure the user is listed in admin interface
3. Prepare for IDOR-based edits

## Instructions

### Step 1: Launch POS App and Login

**Context**: Initiate the automatic user creation process via mobile login.

No specific command; perform manual login in the POS app to https://stocky.shopifyapps.com or equivalent mobile endpoint.

> Upon successful login, the backend creates the POS User. Verify by checking the users list as an admin.

### Step 2: Verify User Creation

**Context**: Confirm the new user exists in the Stocky admin panel.

Navigate to https://stocky.shopifyapps.com/preferences/users and search for the new POS User.

> Expected: New user entry with POS type, no admin flags.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[External Remote Services]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Browser-Developer-Tools]]

## Tags

- [[shopify]]
- [[user-creation]]
