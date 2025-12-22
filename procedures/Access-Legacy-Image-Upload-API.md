---
tags:
  - api-access
  - legacy-endpoint
  - recon
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-api-probe]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T05:32:13.155Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: ad7f4f79-4839-4e35-9c4b-8b6b563bd7f7
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-Legacy-Image-Upload-API

## Summary

This procedure identifies and probes a legacy API endpoint intended for image uploads, confirming the absence of file type restrictions to prepare for exploitation.

## Description

In scenarios involving outdated web applications, legacy API endpoints for media uploads often lack modern validation, allowing attackers to interact freely. This step focuses on discovering the endpoint (e.g., via documentation, source code review, or directory brute-forcing) and sending initial requests to verify accessibility and behavior. The target environment is a web-based API connected to a CDN, where uploads are processed without MIME type checks, leading to potential storage of arbitrary files.

## Requirements

1. Public access to the web application and API endpoint.
2. Knowledge of the API URL (e.g., from API docs or network inspection).
3. HTTP client tool like curl for probing.

## Defense

Defensive measures and detection strategies:

- Implement API versioning to deprecate legacy endpoints.
- Monitor API access logs for unusual probe patterns (e.g., HEAD requests to upload paths).
- Enforce rate limiting on upload endpoints.

## Objectives

1. Confirm endpoint accessibility and lack of authentication.
2. Verify no immediate file type validation occurs.
3. Gather response details for subsequent upload attempts.

## Instructions

### Step 1: Probe the API Endpoint

**Context**: Send a simple HTTP request to the legacy upload endpoint to check for availability and response format.

**Command** ([[commands/curl-api-probe]]):
```bash
curl -X POST https://api.example.com/upload-image -H "Content-Type: multipart/form-data"
```

> This command attempts a POST to the endpoint without a file, expecting an error or schema response that indicates acceptance of uploads. Successful output includes HTTP 200/400 with details on expected parameters like 'file'.

### Step 2: Inspect Response for CDN Integration

**Context**: Analyze the response to identify if uploads route to a CDN and note any returned URLs or headers.

**Command** ([[commands/curl-api-probe]]):
```bash
curl -v -X POST https://api.example.com/upload-image
```

> The verbose (-v) flag reveals headers, such as Location or CDN-related redirects, confirming direct storage potential.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-api-probe]]

## Tools Used


## Tags

- [[api-access]]
- [[legacy-endpoint]]
