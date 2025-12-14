---
id: proc-shopify-setup-001
tags:
  - shopify
  - setup
  - staff-accounts
  - discount-code
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
updated_at: '2025-12-14T17:29:45.062Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Setup-Shopify-Staff-Accounts-and-Discount-Code

## Summary

This procedure sets up the necessary Shopify admin environment by creating two staff accounts and a discount code with an initial comment, preparing for exploitation of the timeline vulnerability.

## Description

In a Shopify store admin panel, create staff accounts with discounts permissions and establish a target discount code. This simulates a multi-user scenario where one staff member can exploit the system to affect others, including admins. The initial comment activates the timeline section, making it vulnerable to disablement via malformed input.

## Requirements

1. Super admin access to Shopify store
2. Web browser for admin panel navigation
3. Permissions to manage staff and discounts

## Defense

Defensive measures and detection strategies:

- Restrict staff account creation to trusted admins
- Monitor for unusual discount code creations
- Implement input sanitization previews in UI

## Objectives

1. Establish authenticated access for multiple users
2. Create a vulnerable discount code with active timeline
3. Prepare for GraphQL mutation testing

## Instructions

### Step 1: Create Staff Accounts

**Context**: Log in as super admin and add two staff accounts with discounts section access.

Navigate to Settings > Users and permissions, add admin1 and admin2, assign permissions for discounts.

**Expected Output**: Accounts created and able to log in.

### Step 2: Create Discount Code and Initial Comment

**Context**: As admin1, create a discount code and post an initial comment to enable timeline.

Go to Discounts > Create discount, set basic details, save, then add a comment like "Initial note".

**Expected Output**: Discount code page shows timeline with comment.

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
- setup
