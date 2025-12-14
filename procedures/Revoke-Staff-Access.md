---
id: p-revoke-staff
name: Revoke-Staff-Access
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:18.713Z'
tactics:
  - '[[Persistence]]'
techniques:
  - '[[Valid Accounts]]'
sub_techniques: []
tags:
  - shopify
  - staff-revocation
  - persistence
commands: []
platforms:
  - Web
tools: []
skill_level: beginner
impact_level: low
detection_risk: low
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---

# Revoke-Staff-Access

## Summary

This procedure revokes the staff account to simulate an ex-employee scenario, highlighting how the leaked token maintains access despite account removal.

## Description

Using owner credentials, the adversary removes the staff account from the Shopify admin. This tests the persistence of the intercepted token, which continues to grant API access without tied authentication. Target: Shopify admin users section. Prerequisites: Owner access post-token capture. Outcomes: Account deletion, but token validity persists, demonstrating the vulnerability's severity.

## Requirements

1. Owner credentials
2. Access to Shopify admin
3. Previously created staff account

## Defense

Defensive measures and detection strategies:

- Automate token invalidation on staff changes
- Audit API access post-revocation
- Enable alerts for lingering app tokens

## Objectives

1. Remove staff authentication
2. Demonstrate token persistence
3. Enable post-revocation exploitation

## Instructions

### Step 1: Log In as Owner

**Context**: Regain control to manage users.

Navigate to https://[store].myshopify.com/admin and log in as owner.

> Expected output: Full admin access restored.

### Step 2: Remove Staff Account

**Context**: Deactivate or delete the staff member.

Go to 'Settings' > 'Users and permissions', select the staff account, and click 'Remove access' or 'Delete'.

> Expected output: Confirmation of removal; staff can no longer log in.

### Step 3: Verify Revocation

**Context**: Confirm account is inaccessible.

Attempt staff login; it should fail.

> Success: Error message on login attempt.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]] Persistence

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[shopify]]
- [[staff-revocation]]
- [[Persistence]]
