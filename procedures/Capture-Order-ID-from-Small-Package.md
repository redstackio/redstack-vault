---
id: proc-uuid-2
tags:
  - idor
  - capture
  - order-id
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
updated_at: '2025-12-14T17:25:33.695Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Capture-Order-ID-from-Small-Package

## Summary

Extracts the order_id from the API response of a small coin package purchase, which will be used to manipulate subsequent transactions in the IDOR attack.

## Description

After intercepting the create_coin_purchase_order request, forward it to receive the response containing the PayPal order_id. This ID is tied to the $1.99 amount but can be swapped due to lack of validation. Save it securely for the next steps.

## Requirements

1. Active interception in Burp Suite
2. Previous step's request forwarded
3. Note-taking for ID storage

## Defense

Defensive measures and detection strategies:

- Bind order_ids to user sessions and validate on every use
- Log and alert on response inspection anomalies
- Use ephemeral IDs that expire quickly

## Objectives

1. Obtain low-value order_id
2. Verify response integrity
3. Prepare for ID swap

## Instructions

### Step 1: Forward and Inspect Response

**Context**: In Burp, forward the intercepted request to get the API response.

No command; manual: View response in Burp Repeater or Inspector.

> Expected: {"order_id": "1CR56170K7852611T"} corresponding to $1.99.

### Step 2: Save Order ID

**Context**: Record the ID for later modification.

Copy the order_id value to a secure note.

> Ensure no accidental completion of the purchase.

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
- response
- paypal
