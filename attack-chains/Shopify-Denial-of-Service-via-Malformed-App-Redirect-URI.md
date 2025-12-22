---
tags:
  - dos
  - shopify
  - oauth
  - input-validation
  - redirect-uri
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Impact]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2024-10-01T00:00:00Z'
procedures:
  - '[[procedures/Create-Shopify-App-with-Invalid-Callback-URL]]'
  - '[[procedures/Install-Shopify-App-via-OAuth]]'
  - '[[procedures/Verify-DoS-on-Shopify-Admin-Apps-Page]]'
step_count: 3
techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:45.024Z'
description: >-
  Exploit improper validation of redirect_uri in Shopify app creation to install
  a malicious app that causes a 500 error on the admin apps management page,
  denying service to shop admins.
skill_level: intermediate
impact_level: high
id: 70999a6f-45e7-451f-a4a6-ad6892cd1481
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[Exploit Public-Facing Application]]'
---
# Shopify Denial of Service via Malformed App Redirect URI

Multi-stage attack chain demonstrating a complete attack workflow exploiting improper input validation in Shopify's app creation process to cause a denial of service on the admin apps page.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Create Malicious App] --> B[Install via OAuth]
    B --> C[Trigger DoS on Apps Page]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome)
- Access to a Shopify Partner account

### Target Environment

- Shopify Partner Dashboard (https://app.shopify.com)
- Target Shopify store (e.g., vulnstore.myshopify.com)
- No specific ports; web-based access required

### Initial Access Requirements

- Valid Shopify Partner credentials for app creation
- Administrative access to the target store for installation testing
- Network access to Shopify services

## Detailed Attack Procedures

### Step 1: Create Malicious App
procedure: [[procedures/Create-Shopify-App-with-Invalid-Callback-URL]]

**Objective**: Register a new Shopify app with a malformed redirect_uri to set up the DoS condition.

**Instructions**: Log in to the Shopify Partner Dashboard and navigate to app creation. Enter app details including the invalid callback URL 'shit:google.com'. Submit to save the app and obtain the client_id.

**Expected Output**: App created successfully with client_id (e.g., cad94488c733b0f377a9a1d7952db802).

**Success Indicators**:
- App listed in partner dashboard
- Client_id generated for OAuth

### Step 2: Install App via OAuth
procedure: [[procedures/Install-Shopify-App-via-OAuth]]

**Objective**: Install the app on the target store to trigger the malformed redirect, corrupting the app management state.

**Instructions**: Construct the OAuth URL using the client_id and scope (e.g., read_customers). Visit the URL in a browser, approve permissions, and complete installation. The process will fail to redirect due to the invalid URI.

**Expected Output**: Installation dialog appears; app installs but no redirect occurs.

**Success Indicators**:
- Permission dialog shown and approved
- App appears as installed in store (but unmanageable)

### Step 3: Verify DoS Effect
procedure: [[procedures/Verify-DoS-on-Shopify-Admin-Apps-Page]]

**Objective**: Confirm the denial of service by accessing the apps management page, which fails due to the malformed app.

**Instructions**: As a shop admin, navigate to the /admin/apps page on the target store. Attempt to load the page to observe the error.

**Expected Output**: 500 Internal Server Error, preventing access to installed apps list or removal options.

**Success Indicators**:
- Page fails to load with 500 error
- Admins cannot manage or remove apps until developer deletes the malicious app

## Attack Chain Summary

### Key Achievements

1. Successful creation of app with unvalidated malformed URI
2. Installation of app causing redirect failure and state corruption
3. Persistent DoS on admin apps page until manual intervention by app developer

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Endpoint Denial of Service]] Endpoint Denial of Service
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Impact]] Impact

---
*Last updated: 2024-10-01T00:00:00Z*
