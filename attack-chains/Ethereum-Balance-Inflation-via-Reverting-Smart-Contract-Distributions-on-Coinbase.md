---
id: ac-coinbase-eth-inflation-001
tags:
  - blockchain
  - ethereum
  - smart-contract
  - business-logic
  - coinbase
  - balance-inflation
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Blockchain
  - Web
  - Ethereum
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Deploy-Smart-Contract-with-Valid-and-Faulty-Coinbase-Wallets]]'
  - '[[procedures/Fund-the-Smart-Contract-with-ETH]]'
  - '[[procedures/Execute-Smart-Contract-Distribution-Causing-Revert]]'
  - '[[procedures/Repeat-Failing-Transactions-to-Inflate-Balance]]'
  - '[[procedures/Withdraw-Inflated-Balance-to-External-Wallet]]'
step_count: 5
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:36.513Z'
description: >-
  A business logic exploit in Coinbase's Ethereum receiving code that credits
  partial ETH transfers from failing smart contracts, allowing attackers to
  inflate account balances without actual fund transfers.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Ethereum Balance Inflation via Reverting Smart Contract Distributions on Coinbase

Multi-stage attack chain demonstrating a business logic vulnerability in Coinbase's Ethereum ETH receiving code, where partial credits from reverting smart contract transactions allow arbitrary balance inflation and unauthorized withdrawals.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~30 minutes per iteration |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Deploy Smart Contract] --> B[Fund Contract]
    B --> C[Execute Distribution with Revert]
    C --> D[Repeat for Inflation]
    D --> E[Withdraw Funds]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Ethereum development environment (e.g., Remix IDE or Hardhat)
- Wallet with ETH for funding (e.g., MetaMask)

### Target Environment

- Ethereum mainnet or testnet
- Coinbase account with associated Ethereum wallet addresses
- Access to deploy and interact with smart contracts

### Initial Access Requirements

- Valid Coinbase Ethereum wallet addresses (attacker's own or controlled)
- Sufficient ETH in attacker's wallet to fund contracts
- Knowledge of Solidity for contract deployment

## Detailed Attack Procedures

### Step 1: Deploy Smart Contract
procedure: [[procedures/Deploy-Smart-Contract-with-Valid-and-Faulty-Coinbase-Wallets]]

**Objective**: Create a smart contract that distributes ETH to multiple valid Coinbase wallets followed by a faulty one that causes a revert.

**Instructions**: Use an Ethereum IDE like Remix to write and deploy a Solidity contract. The contract should include a function to transfer ETH to a list of addresses, with the last address being a faulty contract that always reverts (e.g., via require(false)). Compile and deploy the contract to the Ethereum network using your wallet.

Example Solidity snippet:

```solidity
contract Distributor {
    function distribute(address[] calldata recipients) external payable {
        for (uint i = 0; i < recipients.length; i++) {
            payable(recipients[i]).transfer(msg.value / recipients.length);
        }
    }
}

// Faulty recipient contract
contract Faulty {
    receive() external payable {
        require(false, "Revert always");
    }
}
```

**Expected Output**: Contract deployed with address logged in the transaction receipt.

**Success Indicators**:
- Contract deployment transaction confirmed on blockchain explorer (e.g., Etherscan)
- Faulty recipient contract address created and verified to revert transfers

### Step 2: Fund the Smart Contract
procedure: [[procedures/Fund-the-Smart-Contract-with-ETH]]

**Objective**: Send sufficient ETH to the smart contract to cover intended partial distributions.

**Instructions**: From your Ethereum wallet (e.g., MetaMask), send ETH to the deployed contract address. Calculate the amount based on the number of valid recipients (e.g., 0.1 ETH for 3 valid wallets at 0.03 ETH each, plus buffer for gas). Use the wallet interface or a tool like MyEtherWallet to execute the transfer.

**Expected Output**: Transaction hash confirming ETH transfer to contract.

**Success Indicators**:
- Contract balance updated on Etherscan
- ETH deducted from attacker's wallet

### Step 3: Execute Distribution
procedure: [[procedures/Execute-Smart-Contract-Distribution-Causing-Revert]]

**Objective**: Trigger the distribution function, crediting partial transfers to Coinbase wallets before the revert rolls back the blockchain state.

**Instructions**: Interact with the contract via Remix or Etherscan's contract interface. Call the distribute function with an array of addresses: multiple valid Coinbase wallets followed by the faulty one. Specify the ETH amount to distribute. The transaction will revert due to the faulty wallet, but Coinbase will credit the partial sends.

**Expected Output**: Transaction reverts on blockchain, but Coinbase balance shows increase for valid wallets.

**Success Indicators**:
- Blockchain explorer shows revert status
- Coinbase dashboard reflects credited ETH in targeted wallets

### Step 4: Repeat Transactions
procedure: [[procedures/Repeat-Failing-Transactions-to-Inflate-Balance]]

**Objective**: Iteratively execute the failing distribution to accumulate inflated credits on Coinbase.

**Instructions**: Redeploy or reuse the contract setup, funding and executing multiple times (e.g., 10-20 iterations) until the desired balance inflation is achieved. Monitor Coinbase balances after each transaction to track accumulation.

**Expected Output**: Progressive increase in Coinbase ETH balance without corresponding blockchain transfers.

**Success Indicators**:
- Total inflated balance exceeds initial funding
- No actual ETH loss on attacker's blockchain wallet

### Step 5: Withdraw Funds
procedure: [[procedures/Withdraw-Inflated-Balance-to-External-Wallet]]

**Objective**: Cash out the inflated balance from Coinbase to an external wallet, realizing the exploit.

**Instructions**: Log into Coinbase, navigate to the withdrawal section, and transfer the inflated ETH to an attacker-controlled external wallet (e.g., non-Coinbase Ethereum address). Confirm the transaction and monitor for approval.

**Expected Output**: ETH withdrawn from Coinbase to external wallet.

**Success Indicators**:
- Withdrawal transaction successful
- Funds appear in external wallet on blockchain

## Attack Chain Summary

### Key Achievements

1. Deployed custom smart contract exploiting partial credit logic
2. Inflated Coinbase balances via repeated reverting transactions
3. Withdrew unauthorized funds, causing financial loss to Coinbase

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Windows Command Shell]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]

---
*Last updated: 2023-10-01T00:00:00Z*
