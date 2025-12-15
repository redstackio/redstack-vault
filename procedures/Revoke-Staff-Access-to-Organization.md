---
id: proc-shopify-revoke-access-001
tags:
  - shopify
  - access-revocation
  - authorization
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
updated_at: '2025-12-14T17:29:57.387Z'
skill_level: basic
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Revoke-Staff-Access-to-Organization

## Summary

This procedure removes a staff member's access to the Shopify organization, simulating revocation while the extracted signature remains usable.

## Description

Using the owner account, revoke permissions through the staff management interface. This does not invalidate existing signatures, allowing post-revocation abuse. The staff account loses dashboard access but can still submit requests with the signature.

## Requirements

1. Owner credentials
2. Active staff member to revoke
3. Access to organization settings

## Defense

Defensive measures and detection strategies:

- Invalidate all associated tokens upon revocation
- Audit revocation events and correlate with subsequent API calls
- Use short-lived or permission-checked signatures

## Objectives

1. Remove staff from organization
2. Confirm access denial
3. Test signature persistence

## Instructions

### Step 1: Log In as Owner

**Context**: Switch to owner session for management.

Log in to https://partners.shopify.com with owner credentials.

### Step 2: Access Staff Management

**Context**: Locate the target staff member.

Navigate to Organization Settings > Staff.

### Step 3: Revoke Access

**Context**: Remove the member to deny future access.

Select the staff member and click 'Remove' or 'Revoke Access'. Confirm the action.

**Expected Output**: Staff removed from list; login attempts fail.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]] Persistence

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- shopify
- access-revocation
