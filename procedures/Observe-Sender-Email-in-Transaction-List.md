---
tags:
  - information-disclosure
  - email-collection
  - coinbase
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Android
  - Mobile
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Email Collection]]'
updated_at: '2025-12-14T17:24:41.995Z'
skill_level: novice
impact_level: medium
detection_risk: low
sub_techniques: []
id: f1e77ff5-16e9-46ee-bd08-133ae7e254c5
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Email Collection]]'
---
# Observe-Sender-Email-in-Transaction-List

## Summary

This procedure examines the recipient's transaction history in the Coinbase Android app to identify the unintended display of the sender's email address, confirming the privacy vulnerability.

## Description

After a transaction, the app's UI fails to anonymize the sender's email, violating Coinbase's policy against sharing such details. By navigating to the transactions view, the email is directly visible, allowing collection of personal information. This step validates the root cause: lack of redaction in the mobile UI. Outcomes include screenshot evidence of the disclosure for reporting.

## Requirements

1. Completed transaction from prior procedure
2. Access to recipient account in Coinbase Android app
3. Device capable of capturing screenshots for documentation

## Defense

Defensive measures and detection strategies:

- Redact or pseudonymize user emails in all transaction displays
- Conduct UI privacy audits and fuzz testing for data leaks
- Implement client-side data masking and server-side validation

## Objectives

1. Visually confirm sender email exposure
2. Document the privacy breach
3. Assess potential for further exploitation (e.g., social engineering)

## Instructions

### Step 1: Log In to Recipient Account

**Context**: Switch to the receiving account to access updated history.

In the Coinbase app, log out of sender if needed, log in to recipient, and ensure the app syncs recent transactions.

### Step 2: Navigate to Transactions

**Context**: Locate the specific incoming transaction.

Go to the 'Transactions' or 'Activity' tab, scroll to find the recent bitcoin receive from the sender account.

### Step 3: Inspect Details

**Context**: Observe and record the displayed sender information.

Tap the transaction for details; note the sender's email address shown in the UI (e.g., next to 'From' or user info). Capture a screenshot for verification.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Email Collection]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- information-disclosure
- email-collection
- coinbase
