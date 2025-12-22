---
tags:
  - xss
  - stored-xss
  - account-takeover
  - cookie-theft
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
platforms:
  - Web
complexity: low
procedures:
  - '[[procedures/Navigate-and-Add-to-Cart]]'
  - '[[procedures/Inject-Stored-XSS-Payload]]'
  - '[[procedures/Observe-XSS-Execution]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
description: >-
  Exploitation of a stored XSS vulnerability in the billing address fields of an
  e-commerce checkout process to execute arbitrary JavaScript, steal cookies,
  and achieve account takeover.
skill_level: beginner
impact_level: high
id: 7d640a4d-7855-47a2-b9c2-0962f90c43cf
created_at: '2025-12-13T23:56:20.526Z'
updated_at: '2025-12-13T23:56:20.526Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Stored XSS in Billing Address Fields for Cookie Theft and Account Takeover

Multi-stage attack chain demonstrating the exploitation of a stored XSS vulnerability in an e-commerce site's billing address fields, leading to arbitrary JavaScript execution, cookie theft, and potential account takeover.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~2 minutes |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Access to Shop] --> B[Payload Injection]
    B --> C[XSS Execution and Impact]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
```

## Prerequisites & Requirements

### Required Tools

- None (browser-based exploitation)

### Target Environment

- Web platform
- E-commerce shop running .cfm (likely ColdFusion)
- Vulnerable endpoint: https://shop.aaf.com/Order/step1/index.cfm

### Initial Access Requirements

- Access to the public e-commerce website
- No credentials required for initial steps

## Detailed Attack Procedures

### Step 1: Navigate to Shop and Add Product to Cart
procedure: [[procedures/Navigate-and-Add-to-Cart]]

**Objective**: Access the e-commerce site and initiate the checkout process to reach the vulnerable billing address fields.

**Instructions**: Navigate to https://shop.aaf.com/, select any product such as a t-shirt, add it to the cart, and proceed to checkout.

**Expected Output**: Cart populated with a product and redirection to the billing activity page.

**Success Indicators**:
- Product added to cart successfully
- Redirected to https://shop.aaf.com/Order/step1/index.cfm

### Step 2: Inject XSS Payload in Address Fields
procedure: [[procedures/Inject-Stored-XSS-Payload]]

**Objective**: Inject a stored XSS payload into the address fields during the checkout process to store malicious JavaScript.

**Instructions**: On the billing activity page, enter the payload 'a"><svg/onload=prompt(1)>' into every address field (e.g., street, city, etc.) and click 'OK' to proceed.

**Expected Output**: Payload stored without sanitization, proceeding to the next page.

**Success Indicators**:
- Form submission succeeds without errors
- Payload is accepted and stored

### Step 3: Observe XSS Execution
procedure: [[procedures/Observe-XSS-Execution]]

**Objective**: Trigger the stored XSS payload to execute arbitrary JavaScript, demonstrating potential for cookie theft and account takeover.

**Instructions**: Proceed through the checkout process or refresh the page to trigger the stored payload, observing the execution of the injected JavaScript (e.g., a prompt dialog appears).

**Expected Output**: JavaScript prompt or alert executes, confirming XSS vulnerability.

**Success Indicators**:
- Prompt dialog appears
- Arbitrary JavaScript executes in the user's browser context

## Attack Chain Summary

### Key Achievements

1. Successful injection and storage of XSS payload in address fields
2. Execution of arbitrary JavaScript on page load
3. Potential for stealing session cookies and achieving full account takeover

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]
- [[Collection]]

*Last updated: 2023-10-01*
