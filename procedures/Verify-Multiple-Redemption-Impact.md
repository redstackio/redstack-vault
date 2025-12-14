---
tags:
  - verification
  - impact
  - balance
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:22.967Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
id: 5ae1f283-2c7d-46dc-9077-65121319f584
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Verify-Multiple-Redemption-Impact

## Summary

This procedure checks the account balance post-exploitation to confirm the success of multiple gift card redemptions, quantifying the unauthorized credits gained.

## Description

After executing concurrent requests, navigate to the account section to view Reverb bucks. For a $25 card redeemed 7 times, expect $175 in credits. This validates the race condition's impact, enabling free purchases and demonstrating financial loss to the platform. Prerequisites: Completed exploitation step.

## Requirements

1. Active Reverb session post-attack
2. Access to account balance page

## Defense

Defensive measures and detection strategies:

- Audit logs for redemption events and balance changes
- Alert on sudden balance increases disproportionate to purchases

## Objectives

1. Confirm credit multiplication
2. Assess exploit success
3. Document impact for reporting

## Instructions

### Step 1: Check Account Balance

**Context**: Review Reverb bucks after attack.

Log in and navigate to the wallet or balance section.

**Expected Output**: Balance shows e.g., $175 from $25 card.

### Step 2: Test Purchases

**Context**: Validate usability of credits.

Attempt a small purchase using the excess credits.

**Expected Output**: Purchase succeeds without additional payment.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- verification
- impact
