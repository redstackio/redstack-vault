---
tags:
  - idor
  - web
  - financial-fraud
  - paypal
  - reddit
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Initiate-and-Intercept-Small-Coin-Purchase]]'
  - '[[procedures/Capture-Order-ID-from-Small-Package]]'
  - '[[procedures/Initiate-Larger-Coin-Package-Purchase]]'
  - '[[procedures/Modify-Order-ID-to-Small-Package]]'
  - '[[procedures/Complete-Transaction-and-Receive-Coins]]'
step_count: 5
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:33.715Z'
description: >-
  Exploits an Insecure Direct Object Reference (IDOR) in Reddit's PayPal coin
  purchase endpoint to swap order IDs, allowing payment for a small coin package
  while receiving the larger package's coins.
skill_level: intermediate
impact_level: high
id: fcb5dfb3-fa30-4320-b8cb-623299e4372b
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# IDOR in Reddit Coin Purchase API to Acquire More Coins at Lower Price

Multi-stage attack chain demonstrating exploitation of an IDOR vulnerability in Reddit's coin purchase system via PayPal integration. The attack allows an authenticated user to manipulate order IDs during the purchase flow, paying the price for a small coin package (e.g., 500 coins for $1.99) but receiving the coins from a larger package (e.g., 1100 coins for $3.99). This results in financial loss for Reddit and disrupts the coin gifting economy.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initiate Small Purchase] --> B[Capture Order ID]
    B --> C[Initiate Large Purchase]
    C --> D[Modify Order ID]
    D --> E[Complete Transaction]
    E --> F[Receive Extra Coins]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#27ae60
    style F fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]

### Target Environment

- Web platform
- Reddit account with access to coin purchases
- PayPal account for transactions
- No specific ports; operates over HTTPS

### Initial Access Requirements

- Authenticated Reddit session
- Network access to oauth.reddit.com and PayPal
- No prior elevated access needed; standard user account suffices

## Detailed Attack Procedures

### Step 1: Initiate Small Coin Package Purchase
procedure: [[procedures/Initiate-and-Intercept-Small-Coin-Purchase]]

**Objective**: Start the purchase flow for the smallest coin package to generate a low-value order ID.

**Instructions**: Log in to Reddit, navigate to the coin purchase section, and select the smallest package (500 coins for $1.99). Click the PayPal button to begin the transaction. Use Burp Suite to intercept the request.

**Expected Output**: Intercepted POST request to /api/v2/gold/paypal/create_coin_purchase_order with body including coins=500&pennies=199.

**Success Indicators**:
- Request intercepted successfully
- Purchase flow initiated without errors

### Step 2: Capture Order ID from Small Package
procedure: [[procedures/Capture-Order-ID-from-Small-Package]]

**Objective**: Extract the order_id from the response of the small package purchase for later manipulation.

**Instructions**: In Burp Suite, forward the request and capture the response containing the order_id (e.g., {"order_id": "1CR56170K7852611T"}). Note this ID as it corresponds to the $1.99 transaction.

**Expected Output**: JSON response with order_id tied to the small package.

**Success Indicators**:
- Order_id saved
- No validation errors in response

### Step 3: Initiate Larger Coin Package Purchase
procedure: [[procedures/Initiate-Larger-Coin-Package-Purchase]]

**Objective**: Begin a new purchase for a larger package to set up the ID swap.

**Instructions**: Cancel the previous small purchase if needed, then select and initiate a larger package (e.g., 1100 coins for $3.99) via PayPal. Intercept the new request using Burp Suite.

**Expected Output**: New POST request to the same endpoint with updated body (e.g., coins=1100&pennies=399).

**Success Indicators**:
- Larger package flow started
- Interception active for modification

### Step 4: Modify Order ID to Small Package
procedure: [[procedures/Modify-Order-ID-to-Small-Package]]

**Objective**: Swap the order_id in the larger package response to the one from the small package, tricking the system into associating the large coin amount with the low payment.

**Instructions**: In Burp Suite, intercept the response for the larger package. Edit the JSON to replace the order_id with the saved one from the small package (e.g., change to {"order_id": "1CR56170K7852611T"}). Forward the modified response.

**Expected Output**: Modified response accepted by the client, redirecting to PayPal with the small amount ($1.99).

**Success Indicators**:
- Order_id swapped without rejection
- PayPal page shows $1.99 charge

### Step 5: Complete Transaction and Receive Coins
procedure: [[procedures/Complete-Transaction-and-Receive-Coins]]

**Objective**: Finalize the payment and verify receipt of the larger coin quantity.

**Instructions**: Complete the PayPal transaction for $1.99. Upon success, check Reddit account balance for the larger coin amount (1100 coins).

**Expected Output**: Transaction completes, and account credits 1100 coins despite $1.99 payment.

**Success Indicators**:
- Payment processed at low price
- Extra coins added to account
- No discrepancies flagged

## Attack Chain Summary

### Key Achievements

1. Successful IDOR exploitation via order_id manipulation
2. Financial gain through discounted coin acquisition
3. Demonstration of API validation failure in purchase flow

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Execution]]

---
*Last updated: 2023-10-01T00:00:00Z*
