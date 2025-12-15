---
tags:
  - payment
  - exploit
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:23.575Z'
skill_level: beginner
impact_level: medium
detection_risk: high
sub_techniques: []
id: 0c4eab1f-2751-443a-a1e3-fe4ae0f5f02b
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Complete-Purchase-with-Altered-Currency

## Summary

This procedure finalizes the manipulated order in MailPoet by processing the payment with the unauthorized USD currency, realizing the revenue loss through exchange rate differences.

## Description

Following the IDOR exploitation to set the currency to USD, this procedure involves proceeding through the standard checkout flow to submit and confirm the purchase. The system processes the transaction for the same numerical amount (e.g., 33600) but in USD, leading to an approximate $107 reduction in real value compared to the intended EUR equivalent. This targets the payment integration in the web application and assumes the modified URL persists through the session. The outcome demonstrates the business impact of the vulnerability.

## Requirements

1. Modified order URL with 'cur=usd' active
2. Valid payment method linked to the account
3. Active authenticated session

## Defense

Defensive measures and detection strategies:

- Re-validate currency on payment submission
- Integrate exchange rate checks and anomaly detection in transactions
- Audit payment logs for currency mismatches

## Objectives

1. Submit the order with altered parameters
2. Complete payment processing successfully
3. Achieve reduced real-world payment value

## Instructions

### Step 1: Proceed to Checkout

**Context**: Initiate the payment flow from the modified order page.

Click the purchase or subscribe button to advance to payment details.

> The form retains the USD currency from the URL parameter.

### Step 2: Enter Payment Information

**Context**: Provide necessary details to process the transaction.

Fill in billing and payment method fields, ensuring the amount shows as 33600 USD.

> Confirms the manipulation carries through.

### Step 3: Confirm and Submit

**Context**: Finalize the order to exploit the flaw.

Review and submit the payment.

> Receipt confirms 33600 USD charged, lower than EUR equivalent.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- payment
- exploit
- web
