---
tags:
  - ssrf
  - upload
  - shopify
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 1a7ad1d0-6c1e-411a-8897-cefc4da73f8d
created_at: '2025-12-14T03:46:14.376Z'
updated_at: '2025-12-14T03:46:14.376Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Upload Malicious SVG to Product Endpoint

## Summary

Submits the disguised SVG payload to Shopify's product image upload API, triggering server-side processing and SSRF despite upload failure.

## Description

The endpoint /admin/products/{id}/images.json accepts multipart/form-data uploads. By sending SVG as image/png, the server parses it via GraphicsMagick, fetching external resources before rejecting with 422. This enables SSRF in authenticated admin contexts.

## Requirements

1. Authenticated session cookie for Shopify admin
2. Valid product ID (e.g., 9577763394)
3. HTTP client for POST requests

## Defense

Defensive measures and detection strategies:

- Implement strict MIME type validation before parsing
- Use allowlists for external fetches in image libraries
- Log and alert on 422 responses with image uploads

## Objectives

1. Trigger SVG parsing on server
2. Initiate external request
3. Confirm via attacker logs

## Instructions

### Step 1: Prepare Multipart Request

**Context**: Structure the POST with the disguised file.

Use curl or similar:

```bash
curl -X POST "https://shop.myshopify.com/admin/products/9577763394/images.json" \
  -H "Cookie: your-session-cookie" \
  -F "image=@payload.png" \
  -F "attachment=@payload.png"
```

> Note: Content-Type for image part is image/png, but file is SVG content. Replace URL and cookie.

### Step 2: Submit and Monitor Response

**Context**: Send and check for rejection after processing.

Execute the request and verify 422 Unprocessable Entity.

> Processing happens before rejection, triggering SSRF.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[ssrf]]
- [[shopify]]
