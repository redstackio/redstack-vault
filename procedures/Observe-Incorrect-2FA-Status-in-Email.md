---
tags:
  - business-logic
  - misleading
  - 2fa
type: procedure
tools: []
tactics: []
commands: []
platforms:
  - Web
  - Email
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: low
impact_level: low
detection_risk: low
sub_techniques: []
id: 3dffdcf3-2fd5-4ec3-b3be-c63f3c158639
created_at: '2025-12-14T17:24:45.441Z'
updated_at: '2025-12-14T17:24:45.441Z'
verified: false
validated: true
submitted: true
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Observe-Incorrect-2FA-Status-in-Email

## Summary

This procedure verifies the business logic error by analyzing the email's false claim about 2FA status.

## Description

The email template's conditional (if (services.u2f) ...) fails to check enablement, leading to incorrect messaging. Compare email to actual account state. Outcome: Confirmed vulnerability causing confusion.

## Requirements

1. Received notification email
2. Access to Legal Robot account settings

## Defense

Defensive measures and detection strategies:

- Implement unit tests for email logic
- User feedback loops for notification accuracy
- Regular code reviews for conditional statements

## Objectives

1. Detect false 2FA enabled claim
2. Correlate with account reality
3. Document impact on user trust

## Instructions

### Step 1: Compare Email to Settings

**Context**: Cross-check claims.

Read email's security key reference; verify settings show no U2F and 2FA off.

### Step 2: Note Discrepancy

**Context**: Record the error.

Screenshot or log the misleading text for reporting.

## MITRE ATT&CK Mapping

### Tactics


### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[business-logic]]
- [[misleading]]
- [[2fa]]
