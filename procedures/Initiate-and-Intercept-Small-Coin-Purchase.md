---
id: proc-uuid-1
tags:
  - idor
  - intercept
  - purchase
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:33.708Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Initiate-and-Intercept-Small-Coin-Purchase

## Summary

This procedure initiates the purchase of Reddit's smallest coin package using PayPal and intercepts the API request to prepare for order_id capture, setting up the IDOR exploitation.

## Description

In the context of Reddit's coin purchase system, this step involves navigating the web interface to select the 500-coin package ($1.99), triggering a POST to the vulnerable endpoint. Using a proxy like Burp Suite, the request is intercepted to allow inspection and control over the flow. This is a prerequisite for capturing the low-value order_id without completing the transaction prematurely.

## Requirements

1. Authenticated Reddit session
2. Burp Suite configured as proxy for browser traffic
3. PayPal account ready for transactions

## Defense

Defensive measures and detection strategies:

- Implement request signing or session-bound tokens to prevent interception tampering
- Monitor for unusual proxy traffic patterns in API calls
- Rate-limit purchase initiations per user

## Objectives

1. Generate a valid order_id for the small package
2. Position for request interception
3. Avoid completing the initial transaction

## Instructions

### Step 1: Start Purchase Flow

**Context**: Log in to Reddit and access the coin purchase page to select the small package.

No specific command; manual browser action: Navigate to Reddit coins section, choose 500 coins ($1.99), click PayPal.

> This triggers the API call; ensure Burp is proxying.

### Step 2: Intercept Request

**Context**: Capture the POST request during the flow.

Configure Burp Suite to intercept HTTPS traffic to oauth.reddit.com.

> Expected: POST to https://oauth.reddit.com/api/v2/gold/paypal/create_coin_purchase_order with body coins=500&pennies=199&correlation_id=...

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- idor
- web
- purchase
