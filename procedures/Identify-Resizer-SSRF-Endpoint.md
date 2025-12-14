---
id: proc-uuid-456
tags:
  - recon
  - web
  - ssrf
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-basic-test]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T03:46:09.221Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Identify-Resizer-SSRF-Endpoint

## Summary

This reconnaissance procedure identifies the vulnerable /form endpoint in the Line resizer service, verifying its susceptibility to SSRF by testing external URL handling.

## Description

The resizer service at https://resizer.line-apps.com processes image resize requests via GET parameters. This step involves probing the endpoint to ensure it accepts HTTP URLs, a prerequisite for SSRF exploitation. It simulates legitimate usage to avoid detection while confirming the attack surface.

## Requirements

1. Internet access to the target domain
2. Basic HTTP client like curl
3. No special credentials needed

## Defense

Defensive measures and detection strategies:

- Rate-limit requests to the /form endpoint
- Log all URL parameters for anomaly detection
- Block repeated probes from suspicious IPs

## Objectives

1. Confirm endpoint functionality
2. Verify HTTP URL acceptance
3. Expected outcome: Valid response to external requests

## Instructions

### Step 1: Probe the Endpoint

**Context**: Send a test request to check if the service processes external URLs.

**Command** ([[commands/curl-basic-test]]):
```bash
curl -v "https://resizer.line-apps.com/form?url=http://httpbin.org/get"
```

> Uses httpbin.org for echo response. Expected output: JSON echo of the request, confirming SSRF potential.

### Step 2: Test Image Processing

**Context**: Verify image-specific handling to mimic legitimate traffic.

**Command** ([[commands/curl-basic-test]]):
```bash
curl -v "https://resizer.line-apps.com/form?url=https://example.com/image.jpg"
```

> Expected output: Resized image or processing confirmation.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques

-

## Commands Used

- [[commands/curl-basic-test]]

## Tools Used

-

## Tags

- recon
- web
- ssrf
