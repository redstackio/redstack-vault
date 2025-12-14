---
id: ac-shopify-xss-upload-964550
tags:
  - xss
  - stored-xss
  - file-upload
  - shopify
type: attack_chain
tools:
  - '[[tools/exiftool]]'
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Embed-XSS-Payload-in-PNG-Metadata]]'
  - '[[procedures/Intercept-and-Modify-Avatar-Upload-Request]]'
  - '[[procedures/Upload-Malicious-Avatar-File]]'
  - '[[procedures/Trigger-XSS-by-Accessing-Uploaded-File]]'
step_count: 4
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:49.294Z'
description: >-
  Multi-stage attack exploiting unrestricted file upload in Shopify's avatar
  feature to embed and execute stored XSS via PNG metadata manipulation.
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Stored XSS via Malicious PNG Upload in Shopify Avatar Feature

Multi-stage attack chain demonstrating exploitation of unrestricted file upload in accounts.shopify.com to achieve stored XSS by embedding JavaScript in PNG metadata and manipulating MIME types.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Prepare Malicious PNG] --> B[Intercept Upload Request]
    B --> C[Upload Modified File]
    C --> D[Access and Trigger XSS]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/exiftool]]
- [[tools/Burp-Suite]]

### Target Environment

- Web platform (accounts.shopify.com)
- Required services: Shopify CDN (shopify-assets.shopifycdn.com)
- Network access: Direct HTTP access to upload endpoint

### Initial Access Requirements

- Authenticated session to Shopify accounts (e.g., logged-in user)
- Burp Suite proxy configured for request interception
- No special privileges beyond standard user account

## Detailed Attack Procedures

### Step 1: Prepare Malicious PNG
procedure: [[procedures/Embed-XSS-Payload-in-PNG-Metadata]]

**Objective**: Create a PNG file with an embedded XSS payload in its EXIF metadata to bypass image validation.

**Instructions**: Use [[commands/exiftool-inject-xss-into-png-comment]] to inject the payload into the Comment field of a base PNG image.

```bash
exiftool -Comment="\"><script>alert(prompt('XSS BY ZEROX4'))</script>" xss_comment_exif_metadata_double_quote.png
```

**Expected Output**: Modified PNG file with embedded XSS; exiftool outputs "1 image files updated".

**Success Indicators**:
- File metadata contains the injected script (verify with exiftool -a -G1 file.png)
- Original image renders normally

### Step 2: Intercept Upload Request
procedure: [[procedures/Intercept-and-Modify-Avatar-Upload-Request]]

**Objective**: Capture the avatar upload POST request and alter its Content-Type to treat the PNG as HTML.

**Instructions**: Configure Burp Suite as a proxy, navigate to the avatar upload in accounts.shopify.com, and intercept the request to /accounts/<ID>. Modify the Content-Type header for the file part from image/png to text/html.

**Expected Output**: Intercepted request shows modified headers; forward the request to proceed.

**Success Indicators**:
- Request successfully intercepted and edited in Burp Repeater or Proxy
- No immediate errors on modification

### Step 3: Upload Malicious Avatar
procedure: [[procedures/Upload-Malicious-Avatar-File]]

**Objective**: Submit the modified request to upload the malicious PNG as the account avatar.

**Instructions**: In Burp Suite, submit the multipart/form-data POST to https://accounts.shopify.com/accounts/<ID> with fields: utf8 (true), _method (patch), authenticity_token, and account[avatar] containing the PNG file with Content-Type: text/html and filename="xss_comment_exif_metadata_double_quote.png".

**Expected Output**: Server response indicates successful upload (e.g., 200 OK with avatar update confirmation).

**Success Indicators**:
- Avatar upload succeeds without validation errors
- File stored on Shopify CDN (check response for URL)

### Step 4: Trigger XSS Execution
procedure: [[procedures/Trigger-XSS-by-Accessing-Uploaded-File]]

**Objective**: Access the uploaded avatar URL to execute the stored XSS payload.

**Instructions**: Retrieve the uploaded file URL from the response or account page, such as https://shopify-assets.shopifycdn.com/accounts/production/account/avatar/<UUID>/avatar_36x36_crop_center.png?v=<timestamp>, and open it in a browser.

**Expected Output**: JavaScript alert pops up with "XSS BY ZEROX4", confirming payload execution.

**Success Indicators**:
- Alert or prompt executes in the browser
- Potential for data theft if payload is modified (e.g., to exfiltrate cookies)

## Attack Chain Summary

### Key Achievements

1. Bypassed image upload restrictions by manipulating MIME type and metadata
2. Achieved stored XSS execution on Shopify CDN-served assets
3. Enabled potential session hijacking or phishing via arbitrary JS

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]
- [[Collection]]

---
*Last updated: 2023-10-01T00:00:00Z*
