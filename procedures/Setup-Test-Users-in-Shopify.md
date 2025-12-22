---
id: proc-shopify-setup-users-001
tags:
  - setup
  - shopify
  - authentication
type: procedure
tools: []
tactics:
  - '[[Persistence]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:28:44.636Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Setup-Test-Users-in-Shopify

## Summary

This procedure sets up a test environment in Shopify by creating an owner and a staff user with full permissions, preparing for session management testing.

## Description

In a Shopify test store, an owner account is used to create a staff user with comprehensive access to simulate scenarios where access revocation is attempted. This establishes the baseline for testing session persistence across web and mobile clients. The target is a Shopify store admin interface, requiring owner credentials. Expected outcome is a fully permissioned staff account ready for login and action testing.

## Requirements

1. Access to a Shopify test store (e.g., whitehat-3.myshopify.com) with owner privileges.
2. Web browser for admin access.
3. Basic understanding of Shopify user management.

## Defense

Defensive measures and detection strategies:

- Regularly audit user permissions and session logs in Shopify admin.
- Implement multi-factor authentication (MFA) for all users to add an extra layer beyond session management.

## Objectives

1. Create owner and staff users to test access controls.
2. Ensure staff has full permissions for realistic simulation.
3. Prepare environment for session expiration testing.

## Instructions

### Step 1: Access Shopify Admin as Owner

**Context**: Log in to the test store admin to initiate user creation.

Navigate to the Shopify admin dashboard using owner credentials (e.g., Dimitris) and go to Settings > Users and permissions.

### Step 2: Create Staff User

**Context**: Add a new staff account with full access.

Click 'Add staff', enter details for the staff user (e.g., Alpha), assign full permissions including product management, and save the account.

**Expected Output**: Confirmation of staff user creation with assigned permissions.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[setup]]
- [[shopify]]
- [[authentication]]
