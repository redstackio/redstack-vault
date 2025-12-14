---
tags:
  - 2fa-bypass
  - auth-bypass
  - paper-wallet
  - coinbase
type: procedure
tools: []
tactics:
  - '[[Defense Evasion]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Modify Authentication Process]]'
updated_at: '2025-12-14T17:30:58.873Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: fb6e9fea-b345-40de-b006-46d0f1d63c3d
validated: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Modify Authentication Process]]'
---
# Bypass-2FA-via-Paper-Wallet-Export

## Summary

This procedure exploits a design flaw in Coinbase's implementation by transferring BTC to a paper wallet, which does not trigger the required 2FA verification despite account settings mandating it for all withdrawals.

## Description

Coinbase's web platform treats paper wallet exports as a distinct action separate from standard withdrawals, failing to apply 2FA checks. An attacker with account access can initiate this export to move funds without additional verification, undermining 2FA's protective role and enabling potential theft. The target environment is the Coinbase web interface, requiring an authenticated session with BTC balance. Expected outcome is a successful, unverified transfer, highlighting the vulnerability's severity in cryptocurrency security.

## Requirements

1. Authenticated Coinbase session with 2FA enabled for BTC withdrawals
2. Generated paper wallet address (public key for BTC)
3. Sufficient BTC balance for transfer amount

## Defense

Defensive measures and detection strategies:

- Unify all fund movement actions under consistent 2FA enforcement in application logic
- Log and alert on paper wallet exports as high-risk transactions
- Conduct code reviews for feature-specific auth bypasses

## Objectives

1. Transfer BTC to paper wallet without 2FA prompt
2. Demonstrate unauthorized fund movement capability
3. Expose design flaw for remediation

## Instructions

### Step 1: Generate Paper Wallet

**Context**: Prepare a secure, offline wallet address to receive the bypassed transfer.

Use a trusted BTC paper wallet generator (e.g., bitaddress.org) to create a new wallet. Note the public address for import into Coinbase.

### Step 2: Initiate Export in Coinbase

**Context**: Use the wallet export feature to send BTC, observing the absence of 2FA enforcement.

In the Coinbase dashboard, navigate to the BTC wallet, select "Send" or "Export to Paper Wallet". Enter the paper wallet address and specify the amount. Proceed with the transaction; no 2FA code should be requested despite settings.

> The transfer completes directly, with funds deducted from the account.

### Step 3: Monitor Transaction

**Context**: Confirm the export processed without interruption.

Check the transaction history for the export entry. Verify funds are no longer in the Coinbase balance.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion]] Defense Evasion

### Techniques

- [[Modify Authentication Process]] Modify Authentication Process

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- 2fa-bypass
- auth-bypass
- paper-wallet
- coinbase
