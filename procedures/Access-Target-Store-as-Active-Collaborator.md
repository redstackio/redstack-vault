---
tags:
  - shopify
  - account-takeover
  - web
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
updated_at: '2025-12-14T17:32:01.256Z'
sub_techniques: []
id: 9b4725f6-b6e5-4d94-9bd3-a73e7cbafcc5
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
---

# Access Target Store as Active Collaborator

## Summary

This procedure logs into the target Shopify store's admin panel using the illicitly activated collaborator account, granting full unauthorized access.

## Description

Once converted, the account provides complete collaborator permissions, allowing admin actions like viewing data, editing products, or managing orders without the merchant's knowledge.

## Requirements

1. Active collaborator status on target store
2. Partner dashboard access
3. Target store admin URL

## Defense

Defensive measures and detection strategies:

- Review all collaborator additions manually
- Implement role-based access controls with audits
- Monitor login logs for unusual partner IPs

## Objectives

1. Achieve full store admin access
2. Perform unauthorized actions
3. Maintain persistence if needed

## Instructions

### Step 1: Navigate to Store

**Context**: From partner dashboard, select the target.

In the partners.shopify.com dashboard, go to the target store's page.

> Expected output: Store details load with collaborator options.

### Step 2: Log In to Admin

**Context**: Use collaborator credentials for access.

Click 'Log in to store' or visit the admin URL (e.g., target.myshopify.com/admin) with the account.

> Expected output: Full admin dashboard access granted.

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
- [[account-takeover]]
