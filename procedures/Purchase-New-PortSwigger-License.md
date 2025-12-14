---
tags:
  - business-logic
  - license-management
  - payment-processing
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
  - '[[Account Manipulation]]'
updated_at: '2025-12-14T17:28:36.292Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: e5932dcd-21bb-484b-a627-9b880386c3d0
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Manipulation]]'
---
# Purchase-New-PortSwigger-License

## Summary

This procedure simulates a legitimate purchase of a new 1-user 5-year license to trigger the business logic error in PortSwigger's system, leading to unintended changes in existing licenses.

## Description

Targeting the license purchase flow on PortSwigger's web platform, this step involves selecting and paying for a longer-term license while an existing one is active. The flaw arises from double processing of payment notifications, which modifies existing license attributes. Prerequisites include an active account and payment method; outcomes include confirmation but setup for observation of downgraded seats and extended expiry.

## Requirements

1. Active PortSwigger account with existing license
2. Valid credit card or payment method
3. Access to purchase page without restrictions

## Defense

Defensive measures and detection strategies:

- Validate purchase requests against existing licenses server-side
- Prevent concurrent modifications during payment processing
- Alert on unexpected license attribute changes post-purchase

## Objectives

1. Complete a new license acquisition to invoke faulty logic
2. Ensure double payment processing occurs
3. Set up conditions for expiry extension at seat cost

## Instructions

### Step 1: Access Purchase Page

**Context**: Begin the buying process for the new license.

Log in if needed, then navigate to the Burp Suite or Web Security product page and select the licensing options.

### Step 2: Select and Checkout License

**Context**: Choose a 1-user 5-year plan to contrast with existing multi-user license.

Add the license to cart, proceed to checkout, enter payment details, and submit. Await confirmation.

**Expected Output**: Success message or email with new license key and term details.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Account Manipulation]] Account Manipulation

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[business-logic]]
- [[license-management]]
- [[payment-processing]]
