---
id: proc-starbucks-csrf-basket
tags:
  - csrf
  - automation
type: procedure
tools:
  - '[[tools/Firefox]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[SAML Tokens]]'
updated_at: '2025-12-13T23:52:21.134Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[SAML Tokens]]'
---
# Add-Egift-Card-to-Basket-via-CSRF

## Summary

This procedure exploits the lack of CSRF protection on the 'Add to Basket' action for egift cards, allowing automated state-changing operations without user interaction in phishing attacks.

## Description

The /shop/card/egift endpoint performs basket additions without CSRF tokens, enabling attackers to craft malicious pages that automatically add items, setting up the authenticated context for XSS without user consent.

## Requirements

1. Authenticated session from previous login.
2. Firefox browser.
3. Access to https://www.starbucks.co.uk/shop/card/egift.

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens on all state-changing actions.
- Log and alert on rapid or automated form submissions.

## Objectives

1. Add item to basket without CSRF validation.
2. Demonstrate automation potential.
3. Transition to payment page.

## Instructions

### Step 1: Navigate to Egift Page

**Context**: Load the page hosting the vulnerable action.

In Firefox, enter:

```bash
# Manual: https://www.starbucks.co.uk/shop/card/egift
```

> Expected output: Egift card selection page loads.

### Step 2: Perform Add to Basket

**Context**: Execute the action lacking CSRF protection.

Select a card and click 'Add to Basket'.

> Expected output: Confirmation of addition; no token required.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[SAML Tokens]] Forge Web Credentials (adapted for CSRF enabling execution)

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Firefox]]

## Tags

- [[csrf]]
- [[automation]]
