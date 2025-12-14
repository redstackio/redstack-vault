---
id: proc-demonstrate-claiming
tags:
  - subdomain-takeover
  - dyn
  - claiming
type: procedure
tools:
  - '[[tools/Detectify-Labs-Blog]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Compromise Accounts]]'
updated_at: '2025-12-14T05:32:23.420Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Compromise Accounts]]'
---
# Demonstrate Subdomain Claiming Process

## Summary

This procedure simulates claiming a subdomain on DYN by adding it to the cart, proving control can be gained without full purchase.

## Description

In the attack scenario, the tester adds the unclaimed hostname to DYN's cart, receives activation messages, and removes it to avoid commitment. Repetition from another account confirms reproducibility. This highlights how attackers could purchase and configure for malicious use. Prerequisites: DYN portal access; outcomes include screenshots and messages evidencing vulnerability.

## Requirements

1. Multiple DYN accounts for verification
2. Screenshots tool for documentation
3. Understanding of DYN's registration flow

## Defense

Defensive measures and detection strategies:

- Promptly claim and configure all delegated hostnames
- Set up alerts for cart additions on critical subdomains
- Conduct regular subdomain audits with tools like Subjack

## Objectives

1. Add subdomain to cart for testing
2. Capture confirmation evidence
3. Verify process repeatability

## Instructions

### Step 1: Add to Cart

**Context**: Select and add the subdomain in DYN's interface.

Use browser at http://dyn.com/dns/ to add "web.mopub.com" to cart.

> Expected: Message confirming active DNS but purchasable status.

### Step 2: Remove and Repeat

**Context**: Remove from cart and test from another account.

Remove item, log out, and repeat addition from a second account.

> Expected: Consistent availability and cart success.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Compromise Accounts]] Compromise Accounts

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Detectify-Labs-Blog]]

## Tags

- [[subdomain-takeover]]
- [[dyn]]
- [[claiming]]
