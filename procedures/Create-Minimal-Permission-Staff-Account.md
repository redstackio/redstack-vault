---
id: p-create-staff-account
name: Create-Minimal-Permission-Staff-Account
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:18.724Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Valid Accounts]]'
sub_techniques: []
tags:
  - shopify
  - staff-account
  - initial-access
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
  - '[[Valid Accounts]]'
---

# Create-Minimal-Permission-Staff-Account

## Summary

This procedure creates a staff account in a Shopify store with only 'Apps' permissions, simulating an insider threat or ex-employee setup for subsequent token leakage exploitation.

## Description

In the attack scenario, the adversary logs in as the store owner to create a new staff member via the Shopify admin interface. Permissions are restricted to 'Apps' only, ensuring minimal access while allowing interaction with installed apps like Flow. This sets up the environment for token interception without granting broader admin rights. Prerequisites include owner-level credentials and access to the Shopify admin dashboard. Expected outcomes include a functional staff account that can authenticate to apps but not perform other store operations.

## Requirements

1. Owner credentials for the target Shopify store
2. Access to Shopify admin dashboard (https://[store].myshopify.com/admin)
3. Internet connectivity

## Defense

Defensive measures and detection strategies:

- Implement role-based access controls (RBAC) and regularly audit staff permissions
- Monitor for unusual staff account creations via Shopify audit logs
- Use multi-factor authentication (MFA) for all staff accounts

## Objectives

1. Gain initial legitimate access to the store environment
2. Prepare for app-based interactions without alerting via excessive permissions
3. Simulate ex-employee persistence testing

## Instructions

### Step 1: Log In as Owner

**Context**: Authenticate to the Shopify admin to access staff management features.

Navigate to https://[store].myshopify.com/admin and log in with owner credentials.

> Successful login grants access to the 'Settings' > 'Users and permissions' section.

### Step 2: Create Staff Account

**Context**: Add a new staff member with restricted permissions.

In the admin dashboard, go to 'Settings' > 'Users and permissions' > 'Add staff'. Enter details for the new staff (e.g., email, name) and select only 'Apps' permission. Save the account.

> Expected output: Confirmation message and the staff account appears in the list with 'Apps' scope only.

### Step 3: Verify Permissions

**Context**: Ensure the account has minimal access.

Attempt to log in as the new staff user to confirm it can access apps but not other sections like orders or products.

> Success: Staff login works, but navigation to non-app areas is restricted.

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
- [[staff-account]]
- [[initial-access]]
