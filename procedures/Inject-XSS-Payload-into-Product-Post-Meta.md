---
id: proc-jetpack-payload-injection-001
tags:
  - xss-injection
  - post-meta
  - wordpress
  - jetpack
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
  - WordPress
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:39.032Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-XSS-Payload-into-Product-Post-Meta

## Summary

This procedure demonstrates injecting a JavaScript payload into the 'spay_formatted_price' post meta of a Jetpack product post as a contributor or author, exploiting the lack of sanitization to store malicious code for later execution.

## Description

Low-privilege users in WordPress can create products (custom posts) and add custom meta fields. The Simple Payments module does not validate or escape these values. By setting 'spay_formatted_price' to an XSS payload, the injection persists in the database. This is feasible even without a premium plan by leveraging WordPress core nonce bypasses for meta addition.

## Requirements

1. Contributor or author role in WordPress
2. Access to post editor with custom fields enabled
3. Knowledge of XSS payloads (e.g., <script>alert(document.cookie)</script>)

## Defense

Defensive measures and detection strategies:

- Validate and sanitize all custom meta inputs server-side
- Disable custom fields for low-privilege roles on sensitive post types
- Use nonces properly and audit for bypasses
- Scan database for suspicious meta values containing script tags

## Objectives

1. Create a product post with injected meta
2. Store arbitrary JavaScript without triggering errors
3. Prepare payload for shortcode-based execution

## Instructions

### Step 1: Create Product Post

**Context**: Log in and initiate a new product post to access meta fields.

Navigate to WordPress admin > Products > Add New. Ensure the post type is registered via Jetpack.

**Expected Output**: Blank product post editor open.

### Step 2: Add Custom Meta with Payload

**Context**: Use custom fields to set the vulnerable meta key.

In the post editor, add a custom field: Key = 'spay_formatted_price', Value = `<script>alert('XSS via Jetpack')</script>` or a more advanced payload like `<img src=x onerror=fetch('/wp-admin/admin-ajax.php?action=evil&cookie='+document.cookie)>`. If nonces block, exploit known WP core issues (e.g., unauthenticated meta add in older versions).

**Expected Output**: Meta saved to post without sanitization.

### Step 3: Save and Verify Post

**Context**: Confirm the payload is stored.

Publish or save the post, then view post meta in database (e.g., via phpMyAdmin) to ensure 'spay_formatted_price' contains the script.

**Expected Output**: Raw payload visible in wp_postmeta table.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss-injection
- post-meta
- wordpress
