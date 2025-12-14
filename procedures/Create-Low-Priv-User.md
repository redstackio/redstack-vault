---
tags:
  - user-creation
  - shopify
type: procedure
tools: []
tactics:
  - '[[Persistence]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Create Account]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques:
  - '[[Local Account]]'
id: 53664ae7-349d-46f7-9a8c-173a14ea4938
created_at: '2025-12-14T17:29:57.281Z'
updated_at: '2025-12-14T17:29:57.281Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Create Account]]'
---
# Create-Low-Priv-User

## Summary

This procedure creates a low-privileged staff member in Shopify with minimal permissions, ensuring they cannot normally access Shopify Ping but can obtain tokens for exploitation.

## Description

The attacker uses Shopify admin access to add a staff account with low permissions. This simulates an insider threat or test user. Target is Shopify admin panel. Outcome: A user ready for token generation without Ping access.

## Requirements

1. Admin credentials for Shopify store
2. Access to Shopify admin dashboard
3. Staff permissions management enabled

## Defense

Defensive measures and detection strategies:

- Audit staff account creations
- Enforce approval workflows for new users

## Objectives

1. Add low-priv staff member
2. Assign minimal permissions
3. Verify no default Ping access

## Instructions

### Step 1: Add Staff Member

**Context**: Navigate to Shopify admin and create user.

No command; use web UI: Settings > Users and permissions > Add staff > Enter details with low perms.

> Expected output: Confirmation of user addition.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]]

### Techniques

- [[Create Account]]

### Sub-Techniques

- [[Local Account]]

## Commands Used


## Tools Used


## Tags

- [[user-creation]]
- [[shopify]]
