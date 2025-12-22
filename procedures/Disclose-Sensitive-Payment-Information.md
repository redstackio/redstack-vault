---
id: proc-taxjar-payment-disclosure
name: Disclose-Sensitive-Payment-Information
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:36.473Z'
tactics:
  - '[[Collection]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
tags:
  - access-control
  - information-disclosure
  - payment
  - web
platforms:
  - Web
commands: []
tools: []
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Disclose-Sensitive-Payment-Information

## Summary

This procedure leverages improper access controls in TaxJar to view sensitive payment details, including Stripe-integrated information, accessible to member users despite admin-only intent.

## Description

Targeting subscription details pages in the TaxJar application, this procedure exposes payment data due to missing authorization checks. The scenario involves a member user navigating to protected sections post-login, resulting in unauthorized disclosure of billing information like card details or transaction history.

## Requirements

1. Authenticated member session in TaxJar
2. Access to subscription or billing pages
3. Browser developer tools for inspecting exposed data

## Defense

Defensive measures and detection strategies:

- Encrypt and restrict payment data visibility to authorized roles only
- Implement data loss prevention (DLP) monitoring for sensitive info access
- Regularly audit page permissions and sanitize outputs

## Objectives

1. Access subscription pages without admin privileges
2. Extract and view payment-related sensitive data
3. Demonstrate information disclosure risk

## Instructions

### Step 1: Navigate to Subscription Pages

**Context**: Direct the browser to areas exposing subscription details.

From the dashboard, go to account settings or billing sections, such as https://app.taxjar.com/account/subscription.

### Step 2: Inspect for Exposed Data

**Context**: Load the page and check for unauthorized content visibility.

Observe the page content for payment information; use browser inspect element if data is partially hidden but still accessible.

### Step 3: Extract Information

**Context**: Capture the disclosed details for analysis.

Screenshot or copy the visible payment data, confirming exposure of Stripe-linked details.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[access-control]]
- [[information-disclosure]]
- [[payment]]
- [[web]]
