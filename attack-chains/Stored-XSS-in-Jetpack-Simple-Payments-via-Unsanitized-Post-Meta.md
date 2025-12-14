---
id: ac-jetpack-stored-xss-001
tags:
  - xss
  - stored-xss
  - wordpress
  - jetpack
  - privilege-escalation
  - web-vulnerability
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
verified: false
platforms:
  - Web
  - WordPress
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Code-Review-to-Identify-Jetpack-Stored-XSS]]'
  - '[[procedures/Inject-XSS-Payload-into-Product-Post-Meta]]'
  - '[[procedures/Trigger-Stored-XSS-via-Shortcode-Rendering]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:39.037Z'
description: >-
  Multi-stage attack exploiting a stored XSS vulnerability in Jetpack's Simple
  Payments module, allowing low-privilege users to inject JavaScript payloads
  into product post meta, which execute when rendered via shortcode, potentially
  leading to privilege escalation.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Stored XSS in Jetpack Simple Payments via Unsanitized Post Meta

Multi-stage attack chain demonstrating exploitation of a stored XSS vulnerability in WordPress sites using Jetpack's premium Simple Payments module. Low-privilege users like contributors or authors can inject JavaScript into product post meta fields, which are output without sanitization in shortcode rendering, enabling script execution in viewers' browsers and potential account takeover or escalation.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~15 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Code Review and Identification] --> B[Payload Injection]
    B --> C[Trigger and Execution]
    C --> D[Privilege Escalation]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- WordPress admin access as contributor/author
- Browser developer tools for payload testing

### Target Environment

- WordPress site with Jetpack premium/professional plan enabled
- Simple Payments module active
- PHP-based web server

### Initial Access Requirements

- Low-privilege account (contributor or author role)
- Ability to create/edit custom post types (products)
- No premium plan required for testing if bypassing nonces via core WP bugs

## Detailed Attack Procedures

### Step 1: Code Review and Identification
procedure: [[procedures/Code-Review-to-Identify-Jetpack-Stored-XSS]]

**Objective**: Analyze Jetpack code to identify the stored XSS vulnerability in post meta handling and shortcode output.

**Instructions**: Review the product post type registration and shortcode rendering functions in Jetpack source code. Examine capabilities allowing edit access for low-privilege users and trace unsanitized output of 'spay_formatted_price' meta.

**Expected Output**: Confirmation of vulnerability in output_shortcode and format_price functions.

**Success Indicators**:
- Post type supports custom fields without sanitization
- Shortcode outputs meta directly into HTML

### Step 2: Payload Injection
procedure: [[procedures/Inject-XSS-Payload-into-Product-Post-Meta]]

**Objective**: Create a product post as a low-privilege user and inject a JavaScript payload into the 'spay_formatted_price' meta field.

**Instructions**: Log in as contributor, create a new product post, and use the custom fields interface or AJAX to set 'spay_formatted_price' to a payload like `<script>alert('XSS')</script>`. Bypass any nonces using known WordPress core issues if needed.

**Expected Output**: Product post saved with injected meta value.

**Success Indicators**:
- Meta value stored without validation
- No errors on post creation

### Step 3: Trigger and Execution
procedure: [[procedures/Trigger-Stored-XSS-via-Shortcode-Rendering]]

**Objective**: Insert the shortcode into a post and view it to execute the stored payload in the browser.

**Instructions**: Edit a post to include `[simple-payment id="PRODUCT_POST_ID"]` shortcode, save, and view the post as any user. The shortcode renders the unsanitized price meta, executing the JavaScript.

**Expected Output**: JavaScript alert or payload execution in the viewer's browser.

**Success Indicators**:
- Payload executes on page load
- Potential cookie theft or escalation if payload is malicious

## Attack Chain Summary

### Key Achievements

1. Identified unsanitized post meta output in Jetpack shortcode
2. Injected and stored XSS payload as low-privilege user
3. Triggered execution leading to browser script control

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]

---
*Last updated: 2023-10-01T00:00:00Z*
