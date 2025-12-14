---
tags:
  - xss
  - persistent-xss
  - woocommerce
  - wordpress
  - admin-compromise
type: attack_chain
tools: []
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Set-Up-WordPress-WooCommerce-Environment-and-Create-Customer]]'
  - '[[procedures/Login-as-Customer-to-Access-Account]]'
  - '[[procedures/Inject-XSS-Payload-into-Customer-County-Field]]'
  - '[[procedures/Trigger-XSS-Payload-in-Admin-Context]]'
step_count: 4
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:34.341Z'
description: >-
  A multi-stage attack exploiting a persistent XSS vulnerability in
  WooCommerce's customer address county field to execute arbitrary JavaScript in
  the WordPress admin context, enabling data theft and potential server-side
  compromise.
skill_level: intermediate
impact_level: high
id: df88118d-f66d-4f94-a0a9-7a2626c8923e
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Persistent XSS in WooCommerce Customer Address Leading to Admin JavaScript Execution

Multi-stage attack chain demonstrating a complete attack workflow exploiting a persistent cross-site scripting (XSS) vulnerability in WooCommerce version 3.5.7, where the customer address county field is not properly encoded when displayed in the WordPress admin panel. An attacker with a registered customer account injects a JavaScript payload during checkout or account editing, which persists and executes when an administrator views the customer's profile, allowing arbitrary code execution in the admin's browser context. This can lead to session hijacking, data exfiltration, or further attacks like modifying WordPress files.

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
    A[Setup and Customer Creation] --> B[Customer Login]
    B --> C[Payload Injection]
    C --> D[Admin Trigger and Execution]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Firefox or Chrome with developer tools)
- Access to a WordPress site with WooCommerce installed (version 3.5.7 or vulnerable equivalent)

### Target Environment

- WordPress platform with WooCommerce plugin
- PHP backend
- Web server (e.g., Apache/Nginx) on port 80/443
- Administrative access for triggering; customer registration enabled

### Initial Access Requirements

- Ability to register a customer account
- Network access to the WordPress site (e.g., http://target.com/wordpress/)
- No prior admin credentials needed for injection, but admin must view the profile to trigger

## Detailed Attack Procedures

### Step 1: Setup Environment and Create Customer Account
procedure: [[procedures/Set-Up-WordPress-WooCommerce-Environment-and-Create-Customer]]

**Objective**: Prepare the vulnerable WordPress WooCommerce environment and establish a customer presence for payload injection.

**Instructions**: Install WordPress and WooCommerce, then register a new customer account via the site's registration form.

**Expected Output**: A functional WooCommerce site with a registered customer user (e.g., user ID 4).

**Success Indicators**:
- WooCommerce plugin active and customer registration successful
- Customer dashboard accessible post-registration

### Step 2: Login as Customer
procedure: [[procedures/Login-as-Customer-to-Access-Account]]

**Objective**: Authenticate as the customer to access account editing or checkout features for payload injection.

**Instructions**: Navigate to the My Account page and log in with customer credentials.

**Expected Output**: Redirect to the customer dashboard at /my-account/.

**Success Indicators**:
- Successful login without errors
- Access to edit-address or checkout pages

### Step 3: Inject XSS Payload into County Field
procedure: [[procedures/Inject-XSS-Payload-into-Customer-County-Field]]

**Objective**: Insert a persistent JavaScript payload into the customer address county field, which will be stored and echoed unencoded in the admin panel.

**Instructions**: During checkout or address editing, select UK as country and enter the payload in the County field.

**Expected Output**: Address saved with payload; no immediate execution visible to customer.

**Success Indicators**:
- Payload accepted without validation errors
- Address details updated in customer profile

### Step 4: Trigger Payload as Administrator
procedure: [[procedures/Trigger-XSS-Payload-in-Admin-Context]]

**Objective**: View the customer's profile in the admin panel to execute the injected JavaScript in the administrator's browser session.

**Instructions**: As admin, navigate to Users and select the customer, or directly access the edit user page.

**Expected Output**: JavaScript alert or payload execution (e.g., alert(1)) in the admin browser.

**Success Indicators**:
- Payload triggers on page load in admin context
- Potential for further exploitation like data theft or requests as admin

## Attack Chain Summary

### Key Achievements

1. Successful injection of persistent XSS payload via customer address field in WooCommerce.
2. Execution of arbitrary JavaScript in the high-privilege admin context.
3. Demonstration of impact including data exfiltration and potential server-side escalation through admin actions.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Execution]]

---
*Last updated: 2023-10-01T00:00:00Z*
