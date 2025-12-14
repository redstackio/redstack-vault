---
id: ac-yelp-idor-unauth-cc-001
tags:
  - idor
  - yelp
  - grubhub
  - credit-card
  - unauthorized-access
  - web-vulnerability
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Identify-Yelp-Checkout-Endpoint]]'
  - '[[procedures/Discover-IDOR-in-Credit-Card-Selection]]'
  - '[[procedures/Exploit-IDOR-for-Unauthorized-Order]]'
  - '[[procedures/Validate-IDOR-Vulnerability]]'
step_count: 4
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:25:48.215Z'
description: >-
  Multi-stage attack exploiting an Insecure Direct Object Reference (IDOR) in
  Yelp's checkout process to unauthorizedly charge other users' saved credit
  cards for free food orders through Grubhub integration.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Valid Accounts]]'
---
# IDOR in Yelp Checkout Endpoint for Unauthorized Credit Card Usage via Grubhub

Multi-stage attack chain demonstrating a complete attack workflow exploiting an IDOR vulnerability in Yelp's platform to place free orders using other users' credit cards.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Identify Checkout Endpoint] --> B[Discover IDOR in Credit Card Selection]
    B --> C[Exploit IDOR to Place Unauthorized Order]
    C --> D[Validate Vulnerability]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser with developer tools (e.g., Chrome DevTools)
- Optional: Proxy tool like Burp Suite for request interception

### Target Environment

- Yelp web platform
- Integrated Grubhub service for food ordering
- Web-based application

### Initial Access Requirements

- Valid Yelp user account
- Ability to initiate a checkout process for food ordering
- Knowledge of another user's credit_card_id (e.g., via testing or shared for validation)

## Detailed Attack Procedures

### Step 1: Identify Checkout Endpoint
procedure: [[procedures/Identify-Yelp-Checkout-Endpoint]]

**Objective**: Locate the endpoint responsible for processing food orders via Grubhub integration.

**Instructions**: Log in to your Yelp account and navigate to the food ordering section. Start a checkout process for a Grubhub-integrated restaurant. Use browser developer tools to inspect network requests and identify the /checkout/transaction_platform endpoint used for transaction processing.

**Expected Output**: Identification of the /checkout/transaction_platform endpoint in network logs, showing parameters like credit_card_id.

**Success Indicators**:
- Endpoint URL confirmed
- Request structure observed, including credit_card_id parameter

### Step 2: Discover IDOR in Credit Card Selection
procedure: [[procedures/Discover-IDOR-in-Credit-Card-Selection]]

**Objective**: Test for authorization flaws in the credit card selection mechanism.

**Instructions**: During the checkout flow, capture the request to /checkout/transaction_platform using developer tools or a proxy. Note your own credit_card_id in the request. Modify the request by replacing the credit_card_id with an arbitrary value (e.g., increment by 1 to simulate another user's ID) and resubmit. Observe if the server accepts the change without validation.

**Expected Output**: Server processes the modified request without error, indicating lack of ownership checks.

**Success Indicators**:
- Modified credit_card_id accepted
- No authorization error returned

### Step 3: Exploit IDOR for Unauthorized Order
procedure: [[procedures/Exploit-IDOR-for-Unauthorized-Order]]

**Objective**: Use the IDOR to complete a transaction with another user's credit card, resulting in a free order for the attacker.

**Instructions**: In the captured request, set the credit_card_id to a known valid ID from another user. Submit the full transaction request to /checkout/transaction_platform. Proceed through the order confirmation, ensuring the charge is applied to the unauthorized card.

**Expected Output**: Order completes successfully, charged to the target credit card, delivering free food to the attacker.

**Success Indicators**:
- Order confirmation received
- No payment error; order fulfilled

### Step 4: Validate IDOR Vulnerability
procedure: [[procedures/Validate-IDOR-Vulnerability]]

**Objective**: Confirm the vulnerability without real exploitation by using a controlled test ID.

**Instructions**: Obtain a shared test credit_card_id (e.g., from platform staff for ethical disclosure). Repeat the modification and submission process using this ID. Verify that the system allows the transaction, then report the issue.

**Expected Output**: Successful test transaction using the shared ID, proving the IDOR exists.

**Success Indicators**:
- Test order processes without issues
- Vulnerability confirmed for reporting

## Attack Chain Summary

### Key Achievements

1. Identified vulnerable endpoint in Yelp's Grubhub integration
2. Discovered and exploited IDOR to access unauthorized credit cards
3. Demonstrated potential for free orders affecting over 1,500,000 saved cards
4. Validated ethically without real harm

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Valid Accounts]] Valid Accounts

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Discovery]] Discovery

---
*Last updated: 2023-10-01T00:00:00Z*
