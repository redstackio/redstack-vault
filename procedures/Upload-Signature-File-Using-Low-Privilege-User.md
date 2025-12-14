---
tags:
  - file-upload
  - authentication-bypass
  - http-post
  - shopify
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-upload-signature]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Remote File Copy]]'
updated_at: '2025-12-14T17:29:20.345Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 4965c563-8e61-414a-8253-6e5ae2101727
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Remote File Copy]]'
---
# Upload-Signature-File-Using-Low-Privilege-User

## Summary

This procedure sends a POST request to Shopify's `/admin/secure_files.json` endpoint with a low-privilege account to upload the malicious signature payload, bypassing authorization checks.

## Description

Using a user without transaction permissions, the procedure exploits the endpoint's lack of auth checks to associate the uploaded SVG file with a transaction. The request includes the prepared JSON payload; response provides an S3 URL with temporary AWS credentials. This occurs in Shopify's web admin context, leading to successful file storage and linkage without errors.

## Requirements

1. Low-privilege Shopify account credentials (e.g., staff or customer with basic access)
2. Prepared JSON payload from prior step
3. HTTP client like curl with session handling

## Defense

Defensive measures and detection strategies:

- Enforce role-based access control (RBAC) on API endpoints
- Audit file uploads for privilege mismatches
- Block or scan uploads to S3 from unauthorized sources

## Objectives

1. Successfully upload file without auth denial
2. Obtain S3 URL confirming storage
3. Associate file with target transaction

## Instructions

### Step 1: Authenticate Low-Privilege Session

**Context**: Log in as a low-priv user to obtain session cookies or API token.

Use Shopify login flow to get auth headers (e.g., shop_session or API key).

> Ensure no high-priv roles; test with read-only permissions.

### Step 2: Send POST Request

**Context**: Submit the payload to the endpoint.

Execute [[commands/curl-upload-signature]] with your payload and auth:

```bash
curl -X POST -H "Content-Type: application/json" -H "Cookie: shop_session=your_session" -d '@payload.json' https://your-shop.myshopify.com/admin/secure_files.json
```

> Replace URL, session, and file path. Expected: 200 OK with JSON response containing 'secure_file' URL, AWS keys, expiration, and sig.

### Step 3: Validate Upload Response

**Context**: Check response for success indicators.

Parse the JSON response to extract the S3 URL and attempt temporary access.

> Success if URL loads the SVG without errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Remote File Copy]]

### Sub-Techniques


## Commands Used

- [[commands/curl-upload-signature]]

## Tools Used


## Tags

- [[file-upload]]
- [[authentication-bypass]]
