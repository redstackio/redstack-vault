---
tags:
  - account-creation
  - insider-threat
type: procedure
tools: []
tactics:
  - '[[Persistence]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Valid Accounts]]'
skill_level: low
impact_level: medium
detection_risk: low
sub_techniques:
  - '[[T1078.004]]'
id: 13bd2f7a-f792-4ab3-abd0-76ef5521cf62
created_at: '2025-12-11T06:10:15.700Z'
updated_at: '2025-12-11T06:10:15.700Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0003]]'
mitre_techniques:
  - '[[T1078]]'
---
# Create Sockpuppet Account

## Summary

This procedure covers creating an alternate platform account to disguise identity while submitting stolen data, avoiding links to the primary employee profile.

## Description

The attacker registers a new account under a handle like 'rzlr' to resubmit vulnerabilities without traceability, leveraging platform features for anonymity.

## Requirements

1. Access to the public platform registration
2. Unique email or credentials not tied to primary identity
3. Knowledge of platform account policies

## Defense

Defensive measures and detection strategies:

- Monitor for duplicate IP or device usage across accounts
- Require identity verification for accounts

## Objectives

1. Establish anonymous submission channel
2. Prevent linkage to insider identity
3. Enable fraudulent submissions

## Instructions

### Step 1: Register New Account

**Context**: Use platform signup to create an alternate profile.

> Choose a handle like 'rzlr' and complete verification.

### Step 2: Verify and Test Account

**Context**: Ensure the account can submit reports without issues.

> Test basic functionality to confirm anonymity.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques

- [[T1078.004]]

## Commands Used



## Tools Used



## Tags

- [[account-creation]]
- [[insider-threat]]
