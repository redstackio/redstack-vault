---
tags:
  - user-creation
  - wordpress
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
updated_at: '2025-12-14T17:31:42.771Z'
sub_techniques: []
id: c21743d6-d683-445f-a4d1-9b0ea2b4236d
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Create-User-Account-on-WordPress-Site-with-Target-Email

## Summary

This procedure creates a local user account on the target WordPress site using the victim's email address, setting up the matching condition for the later SSO bypass.

## Description

WordPress allows admins to create users with any email without immediate verification. This account remains dormant until matched via JetPack SSO. In the attack, this enables the attacker to impersonate the user once the email is 'verified' on WordPress.com. The procedure is performed in the WordPress admin interface and does not notify the email owner.

## Requirements

1. Admin privileges on the target WordPress site
2. Knowledge of the victim's email address
3. JetPack already installed (from prior procedure)

## Defense

Defensive measures and detection strategies:

- Require email confirmation during user creation
- Audit user accounts for suspicious emails
- Limit admin capabilities for user management

## Objectives

1. Plant a user account tied to the victim's email
2. Enable future SSO matching
3. Avoid triggering victim notifications

## Instructions

### Step 1: Access User Management

**Context**: Navigate to the user creation interface.

In the WordPress dashboard, go to Users > Add New.

> The form loads with fields for username, email, and role.

### Step 2: Fill and Save User Details

**Context**: Enter the victim's details without verification.

Set Username to something generic (e.g., victim-user), Email to victim@company.com, select Administrator role, and click Add New User. Skip sending password to email.

> User is added to the list; check Users page to confirm.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- user-creation
- wordpress
