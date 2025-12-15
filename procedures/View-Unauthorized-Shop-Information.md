---
tags:
  - data-exposure
  - shop-details
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
updated_at: '2025-12-14T17:29:44.867Z'
sub_techniques: []
id: e4900376-a6cc-4f65-8d65-4bc239a1fd2f
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# View-Unauthorized-Shop-Information

## Summary

This procedure views sensitive shop details accessed via IDOR, demonstrating persistence even after ownership transfer.

## Description

Once the IDOR URL is accessed, internal data like shop configs is exposed. Separate checks prevent actual transfer, but viewing succeeds due to flawed controller permissions.

## Requirements

1. Successful IDOR URL access
2. Limited session
3. Post-transfer test setup

## Defense

Defensive measures and detection strategies:

- Enforce per-endpoint authorization
- Audit data access logs

## Objectives

1. Extract shop metadata
2. Verify bypass effectiveness
3. Assess privacy impact

## Instructions

### Step 1: Load Shop Page

**Context**: Observe exposed data.

With the IDOR URL open, review shop information displayed.

> Details include internal configs and status.

### Step 2: Test Persistence

**Context**: Confirm after transfer.

As admin, transfer ownership to another staff (pending), then reload as limited user.

> Data remains visible.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[data-exposure]]
- [[shop-details]]
- [[shopify]]
