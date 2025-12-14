---
tags:
  - staff-account
  - low-priv
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
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:29:09.444Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: e3ff9147-be57-4576-9a9c-3860952b3c59
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Create-Zero-Permission-Staff-Account

## Summary

This procedure creates a staff account in a Shopify sandbox store with no assigned permissions, allowing testing of access controls by simulating a low-privileged user who should not access admin functions.

## Description

Shopify allows admins to add staff members via the admin panel, but permissions must be explicitly assigned. By creating an account without any roles, you can log in as a restricted user and probe for broken access controls, such as direct URL access to sensitive endpoints. The target environment is the Shopify admin panel in a sandbox store. Prerequisites include admin access to the store. Expected outcomes: A functional staff account with confirmed restrictions on standard admin areas.

## Requirements

1. Admin access to the Shopify sandbox store.
2. An email address for the staff account (e.g., a disposable one).
3. Separate browser session for staff login to avoid cookie conflicts.

## Defense

Defensive measures and detection strategies:

- Enforce mandatory permission assignment during staff creation via UI validations.
- Log all staff account creations and monitor for logins from low-priv accounts attempting admin access.

## Objectives

1. Generate a low-privileged user for vulnerability testing.
2. Validate restricted access to confirm baseline permissions.
3. Prepare for escalation testing via unauthorized endpoints.

## Instructions

### Step 1: Add Staff Account

**Context**: From the admin dashboard, create the staff user without permissions.

Navigate to "Settings" > "Users and permissions" > "Add staff". Enter email, name, and store access details, but skip all permission checkboxes.

> Send the invitation; the account is created upon acceptance.

### Step 2: Log In as Staff and Verify Restrictions

**Context**: Test the account to ensure no admin functions are accessible.

In a new browser, go to https://<store>.myshopify.com/admin/login and use staff credentials. Attempt to access areas like products or settings.

> Expect permission denied errors or redirects to restricted views.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[staff-account]]
- [[low-priv]]
- [[authorization]]
