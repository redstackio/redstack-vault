---
id: proc-uuid-prepare-checkout
tags:
  - web
  - checkout
  - preparation
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
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
updated_at: '2025-12-14T17:29:29.061Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Prepare-Zomato-Checkout

## Summary

This procedure sets up a legitimate checkout flow on Zomato's website to reach the point where the support rider donation can be manipulated, simulating normal user behavior to avoid detection.

## Description

In the context of exploiting a business logic flaw in Zomato's e-commerce platform, this procedure involves navigating the site, adding items, and initiating checkout to trigger the vulnerable donation addition request. It requires standard web access and assumes no prior authentication issues. The outcome is a cart ready for tampering, with expected server responses confirming the setup.

## Requirements

1. Internet access to zomato.com
2. Web browser (e.g., Chrome, Firefox)
3. Optional: Proxy tool like Burp Suite for traffic routing
4. Zomato user account for checkout (login if prompted)

## Defense

Defensive measures and detection strategies:

- Implement client-side input sanitization for donation amounts
- Monitor for unusual cart total reductions in logs
- Rate-limit checkout requests to detect proxy usage

## Objectives

1. Establish a valid order context for exploitation
2. Trigger the support rider donation UI element
3. Prepare for HTTP interception without alerting the system

## Instructions

### Step 1: Access Zomato Site

**Context**: Begin the attack by loading the target application.

No specific command; use browser to visit https://www.zomato.com.

> Expected: Homepage loads; search for restaurants.

### Step 2: Add Item to Cart

**Context**: Build a cart to enable checkout.

Select a restaurant and menu item via UI; click 'Add to Cart'.

> Expected: Cart updates with item and price.

### Step 3: Initiate Checkout and Donation

**Context**: Reach the vulnerable stage.

Proceed to checkout; select a donation option (25/50/100 rupees).

> Expected: HTTP request for donation generated (intercept if proxy active).

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- web
- checkout
