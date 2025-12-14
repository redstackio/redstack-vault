---
tags:
  - staff-addition
  - transfer
  - shopify
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:29:44.875Z'
sub_techniques: []
id: 775d49cd-15b9-47c9-b6d3-fb47fb87c2cb
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Add-Staff-Member-to-Store

## Summary

This procedure adds a staff account to the development store, populating sensitive data for exposure via IDOR.

## Description

By simulating ownership transfer, a staff member is added, creating account details that can be leaked through insufficient checks. This targets the privacy aspect of the vulnerability.

## Requirements

1. Existing development store
2. Admin access to store settings
3. Transfer feature enabled

## Defense

Defensive measures and detection strategies:

- Validate permissions before staff listing
- Audit transfer attempts

## Objectives

1. Create staff account in store
2. Prepare for staff enumeration
3. Test persistence post-transfer

## Instructions

### Step 1: Initiate Transfer

**Context**: Access staff addition interface.

Go to https://partners.shopify.com/[business_id]/development_stores, select store, and click 'Transfer store to client'.

> Transfer options load.

### Step 2: Add Staff

**Context**: Save the new account.

Click 'Add a staff account', enter details, and save.

> Staff appears in dropdown for transfer.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[staff-addition]]
- [[transfer]]
- [[shopify]]
