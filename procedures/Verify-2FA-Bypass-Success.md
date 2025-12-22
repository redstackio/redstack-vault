---
tags:
  - verification
  - bypass-confirmation
  - coinbase
  - evidence-collection
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Modify Authentication Process]]'
updated_at: '2025-12-14T17:30:58.868Z'
skill_level: basic
impact_level: high
detection_risk: low
sub_techniques: []
id: 6a7c6033-aa9b-4415-bcb4-32dd46e30328
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Modify Authentication Process]]'
---
# Verify-2FA-Bypass-Success

## Summary

This procedure confirms the effectiveness of the 2FA bypass by reviewing transaction details and gathering evidence of the unverified transfer, essential for reporting and remediation.

## Description

After executing the paper wallet export, this step involves inspecting Coinbase's transaction logs and external wallet confirmations to validate that no 2FA was enforced. It captures screenshots and details to document the flaw, where the system incorrectly classifies exports as non-withdrawal actions. In a real attack scenario, this enables attackers to exfiltrate funds stealthily. The procedure targets the web platform's history interface and requires prior access to the account.

## Requirements

1. Completed paper wallet export transaction
2. Access to both Coinbase dashboard and paper wallet verification tools
3. Screenshot capture capability (e.g., browser dev tools)

## Defense

Defensive measures and detection strategies:

- Enhance logging to include 2FA enforcement attempts for all fund movements
- Implement anomaly detection for transfers without verification
- Require manual review for high-value paper wallet exports

## Objectives

1. Confirm absence of 2FA in transaction process
2. Collect evidence like screenshots and IDs
3. Validate fund transfer success

## Instructions

### Step 1: Review Coinbase Transaction History

**Context**: Check internal logs for signs of bypassed security.

Log in to Coinbase, go to "Accounts" > "BTC" > "Transactions". Locate the recent export entry and note the absence of any 2FA-related notes or timestamps.

### Step 2: Verify Funds in Paper Wallet

**Context**: Ensure the transfer arrived without issues, confirming the bypass worked end-to-end.

Import the paper wallet private key into a viewer (e.g., blockchain explorer) or wallet software. Search for the transaction ID from Coinbase to see the incoming BTC.

> Balance updates to reflect received amount.

### Step 3: Capture Evidence

**Context**: Document the vulnerability for reporting.

Take screenshots of the settings (showing 2FA enabled), the export interface (no prompt), and transaction history. Attach these to a report, including details like account ID (redacted) and timestamps.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Modify Authentication Process]] Modify Authentication Process

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- verification
- bypass-confirmation
- coinbase
- evidence-collection
