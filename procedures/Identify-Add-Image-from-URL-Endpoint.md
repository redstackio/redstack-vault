---
id: 123e4567-e89b-12d3-a456-426614174001
name: Identify-Add-Image-from-URL-Endpoint
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:39:09.800Z'
tactics:
  - '[[Reconnaissance]]'
techniques:
  - '[[Active Scanning]]'
sub_techniques: []
tags:
  - ssrf
  - reconnaissance
  - shopify
commands:
  - '[[commands/shopify-add-image-normal]]'
platforms:
  - Web
tools: []
skill_level: intermediate
impact_level: low
detection_risk: low
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---

# Identify-Add-Image-from-URL-Endpoint

## Summary

This procedure identifies the Shopify admin endpoint used for adding product images from URLs, revealing the image[src] parameter that fetches external resources, setting the stage for SSRF exploitation.

## Description

In a Shopify store admin panel, the 'Add Image from URL' feature sends a POST request to /admin/products/{id}/images, where the server fetches the provided URL to attach as a product image. This involves authenticated access and CSRF protection. Analyzing this endpoint shows no initial restrictions on URLs, but validation exists that can be bypassed. Prerequisites include admin login and a valid product ID.

## Requirements

1. Authenticated Shopify admin session with CSRF token
2. Valid product ID (e.g., 922460995)
3. Browser developer tools or proxy like Burp Suite for request inspection

## Defense

Defensive measures and detection strategies:

- Implement strict URL whitelisting in image fetch endpoints
- Log and monitor all outbound fetches from admin panels
- Use WAF rules to block suspicious redirect patterns

## Objectives

1. Confirm the endpoint and parameter behavior
2. Verify legitimate URL fetching works
3. Identify validation mechanisms for later bypass

## Instructions

### Step 1: Log In and Navigate to Product

**Context**: Gain access to the admin panel and select a product to expose the image upload feature.

No command needed; use the web interface to go to https://yourstore.myshopify.com/admin/products/{id}.

### Step 2: Observe and Test Legitimate Request

**Context**: Capture the POST request to understand the structure and confirm server-side fetching.

**Command** ([[commands/shopify-add-image-normal]]):
```bash
curl -X POST 'https://test-4925.myshopify.com/admin/products/922460995/images' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -H 'X-CSRF-Token: F7cvLpquxqr+rFmnGVFhNEK6rV8njtebHikevxGlLJA=' \
  -d 'utf8=%E2%9C%93&authenticity_token=F7cvLpquxqr%2BrFmnGVFhNEK6rV8njtebHikevxGlLJA%3D&product_id=922460995&image%5Bsrc%5D=https://example.com/image.jpg&_method=post'
```

> This simulates adding a valid image URL. Expected output is a JSON response indicating success, with the image attached to the product.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques


## Commands Used

- [[commands/shopify-add-image-normal]]

## Tools Used


## Tags

- [[ssrf]]
- [[Reconnaissance]]
- [[shopify]]
