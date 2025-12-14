---
tags:
  - upload
  - woocommerce
  - stored-xss
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - WordPress
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-13T23:52:33.424Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 0b6fb200-45c6-44a9-929a-5148998d484e
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Upload-Malicious-Image-to-WooCommerce

## Summary

This procedure uploads an image containing XSS payload in its metadata to a WooCommerce product, storing the vulnerability for later execution on viewed pages.

## Description

WooCommerce processes uploaded images for products without fully sanitizing metadata like the title field. An authenticated admin can attach the malicious image to a product, persisting the payload on the server. When the product page loads, the metadata is echoed back, triggering XSS. This targets WordPress sites with WooCommerce, requiring admin privileges.

## Requirements

1. Authenticated access to WordPress admin (e.g., admin credentials)
2. Prepared image with XSS in title metadata
3. Active WooCommerce plugin

## Defense

Defensive measures and detection strategies:

- Validate and sanitize uploads with wp_handle_upload_prefilter
- Use plugins like Wordfence to scan uploads for malicious content
- Restrict file upload types and sizes
- Audit product images for anomalous metadata

## Objectives

1. Successfully store the malicious image on the server
2. Associate it with a visible product element (e.g., featured image)
3. Ensure metadata preservation through upload

## Instructions

### Step 1: Access Product Editor

**Context**: Log in to the admin panel and create a new product to attach the image.

Navigate to Products > Add New in the WordPress dashboard.

> Fill in basic product details like name and description to make it savable.

### Step 2: Upload and Set Image

**Context**: Attach the malicious image as the product image.

In the Product Data section, click "Set product image" and upload the prepared file (e.g., test.jpg). Alternatively, add to gallery.

Save the product by clicking Publish.

> The upload succeeds if the file is a valid image; metadata is not stripped by default WooCommerce handling.

### Step 3: Verify Upload

**Context**: Confirm the image is attached without errors.

Preview the product or view media library to see the image listed.

> Expected: Image displays correctly; no upload rejection.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- upload
- woocommerce
- xss
