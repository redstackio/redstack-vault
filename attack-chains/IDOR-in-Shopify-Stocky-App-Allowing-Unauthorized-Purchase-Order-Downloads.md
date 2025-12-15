---
id: ac-uuid-001
tags:
  - idor
  - shopify
  - unauthorized-access
  - purchase-orders
  - access-control
type: attack_chain
tools: []
tactics:
  - '[[Discovery]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
  - Shopify
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Test-Access-Controls-in-Stocky-App]]'
  - '[[procedures/Exploit-IDOR-to-Download-Purchase-Orders]]'
step_count: 2
techniques:
  - '[[Account Discovery]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:29:44.387Z'
description: >-
  Multi-stage exploitation of an Insecure Direct Object Reference (IDOR)
  vulnerability in the Shopify Stocky application, enabling users without draft
  order permissions to access and download sensitive purchase order data.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Discovery]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Account Discovery]]'
  - '[[Exploit Public-Facing Application]]'
---
# IDOR in Shopify Stocky App Allowing Unauthorized Purchase Order Downloads

Multi-stage attack chain demonstrating the exploitation of an IDOR vulnerability in the Shopify Stocky application, where missing permission checks allow unauthorized users to access draft orders and download sensitive purchase order data. Discovered by researcher imranhudaa via access control testing, this led to unauthorized data exposure and a $500 bounty upon resolution by adding the missing check.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Access Control Testing] --> B[IDOR Exploitation]
    B --> C[Data Exfiltration]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome with developer tools)
- Access to a Shopify account without draft order permissions

### Target Environment

- Shopify platform
- Stocky application (inventory management app)
- Web-based interface for draft orders and purchase orders

### Initial Access Requirements

- Valid Shopify user account (non-admin, lacking draft order permissions)
- Network access to Shopify's web services
- No prior elevated access needed

## Detailed Attack Procedures

### Step 1: Access Control Testing
procedure: [[procedures/Test-Access-Controls-in-Stocky-App]]

**Objective**: Identify missing permission checks in the Stocky app's draft orders and purchase orders functionality.

**Instructions**: Log in to the Shopify admin panel with a user account that lacks draft order permissions. Navigate to the Stocky app and attempt to access the draft orders section. Use the browser's developer tools to inspect network requests for any endpoints related to draft orders (e.g., /draft_orders or similar API paths). Test by trying to view or interact with draft orders without the required role.

**Expected Output**: Successful access to draft order interfaces despite lacking permissions, indicating a missing authorization check.

**Success Indicators**:
- Ability to view draft orders UI elements
- No permission denial errors in UI or network responses

### Step 2: IDOR Exploitation
procedure: [[procedures/Exploit-IDOR-to-Download-Purchase-Orders]]

**Objective**: Exploit the IDOR to download sensitive purchase order data attached to draft orders.

**Instructions**: With access confirmed, select a draft order and navigate to the purchase orders feature within Stocky. Attempt to trigger a download action on the purchase orders endpoint (e.g., via a POST request to /purchase_orders/download or similar). Use browser dev tools to modify or replay the request if needed, ensuring the direct object reference (draft order ID) is passed without additional auth checks.

**Expected Output**: Downloadable file containing sensitive purchase order details, such as vendor information, quantities, and pricing.

**Success Indicators**:
- File download initiates and completes
- Data in the file reveals unauthorized sensitive information

## Attack Chain Summary

### Key Achievements

1. Bypassed permission checks to access draft order functionalities
2. Exploited IDOR to exfiltrate purchase order data
3. Demonstrated high-impact unauthorized data access in a production e-commerce environment

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Account Discovery]]
- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Discovery]]
- [[Collection]]

---
*Last updated: 2023-10-01T00:00:00Z*
