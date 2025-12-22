---
id: proc-coinbase-access-info-001
tags:
  - information-disclosure
  - web
  - ios
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
  - iOS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:28:52.121Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Access-Account-Information-in-Coinbase

## Summary

Following the authentication bypass, this procedure allows viewing of sensitive account details like transaction history and wallet balance directly on the dashboard without any additional authorization.

## Description

Once logged in via the iOS browser bypass, the Coinbase dashboard loads unrestricted, exposing personal financial data. This includes full transaction logs and current balances, which would normally require verified sessions. The procedure highlights the information disclosure risk from the flawed login flow, enabling attackers to assess account value and plan further actions.

## Requirements

1. Successful completion of iOS browser login bypass
2. Active session in iOS browser
3. No additional tools needed

## Defense

Defensive measures and detection strategies:

- Session validation checks post-login across all endpoints
- Rate limiting and anomaly detection on dashboard access from mobile agents
- Encrypt and log sensitive data access attempts

## Objectives

1. Disclose transaction history and wallet details
2. Evaluate account sensitivity for escalation
3. Confirm persistence of unauthorized access

## Instructions

### Step 1: Observe Dashboard Load

**Context**: After login, the dashboard automatically displays account information without prompts.

No command required; simply view the loaded page content.

> The page shows transactions and balance totals, indicating successful disclosure.

### Step 2: Review Sensitive Data

**Context**: Scroll and interact with dashboard elements to access full details.

No command required; navigate UI elements to view history.

> Detailed transaction records and balance are visible and accessible.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- information-disclosure
- web
- ios
