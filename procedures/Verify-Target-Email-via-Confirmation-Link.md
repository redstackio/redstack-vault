---
tags:
  - email-verification
  - auth-bypass
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Valid Accounts]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 01e14bfa-c1b1-4038-aaf4-495dc2cd18b8
created_at: '2025-12-11T06:10:40.581Z'
updated_at: '2025-12-11T06:10:40.581Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1078]]'
---
# Verify Target Email via Confirmation Link

## Summary

This procedure uses the obtained link to confirm the target email on the attacker's Shopify account.

## Description

Clicking the link verifies the email without needing access to the target's inbox, completing the bypass.

## Requirements

1. Verification link from email
2. Active Shopify session

## Defense

Defensive measures and detection strategies:

- Implement token-based verification checks
- Audit confirmation logs for mismatches

## Objectives

1. Associate target email with attacker account
2. Enable SSO integration

## Instructions

### Step 1: Access Confirmation Link

**Context**: Click to verify.

Access the link in the email, which confirms the target email on the attacker's Shopify instance.

> Confirmation should succeed without errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- email-verification
- auth-bypass
