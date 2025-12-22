---
id: proc-starbucks-identify-upload
tags:
  - web-recon
  - file-upload
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-endpoint-probe]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-13T23:52:49.753Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Identify Unrestricted File Upload Endpoint

## Summary

This procedure involves reconnaissance to locate and test file upload endpoints on a web application, confirming if they lack restrictions on file types or content, as seen in the Starbucks Singapore campaign site.

## Description

In web applications, file upload features are common but often insecure. This procedure targets public-facing APIs like /api/upload, testing for validation bypasses. In the Starbucks case, the endpoint at https://campaign.starbucks.com.sg/api/upload accepted arbitrary files without checks, enabling further exploitation. Prerequisites include access to the target site and tools for HTTP requests.

## Requirements

1. Network access to the target web application.
2. Basic HTTP client (e.g., curl or browser).
3. Knowledge of the site's structure or API documentation.

## Defense

Defensive measures and detection strategies:

- Implement file type whitelisting and content scanning on uploads.
- Log and monitor upload attempts for anomalous patterns (e.g., non-image files to image endpoints).

## Objectives

1. Discover upload endpoints vulnerable to unrestricted access.
2. Validate lack of server-side checks.
3. Prepare for payload upload.

## Instructions

### Step 1: Probe for Upload Endpoints

**Context**: Use network inspection or directory fuzzing to find potential upload APIs.

**Command** ([[commands/curl-endpoint-probe]]):
```bash
curl -X POST https://campaign.starbucks.com.sg/api/upload -F "file=@test.txt" -v
```

> This sends a simple file upload request and verbose output reveals if the endpoint exists and accepts the request without errors.

### Step 2: Analyze Response

**Context**: Check for acceptance of arbitrary files by varying types (e.g., .txt, .html).

**Command** ([[commands/curl-endpoint-probe]]):
```bash
curl -X POST https://campaign.starbucks.com.sg/api/upload -F "file=@malicious.html" -v
```

> Success if no rejection; response may include upload path.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used

- [[commands/curl-endpoint-probe]]

## Tools Used


## Tags

- [[web-recon]]
- [[file-upload]]
