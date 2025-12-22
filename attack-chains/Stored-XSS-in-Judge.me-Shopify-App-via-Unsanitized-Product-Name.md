---
tags:
  - xss
  - stored-xss
  - shopify
  - judge.me
type: attack_chain
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
platforms:
  - Web
  - Shopify
complexity: medium
procedures:
  - '[[procedures/Create-Product-with-XSS-Payload]]'
  - '[[procedures/Submit-Question-Referencing-Malicious-Product]]'
  - '[[procedures/Edit-Question-to-Trigger-XSS]]'
step_count: 3
techniques:
  - '[[JavaScript]]'
description: >-
  Exploits a stored XSS vulnerability in Judge.me by injecting JavaScript
  payload into a Shopify product name, which is reflected unsafely in the admin
  question editing interface, enabling admin session hijacking.
skill_level: intermediate
impact_level: high
id: f234dacb-12b7-4af7-a68a-1cca2decdaf3
created_at: '2025-12-14T03:16:19.962Z'
updated_at: '2025-12-14T03:16:19.962Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Stored XSS in Judge.me Shopify App via Unsanitized Product Name

## Overview

This attack chain demonstrates a stored Cross-Site Scripting (XSS) vulnerability in the Judge.me Shopify app. The vulnerability arises because product names are not properly sanitized when reflected in the question editing interface within the Shopify admin panel. An attacker with access to create products in a Shopify store can inject a malicious JavaScript payload into a product name. When a question referencing that product is submitted and later edited by an admin, the payload executes in the admin's browser context, potentially stealing session cookies or performing other client-side attacks. This chain requires a Shopify account with product creation privileges and assumes the Judge.me app is installed.

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
    A[Create Malicious Product] --> B[Submit Question to Product]
    B --> C[Edit Question in Admin Panel]
    C --> D[XSS Execution and Cookie Theft]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (uses Shopify web interface)

### Target Environment

- Shopify store with Judge.me app installed
- Web browser for admin access
- No specific ports or services beyond standard HTTPS

### Initial Access Requirements

- Valid Shopify account with permissions to create products and submit questions
- Access to the store frontend and admin panel
- Judge.me app enabled for product reviews and questions

## Detailed Attack Procedures

### Step 1: Create Malicious Product
procedure: [[procedures/Create-Product-with-XSS-Payload]]

**Objective**: Inject an XSS payload into a product name to store the malicious script for later reflection.

**Instructions**: Log in to your Shopify account, navigate to the Products section in the admin panel, and create a new product. Set the product title to an HTML entity-encoded XSS payload, such as '&#60;img src=x onerror=prompt(&#100;&#111;&#99;&#117;&#109;&#101;&#110;&#116;&#46;&#100;&#111;&#109;&#97;&#105;&#110;)', which decodes to '<img src=x onerror=prompt(document.domain)>'. Save the product.

**Expected Output**: The product is created and listed in the store with the malicious name.

**Success Indicators**:
- Product appears in the store catalog
- Name displays without immediate execution (payload is stored)

### Step 2: Submit Question Referencing Malicious Product
procedure: [[procedures/Submit-Question-Referencing-Malicious-Product]]

**Objective**: Associate the malicious product with a user-submitted question to enable reflection in the admin interface.

**Instructions**: Visit the store frontend, locate the newly created product, and use the Judge.me question submission feature to post a question about it. In the question form, reference the product and include a similar encoded payload if needed, but the primary payload is in the product name. For example, use '><img src=x onerror=prompt(document.domain)>' in the question body if additional injection is desired. Submit the question.

**Expected Output**: The question is posted and visible on the product page.

**Success Indicators**:
- Question appears under the product in Judge.me
- No immediate alert or block from the system

### Step 3: Edit Question to Trigger XSS
procedure: [[procedures/Edit-Question-to-Trigger-XSS]]

**Objective**: Trigger the execution of the stored XSS payload by accessing the unsanitized reflection in the admin panel.

**Instructions**: Log in to the Shopify admin panel as an authenticated user (e.g., store admin). Navigate to Apps > Judge.me Product Reviews > Questions. Locate the submitted question, click to edit it. The product name will be reflected without sanitization in the editing interface, causing the XSS payload to execute immediately upon load, such as displaying a prompt with the document domain.

**Expected Output**: JavaScript alert or prompt executes, confirming payload activation.

**Success Indicators**:
- Browser prompt appears with domain info
- Inspect network/dev tools for potential cookie exfiltration if payload is modified

## Attack Chain Summary

### Key Achievements

1. Successful injection and storage of XSS payload in product data
2. Reflection of unsanitized payload in admin context
3. Execution of arbitrary JavaScript, enabling session theft or further attacks

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Execution]]
- [[Collection]]

*Last updated: 2023-10-01T00:00:00Z*
