---
id: proc-shopify-trigger-xss-001
tags:
  - xss
  - execution
  - trigger
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:46:37.782Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-on-Thank-You-Page

## Summary

This procedure renders the post-order thank you page to execute the stored XSS payload, demonstrating arbitrary JavaScript on checkout.shopify.com and transferable execution to the store's .myshopify.com domain.

## Description

The injected payload breaks out of the <title> tag and injects <html onmouseover=alert(2)>, triggering on user interaction. For broader impact, access the page via the store domain using the checkout ID, affecting admins and users viewing orders. This enables data theft like CSRF tokens.

## Requirements

1. Completed order with payload
2. Checkout ID from thank you URL
3. Access to store admin or user views

## Defense

Defensive measures and detection strategies:

- Escape all user inputs in HTML contexts, especially titles
- Use strict CSP to prevent JS execution
- Monitor page loads for alert() or unusual JS errors
- Sanitize order data before rendering thank you pages

## Objectives

1. Execute injected JavaScript
2. Verify impact on multiple domains
3. Demonstrate data exfiltration potential

## Instructions

### Step 1: View Initial Thank You Page

**Context**: Trigger on checkout domain.

After completion, the page at checkout.shopify.com loads; hover mouse to activate onmouseover.

### Step 2: Access Store Domain Page

**Context**: Extend execution scope.

Construct URL: `<store>.myshopify.com/0/checkouts/<id>/thank_you` (e.g., https://zh5402.myshopify.com/14372648/checkouts/5e566284338e71d6adc542b6567b4cf0/thank_you) and navigate.

### Step 3: Interact to Trigger

**Context**: Execute payload.

Hover over the page element to fire the alert.

**Expected Output**: Alert(2) pops up, confirming XSS.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- javascript-execution
- thank-you-page
