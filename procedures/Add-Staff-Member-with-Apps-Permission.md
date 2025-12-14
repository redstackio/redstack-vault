---
id: uuid-placeholder-1
tags:
  - shopify
  - staff-management
  - permission-setup
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
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:30:07.363Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Add-Staff-Member-with-Apps-Permission

## Summary

This procedure creates a new staff account in Shopify with only 'Apps' permission, simulating limited access for testing authorization boundaries in apps like Flow.

## Description

In the context of exploiting improper authorization in Shopify Flow, this step sets up a staff member who can access app connectors. The account is created via the Shopify admin panel, granting minimal permissions to avoid broad access while enabling interaction with the Flow app. This is a prerequisite for generating signed URLs that lack proper session validation.

## Requirements

1. Valid Shopify store owner credentials with staff management permissions.
2. Access to the Shopify admin panel (https://admin.shopify.com).
3. Email address for the new staff account.

## Defense

Defensive measures and detection strategies:

- Implement role-based access control (RBAC) with granular permissions and regular audits.
- Monitor staff account creations and permission changes via Shopify logs.

## Objectives

1. Establish a test account with restricted access to apps.
2. Prepare for subsequent steps in the authorization bypass chain.
3. Verify permission scoping in Shopify admin.

## Instructions

### Step 1: Log In as Owner

**Context**: Gain administrative access to manage staff.

Navigate to the Shopify admin panel and log in with owner credentials.

### Step 2: Create New Staff Account

**Context**: Add a staff member with specific permissions.

Go to Settings > Users and permissions > Add staff. Enter details and select only 'Apps' permission. Save and send invitation.

> Expected output: Staff account created, invitation email sent.

### Step 3: Verify Account

**Context**: Confirm the account can log in with limited access.

Log in with the new staff credentials to ensure only Apps section is accessible.

> Expected output: Successful login, restricted navigation.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[shopify]]
- [[staff-management]]
