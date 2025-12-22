---
id: proc-uuid-3
tags:
  - xss
  - url-crafting
  - shopify
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-shopify-cart-add]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:16:07.952Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Construct Malicious Cart Addition URL

## Summary

This procedure assembles a complete URL for the Shopify /cart/add endpoint, embedding the XSS payload to store the malicious properties[builder_id] in the victim's cart.

## Description

Using a valid product ID (e.g., 1106494145), the URL adds the item while injecting the nested array payload. The backend stores it persistently, affecting cart views for the session or longer, enabling stored XSS without further interaction from the attacker.

## Requirements

1. Valid product ID from target Shopify site
2. Encoded XSS payload from prior procedure
3. curl or browser for testing

## Defense

Defensive measures and detection strategies:

- Rate limiting on /cart/add requests
- Parameter length and format validation
- Audit logs for suspicious property values

## Objectives

1. Create functional malicious URL
2. Verify payload storage in cart
3. Ensure no immediate errors

## Instructions

### Step 1: Gather Components

**Context**: Identify product ID and other required params (e.g., quantity).

From site inspection, use id=1106494145.

### Step 2: Build and Execute URL

**Context**: Append payload and send request using [[commands/curl-shopify-cart-add]]:

```bash
curl -X GET "http://hardware.shopify.com/cart/add?id=1106494145&properties[builder_id][%20onmouseover%3dalert(document.cookie)%20\"]=shapp_options_421549285_1455208671885"
```

> This sends the GET request, adding the item with payload. Expected output: Redirect to cart or success status.

**Expected Output**: Cart updated with injected properties.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-shopify-cart-add]]

## Tools Used


## Tags

- [[xss]]
- [[url-crafting]]
