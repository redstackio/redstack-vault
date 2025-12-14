---
id: proc-uuid-5
tags:
  - xss
  - execution
  - shopify
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:36.278Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-Stored-XSS-on-Checkout-Page

## Summary

This procedure activates the stored XSS by clicking the rendered artwork link on Shopify's checkout page, executing the javascript payload.

## Description

On the checkout interface at https://checkout.shopify.com/, the malicious URL is displayed as a hyperlink for the custom gift card. Clicking it executes the javascript:alert(document.domain), demonstrating arbitrary code run in the page context. This could extend to stealing cookies or hijacking sessions for victims processing the tainted order.

## Requirements

1. Checkout page loaded with malicious item
2. Link visible in the order summary
3. Victim-like interaction

## Defense

Defensive measures and detection strategies:

- Neutralize javascript: schemes in rendered links
- Use Content Security Policy to block inline scripts

## Objectives

1. Execute the stored payload
2. Confirm XSS impact
3. Highlight potential for broader attacks

## Instructions

### Step 1: Locate Artwork Link

**Context**: Identify the clickable element for the uploaded artwork.

No command required.

> In the checkout summary, find the "Artwork File" link for the custom gift card.

### Step 2: Click to Trigger

**Context**: Interact with the link to run the payload.

No command required.

> Click the link. An alert should appear showing the document domain, confirming execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[Execution]]
- [[shopify]]
