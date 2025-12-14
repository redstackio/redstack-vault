---
tags:
  - information-disclosure
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: low
impact_level: high
detection_risk: low
sub_techniques: []
id: abc731e3-87fd-4295-89ba-865d95258be9
created_at: '2025-12-14T17:28:51.744Z'
updated_at: '2025-12-14T17:28:51.744Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-Coinbase-Account-Dashboard-Without-Verification

## Summary

This procedure accesses the Coinbase account dashboard immediately after a bypassed login, exposing wallet transactions and balance without any additional authorization prompts.

## Description

Following the authentication bypass, the web application redirects to the dashboard, which displays sensitive financial data. The root cause is the lack of session validation post-login for certain mobile user-agents, resulting in unauthorized information disclosure.

## Requirements

1. Successful bypassed login from previous procedure
2. Active session in Windows Phone browser
3. Access to https://www.coinbase.com/dashboard

## Defense

Defensive measures and detection strategies:

- Require re-authentication for sensitive data views
- Log and alert on dashboard access from mobile devices without MFA confirmation
- Use client-side checks to enforce verification regardless of user-agent

## Objectives

1. View unauthorized wallet transactions
2. Expose account balance
3. Collect data for further exploitation

## Instructions

### Step 1: Observe Post-Login Redirect

**Context**: The application automatically loads the dashboard after login submission.

Wait for the redirect to the account dashboard.

> Transactions history and total balance are visible without barriers.

### Step 2: Review Exposed Data

**Context**: Inspect the disclosed information.

Scroll through the transactions list and note the balance.

> Data includes timestamps, amounts, and counterparties, enabling reconnaissance of user activity.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[information-disclosure]]
