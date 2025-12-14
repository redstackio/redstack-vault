---
id: proc-access-pos-staff-001
name: Access-Shopify-POS-Staff-Management
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:35.629Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - shopify
  - access-control
commands: []
platforms:
  - Web
tools:
  - '[[tools/Browser-Developer-Tools]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Access-Shopify-POS-Staff-Management

## Summary

This procedure outlines navigating to the Shopify Point of Sale staff management interface to select a target staff member or store owner account, setting the stage for unauthorized modifications in stores using Google Apps login.

## Description

In Shopify stores configured for Google Apps authentication, staff members with POS access can reach the staff management page. This procedure assumes the attacker has legitimate staff credentials and targets accounts with Shopify IDs but no existing Google linkage. The goal is to load the target's profile for subsequent GraphQL interception and modification, exploiting broken access control to view and select other users' details.

## Requirements

1. Valid staff credentials with Point of Sale access permissions
2. Access to a Shopify store enabled for Google Apps login
3. Modern web browser with developer tools enabled

## Defense

Defensive measures and detection strategies:

- Implement role-based access control (RBAC) to restrict staff from viewing or selecting other staff profiles
- Monitor admin interface access logs for unusual staff management activity
- Enable multi-factor authentication (MFA) beyond Google linkage for staff accounts

## Objectives

1. Gain visibility into target staff or owner accounts
2. Prepare for email update exploitation
3. Validate POS access without triggering alerts

## Instructions

### Step 1: Log In to Shopify Admin

**Context**: Authenticate with attacker credentials to access the admin dashboard.

Navigate to the Shopify admin portal and log in using staff credentials.

### Step 2: Navigate to POS Staff Management

**Context**: Access the Point of Sale section to reach staff listings.

From the admin sidebar, select "Point of Sale" > "Staff" to load the staff management page.

### Step 3: Select Target Account

**Context**: Choose the victim's profile to trigger the update interface.

Click on the target staff member or store owner account to open their profile details.

**Expected Output**: Profile page loads, displaying editable fields including email.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Browser-Developer-Tools]]

## Tags

- shopify
- pos
- staff-management
