---
id: proc-imgur-ssrf-identify
tags:
  - ssrf
  - recon
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:39:09.822Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Identify Imgur VideoToGIF SSRF Endpoint

## Summary

This procedure involves examining Imgur's /vidgif/url endpoint to identify the lack of validation on the 'url' GET parameter, enabling Server-Side Request Forgery (SSRF) by allowing arbitrary external URLs to be fetched by the server.

## Description

In the context of Imgur's Video to GIF conversion feature, the /vidgif/url endpoint processes user-supplied URLs without sanitization or verification. This allows attackers to supply external domains, internal IPs (e.g., 192.168.1.1), or malicious payloads, leading to SSRF. The procedure focuses on reconnaissance to confirm vulnerability before exploitation, typically in a web-based environment using Ruby backend.

## Requirements

1. Access to Imgur's public API or web interface
2. Tools for inspecting HTTP requests (e.g., browser dev tools or proxy)
3. Basic knowledge of HTTP GET parameters

## Defense

Defensive measures and detection strategies:

- Implement URL whitelisting and validation to restrict to trusted domains
- Use network segmentation to block internal requests from public-facing apps
- Monitor server outbound traffic for anomalies from application servers

## Objectives

1. Confirm the endpoint accepts arbitrary URLs
2. Identify lack of sanitization for external/internal requests
3. Prepare for SSRF exploitation testing

## Instructions

### Step 1: Examine Endpoint Documentation and Behavior

**Context**: Review available documentation or test the endpoint to understand parameter handling.

No specific command; use browser or curl to probe:

```bash
curl "https://i.imgur.com/vidgif/url?url=https://example.com"
```

> This tests if the endpoint processes the URL without rejection. Expected output: Server response without validation errors.

### Step 2: Test for Validation Gaps

**Context**: Supply various URL types (external, internal) to check for restrictions.

Use manual testing or scripting to send requests with different URLs, observing responses.

> Look for successful processing of non-Imgur domains, indicating SSRF potential.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[ssrf]]
- [[web]]
- [[recon]]
