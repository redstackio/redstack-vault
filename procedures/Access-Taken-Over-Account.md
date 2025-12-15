---
id: proc-uuid-5
name: Access Taken Over Account
tags:
  - account-takeover
  - data-access
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:33:34.276Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Access Taken Over Account

## Summary

This final procedure logs into the victim's Remitly account using the reset password, achieving full control and access to sensitive features.

## Description

Post-reset, the attacker sets a new password during the flow (if prompted) or uses the default. Logging in provides access to personal data, transaction history, and money transfer capabilities, enabling theft or further exploitation.

## Requirements

1. Successful reset from prior step
2. New password known
3. Victim's email

## Defense

Defensive measures and detection strategies:

- Notify users immediately on password resets with details
- Require additional verification (e.g., security questions) post-reset
- Monitor logins from unusual IPs post-reset events

## Objectives

1. Gain authenticated access to victim account
2. Verify control over sensitive functions
3. Exfiltrate data or perform actions like transfers

## Instructions

### Step 1: Log In

**Context**: Use new credentials.

Navigate to login page and enter victim's email + new password.

> No proxy needed; direct browser login.

### Step 2: Verify Access

**Context**: Check account features.

Access dashboard, view balances, attempt a small transfer.

> Success: Full navigation without blocks.

### Step 3: Document Control

**Context**: Confirm takeover.

Screenshot or note accessible data.

> Indicators: Personal info, funds visible.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[account-takeover]]
- [[data-access]]
