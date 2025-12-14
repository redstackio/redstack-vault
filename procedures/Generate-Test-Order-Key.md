---
id: proc-mopub-order-key-001
tags:
  - order-generation
  - mopub
  - reconnaissance
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T12:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:25:48.023Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Generate-Test-Order-Key

## Summary

This procedure creates a test order on the MoPub platform to obtain a valid orderKey (UUID v4), which is used to understand the parameter format for the subsequent IDOR exploitation.

## Description

MoPub orders represent ad campaigns, and each is assigned a unique UUID v4 orderKey. By creating an order, an attacker can inspect the key's structure (32 alphanumeric characters) and use it as a template for targeting other users' keys. This step occurs after authentication and involves navigating the web interface. Expected outcomes include a functional orderKey that can be modified or replaced in API requests.

## Requirements

1. Authenticated session on MoPub
2. Access to https://app.mopub.com/orders
3. Basic understanding of UUID format

## Defense

Defensive measures and detection strategies:

- Log all order creations and monitor for unusual patterns
- Implement ownership verification on order access
- Rate limit order creation per account

## Objectives

1. Acquire a sample orderKey for parameter manipulation
2. Familiarize with order creation workflow
3. Enable preparation for IDOR testing

## Instructions

### Step 1: Navigate to Orders Page

**Context**: Access the orders management interface.

After login, visit https://app.mopub.com/orders.

**Expected Output**: Orders dashboard loads.

### Step 2: Create New Order

**Context**: Submit a new order to generate the UUID.

Fill in order details (e.g., name, budget) and create the order.

**Expected Output**: Order created with visible orderKey in details or network tab.

**Success Indicators**:
- Order appears in list
- UUID extracted (e.g., via browser dev tools)

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- order-generation
- mopub
