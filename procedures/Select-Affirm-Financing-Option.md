---
id: proc-uuid-2
tags:
  - financing
  - api-trigger
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:47.482Z'
skill_level: intermediate
impact_level: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Select-Affirm-Financing-Option

## Summary

This procedure selects Affirm as the payment method during checkout, triggering the generation of a unique 'checkout_ari' parameter in the API request.

## Description

During the checkout process on razer.com, choosing Affirm initiates a POST request to Affirm's API endpoint (/api/██████/), which includes the 'checkout_ari' identifier. This step is crucial as it creates the vulnerable reference point for IDOR exploitation.

## Requirements

1. Active checkout session on razer.com
2. Proxy tool configured to capture traffic
3. Knowledge of payment flow

## Defense

Defensive measures and detection strategies:

- Validate user session before generating ARIs
- Log financing selections for anomaly detection

## Objectives

1. Activate Affirm integration
2. Generate 'checkout_ari'
3. Expected outcome: API request with parameter visible

## Instructions

### Step 1: Choose Payment Method

**Context**: Reach the payment selection screen.

Select 'Affirm' from available financing options.

> This sends the POST request; intercept if proxied.

### Step 2: Monitor Request

**Context**: Observe the network for the API call.

Use Burp Suite to capture the request body containing 'checkout_ari': 'XXXXXXXXXXXXXXXX'.

> Expected output: Request details in proxy tool.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[financing]]
- [[api-trigger]]
