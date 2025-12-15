---
id: proc-redeem-rewards-1070510
tags:
  - reward-abuse
  - financial-impact
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Collection]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:36.343Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Redeem-Unlimited-Rewards

## Summary

This procedure redeems Prime-only rewards from the Streamlabs All Stars system using the API bypass, allowing unlimited claims of items like $30 Logitech gaming mouse coupons via email delivery.

## Description

With the tampered response enabling the UI, the redemption flow proceeds without server validation, sending coupons to any provided email. This can be scaled with multiple accounts for mass abuse, leading to significant financial losses for Streamlabs partners like Logitech.

## Requirements

1. Unlocked rewards page via prior bypass
2. Disposable email service (e.g., for HackerOne reporting)
3. Active proxied session

## Defense

Defensive measures and detection strategies:

- Tie redemptions to verified subscriptions with backend checks
- Limit redemptions per account and monitor for bulk patterns
- Partner with email providers to flag suspicious volumes

## Objectives

1. Claim high-value reward without payment
2. Receive deliverable coupon code
3. Highlight scalability for abuse

## Instructions

### Step 1: Select Reward

**Context**: Choose a Prime-eligible item from the catalog.

On the rewards page, select a Logitech gaming mouse or similar high-value option.

### Step 2: Enter Email and Redeem

**Context**: Provide details to trigger the backend redemption.

Input an email address (e.g., a temporary alias) and click the 'redeem' button.

**Expected Output**: Success message; check email for coupon code.

### Step 3: Repeat for Unlimited Claims

**Context**: Exploit lack of limits by refreshing or using new accounts.

Navigate back and redeem again; scale with account creation.

**Expected Output**: Multiple coupons received, demonstrating abuse potential.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[reward-abuse]]
- [[financial-impact]]
