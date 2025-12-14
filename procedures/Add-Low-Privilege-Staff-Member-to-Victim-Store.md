---
id: proc-add-low-priv-staff
tags:
  - shopify
  - staff-permissions
  - access-control
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
  - Shopify
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:29:44.432Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Add Low-Privilege Staff Member to Victim Store

## Summary

This procedure invites a secondary account as a staff member to the victim Shopify store with zero permissions, enabling the simulation of unauthorized internal access for IDOR exploitation.

## Description

To test permission bypasses, use the primary admin account to add the attacker as staff via the Shopify admin interface. Assign no permissions to ensure the account can log in but cannot perform actions. This creates a low-privilege context for accessing app endpoints. The invitation is sent via email, and upon acceptance, the staff can view the restricted dashboard. This step is crucial for demonstrating disclosure without elevated rights.

## Requirements

1. Admin access to the victim store
2. Email address for the target staff account
3. Shopify's user management enabled

## Defense

Defensive measures and detection strategies:

- Enforce multi-factor authentication for staff invites
- Audit staff additions and permission changes in Shopify logs
- Limit staff logins to IP whitelists or require approval workflows

## Objectives

1. Grant minimal access to simulate insider threat
2. Establish session for cross-store endpoint testing
3. Verify permission restrictions hold for actions but not disclosure

## Instructions

### Step 1: Invite Staff

**Context**: From the victim store admin, initiate the staff addition.

Go to Settings > Users and permissions > Add staff, enter the attacker's email, and select 'No access' for all permissions.

> Invitation sent via Shopify's built-in email system.

### Step 2: Accept Invitation

**Context**: Switch to the attacker account to join the store.

Check email, click the invite link, log in, and confirm staff role.

> Manual acceptance; dashboard loads with restrictions.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[shopify]]
- [[staff-permissions]]
