---
tags:
  - information-disclosure
  - privacy-breach
  - coinbase
  - android
  - bitcoin
type: attack_chain
tools: []
tactics:
  - '[[Collection]]'
verified: false
platforms:
  - Android
  - Mobile
submitted: true
complexity: low
created_at: '2024-01-01T00:00:00Z'
procedures:
  - '[[procedures/Create-Multiple-Coinbase-Test-Accounts]]'
  - '[[procedures/Initiate-Bitcoin-Transaction-Between-Accounts]]'
  - '[[procedures/Observe-Sender-Email-in-Transaction-List]]'
step_count: 3
techniques:
  - '[[Email Collection]]'
updated_at: '2025-12-14T17:24:42.026Z'
description: >-
  Demonstrates information disclosure vulnerability in Coinbase Android app
  where sender's email is revealed in recipient's transaction history, breaching
  privacy.
skill_level: novice
impact_level: medium
id: 8fd81850-687d-4bef-bb1f-06be1b434cd0
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Email Collection]]'
---
# Email Disclosure via Bitcoin Transactions in Coinbase Android App

Multi-stage attack chain demonstrating a complete attack workflow to exploit an information disclosure vulnerability in the Coinbase Android app.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~5 minutes |
| Skill Level | Novice |
| Complexity | Low |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Create Test Accounts] --> B[Initiate Transaction]
    B --> C[View Transaction Details]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
```

## Prerequisites & Requirements

### Required Tools

- Android device or emulator with Coinbase app installed
- Multiple unique email addresses for account creation

### Target Environment

- Coinbase Android app (version affected by the vulnerability)
- Internet access for app registration and transactions
- No specific services/ports required beyond app connectivity

### Initial Access Requirements

- No prior credentials needed; accounts are created fresh
- Local device access to the Android app
- Basic knowledge of cryptocurrency transactions

## Detailed Attack Procedures

### Step 1: Create Test Accounts
procedure: [[procedures/Create-Multiple-Coinbase-Test-Accounts]]

**Objective**: Establish sender and recipient accounts to simulate a transaction and test the disclosure.

**Instructions**: Install the Coinbase app on an Android device. Use unique email addresses to register at least two accounts, completing any verification steps required for basic functionality.

**Expected Output**: Two functional Coinbase accounts linked to distinct emails, ready for transactions.

**Success Indicators**:
- Accounts successfully registered and logged in
- Email addresses associated but not yet exposed

### Step 2: Initiate Transaction
procedure: [[procedures/Initiate-Bitcoin-Transaction-Between-Accounts]]

**Objective**: Perform a small bitcoin transfer from sender to recipient to trigger the transaction history update.

**Instructions**: Log in to the sender account in the Coinbase app. Navigate to the send feature, select bitcoin, enter the recipient's account address or scan QR code, and send a minimal amount (e.g., equivalent to $1) to avoid fees or limits.

**Expected Output**: Transaction confirmation in the sender's history; pending or confirmed in recipient's.

**Success Indicators**:
- Transaction sent successfully
- No errors in transfer process

### Step 3: Observe Disclosure
procedure: [[procedures/Observe-Sender-Email-in-Transaction-List]]

**Objective**: Inspect the recipient's transaction list to reveal the sender's email address.

**Instructions**: Switch to the recipient account in the app. Go to the transactions section and locate the incoming bitcoin transaction. Note the display of the sender's email alongside the details.

**Expected Output**: Sender's email visibly shown in the UI next to the transaction.

**Success Indicators**:
- Email address exposed in transaction view
- Confirmation of privacy policy violation

## Attack Chain Summary

### Key Achievements

1. Successful creation of test accounts without exposure
2. Execution of a transaction that inadvertently discloses sender info
3. Direct observation of email in recipient's app UI, enabling potential targeting

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Email Collection]]

### MITRE ATT&CK Tactics

- [[Collection]]

---
*Last updated: 2024-01-01T00:00:00Z*
