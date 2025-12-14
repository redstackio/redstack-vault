---
id: proc-uuid-4
tags:
  - idor
  - modification
  - swap
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
updated_at: '2025-12-14T17:25:33.680Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Modify-Order-ID-to-Small-Package

## Summary

Modifies the API response for the larger package by replacing its order_id with the one from the small package, enabling the IDOR to associate high-value coins with low payment.

## Description

In the intercepted response, edit the JSON payload to insert the previously captured order_id. This bypasses validation, causing PayPal to process the cheaper amount while Reddit credits the larger quantity upon completion.

## Requirements

1. Intercepted larger package response in Burp
2. Saved small package order_id
3. JSON editing capability in proxy

## Defense

Defensive measures and detection strategies:

- Server-side verification of order_id against purchase params
- Encrypt or hash order_ids to prevent tampering
- Audit logs for response modifications

## Objectives

1. Swap order_ids successfully
2. Forward modified response
3. Redirect to low-price PayPal

## Instructions

### Step 1: Edit Response

**Context**: Alter the order_id in the JSON response.

In Burp, drop or edit the response body to {"order_id": "SAVED_SMALL_ID"}.

> Example: Change from large ID to "1CR56170K7852611T".

### Step 2: Forward Modified Response

**Context**: Send the tampered response to the client.

Forward in Burp; observe redirect to PayPal showing $1.99.

> No errors should occur if IDOR is present.

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
- tampering
- response
