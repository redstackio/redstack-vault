---
tags:
  - xss
  - injection
  - shopify
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
  - Shopify
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 564b99dc-f9ec-45b3-a2b4-61a9628c6f61
created_at: '2025-12-13T23:52:25.684Z'
updated_at: '2025-12-13T23:52:25.684Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject XSS Payload into Product Type

## Summary

This procedure involves creating a product in Shopify and injecting a stored XSS payload into the 'Product Type' field, which persists the malicious script for later execution in connected apps like Judge.me.

## Description

Shopify's product creation form allows admins to set a 'Product Type' without sanitization for script tags. The payload "><img src=x onerror=prompt(document.domain)> closes any parent tags and injects an image that executes JavaScript on error, alerting the domain. This stored payload is retrieved and displayed unsafely in Judge.me's filters.

## Requirements

1. Shopify admin access with product creation permissions
2. Active store environment
3. Knowledge of basic XSS payloads

## Defense

Defensive measures and detection strategies:

- Implement input validation on product fields to strip script tags
- Use Content Security Policy (CSP) to block inline scripts
- Audit product data for suspicious strings like 'onerror' or 'src=x'

## Objectives

1. Persist malicious JavaScript in product metadata
2. Ensure the product is active for visibility in filters
3. Avoid detection during save

## Instructions

### Step 1: Create New Product

**Context**: Set up a product to host the payload.

In Shopify admin, navigate to Products > Add product. Set the status to Active and fill in basic details like title (e.g., "Test Product").

### Step 2: Insert Payload in Product Type

**Context**: Inject the XSS script into the vulnerable field.

In the Product Type field, enter: "><img src=x onerror=prompt(document.domain)>

Save the product.

**Expected Output**: Product saved; no errors if payload is accepted.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[injection]]
- [[shopify]]
