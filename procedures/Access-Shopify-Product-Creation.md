---
id: proc-shopify-access
tags:
  - shopify
  - access
  - product
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T05:32:10.499Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Access-Shopify-Product-Creation

## Summary

This procedure logs into a Shopify admin panel and navigates to the product creation interface to prepare for image uploads that can exploit SSRF vulnerabilities.

## Description

Shopify stores allow authenticated users to create products with image attachments. This step establishes the foothold for uploading malicious SVGs. Requires valid credentials; outcomes include access to the upload feature where the parser vulnerability resides.

## Requirements

1. Valid Shopify admin login credentials
2. Web browser access to the store URL
3. No additional tools needed

## Defense

Defensive measures and detection strategies:

- Implement role-based access controls for product management
- Log and monitor admin logins and product creation activities
- Rate-limit upload attempts to prevent abuse

## Objectives

1. Authenticate to the Shopify admin
2. Reach the product image upload section
3. Set up for exploitation

## Instructions

### Step 1: Login to Admin

**Context**: Enter credentials at the store's admin URL.

Navigate to https://yourstore.myshopify.com/admin and log in.

> Expected: Dashboard loads successfully.

### Step 2: Navigate to Products

**Context**: Go to the product management area.

Click Products > Add Product.

> Expected: Form opens with fields including image upload.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- shopify
- admin-access
