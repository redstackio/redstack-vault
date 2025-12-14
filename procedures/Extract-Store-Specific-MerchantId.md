---
tags:
  - csrf
  - shopify
  - token-extraction
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:57.902Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: ba022ac4-dd59-498e-bde8-96dd63911ab7
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Extract-Store-Specific-MerchantId

## Summary

This procedure captures the static, base64-encoded merchantId token from Shopify's PayPal activation request, which serves as a weak CSRF protector and can be reused if leaked.

## Description

The merchantId is generated during PayPal Express Checkout activation and embedded in GET parameters. It's store-specific, combining a timestamp and hex value, but static until expiry (reported 24 hours). Attackers with prior access (e.g., former admins) can extract and reuse it. This targets the `/admin/settings/payments` endpoint and requires inspecting network traffic.

## Requirements

1. Admin access to the target Shopify store
2. Browser with developer tools (e.g., Chrome DevTools)
3. Base64 decoding capability (built-in browser console or online tool)

## Defense

Defensive measures and detection strategies:

- Implement proper CSRF tokens that are per-session and unpredictable
- Rotate tokens frequently and invalidate on logout
- Log and alert on repeated activation attempts from suspicious IPs

## Objectives

1. Obtain the vulnerable merchantId for CSRF bypass
2. Decode and validate the token format
3. Enable crafting of the malicious activation URL

## Instructions

### Step 1: Initiate PayPal Activation

**Context**: Trigger the activation process to generate the merchantId in the network request.

In the Shopify admin, navigate to payments and click 'Activate PayPal Express Checkout'.

Visit `https://YOURDOMAIN.myshopify.com/admin/settings/payments` and select the activation link.

> The browser will make a GET request; do not complete the flow.

### Step 2: Inspect and Extract merchantId

**Context**: Use developer tools to capture the base64-encoded parameter from the request.

Open DevTools (F12), go to Network tab, and filter for the request to `/admin/payments/complete_paypal_incontext_oauth/`. Copy the `merchantId` query parameter.

Example: `MTU4MzAzMDUwNDowMTBmMDZkYjg1NzM0YjQ4NWVkMDk1YzQ1YWYxY2ZlNw==`

> Decode using JavaScript console: `atob('MTU4MzAzMDUwNDowMTBmMDZkYjg1NzM0YjQ4NWVkMDk1YzQ1YWYxY2ZlNw==')` outputs `1583030504:010f06db85734b485ed095c45af1cfe7`.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[shopify]]
- [[token-extraction]]
