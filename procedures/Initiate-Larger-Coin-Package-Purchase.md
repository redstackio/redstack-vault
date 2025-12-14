---
id: proc-uuid-3
tags:
  - idor
  - purchase
  - large-package
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:33.685Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Initiate-Larger-Coin-Package-Purchase

## Summary

Starts a new purchase flow for a larger coin package (e.g., 1100 coins for $3.99) to create an opportunity for order_id swapping in the IDOR vulnerability.

## Description

Cancel any pending small purchase, then select the larger package in Reddit's interface. This generates a new API request that can be intercepted and modified to reference the cheaper order_id, exploiting the lack of cross-validation.

## Requirements

1. Reddit session active
2. Burp Suite interception enabled
3. Previous order_id saved

## Defense

Defensive measures and detection strategies:

- Validate package size against order_id on fulfillment
- Track purchase attempts and flag rapid switches
- Implement client-side integrity checks

## Objectives

1. Trigger larger package request
2. Intercept for modification
3. Maintain flow control

## Instructions

### Step 1: Cancel and Restart

**Context**: End the small purchase and begin the large one.

Manual: Cancel current order, select 1100 coins ($3.99), click PayPal.

> This initiates a new POST with coins=1100&pennies=399.

### Step 2: Intercept New Request

**Context**: Capture the larger package's API call.

Use Burp to intercept the POST to create_coin_purchase_order.

> Prepare to hold the response for editing.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- idor
- initiation
- escalation
