---
id: proc-deploy-faulty-distributor-001
tags:
  - smart-contract
  - deployment
  - solidity
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Blockchain
  - Ethereum
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Windows Command Shell]]'
updated_at: '2025-12-14T17:28:36.512Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Windows Command Shell]]'
---
# Deploy Smart Contract with Valid and Faulty Coinbase Wallets

## Summary

This procedure deploys a Solidity smart contract on Ethereum designed to distribute ETH to a list of recipient wallets, including multiple valid Coinbase-associated addresses followed by a deliberately faulty one that triggers a revert, exploiting partial credit logic.

## Description

In the context of the Coinbase Ethereum receiving vulnerability, this procedure sets up the core exploit component: a distributor contract that attempts ETH transfers in sequence. Valid transfers to Coinbase wallets are credited immediately by Coinbase's monitoring, but the final revert rolls back the entire transaction on the blockchain, leaving no net ETH transfer while accumulating credits. Prerequisites include basic Solidity knowledge and an Ethereum wallet for deployment.

## Requirements

1. Ethereum development IDE (e.g., Remix)
2. Wallet with ETH for gas fees (e.g., MetaMask with at least 0.01 ETH)
3. List of valid Coinbase Ethereum wallet addresses (attacker-controlled)
4. Ethereum network access (mainnet for real exploit)

## Defense

Defensive measures and detection strategies:

- Monitor for unusual patterns of reverting transactions targeting exchange wallets
- Implement full transaction success verification before crediting balances
- Use blockchain analytics to detect iterative failing distributions

## Objectives

1. Deploy a functional distributor contract
2. Ensure faulty recipient causes reliable reverts
3. Prepare for ETH distribution without net transfer

## Instructions

### Step 1: Write the Distributor Contract

**Context**: Create the main contract logic for sequential ETH transfers.

Use Remix IDE to author the Solidity code:

```solidity
pragma solidity ^0.8.0;

contract Distributor {
    function distribute(address[] calldata recipients) external payable {
        require(msg.value > 0, "Must send ETH");
        uint amount = msg.value / recipients.length;
        for (uint i = 0; i < recipients.length; i++) {
            payable(recipients[i]).transfer(amount);
        }
    }
}
```

> This contract divides sent ETH equally among recipients. Expected: Compilation success without errors.

### Step 2: Create Faulty Recipient Contract

**Context**: Deploy a separate contract that always reverts on receive to trigger rollback.

In Remix, create and deploy:

```solidity
pragma solidity ^0.8.0;

contract FaultyRecipient {
    receive() external payable {
        revert("Deliberate failure");
    }
}
```

> Deploy this first and note its address. Expected: Deployment tx confirmed, but transfers to it will fail.

### Step 3: Deploy Distributor

**Context**: Compile and deploy the distributor using your wallet.

In Remix, select compiler 0.8.x, compile, and deploy to network via injected provider (MetaMask). Pay gas fees.

> Expected: Transaction receipt with contract address.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Windows Command Shell]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[smart-contract]]
- [[deployment]]
- [[solidity]]
