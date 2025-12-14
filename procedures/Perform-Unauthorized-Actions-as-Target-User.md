---
tags:
  - account-takeover
  - unauthorized-payment
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
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:32:57.947Z'
skill_level: intermediate
impact_level: critical
detection_risk: high
sub_techniques: []
id: 665b592b-8a58-4f22-a3db-d0515daba18c
validated: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Perform Unauthorized Actions as Target User

## Summary

As compromised account (marten.mickos), manipulate transactions to pay pending bounties.

## Description

Post-takeover, load transactions for 05/2020 and execute payments, demonstrating full control.

## Requirements

1. Target session
2. Access to payment features

## Defense

Defensive measures: Multi-factor for high-value actions, audit logs; Detection: Alert on unusual payment patterns.

## Objectives

1. Access transactions
2. Execute unauthorized pays
3. Expected outcome: Bounties disbursed

## Instructions

### Step 1: Load Transactions

**Context**: View pending items.

Navigate to transactions/05/2020.

> Expected output: List of bounties.

### Step 2: Pay Bounties

**Context**: Confirm actions.

Select and pay all pending.

> Expected output: Payments processed.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion]] Defense Evasion (impact phase)

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques

- None

## Commands Used


## Tools Used


## Tags

- account-takeover
- unauthorized-payment
