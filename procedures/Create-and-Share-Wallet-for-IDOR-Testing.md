---
tags:
  - setup
  - web
  - wallet
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:23.436Z'
sub_techniques: []
id: f5c94918-cb8d-4565-94d5-06cd111f7121
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-and-Share-Wallet-for-IDOR-Testing

## Summary

This procedure sets up a shared wallet in the Enter wallet application by creating a new wallet as the owner and granting access to multiple other users, preparing the environment for testing IDOR vulnerabilities in the sharing deletion feature.

## Description

In the context of exploiting an IDOR in the wallet sharing system, this initial setup involves logging in as the wallet owner (User A), creating a test wallet, and sharing it with additional users (B and C). This establishes the necessary shared state where unauthorized deletion can be tested. The procedure assumes access to the web-based Enter wallet app at wallet.romit.io and valid user credentials. Expected outcomes include confirmed shares visible to all parties, setting the stage for access control bypass demonstrations.

## Requirements

1. Valid login credentials for the wallet owner account (User A).
2. Access to at least two additional user accounts (Users B and C) for sharing.
3. Web browser with JavaScript enabled to interact with the dashboard.

## Defense

Defensive measures and detection strategies:

- Implement role-based access controls (RBAC) to ensure only owners can manage shares.
- Log all sharing actions with user IDs for anomaly detection, alerting on deletions by non-owners.

## Objectives

1. Create a new wallet owned by User A.
2. Share the wallet with Users B and C to simulate collaborative access.
3. Verify share establishment to confirm setup success.

## Instructions

### Step 1: Login and Create Wallet

**Context**: Authenticate as the owner and initiate wallet creation to establish ownership.

Log in to https://wallet.romit.io/dashboard using User A's credentials. Navigate to the wallet creation section and create a new wallet named 'BITCOINS' with default settings.

> Upon success, the wallet appears in the dashboard with User A as owner.

### Step 2: Share Wallet with Other Users

**Context**: Grant access to additional users to create the shared state vulnerable to IDOR exploitation.

In the wallet's sharing settings, enter the bankUserIds or emails for User B and User C. Submit the share request and confirm via any required notifications.

> Expected output: Share confirmations sent, and Users B and C gain view access to 'BITCOINS'.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[setup]]
- [[web]]
- [[wallet]]
