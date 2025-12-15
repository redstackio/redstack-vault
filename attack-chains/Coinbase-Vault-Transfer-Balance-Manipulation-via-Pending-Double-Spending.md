---
tags:
  - business-logic
  - double-spending
  - cryptocurrency
  - coinbase
  - vault
  - balance-manipulation
type: attack_chain
tools: []
tactics:
  - '[[Impact]]'
verified: false
platforms:
  - Web
  - Bitcoin (BTC)
  - Coinbase Vault
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Create-Coinbase-Vault]]'
  - '[[procedures/Initiate-Pending-Vault-Transfer]]'
  - '[[procedures/Execute-Concurrent-External-Transfer]]'
  - '[[procedures/Approve-Vault-Transfer-for-Negative-Balance]]'
step_count: 4
techniques:
  - '[[Data Manipulation]]'
  - '[[Stored Data Manipulation]]'
updated_at: '2025-12-14T17:28:20.302Z'
description: >-
  A business logic vulnerability in Coinbase's vault transfer feature allows
  double-spending by initiating a pending vault transfer without locking funds,
  enabling concurrent external withdrawals and resulting in negative balances
  upon approval.
skill_level: intermediate
impact_level: high
id: d5dc804a-209e-415b-98f7-7657afdeef3e
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Data Manipulation]]'
  - '[[Stored Data Manipulation]]'
---
# Coinbase Vault Transfer Balance Manipulation via Pending Double-Spending

Multi-stage attack chain demonstrating a business logic flaw in Coinbase's vault transfer feature, enabling double-spending of cryptocurrency funds during the pending approval state.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Create Vault] --> B[Initiate Pending Transfer]
    B --> C[Concurrent External Transfer]
    C --> D[Approve Vault Transfer]
    D --> E[Negative Balance Achieved]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (UI-based via Coinbase web interface)

### Target Environment

- Coinbase web platform
- Active Coinbase account with BTC balance
- Access to external BTC wallet for receiving funds

### Initial Access Requirements

- Valid Coinbase account credentials
- Sufficient BTC balance in main wallet
- No prior vault setup required

## Detailed Attack Procedures

### Step 1: Create Vault
procedure: [[procedures/Create-Coinbase-Vault]]

**Objective**: Set up a standard vault in the Coinbase account to enable transfer functionality.

**Instructions**: Navigate to the vault creation feature in the Coinbase wallet interface and follow the prompts to create a new vault.

**Expected Output**: A new vault is created and visible in the account dashboard.

**Success Indicators**:
- Vault appears in the account overview
- Vault status shows as active and ready for transfers

### Step 2: Initiate Pending Vault Transfer
procedure: [[procedures/Initiate-Pending-Vault-Transfer]]

**Objective**: Start a transfer from the main wallet to the vault, placing it in a pending approval state without locking the funds.

**Instructions**: In the Coinbase wallet interface, select the main wallet balance (e.g., BTC), choose the vault as the destination, enter the transfer amount, and confirm to initiate. The transfer will enter a pending state lasting a few minutes.

**Expected Output**: Transfer shows as pending in the transaction history; main wallet balance remains unchanged and available.

**Success Indicators**:
- Pending transfer notification appears
- Main wallet balance is still fully accessible for other actions

### Step 3: Execute Concurrent External Transfer
procedure: [[procedures/Execute-Concurrent-External-Transfer]]

**Objective**: While the vault transfer is pending, send the same funds to an external BTC wallet, exploiting the lack of balance locking.

**Instructions**: With the pending vault transfer active, immediately initiate a new transfer from the main wallet using the same amount to an external BTC address. Confirm the external transfer.

**Expected Output**: External transfer processes successfully; funds are sent to the external wallet.

**Success Indicators**:
- External transfer completes without errors
- Main wallet balance deducts for the external transfer but remains usable

### Step 4: Approve Vault Transfer for Negative Balance
procedure: [[procedures/Approve-Vault-Transfer-for-Negative-Balance]]

**Objective**: Approve the pending vault transfer, causing the main wallet to deduct the amount twice and result in a negative balance.

**Instructions**: Return to the pending vault transfer in the Coinbase interface and approve it. Observe the balance update.

**Expected Output**: Vault transfer completes; main wallet balance goes negative due to double deduction.

**Success Indicators**:
- Vault receives the funds
- Main wallet shows negative balance
- Potential for unauthorized withdrawals beyond original funds

## Attack Chain Summary

### Key Achievements

1. Successful creation of a vault for transfer testing
2. Exploitation of pending state to enable double-spending
3. Achievement of negative balance, demonstrating balance manipulation
4. Highlight of business logic flaw allowing unauthorized fund extraction

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Data Manipulation]] Data Manipulation
- [[Stored Data Manipulation]] Stored Data Manipulation

### MITRE ATT&CK Tactics

- [[Impact]] Impact

---

*Last updated: 2023-10-01T00:00:00Z*
