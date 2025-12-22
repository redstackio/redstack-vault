---
tags:
  - shopify
  - web
  - recon
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
updated_at: '2025-12-14T03:46:37.115Z'
sub_techniques: []
id: cfd48ced-c03d-4b81-a6e3-054d69e99a41
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
---

# Access-Custom-Gift-Card-Page

## Summary

This procedure navigates to the custom gift card product page on a Shopify store, setting up the environment for exploiting the cart addition vulnerability.

## Description

In the context of the Shopify hardware store, this step accesses the specific product page that allows customization including artwork uploads, which is vulnerable due to improper handling in the subsequent cart addition. It requires no authentication and serves as the entry point for the attack chain, enabling preparation for payload injection.

## Requirements

1. Web browser access to the internet
2. Target URL: http://hardware.shopify.com/collections/gift-cards/products/custom-gift-card
3. No special tools beyond a standard browser

## Defense

Defensive measures and detection strategies:

- Implement rate limiting on product page views
- Monitor for unusual traffic patterns to gift card pages
- Use WAF rules to detect automated access

## Objectives

1. Load the vulnerable product page
2. Verify form availability for cart addition
3. Prepare for request interception

## Instructions

### Step 1: Navigate to Product Page

**Context**: Directly access the custom gift card product to initiate the attack surface exposure.

No specific command; use browser navigation:

Visit: http://hardware.shopify.com/collections/gift-cards/products/custom-gift-card

> This loads the page with customization options. Expected output: Page renders with image upload field and 'Add to Cart' button.

### Step 2: Select Customization Options

**Context**: Interact minimally to trigger the form without adding yet, confirming functionality.

Select a sample image for artwork but do not submit.

> Prepares the form data structure for interception in later steps.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[shopify]]
- [[web]]
- [[recon]]
