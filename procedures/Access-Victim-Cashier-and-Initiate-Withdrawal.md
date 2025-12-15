---
tags:
  - info-disclosure
  - unauthorized-withdrawal
type: procedure
tools:
  - '[[tools/Browser-Developer-Tools]]'
tactics:
  - '[[Collection]]'
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Data from Information Repositories]]'
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:25:12.977Z'
sub_techniques: []
id: 6f3d7490-5105-47f3-b9ce-9b7d6f92f1b0
validated: true
mitre_tactics:
  - '[[Collection]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Data from Information Repositories]]'
  - '[[Valid Accounts]]'
---
# Access-Victim-Cashier-and-Initiate-Withdrawal

## Summary

This procedure interacts with the exploited victim's cashier to disclose PII and initiate withdrawals to the attacker's payment methods, demonstrating full impact.

## Description

Once loaded, the victim's cashier allows viewing details via the customer name link and submitting withdrawals. For payouts, repeat the flow but set Action=PAYOUT; submissions go to attacker's linked methods like credit card or Skrill, though manual review may block completion.

## Requirements

1. Successfully modified iframe loading victim's cashier
2. Victim's account must have funds for withdrawal simulation
3. Attacker's payment methods linked

## Defense

Defensive measures and detection strategies:

- Require 2FA or additional auth for sensitive actions like withdrawals
- Implement anomaly detection for cross-account access patterns
- Manual review queues with alerts for unusual payout destinations

## Objectives

1. Exfiltrate sensitive user information
2. Demonstrate fund transfer capability
3. Highlight lack of access controls

## Instructions

### Step 1: View Account Details

**Context**: Access PII in the loaded iframe.

Click the "Cashier" button, then the "View" link next to the customer name to reveal full name, email, and phone.

### Step 2: For Deposit Flow - Confirm Access

**Context**: Validate unauthorized login.

Interact with deposit options to ensure full control.

### Step 3: Initiate Withdrawal (Payout Flow)

**Context**: Modify for withdrawal exploitation.

Reload the process with Action=PAYOUT in src, select attacker's payment method, enter amount, and submit.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]
- [[Execution]]

### Techniques

- [[Data from Information Repositories]]
- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Browser-Developer-Tools]]

## Tags

- [[info-disclosure]]
- [[unauthorized-withdrawal]]
