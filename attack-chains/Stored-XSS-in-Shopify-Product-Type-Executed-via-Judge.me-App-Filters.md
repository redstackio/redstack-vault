---
tags:
  - xss
  - stored-xss
  - shopify
  - judgeme
type: attack_chain
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
  - Shopify
complexity: medium
procedures:
  - '[[procedures/Install-Judge-me-App-in-Shopify]]'
  - '[[procedures/Inject-XSS-Payload-into-Product-Type]]'
  - '[[procedures/Trigger-XSS-via-Judge-me-Filters]]'
step_count: 3
techniques:
  - '[[JavaScript]]'
description: >-
  A multi-stage attack exploiting a stored XSS vulnerability in Shopify's
  product type field, triggered through the Judge.me app's product filters,
  allowing JavaScript execution in the admin context.
skill_level: intermediate
impact_level: high
id: c2f57b1a-24b6-4ebf-bb15-8bb136a6da88
created_at: '2025-12-13T23:52:33.395Z'
updated_at: '2025-12-13T23:52:33.395Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Stored XSS in Shopify Product Type Executed via Judge.me App Filters

## Overview

This attack chain demonstrates a stored cross-site scripting (XSS) vulnerability in the Judge.me Shopify app. An attacker with Shopify admin access injects a malicious JavaScript payload into a product's 'type' field. When another admin uses the Judge.me app's product filter dropdown to select that type, the unsanitized payload executes in the victim's browser, potentially leading to session hijacking or impersonation, though limited by HttpOnly cookie flags.

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
    A[Install Judge.me App] --> B[Inject XSS Payload]
    B --> C[Trigger via Filters]
    C --> D[JavaScript Execution]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome)
- Shopify admin credentials

### Target Environment

- Shopify store with admin access
- Judge.me app installed
- Web platform

### Initial Access Requirements

- Valid Shopify admin account with product edit permissions
- Access to the store's admin panel
- No special network access beyond standard internet

## Detailed Attack Procedures

### Step 1: Install Judge.me App
procedure: [[procedures/Install-Judge-me-App-in-Shopify]]

**Objective**: Gain access to the Judge.me app interface within the Shopify admin to enable product filtering.

**Instructions**: Log in to the Shopify admin panel and install the Judge.me app from the Shopify App Store. This sets up the environment for the subsequent XSS trigger.

**Expected Output**: Judge.me app appears in the admin apps list, accessible at /admin/apps/judgeme.

**Success Indicators**:
- App installation confirmation
- Navigation to Judge.me products page possible

### Step 2: Inject XSS Payload into Product Type
procedure: [[procedures/Inject-XSS-Payload-into-Product-Type]]

**Objective**: Store a malicious JavaScript payload in the Shopify product data that will later be reflected in the Judge.me filters.

**Instructions**: Create a new active product in Shopify admin, and insert the payload "><img src=x onerror=prompt(document.domain)> into the Product Type field. Save the product to persist the injection.

**Expected Output**: Product saved successfully with the malicious type field.

**Success Indicators**:
- Product appears in the store's product list
- Payload stored without immediate error

### Step 3: Trigger XSS via Judge.me Filters
procedure: [[procedures/Trigger-XSS-via-Judge-me-Filters]]

**Objective**: Cause the stored payload to execute by interacting with the vulnerable filter in the Judge.me app.

**Instructions**: Navigate to the Judge.me products page (e.g., https://xxx.myshopify.com/admin/apps/judgeme/products). Click the TYPE filter dropdown and select the malicious product type. The payload renders and executes.

**Expected Output**: Alert box prompting the document domain, confirming JavaScript execution.

**Success Indicators**:
- Payload triggers onerror event
- Potential for further exploitation like session access

## Attack Chain Summary

### Key Achievements

1. Successful installation and setup of the Judge.me app
2. Injection of stored XSS payload into product metadata
3. Execution of arbitrary JavaScript in admin context via filter interaction

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Execution]]

---
*Last updated: 2023-10-01*
