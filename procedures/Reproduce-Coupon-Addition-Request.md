---
tags:
  - csrf
  - reproduction
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-add-coupon-csrf]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:29.821Z'
sub_techniques: []
id: ce904126-75f1-4f75-a2ec-8bb5dcb5c233
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Reproduce Coupon Addition Request

## Summary

This procedure manually reproduces the process of adding a coupon to a shopping basket on the Teavana website to capture the underlying HTTP request for further analysis.

## Description

In a real-world scenario, an attacker first needs to understand the legitimate flow of adding a coupon. By logging in as a user, applying the 'BOGO50' coupon, and inspecting the network traffic, the POST request to the vulnerable endpoint is captured. This reveals the parameters used and confirms the action's state-changing nature, setting the stage for identifying CSRF weaknesses. The target environment is the Teavana web application built on Demandware (Salesforce Commerce Cloud), requiring an authenticated session.

## Requirements

1. Authenticated account on Teavana website
2. Modern web browser with developer tools enabled
3. Network access to teavana.com

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens on all state-changing endpoints
- Monitor for anomalous basket modifications from unexpected sources
- Use Content Security Policy (CSP) to restrict form submissions

## Objectives

1. Capture the exact HTTP request for coupon addition
2. Verify the endpoint modifies user data
3. Prepare for vulnerability verification

## Instructions

### Step 1: Authenticate and Navigate

**Context**: Establish a valid session and reach the point where coupons can be applied.

Log in to https://www.teavana.com and add an item to your basket to access the coupon input field.

### Step 2: Apply Coupon and Intercept Request

**Context**: Submit the coupon and capture the network traffic to document the request.

Enter 'BOGO50' as the coupon code and submit. Open developer tools (F12), go to the Network tab, and filter for POST requests. Locate the request to `/on/demandware.store/Sites-Teavana-Site/default/Home-AddCouponToBasket`.

Execute [[commands/curl-add-coupon-csrf]] to simulate and verify the request syntax:

```bash
curl -X POST 'https://www.teavana.com/on/demandware.store/Sites-Teavana-Site/default/Home-AddCouponToBasket' -d 'couponcode=BOGO50&format=ajax' -H 'Cookie: session=your_cookie_here'
```

> This command sends the POST with session cookie; expect a JSON response indicating success if authenticated.

**Expected Output**: HTTP 200 response with basket update confirmation.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-add-coupon-csrf]]

## Tools Used


## Tags

- [[csrf]]
- [[web]]
- [[reproduction]]
