---
id: proc-uuid-1
tags:
  - coinbase
  - vault-setup
  - business-logic
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - Coinbase Vault
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:28:20.299Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Create-Coinbase-Vault

## Summary

This procedure sets up a standard vault within a Coinbase account, preparing the environment for testing vault transfer functionalities and exploiting related business logic flaws.

## Description

In the context of Coinbase's cryptocurrency wallet, creating a vault adds a secure storage layer that requires multi-step approval for transfers. This step is foundational for attacks involving pending transfers, as it enables the initiation of vault-bound transactions without immediate fund locking. The target environment is the Coinbase web platform, requiring an active account with sufficient permissions. Expected outcomes include a fully operational vault ready for transfers, with no immediate impact on balances.

## Requirements

1. Active Coinbase account with login credentials
2. Web browser access to coinbase.com
3. No existing vaults (though multiple can be created)

## Defense

Defensive measures and detection strategies:

- Monitor account for unusual vault creations via Coinbase audit logs
- Implement rate limiting on vault setup to prevent abuse in testing scenarios

## Objectives

1. Establish a vault for transfer operations
2. Verify vault integration with main wallet
3. Prepare for pending transfer exploitation

## Instructions

### Step 1: Access Vault Creation Interface

**Context**: Log in to Coinbase and navigate to the wallet section to locate the vault creation option.

**Instructions**: Go to the Coinbase dashboard, select 'Wallets', and choose 'Create a vault' under the security features.

> Follow on-screen prompts to name the vault and set recovery options. No commands are executed; this is UI-driven.

### Step 2: Confirm Vault Setup

**Context**: Finalize the creation to ensure the vault is active.

**Instructions**: Review vault details and confirm creation.

> Upon success, the vault appears in the account overview, ready for use.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[coinbase]]
- [[vault-setup]]
- [[business-logic]]
