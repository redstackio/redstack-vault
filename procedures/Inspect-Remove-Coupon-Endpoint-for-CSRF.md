---
id: proc-uuid-12345
name: Inspect-Remove-Coupon-Endpoint-for-CSRF
tags:
  - csrf
  - web
  - inspection
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
updated_at: '2025-12-14T17:27:35.546Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Inspect-Remove-Coupon-Endpoint-for-CSRF

## Summary

This procedure involves inspecting the HTTP request sent when removing a coupon from the Teavana shopping cart to confirm the absence of CSRF protection, enabling the identification of a cross-site request forgery vulnerability.

## Description

In an e-commerce environment like Teavana's Demandware platform, state-changing operations such as removing coupons from a cart should include CSRF tokens to prevent unauthorized requests. This procedure uses browser developer tools to capture and analyze the POST request, revealing the lack of such protection. The vulnerability allows attackers to forge requests from external sites, potentially modifying user sessions without consent. Prerequisites include an authenticated session and a coupon added to the cart.

## Requirements

1. Access to Teavana website with valid login
2. Browser with developer tools (e.g., Chrome DevTools)
3. Coupon added to shopping cart

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens on all state-changing endpoints
- Monitor for anomalous cart modifications from unexpected referers
- Use Content Security Policy (CSP) to restrict form submissions

## Objectives

1. Confirm absence of CSRF token in coupon removal request
2. Document endpoint details for exploitation
3. Assess impact on user shopping session

## Instructions

### Step 1: Add Coupon to Cart

**Context**: Prepare the cart for removal testing to trigger the vulnerable request.

Navigate to the Teavana website, log in, and add a coupon to your shopping cart via the legitimate interface.

### Step 2: Capture Removal Request

**Context**: Use developer tools to intercept the HTTP request during coupon removal.

Open browser developer tools (F12), go to the Network tab, attempt to remove the coupon from the cart, and inspect the captured POST request.

**Technical Details**:
The request targets `POST /on/demandware.store/Sites-Teavana-Site/default/Cart-RemoveCoupon` with a body parameter `couponCode=exampleCode`, but no CSRF token header or field is present.

### Step 3: Verify CSRF Absence

**Context**: Analyze the request headers and body to confirm vulnerability.

Check for tokens like `csrf-token` or `X-CSRF-Token` in headers or form data. Absence indicates the endpoint is vulnerable to forged requests.

**Expected Output**: Request details showing state-changing POST without protection.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[web]]
- [[demandware]]
