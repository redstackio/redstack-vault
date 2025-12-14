---
tags:
  - bitcoin-transaction
  - app-interaction
  - coinbase
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Android
  - Mobile
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:24:42.000Z'
skill_level: novice
impact_level: low
detection_risk: low
sub_techniques: []
id: 60e7b8fd-94f6-4691-bfa6-fbb330c20046
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Initiate-Bitcoin-Transaction-Between-Accounts

## Summary

This procedure involves sending a small bitcoin amount from one Coinbase account to another within the Android app, setting up the conditions for observing information disclosure in the transaction history.

## Description

To test the vulnerability, a legitimate bitcoin transaction is initiated between test accounts. This mimics user behavior and populates the recipient's transaction list, where the flaw reveals the sender's email. The process uses the app's built-in send feature, requiring funded accounts (minimal balance). Outcomes include a confirmed transfer that indirectly exposes personal data due to UI rendering issues.

## Requirements

1. Two active Coinbase accounts from prior setup
2. Small bitcoin balance in sender account (e.g., 0.0001 BTC, obtainable via app faucet or purchase)
3. Android app access with transaction permissions enabled

## Defense

Defensive measures and detection strategies:

- Anonymize sender identifiers in transaction UIs (e.g., show usernames or hashes instead of emails)
- Log and alert on transaction patterns that could indicate testing/abuse
- Enforce privacy controls in app code to redact sensitive fields

## Objectives

1. Trigger update to recipient's transaction history
2. Ensure transaction processes without errors
3. Prepare for inspection of disclosed data

## Instructions

### Step 1: Log In to Sender Account

**Context**: Access the sending account to prepare the transaction.

Open the Coinbase app on Android, log in with sender credentials, and navigate to the 'Portfolio' or 'Assets' section to select Bitcoin.

### Step 2: Prepare Send

**Context**: Input recipient details to initiate the transfer.

Tap 'Send', select Bitcoin, enter the amount (small test value), and paste the recipient's Bitcoin address from their account (found in 'Receive' section).

### Step 3: Confirm and Execute

**Context**: Finalize the transaction to broadcast it on the network.

Review details, confirm the send, and wait for processing (usually seconds to minutes). Check sender's history for confirmation.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- bitcoin-transaction
- app-interaction
- coinbase
