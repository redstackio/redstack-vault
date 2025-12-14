---
id: proc-create-limited-staff-account
tags:
  - shopify
  - staff-account
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
updated_at: '2025-12-14T17:29:19.748Z'
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
# Create-Limited-Staff-Account

## Summary

This procedure creates a Shopify staff account with restricted permissions, specifically granting 'Manage and install apps and channels' while omitting 'Develop apps', to test and exploit authorization bypasses in app management functions.

## Description

In the context of Shopify's admin panel, staff permissions control access to various features. This procedure sets up a test account that can interact with apps but lacks developer-level access, enabling demonstration of improper authorization in GraphQL API endpoints. Prerequisites include owner-level access to the store settings. Expected outcome is a functional staff user ready for authenticated requests.

## Requirements

1. Valid Shopify store owner credentials
2. Access to the Shopify admin panel (https://*.myshopify.com/admin)
3. Browser or API client for navigation

## Defense

Defensive measures and detection strategies:

- Enforce principle of least privilege by auditing staff roles regularly
- Monitor staff account creations and permission changes via Shopify audit logs
- Implement multi-factor authentication (MFA) for all staff accounts

## Objectives

1. Establish a low-privilege account for testing auth bypass
2. Verify permission assignment excludes developer access
3. Prepare for subsequent API interactions

## Instructions

### Step 1: Access User Management

**Context**: Log in as store owner and navigate to staff settings to create a new user.

No command required; use the web interface:

1. Go to Settings > Users and permissions.
2. Click 'Add staff'.

**Expected Output**: Form for new staff account appears.

### Step 2: Configure Permissions

**Context**: Assign limited role to mimic a non-developer staff member.

1. Enter staff details (name, email).
2. Select 'Standard' permissions and check only 'Manage and install apps and channels'.
3. Ensure 'Develop apps' is unchecked.
4. Save the account and send invitation.

**Expected Output**: Staff account listed with limited role.

### Step 3: Verify Login

**Context**: Confirm the account can log in and access app sections without developer tools.

1. Log in with new credentials.
2. Navigate to Apps; confirm view access but no uninstall options via UI.

**Expected Output**: Successful login; apps visible but limited actions.

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
- staff-account
- permissions
