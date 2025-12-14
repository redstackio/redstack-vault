---
id: ac-uuid-001
name: Stored XSS in Shopify Wholesale Price List Leading to Cross-Shop Data Leakage
tags:
  - xss
  - stored-xss
  - shopify
  - data-leakage
  - javascript
  - web-vulnerability
type: attack_chain
tools:
  - '[[tools/HTTP-Proxy-Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
  - Shopify
submitted: true
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Setup-Wholesale-Sales-Channel]]'
  - '[[procedures/Create-and-Upload-Price-List]]'
  - '[[procedures/Intercept-and-Inject-XSS-Payload]]'
  - '[[procedures/Trigger-XSS-and-Exploit-Data-Leakage]]'
step_count: 4
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T00:11:16.216Z'
description: >-
  A multi-stage attack exploiting a stored XSS vulnerability in Shopify's
  Wholesale sales channel to inject JavaScript payloads via price list CSV file
  names, enabling execution on a shared domain and leakage of sensitive data
  from other shops owned by the same user.
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Stored XSS in Shopify Wholesale Price List Leading to Cross-Shop Data Leakage

Multi-stage attack chain demonstrating exploitation of a stored XSS vulnerability in Shopify's Wholesale sales channel, allowing arbitrary JavaScript execution on the shared domain https://wholesale.shopifyapps.com to leak and modify data across multiple shops owned by the same user.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~15 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Access: Setup Channel] --> B[Discovery: Create Price List]
    B --> C[Execution: Inject XSS]
    C --> D[Collection: Trigger and Exfil Data]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/HTTP-Proxy-Burp-Suite]]

### Target Environment

- Shopify store with admin access
- Wholesale sales channel app installed
- Web browser for navigation
- Network access to Shopify admin panel

### Initial Access Requirements

- Valid Shopify admin credentials for a store
- Ability to install apps from Shopify App Store
- No prior access to other shops needed, but attack impacts multi-shop users

## Detailed Attack Procedures

### Step 1: Setup Wholesale Sales Channel
procedure: [[procedures/Setup-Wholesale-Sales-Channel]]

**Objective**: Install and access the Wholesale sales channel to prepare for price list manipulation.

**Instructions**: Visit the Wholesale app installation page and add it to your Shopify account, then navigate to the admin interface for the channel.

**Expected Output**: Successful installation and access to https://your-store.myshopify.com/admin/apps/wholesale.

**Success Indicators**:
- App installed without errors
- Admin panel for Wholesale channel accessible

### Step 2: Create and Upload Price List
procedure: [[procedures/Create-and-Upload-Price-List]]

**Objective**: Generate a price list via CSV import to establish a modifiable entry for payload injection.

**Instructions**: Download the sample CSV, modify it with a valid product SKU, and upload it through the price list creation interface.

**Expected Output**: New price list created and listed in the admin panel.

**Success Indicators**:
- CSV upload completes successfully
- Price list appears in the Wholesale dashboard

### Step 3: Intercept and Inject XSS Payload
procedure: [[procedures/Intercept-and-Inject-XSS-Payload]]

**Objective**: Capture the price list update request and inject a JavaScript payload into the CSV file name parameter.

**Instructions**: Edit the price list to trigger a POST request, intercept it using an HTTP proxy, and modify the price_list[csv_file_name] parameter to include the XSS payload like 'sample-csv-sku.csv"-alert(document.domain)-"', then forward the request. Use [[commands/modify-post-request-burp]] for interception if simulating via proxy.

```bash
# Example curl simulation of modified POST (adapt to actual endpoint)
curl -X POST 'https://admin.shopify.com/admin/shops/x/price_lists/x' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'price_list[csv_file_name]=sample-csv-sku.csv"-alert(document.domain)-"'
```

**Expected Output**: Request forwarded successfully; price list updates without immediate error.

**Success Indicators**:
- Intercepted request shows modifiable parameters
- Update succeeds, storing the payload

### Step 4: Trigger XSS and Exploit Data Leakage
procedure: [[procedures/Trigger-XSS-and-Exploit-Data-Leakage]]

**Objective**: View the price list to execute the injected JavaScript, enabling access to data from other shops on the shared domain.

**Instructions**: Navigate back to the price list page in the Wholesale admin; the payload executes automatically. Extend the payload to exfiltrate data like customer names, emails, and addresses via additional scripts targeting shared storage or APIs.

**Expected Output**: JavaScript alert or console execution confirming domain; potential data leakage visible in network requests.

**Success Indicators**:
- Alert pops up with domain https://wholesale.shopifyapps.com
- Access to other shops' Wholesale data (e.g., via document.cookie or localStorage inspection)

## Attack Chain Summary

### Key Achievements

1. Successful installation and setup of the vulnerable Wholesale channel
2. Injection of stored XSS payload via CSV file name parameter
3. Execution of JavaScript on shared domain leading to cross-shop data access
4. Potential for data exfiltration including customer PII and modification of Wholesale settings

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]
- [[Collection]]

---
*Last updated: 2023-10-01T00:00:00Z*
