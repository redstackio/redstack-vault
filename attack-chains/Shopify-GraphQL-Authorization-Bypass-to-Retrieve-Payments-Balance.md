---
id: ac-shopify-graphql-bypass-001
name: Shopify GraphQL Authorization Bypass to Retrieve Payments Balance
type: attack_chain
description: >-
  An authorization bypass in Shopify's GraphQL API allowing staff with no
  permissions to access sensitive Shopify Payments information including
  balances and payouts.
verified: false
submitted: true
step_count: 3
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:59.765Z'
procedures:
  - '[[procedures/Create-No-Permission-Staff-Account]]'
  - '[[procedures/Login-and-Verify-Restricted-Access]]'
  - '[[procedures/Exploit-GraphQL-for-Payments-Data]]'
techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
tags:
  - authorization-bypass
  - graphql
  - shopify
  - information-disclosure
  - payments
platforms:
  - Web
tools:
  - '[[tools/Burp-Suite]]'
complexity: medium
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
---

# Shopify GraphQL Authorization Bypass to Retrieve Payments Balance

Multi-stage attack chain demonstrating an authorization bypass in Shopify's admin GraphQL API to disclose sensitive Shopify Payments financial data to staff members without any permissions.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Create No-Permission Staff Account] --> B[Login and Verify Restrictions]
    B --> C[Intercept and Modify GraphQL Query]
    C --> D[Retrieve Payments Balance Data]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]

### Target Environment

- Shopify admin platform (Web)
- Access to Shopify store admin as owner/admin for account creation
- GraphQL API endpoint (/admin/api/graphql)

### Initial Access Requirements

- Valid owner/admin credentials to create staff account
- Network access to the target Shopify store domain (e.g., example.myshopify.com)
- No special ports required; standard HTTPS (443)

## Detailed Attack Procedures

### Step 1: Create No-Permission Staff Account
procedure: [[procedures/Create-No-Permission-Staff-Account]]

**Objective**: Establish a low-privilege staff account with zero explicit permissions to test authorization controls.

**Instructions**: As a store owner or admin, navigate to the Shopify admin interface and create a new staff member account, ensuring all permission checkboxes are unchecked.

**Expected Output**: Staff account created successfully with email and login credentials, but no access rights assigned.

**Success Indicators**:
- Account confirmation email sent
- Staff listed in admin with no roles

### Step 2: Login and Verify Restricted Access
procedure: [[procedures/Login-and-Verify-Restricted-Access]]

**Objective**: Confirm the staff account has no UI access to sensitive areas, setting up for API testing.

**Instructions**: Log in to the Shopify admin UI using the staff credentials and observe the interface for lack of menus or home content.

**Expected Output**: Login successful, but dashboard shows restricted view with no navigable sections.

**Success Indicators**:
- Successful authentication
- Visual confirmation of empty or restricted UI (no menus, no home section)

### Step 3: Intercept and Exploit GraphQL Query
procedure: [[procedures/Exploit-GraphQL-for-Payments-Data]]

**Objective**: Bypass UI restrictions by intercepting and modifying a GraphQL request to access Shopify Payments balance and payouts.

**Instructions**: Configure Burp Suite as a proxy, trigger a request from the restricted UI, intercept the GraphQL POST to /admin/api/graphql, and modify the query to include shopifyPaymentsAccount fields. Send the modified request using [[commands/shopify-graphql-payments-query]].

```bash
# Example using curl for the modified GraphQL query (proxied via Burp)
curl -X POST https://example.myshopify.com/admin/api/graphql \
  -H "Content-Type: application/json" \
  -H "x-shopify-web-force-proxy: 1" \
  -H "Origin: https://example.myshopify.com" \
  -b "cookies_here" \
  -d '{"operationName":"HomeIndex","variables":{"localTime":"22:59"},"query":"query HomeIndex($localTime: DateTime!) { shop { shopifyPaymentsAccount { balance { ... on MoneyV2 { amount currencyCode } } payouts(first: 2, reverse: true) { edges { ... on ShopifyPaymentsPayoutEdge { node { gross { amount currencyCode } id issuedAt status } } } } } } } }"}'
```

**Expected Output**: JSON response containing shopifyPaymentsAccount with balance array (potentially empty) and payouts, revealing payment provider and financial details.

**Success Indicators**:
- Response includes shopifyPaymentsAccount object
- Balance and payouts data visible despite no permissions

## Attack Chain Summary

### Key Achievements

1. Created and authenticated a zero-permission staff account
2. Verified UI restrictions to confirm low privilege
3. Bypassed authorization via GraphQL to disclose sensitive payments data

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]] Valid Accounts
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Collection]] Collection

---
*Last updated: 2023-10-01T00:00:00Z*
