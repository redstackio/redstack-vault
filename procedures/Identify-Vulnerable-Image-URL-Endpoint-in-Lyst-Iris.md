---
id: proc-ssrf-identify-lyst-001
tags:
  - ssrf
  - recon
  - web
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-get-endpoint-test]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:08:55.492Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Identify Vulnerable Image URL Endpoint in Lyst Iris

## Summary

This procedure identifies the vulnerable /models/default/classification/color endpoint in the Lyst Iris API, which accepts user-supplied URLs in the 'images' array and fetches them server-side without validation, enabling SSRF attacks.

## Description

In the context of the Lyst Iris service at iris.lystit.com, this step involves testing the REST API to discover endpoints that process image URLs for classification tasks. The target runs on Python with Django REST Framework and is exposed publicly despite being intended for internal use. Successful identification confirms the lack of URL whitelisting, allowing subsequent SSRF exploitation for internal access and reconnaissance.

## Requirements

1. Public network access to https://iris.lystit.com
2. Tool for HTTP requests like curl
3. Basic knowledge of REST APIs and JSON payloads

## Defense

Defensive measures and detection strategies:

- Implement URL whitelisting to restrict fetches to trusted domains
- Monitor server-side HTTP requests for anomalies like localhost or internal IPs
- Use web application firewalls (WAF) to block suspicious URL patterns in payloads

## Objectives

1. Locate and validate the vulnerable endpoint
2. Confirm server-side fetching behavior
3. Prepare for SSRF exploitation

## Instructions

### Step 1: Test Endpoint Accessibility

**Context**: Send a basic request to verify the endpoint exists and processes image URLs.

**Command** ([[commands/curl-get-endpoint-test]]):
```bash
curl -X GET https://iris.lystit.com/models/default/classification/color
```

> This command checks if the endpoint is reachable and returns any error or schema information. Expected output: HTTP 200 or 405 with details on accepted methods (POST).

### Step 2: Probe with Sample Payload

**Context**: Submit a test JSON payload with a benign external image URL to observe server-side fetching.

**Command** ([[commands/curl-post-basic-test]]):
```bash
curl -X POST https://iris.lystit.com/models/default/classification/color -H "Content-Type: application/json" -d '{"images": ["https://example.com/test-image.png"]}'
```

> This triggers the server to fetch the URL and classify the image. Expected output: JSON with classification data, confirming SSRF potential.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-get-endpoint-test]]
- [[commands/curl-post-basic-test]]

## Tools Used

- [[tools/curl]]

## Tags

- ssrf
- recon
- api-testing
