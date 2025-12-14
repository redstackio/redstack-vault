---
id: proc-coinbase-withdrawal-16696-4
tags:
  - cryptocurrency-theft
  - fund-exfiltration
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
  - '[[Data from Cloud Storage]]'
updated_at: '2025-12-14T17:24:45.400Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Data from Cloud Storage]]'
---
# Execute-Fraudulent-Bitcoin-Withdrawals-on-Coinbase

## Summary

This procedure performs unauthorized Bitcoin withdrawals on a taken-over Coinbase account, exploiting the absence of post-2FA-change safeguards to move funds up to the daily limit immediately.

## Description

With control over 2FA, attackers authenticate and initiate withdrawals to external wallets, targeting the cryptocurrency exchange's web interface. The attack leverages the $1,000 daily limit, splitting into multiple transactions. This scenario assumes full account access post-2FA switch. Outcomes include financial loss, with no platform interventions like IP checks or delays.

## Requirements

1. Full authenticated access to Coinbase account
2. Intercepted SMS for transaction verifications
3. Attacker-controlled Bitcoin wallet addresses

## Defense

Defensive measures and detection strategies:

- Enforce withdrawal delays or secondary confirmations after 2FA changes
- Implement IP whitelisting and device binding for high-value transactions
- Use real-time monitoring for unusual withdrawal patterns

## Objectives

1. Transfer funds out of the compromised account
2. Maximize theft within daily limits
3. Complete actions before detection

## Instructions

### Step 1: Authenticate Account Session

**Context**: Log in and verify control using SMS codes.

Access Coinbase dashboard and confirm 2FA with an intercepted code.

> Ensure session is active without errors.

### Step 2: Initiate Withdrawals

**Context**: Set up and execute transfers to attacker wallets.

Navigate to withdrawal section, select Bitcoin, enter amounts (e.g., $666.28 first), and provide wallet address; verify with SMS.

> Repeat for second transaction ($333.17) to approach limit.

### Step 3: Confirm and Monitor

**Context**: Ensure transactions process without interruption.

Submit and watch for completion, noting no freezes occur.

> Expected output: Funds transferred, totaling $999.45 in Bitcoin.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Data from Cloud Storage]] Data from Cloud Storage Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[cryptocurrency-theft]]
- [[fund-exfiltration]]
