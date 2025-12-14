---
tags:
  - 2fa-bypass
  - auth-bypass
  - parameter-tampering
  - coinbase
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:47.729Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 1e497a65-eebf-4a4f-9130-0dbe45a10084
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
---
# Bypass-Coinbase-2FA-via-Internal-Transfer-Manipulation

## Summary

This procedure exploits a vulnerability in Coinbase's internal wallet transfer feature to bypass two-factor authentication (2FA) for Bitcoin (BTC) transfers to external wallets. By intercepting and modifying the HTTP POST request's transaction[to] parameter using Burp Suite, an attacker with account access can redirect funds to arbitrary external addresses without entering the 2FA code, enabling unauthorized fund exfiltration.

## Description

The attack targets the POST /accounts/transfer_money endpoint, where internal transfers do not require 2FA, but the backend fails to validate that the transaction[to] parameter points only to account-owned wallets. Wallet IDs are MongoDB BSON objects extractable from the page DOM (e.g., via data-wallet-id attributes). With account login, an attacker initiates an internal transfer, intercepts it, swaps the to-ID to an external one, and forwards the request. This bypasses 2FA checks, as the system treats it as internal. Prerequisites include a Coinbase account with BTC, 2FA enabled for transfers, and at least two wallets. Expected outcome: Funds transferred externally without additional auth.

## Requirements

1. Valid Coinbase account with BTC balance and 2FA enabled for transfers
2. Access to Burp Suite for HTTP interception and modification
3. Knowledge of target external wallet's MongoDB BSON ID (obtainable from DOM or blockchain explorers)
4. Proxy configuration in browser to route traffic through Burp Suite

## Defense

Defensive measures and detection strategies:

- Implement server-side validation to restrict transaction[to] to verified internal wallets only
- Enforce 2FA for all transfers regardless of internal/external classification
- Monitor for anomalous request patterns, such as parameter tampering in transfer endpoints
- Use rate limiting and anomaly detection on wallet transfer APIs

## Objectives

1. Bypass 2FA to enable unauthorized external BTC transfers
2. Exfiltrate funds from the victim's Coinbase account
3. Demonstrate parameter validation flaws in financial APIs

## Instructions

### Step 1: Setup Account and Enable 2FA

**Context**: Configure the account to require 2FA for BTC transfers and create multiple wallets for internal simulation.

Log in to Coinbase, go to Settings > Security, and enable advanced 2FA for sending bitcoins. Then, navigate to https://coinbase.com/accounts, create a second BTC wallet, and note the wallet IDs from the DOM (e.g., inspect elements for data-wallet-id).

### Step 2: Initiate Internal Transfer

**Context**: Start a legitimate internal transfer to capture the request structure without triggering 2FA.

Select source wallet as 'From', second wallet as 'To', enter amount (e.g., 0.1 BTC), add notes if desired, and click Transfer. Ensure Burp Suite is proxying traffic to intercept the POST to /accounts/transfer_money.

### Step 3: Intercept and Modify Request

**Context**: Capture the multipart form-data request and alter the transaction[to] to an external wallet ID.

In Burp Suite, view the intercepted request. Change transaction[to] from internal ID (e.g., 1253440a8092adb7d95000001d) to external ID (e.g., 851cf4e552f31a99ce200001b). Preserve other parameters like transaction[from], transaction[amount], and transaction[notes].

### Step 4: Forward and Verify Transfer

**Context**: Submit the modified request to execute the bypass and confirm no 2FA is required.

Forward the request in Burp Suite. Monitor the response for success (200 OK with transfer confirmation). Check transaction history and external wallet for funds arrival.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- 2fa-bypass
- auth-bypass
- parameter-tampering
