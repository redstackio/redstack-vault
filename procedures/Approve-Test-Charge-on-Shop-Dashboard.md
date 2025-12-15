---
id: proc-shopify-approve-test-charge
tags:
  - test-charge
  - shopify
  - dashboard
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
updated_at: '2025-12-14T17:30:18.142Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Approve-Test-Charge-on-Shop-Dashboard

## Summary

This procedure approves the simulated test charge in the Shopify shop dashboard, advancing the free theme installation without incurring real costs.

## Description

The staging purchase redirects to the user's main Shopify admin dashboard, presenting a test charge for a nominal amount (e.g., $0.00 or test value). Approving this leverages the environment's test mode, bypassing production payment gateways. This is due to improper isolation of staging from production flows. Successful approval enables theme download and use.

## Requirements

1. Redirect from staging purchase to shop dashboard
2. Active Shopify admin access
3. No payment method configured for real charges

## Defense

Defensive measures and detection strategies:

- Separate test and production charge workflows
- Require manual approval for staging charges with logging
- Detect cross-environment redirects and block them

## Objectives

1. Handle test charge prompt in dashboard
2. Approve without real payment
3. Proceed to installation

## Instructions

### Step 1: Access Dashboard Redirect

**Context**: Follow the automatic redirect from staging to shop interface.

Upon initiating purchase, the browser redirects to your Shopify shop admin showing the test charge screen.

> The screen displays a test transaction details.

### Step 2: Approve Charge

**Context**: Confirm the test charge to continue.

Click 'approve charge' on the dashboard interface.

> Approval completes instantly without financial impact.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[test-charge]]
- [[shopify]]
- [[dashboard]]
