---
tags:
  - business-logic
  - license-management
  - verification
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Manipulation]]'
updated_at: '2025-12-14T17:28:36.290Z'
skill_level: basic
impact_level: medium
detection_risk: low
sub_techniques: []
id: 17c12238-477b-471f-a631-ba79489e2bfc
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Account Manipulation]]'
---
# Verify-License-Modifications

## Summary

This procedure checks the license management page post-purchase to confirm the business logic flaw's effects, such as reduced user seats and extended expiry dates.

## Description

After purchasing a new license, revisit the PortSwigger license view page to inspect changes. The root cause is incorrect handling of new purchases against existing ones, resulting in modifications like dropping user count to 1 while extending expiry to the new term. This step validates the impact in a web environment with an authenticated session.

## Requirements

1. Recently completed license purchase
2. Access to license viewing page
3. Baseline notes from existing license

## Defense

Defensive measures and detection strategies:

- Implement atomic transactions for license updates
- Log all license attribute changes with user context
- Require manual approval for multi-license modifications

## Objectives

1. Observe downgrade in user seats on existing license
2. Confirm unauthorized expiry extension
3. Document the flawed state for reporting

## Instructions

### Step 1: Return to License Page

**Context**: Reload the management interface to reflect changes.

Navigate back to the license section (e.g., https://portswigger.net/support/licensing) and refresh the page.

### Step 2: Compare License Details

**Context**: Check for anomalies against pre-purchase baseline.

Review existing license: expect user count reduced (e.g., to 1) and expiry extended (e.g., to 5 years from now). Note new license details as well.

**Expected Output**: Updated display showing modified user count and expiry dates.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Account Manipulation]] Account Manipulation

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[business-logic]]
- [[license-management]]
- [[verification]]
