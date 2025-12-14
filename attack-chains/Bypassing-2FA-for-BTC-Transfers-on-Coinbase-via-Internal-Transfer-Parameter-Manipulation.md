---
tags:
  - 2fa-bypass
  - auth-bypass
  - coinbase
  - btc-transfer
  - parameter-tampering
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Bypass-Coinbase-2FA-via-Internal-Transfer-Manipulation]]'
step_count: 5
techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:47.733Z'
description: >-
  A multi-step attack exploiting Coinbase's internal transfer feature to bypass
  2FA requirements for external BTC transfers by modifying HTTP request
  parameters.
skill_level: intermediate
impact_level: high
id: 7663b43e-a75f-46f2-970e-1d396506d5a9
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
---
# Bypassing 2FA for BTC Transfers on Coinbase via Internal Transfer Parameter Manipulation

Multi-stage attack chain demonstrating a complete attack workflow exploiting Coinbase's internal transfer mechanism to bypass 2FA for external wallet transfers.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Setup 2FA and Wallets] --> B[Initiate Internal Transfer]
    B --> C[Intercept and Modify Request]
    C --> D[Execute External Transfer]
    D --> E[Fund Exfiltration]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]

### Target Environment

- Web platform (Coinbase account with BTC wallets)
- Required services: Coinbase API for wallet transfers
- Network access requirements: Valid Coinbase login session

### Initial Access Requirements

- Existing Coinbase account credentials
- Network position: Direct access to Coinbase web interface
- Prior access needed: Account login to manage wallets

## Detailed Attack Procedures

### Step 1: Enable 2FA and Create Second Wallet
procedure: [[procedures/Bypass-Coinbase-2FA-via-Internal-Transfer-Manipulation]]

**Objective**: Prepare the account by enabling 2FA for transfers and setting up multiple internal wallets to simulate an internal transfer.

**Instructions**: Log in to your Coinbase account, navigate to security settings, and enable 2FA specifically for BTC transfers. Then, create a second BTC wallet via the Manage Accounts page at https://coinbase.com/accounts.

**Expected Output**: 2FA enabled confirmation and a new wallet listed under accounts.

**Success Indicators**:
- 2FA prompt appears for test transfers
- Second wallet ID visible in DOM (e.g., data-wallet-id="53440a8092adb7d95000001d")

### Step 2: Initiate Internal Transfer and Intercept Request
procedure: [[procedures/Bypass-Coinbase-2FA-via-Internal-Transfer-Manipulation]]

**Objective**: Start an internal BTC transfer to capture the legitimate HTTP request structure using Burp Suite.

**Instructions**: Select the source wallet as 'From', choose the second internal wallet as 'To', enter a small amount (e.g., 0.1 BTC), add optional notes, and click Transfer. Configure Burp Suite as a proxy to intercept the POST request to /accounts/transfer_money, which contains multipart form-data including transaction[from], transaction[to], transaction[amount], and transaction[notes].

**Expected Output**: Intercepted POST request with internal wallet IDs.

**Success Indicators**:
- Request captured showing internal transaction[to] value
- No 2FA prompted yet due to internal nature

### Step 3: Modify the Transaction To Parameter
procedure: [[procedures/Bypass-Coinbase-2FA-via-Internal-Transfer-Manipulation]]

**Objective**: Alter the request to target an external wallet by replacing the internal ID with an external MongoDB BSON ID.

**Instructions**: In Burp Suite, edit the transaction[to] parameter from the internal wallet ID (e.g., 1253440a8092adb7d95000001d) to an external target ID (e.g., 851cf4e552f31a99ce200001b). External IDs can be obtained from the DOM or known wallet addresses converted to BSON format.

**Expected Output**: Modified request with external transaction[to] value.

**Success Indicators**:
- Parameter changed without breaking request format
- Request remains valid multipart form-data

### Step 4: Forward the Modified Request
procedure: [[procedures/Bypass-Coinbase-2FA-via-Internal-Transfer-Manipulation]]

**Objective**: Submit the tampered request to execute the transfer to the external wallet without triggering 2FA.

**Instructions**: Forward the modified POST request in Burp Suite to the server. The backend will process it as an internal transfer, skipping 2FA validation.

**Expected Output**: Transfer confirmation without 2FA prompt; funds moved to external wallet.

**Success Indicators**:
- No 2FA code requested
- Transaction history shows transfer to external address

### Step 5: Verify Fund Exfiltration
procedure: [[procedures/Bypass-Coinbase-2FA-via-Internal-Transfer-Manipulation]]

**Objective**: Confirm the bypass success by checking the transfer outcome and potential fund theft.

**Instructions**: Review the Coinbase transaction history and external wallet balance to verify the BTC arrival without 2FA intervention.

**Expected Output**: Successful transfer logged, funds in external wallet.

**Success Indicators**:
- BTC transferred externally
- No security alerts or 2FA enforcement

## Attack Chain Summary

### Key Achievements

1. Enabled 2FA setup to confirm bypass necessity
2. Intercepted and manipulated internal transfer request
3. Executed external transfer without authentication
4. Demonstrated potential for complete fund theft

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]]
- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---

*Last updated: 2023-10-01T00:00:00Z*
