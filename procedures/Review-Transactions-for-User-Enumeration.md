---
id: proc-uuid-3
tags:
  - user-enumeration
  - information-disclosure
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:32:01.699Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Review-Transactions-for-User-Enumeration

## Summary

This procedure involves checking the Coinbase transactions page after sending money requests to various emails, exploiting inconsistent user display (full names for members vs. emails for non-members) to enumerate valid accounts and disclose personal information.

## Description

After replaying requests, the /transactions page lists them with varying detail levels: Coinbase members show full first and last names, while non-members appear as raw emails. This inconsistency allows attackers to infer account existence and harvest names without authentication. The attack relies on the prior rate limit bypass to send enough requests for meaningful enumeration.

## Requirements

1. Authenticated session with sent requests visible.
2. Access to https://coinbase.com/transactions.
3. List of tested emails for correlation.

## Defense

Defensive measures and detection strategies:

- Normalize user display to always show emails or require sender verification.
- Implement access controls to hide recipient details from senders.

## Objectives

1. Identify valid Coinbase users via display differences.
2. Disclose full names of enumerated members.
3. Compile a list of confirmed accounts for further abuse.

## Instructions

### Step 1: Navigate to Transactions Page

**Context**: View the list of recently sent money requests.

Go to https://coinbase.com/transactions.

**Expected Output**: Table or list showing pending requests with recipient info.

### Step 2: Observe Display Formats

**Context**: Compare how different recipients appear.

Look for entries: members display as "John Doe (john.doe@email.com)", non-members as "nonmember@email.com".

**Expected Output**: Clear distinction enabling yes/no on account existence.

### Step 3: Extract Names and Log Results

**Context**: Harvest disclosed information.

Note full names for member entries; mark emails as valid/invalid.

**Expected Output**: Spreadsheet or notes with enumerated users and names (e.g., first_name: John, last_name: Doe).

### Step 4: Validate Enumeration

**Context**: Confirm accuracy by testing known members/non-members.

Cross-check with known emails.

**Expected Output**: High success rate in distinguishing users.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- user-enumeration
- information-disclosure
