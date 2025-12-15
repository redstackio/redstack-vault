---
id: proc-shopify-add-staff-001
tags:
  - shopify
  - staff-management
  - authorization
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
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:30:07.071Z'
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
# Add-Staff-Member-with-Manage-Shops-Permission

## Summary

This procedure creates a new staff member in a Shopify organization and assigns the 'Manage Shops' permission, enabling access to sensitive signatures for later exploitation.

## Description

In the context of Shopify Partners, organization owners can add staff members via the dashboard. Assigning 'Manage Shops' grants access to development store creation pages, where persistent signatures are exposed. This step sets up the authorized session needed to extract the signature before revocation. Prerequisites include owner-level access to the organization settings.

## Requirements

1. Valid owner credentials for the Shopify organization
2. Access to partners.shopify.com
3. Organization must support staff management (most do)

## Defense

Defensive measures and detection strategies:

- Implement role-based access controls with granular permissions
- Monitor staff additions via audit logs in Shopify admin
- Require approval workflows for new staff permissions

## Objectives

1. Create a temporary staff account with elevated permissions
2. Enable access to signature-exposed endpoints
3. Prepare for signature extraction in subsequent steps

## Instructions

### Step 1: Log In as Organization Owner

**Context**: Authenticate with owner credentials to access management interfaces.

Navigate to https://partners.shopify.com and log in with owner account.

### Step 2: Navigate to Staff Management

**Context**: Access the section for adding and managing staff.

Go to Organization Settings > Staff, then click 'Add staff'.

### Step 3: Create and Assign Permissions

**Context**: Fill in staff details and select 'Manage Shops' permission.

Enter email, name, and assign 'Manage Shops' via the permissions dropdown. Save changes.

**Expected Output**: Confirmation message and staff listed in dashboard.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- shopify
- staff-management
